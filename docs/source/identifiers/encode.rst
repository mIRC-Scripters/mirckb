$encode
=======

The $encode identifier allows you to encode literal text, or text in :doc:`%vars </beginner/variables>` or :ref:`binary_variables`. The $encode identifier uses either Uuencode or Base64|MIME or Base32 or Z85 to encode. Additionally, $encode is capable of utilizing Blowfish to encrypt the target before encoding using u/m/a/v encoding.

Synopsis
--------

.. code:: text

    ; encoding only
    $encode(text/%var/&binvar [, btumav] [, N] )
    
    ; encryption
    $encode(text/%var/&binvar, celsirznpbtumav, key[, salt/iv if s|i used] [,N] )

Parameters
----------

Encoding
^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - text/%var/&binvar
      - The target to be encoded
    * - b
      - Target is a :ref:`binary_variables`
    * - t
      - Target is text (this is default target type)
    * - u
      - Target should be encoded using Uuencode (this is default encode type when 'tuma' not used)
    * - m
      - Target should be encoded using Mime (base64) (favored; has shortest output)
    * - a
      - Target should be encoded using Base32
    * - v
      - Target should be encoded using Z85
    * - N
      - Integer Reference index for the Nth chunk (can't use without at least 1 switch)

* 'b' recognizes target is a binary variable instead of text beginning with '&'.
* 'b' returns encoded output back to the same binary variable, then the $encode identifier 'returns' N where N is the new length of the &binary variable. Most common usage would be to $encode as an argument to noop or conditional checking if non-zero to detect failure.
* When target is text or %variable, content is UTF-8 encoded before encoding. To avoid this, you must load text into a binary variable using 'bset -ta' then use $encode's 'b' switch to allow using that binary variable as the target. (Assuming string does not contain codepoints 256+)
* 'm' mime/base64 and 'u' UUencode encode 3 bytes into 4 printable characters, with u also prepending a length byte before each chunk of up to 60 encoded characters.
* 'a' Base32 encodes 5 bytes into 8 printable characters.
* 'v' Z85 variant of Base85 encodes 4 bytes into 5 printable characters.
* If N parameter is present, N=0 returns the number of chunks in the output, N >= 1 returns the Nth encoded chunk of the output or $null if N is greater than the N=0 value. N allows handling encoded output output of &binary strings too long to fit within %variables or mIRC's maximum line length.
* except for the final possibly partial length, N Chunks contain 60 encoding characters, except for base32 which contains 72, and except for 'u' which inserts a length byte in front of each chunk. This feature was added prior to UTF8 support, so it's possible for this feature to split the encoding of UTF8 codepoints across 2 chunks.
* $decode is currently able to decode mime/UUencode encoded strings without the "`" or "=" padding added by $encode, but don't count on pre-v7.53 or other applications accepting them for all cases for all encoding types.
* This version of Base32 is different than the base32 used in $totp and $hotp. Base32 uses a 32-item alphabet consisting of upper-case A-Z and the numbers 2-7. However, in addition to accepting base32 as case-insensitive, $decode also accepts these invalid numbers the same as if valid characters were used: Number 1 as if the letter L, Number 8 as if the letter B.

.. code:: text

    //var -s %a $encode(PWETA,a) | echo -a $decode(%a,a) vs $decode($replace(%a,8,b,1,l),a) vs $decode($lower(%a),a)

Encryption
^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - c
      - CBC encryption mode defaults to using a mirc-generated pseudo-random binary salt. Adds 16-byte header inside u/m/a/v encoding: %Salted% $+ 8-byte-random-binary-salt.
    * - e
      - ECB encryption mode, 'sir' switches become invalid.

.. note:: 'c' is ignored if both of the conflicting c/e are used. Using 'c' or 'e' requires the key Parameter#3 be present. If the key is blank, instead of being an invalid parameter, it substitutes as if the user used a key consisting entirely of 0x00 bytes.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - l
      - Literal key parameter used as key. For 'c' this avoids using an algorithm to hash the key parameter. For 'e' this changes the key length limit from 72 down to 56 bytes. However $encode allows using 'cl' but ignores it when you do not use 's'.
    * - s
      - user defined 8-byte salt instead of random. (valid only when 'c' also used) When shorter than 8 bytes, is padded to 8 using 0x00 bytes. Same 16-byte header as non-s, except the 8-byte salt is the 1st 8 bytes of Parameter#4. Salt is interpreted in ANSI mode without encoding codepoints 128-255 to 2 bytes, and codepoint >255 is an invalid parameter. Warning: $encode truncates a string longer than 8 instead of treating as an invalid parameter
    * - r
      - random IV (valid only when 'c' also used. Adds 16-byte header inside u/m/a/v encoding: RandomIV $+ X... where X is the randomly generated literal IV.  When not using 'l', this uses a hash method that's much weaker than the algorithm used for salted keys.
    * - i
      - same as 'r' except uses user-defined string provided in Parameter#4 using same string handling rules as used when that parameter is a SALT belonging to the 's' switch. If also used alongside 'r', the string placed inside the 16-byte header is the user-defined string instead of random. If 'r' is not used, the exact same key/iv is used, except there is no 16-byte header inserted in front of the ciphertext. 's' and 'i' should not be used together, as 'i' causes 's' to be ignored. Random IV/Salt created in the absence of Parameter#4 can contain 0x00 bytes in any position.
    * - z
      - 1-8 0x00's padding ( no more than 1 of 'z n p' should be used at the same time)
    * - n
      - padding 0x80 plus 0-7 0x00's
    * - p
      - 1-8 0x20 spaces padding
    * -  
      - Padding when none of 'znp' used = PKCS#7: Append N bytes of $chr(N) where N is 1-8

Notes:
* Using the 'v' Z85 encoding added in v7.73 has the advantage that it encodes the Blowfish binary into shorter strings than mime, due to encoding 4 binary as 5 text instead of encoding 3 binary as 4 text. For example, a ciphertext of 336 bytes which encodes as length 448 using 'm' mime would encode as length 420 using 'v' Z85, and would have a better chance of fitting within the fixed limit of an IRC message. However, because the Z85 alphabet contains characters such as $ % # etc, you must be careful to avoid using it in contexts where it could be double-evaluated in places such as a timer command string other other places described in :doc:`injection </beginner/injection>`
* 'N' chunk parameter uses the same rules as non-encryption. It's an optional extra parameter past those required by the presence of other switches ('ec' require Parm3 <key>, 'c(s|i)' also require Parm4 <salt|iv>)
* 'e' ECB mode is invalid syntax with switches 's|i|r'. In ECB mode, same key always encrypts identical groups of 8 plaintext bytes into the same 8 ciphertext bytes. Key is always literal UTF-8 'key' parameter of 0-72 bytes, except 'l' switch limits literal ECB key to 56.
* 'c' default random salt allows same key to create different session-key:IV each time salt differs. If 8-byte random salt is randomly distributed across all 2^64 values, would require more than 2^32 messages before 50% probability of any 2 matching 'salt' values.
* Salt/IV parameter is silently truncated to 8 bytes, and uses 0x00 byte padding to length 8 if shorter. Parameter#4 is interpreted in ANSI mode, where ASCII 128-255 are not UTF-8 encoded into byte-pairs and codepoint > 255 are invalid.

* Blowfish 'c' encryption by default has 16-byte header beneath the encoding: The 8-byte string %Salted% followed by 8 'random' bytes. If using the 's' switch, the 4th 'salt' parameter is placed in the header instead of the 'random' salt.
* any of s|i|r disables default random salt, and s|i require presence of 4th Salt/IV parameter
* <without s|i|r>  Header is: %Salted% $+ 8-random-bytes
* 's'  changes header to: '%Salted%' $+ Parameter-#4
* 'r'  changes header to: 'RandomIV' $+ 8-random-bytes
* 'ir' changes header to: 'RandomIV' $+ Parameter-#4 (Chopped to 8 bytes or padded with 0x00's to length 8)
* 'i'  without 'r' means Parameter-#4 user defined IV is required, but is kept a secret without adding the 16-byte header to the encrypted string which reveals the IV.

Note that older mIRC versions had different handling of various parameters which differ from the current improved handling. For example some older versions allowed Salt/IV parameter containing codepoints > 255 then interpreted as $chr(63). Non-literal key strings are currently limited to 100+$maxlenm, but there were 3 other length limits in the past. Some past versions truncated the randomly generated salt if it contained any 0x00 bytes, but did not do the same for random IV's

.. note:: 'i' is the only option that does not ''"blow your cover,"'' as any of the other (s|r|ir|<none>) options above will positively identify that the message is Blowfish encrypted by placing a plain-text header ("%Salted%" or "RandomIV") at the beginning of the encoded digest, along with the Salt/IV that was used.  Using 'i' will be the most popular choice for this reason.  You must provide a #4 parameter, but you can leave it empty for all 0x00's IV, or use a predictable changing IV like the current time, an incriminating nonce, or use it as a second 8-character secret password.

maroon alternate note: 'ci' cannot be the popular choice without a way for the decrypter to know the IV used when encrypting. You should not use a constant salt/IV of all 0x00's or any other value because their purpose is to be a unique string for each message encrypted using that key. You should not use the $ctime string as your salt/IV because $encode silently chops the 10-char string to length 8, causing all messages for a 100-seconds period to be encrypted using the same Salt/IV, which for identical plaintexts would 'blow your cover'. Even if using the right-most 8 bytes of $ctime to avoid this, it still allows collisions with other users of a shared KEY also using $right($ctime,8) due to everyone using the same narrow group of salt/IV values which slowly shift together across time, and would require either including a 'blow your cover' string in the encrypted string or require brute force guessing to find the correct value. Blowing your cover can include sending mime strings which always decode to a multiple of length 8. Solutions can be, as described in examples: Stripping the 1st 8 bytes of the header but leaving the random salt/iv and having the decryptor insert the text header before feeding to $decode. Also, 'blow your cover' can include using a salt parm left in the encoded string which never contain the 0x00 byte, or worse if they are always simple alphanumeric text. You can minimize this issue by using the $randsalt alias for creating random Salt/IV parms if needing to communicate with the past versions which did not correctly handle random salts containing 0x00 bytes, or using the examples below which avoid storing the "%Salted%" or "RandomIV" string in the header, but leave the other (hopefully) random Salt/IV parm generated by the 'c' or 'cr' switch combos. Also, 'ci' should be avoided because $decode is designed to ignore the switch combo in certain rare cases.

maroon conclusion: Popular choice should be:
1. Avoid using Blowfish function prior to v7.58, as it fixes several weaknesses and security vulnerabilities mentioned here. v7.72 also has a fix that should not affect people who do not use extremely long key parameter strings
2. Use either no-padding-switches or 'n' to avoid false matching the original message as if padding.
3. If using v7.56+, use 'c' without the 's' switch to have a random salt. If worried about the '%Salted%" header, you can script the removal/reinstatement of the header as in example below.
4. If using <= v7.55, use 'c' WITH the 's' switch, but use the $randsalt alias to define a random salt string which cannot contain embedded 0x00's. This avoids a bug where embedded 0x00 bytes in the Salt causes many unique salt strings to generate identical salted keys. Be sure to avoid non-literal keys longer than 56 bytes in v7.52-7.55, as bytes 57+ are silently ignored. Later versions silently ignored key parameter strings longer than 612 bytes, 
5. Always avoid using 'r' and/or 'i' switches without the 'l' switch, because the method used to hash the key parameter lowers the strength of the key parameter down to 'only' 128 bits. Even a literal key of 56 hex digits with the 'l' switch would've had 2^224 possible combos.
6. Avoid using the 'ci' without 'r' switch combo. The broken design for $decode can cause a GPF crash in versions 7.57+earlier, or incorrect decryption in v7.58+.

Padding of 8-byte blocks with 1-8 bytes of padding ensures encryption sees binary message length as exact multiple of 8. Padding is added by $encode depending which of the 'n|p|z|none' padding switches are used.
* default: if 'npz' not specified, PKCS#7 padding = appends 1-8 of $chr(N) where N is the number of bytes to be padded. ie: padding length 1 = $chr(1), 2 = 2x $chr(2)'s, ..., 8 = 8x $chr(8)'s
* 'n' Bit Padding = Appends $chr(128) character followed by 0-7 0x00's
* 'p' Appends 1-8 $chr(32) spaces
* 'z' Appends 1-8 0x00 nulls
* Due to the broken by-design behavior of $decode, the 'z' padding switch should NOT be used, even for text messages which cannot contain the 0x00's appended by 'z' padding. Instead of removing the indicated type of padding, $decode ignores any padding switches used, and instead searches for all 4 supported types of padding. The attempt to match 'z' padding has a false match with 'n' padding if the plaintext ends with the 0x80 byte and the length of the plaintext is not already a length that's a multiple of 8, as happens for ALL unicode codepoints 128+ which are a multiple of 64. You cannot reliably detect use of bad keys by checking the length of the decrypted string, because decrypting with the wrong password has a 4/256 chance of false matching padding due to matching at minimum final byte values being any of the 4: 0x00 0x20 0x01 0x80. Example of the final character of the text message being destroyed by using 'z' padding:
//bset -t &v 8 0 | while (8 // $bvar(&v,0)) { bset -tc &v 1 $str(.,$r(1,7)) $+ $chr($calc(64*$rand(3,800))) } | echo -a original: = $bvar(&v,1-) displays as: $bvar(&v,1-).text | noop $encode(&v,bmcz,key) $decode(&v,bmcz,key) | echo 4 -a decrypted = $bvar(&v,1-) displays.... as: $bvar(&v,1-).text

'p' padding is OK to use with text messages where removing 1-7 extra trailing spaces is harmless. But due to the broken $decode handling of padding, you should avoid using 'z' padding, and is best to use only the 'n' switch or PKCS#7 from no-padding-switch used.

If possible, use mIRC version v7.58+ which fixes most of the security/design issues with $encode. Starting with v7.56:
1. 'c' used without 'l' switch for non-literal keys no longer silently chops hashed key parameter to 56 bytes, and instead silently chopped at 612
2. 'i' and 's' switches no longer permit Parm#4 Salt/IV strings containing codepoint 256+ which formerly were each silently replaced with the same codepoint 63.
3. Salts are now treated as 8-byte binary strings the same as IV are, instead of being truncated at the first 0x00 byte, which happens with the 3% of 8-byte random strings where at least 1 bytes is 0x00. This formerly resulted in a significant portion of unique random salts being treated as if identical. i.e. 1/256 of all random salts began with 0x00, and were all treated as identical $null salt.
Remaining security issues your script needs to avoid:
1. $encode/$decode accept invalid $null key parameter, so you must either verify if %key is $null, or use $$+(%key) to halt it if it's $null
2. $encode accepts invalid 's|i' parameters longer than 8 bytes, then silently chops them to the valid length 8 bytes.
3. $decode's by-design ignoring padding switches and instead searching for match with 4 types of padding means you should avoid using 'z' padding when there's a possibility that the final UTF8-encoded byte of the message is 0x80, so you should either use 'n' or no-padding-switch.

Incompatibilities between v7.56+ and earlier versions due to fixing bugs causing incorrect encryption/decryption in older versions. Possible workarounds are explained in more detail at https://forums.mirc.com/ubbthreads.php/topics/265396/re-invalid-key-lengths-in-encode-data-lt-e-l-cl-gt-key#Post265396
1. For the approx 3.1% of random 64-bit salt strings which contain at least 1 0x00 byte, the incompatible salt string handling can make it difficult to manipulate old messages so they can be decoded in new mIRC, but is generally impossible for older mIRC's to decode those 3.1% of messages created in newer mIRC.
2. For older messages created where byte values 57+ of the key parameter are ignored, v7.56+ can use $left(key parameter,56) to decode them, as long as the 56-byte string does not end with a partial UTF-8 character encoding.
3. For older messages created using 's|i' parameters containing codepoints 256+, these were encrypted using the '?' character instead, so v7.56+ can simply use the '?' in all salt|IV parameters which formerly included those characters, which are now invalid.
4. Using 'ci' without 'r' should not be used because of the 2 cases per 4 billion where decrypted messages are either missing the first 16 decoded bytes or the output is garbled. This is due to $decode incorrectly ignoring the 'ci' switches used if the data happens to be encrypted into ciphertext beginning with the binary bytes happening to form the magic RandomIV or %Salted% strings. If you do use this switch combo, you should check check if the encrypted mime string begins with either UmFuZG9tSV or U2FsdGVkX1, and if so you should place the encrypted string into a binary variable then use ONLY the the 'm' switch to test if the ciphertext begins with either of the 2 magic strings.

The strongest known attack against Blowfish is the SWEET32 attack against the 64-bit block size. You can mitigate this problem by avoiding the encryption of hundreds of megabytes of data using the same encryption key, because SWEET32 is looking only for massive amounts of ciphertext using the identical binary key. A random+unique salt is enough to defend against this attack, since each message then uses a different encryption key. Note the SWEET32 attack works against using the identical encryption key with a random literal IV created from the 'r' and/or 'i' switches, and cannot be defended against by using a longer encryption key. This means that when using $encode's encryption, you should use a randomly changing salt, without using the 'i|r' switches. Even if the salt being used is a sequential counter which is predictable and could be duplicated between users in a small number of messages, the fact that the salt+key_parameter combo is identical in only a very small number of 8-byte blocks means the SWEET32 method has very little data to work with, and as long as users avoid using the same sequence again, that salt will not be repeated where the SWEET32 attacker could use it. Because $right($ticks,8) can repeat against your past messages prior to reboot, it should not be used. $right($ctime,8) should be enough to avoid repeating your own SALT2 as long as the key_parameter is changed prior to that value repeating every 3.1 years. However this still has the problem of frequently matching a salt by another user sharing the same key

Examples
--------

Echo to the active screen the following encode text, using Mime (base64) encoding:

.. code:: text

    //echo -a $encode(Hello there! This will be encoded using Mime.,m)

Mime encodes 3 input bytes as 4 output text characters using a 64-item alphabet, padded with '=' to a length that's a multiple of 4.

.. code:: text

    The 'N' parameter is ignored by $decode, but is used to encode individual chunks of long binary variables, potentially chopping UTF8 encoding characters across separate chunks. When 'N' is 0, returns the number of chunks in the input string, otherwise for N >= 1 it encodes the Nth group of 45 bytes in the input string. Note how this example splits the encoding, resulting in chunk 1 ending with the alt+195 byte and the chunk 2 begins with the alt+169 byte:
    
    //var -s %a $str($chr(233),100)) , %b $encode(%a,m,1) , %c $encode(%a,m,2) , %d $decode(%b,m) vs $decode(%c,m)

.. code:: text

    $encode encrypts the string then applies u/m/a coding to change binary encrypted data to text.
    Decoding with matching u/m/a without using e|c displays the header and cipher binary hidden beneath (some strings can be truncated when 0x00 are encountered in decoded mime string):
    
    //var %a $encode(text,csm,key,ParmSalt) | echo -a %a -> $decode(%a,m)

.. code:: text

    /*
    These are 2 methods of encrypting channel messages where everyone in a channel uses the same shared password. They intentionally does not support '/me action' or /query windows, and handle only 1-word messages of length 25+. To defend against different users unknowingly using the same salt, the messages include the sender's nick as part of the key, which causes the same salt to NOT generate the same encryption key. Message is encrypted using a random salt, but the '%Salted%' header is removed from the mimed string before sent to channel, then added to message before decryption. Add 'g' switch to echoes to avoid them being logged.
    */
    ON *:TEXT:=*:##maroon,#channelname: { if (($2 != $null) || ($len($1) < 25)) return | fake_secret_chat $1 }
    ON &*:INPUT:##maroon,#channelname:{ if ((/* iswm $1) || ($ctrlenter) || ($inpaste)) return | fake_secret_chat $1- }
    ON *:CONNECT:{ if (!$hget(secret_chat)) hload secret_chat secret_chat.txt }
    ON *:EXIT:{    if ( $hget(secret_chat)) hsave secret_chat secret_chat.txt }
    
    ; remove the number from either alias name ending with chat1 or chat2
    alias fake_secret_chat1 {
      if (!$chan) return
      ; //hadd -m secret_chat $network $+ ##maroon Change this Shared Secret
      var %main_key $hget(secret_chat,$network $+ $chan)
      if (%main_key == $null) { echo -g $chan Note: Secret_Chat halted due to missing password! add password: /hadd -m secret_chat $network $+ $chan Password goes here | return }
      if ($event == input) {
        bset -tc &secret_chat_msg 1 $encode($1-,mc,$me %main_key) | noop $decode(&secret_chat_msg,bm)
        bcopy -c &secret_chat_msg 1 &secret_chat_msg 9 -1 | noop $encode(&secret_chat_msg,bm)
        msg # = $+ $bvar(&secret_chat_msg,1-).text | echo 3 -tc own # Channel sees Encryption of: $+(<,$nick($chan,$me).pnick,>) $1-
        halt
      }
      else {
        bset -tc &secret_chat_msg 1 $mid($1,2) | noop $decode(&secret_chat_msg,bm)
        bcopy &secret_chat_msg 9 &secret_chat_msg 1 -1
        bset -t &secret_chat_msg 1 %Salted% | noop $encode(&secret_chat_msg,bm) $decode(&secret_chat_msg,bmc,$nick %main_key)
        echo -tcl normal # Decoded $+(<,$nick,>,:) $bvar(&secret_chat_msg,1-).text
      }
    }
    
    /*
    This is a more complicated channel encryption, which includes a shared salt contained in the #channel topic, allowing the same shared password to behave similar to an unrelated password each time the #topic salt changes. This uses a superior method to hash the key parameter without using MD5. Each message generates a new 9-byte string where each byte can be values 0-255, and the 12-byte mime-encoding of this string is included in the message sent to the channel, instead of the actual IV or Salt used to encrypt the message. This mime-string + sender's nick + topic salt + main password are hashed with SHA-512 to create a 64-byte secret string which is split into a 56-byte literal key parameter and an 8-byte salt parameter. Since text salt parameters are truncated if they contain embedded 0x00 bytes, the 9-byte message salt is changed to avoid strings where the 1st 7 bytes contain the 0x00 byte. The attacker cannot know either the key parameter or the IV without also knowing the %main_key for that channel. Assuming the 9-byte string is generated randomly, the only way to identify which of the 2 aliases was used to encrypt the message is whether the mimed string's length is 8N or 8N+1.
    */
    
    alias fake_secret_chat2 { if (!$chan) return
      ; //hadd -m secret_chat $network $+ ##maroon Change this Shared Secret
      noop $regex(foo,$chan($chan).topic,salt:(\S+) ) | var %chan.salt $regml(foo,1)
      var %main_key $hget(secret_chat,$network $+ $chan)
      if (%main_key == $null) { echo -g $chan Note: Secret_Chat halted due to missing password! add password: /hadd -m secret_chat $network $+ $chan Password goes here | return }
      if ($event == input) {
        :make_another_salt
        bset -c &secret_chat_salt 1 $regsubex(foo,$str(x,9),/x/g,$rand(0,255) $chr(32))
        noop $encode(&secret_chat_salt,bm) | var %msg.salt $bvar(&secret_chat_salt,1-).text
        bset -c &secret_chat_digest 1 $regsubex(foo,$sha512(%msg.salt $me %chan.salt %main_key %chan.salt),/(..)/g,$base(\t,16,10) $chr(32))
        if ($istok($bvar(&secret_chat_digest,1-7),0,32)) goto make_another_salt
        var -p %iv $regsubex(foo,$bvar(&secret_chat_digest,1-8),/(\d+)\s?/g,$chr(\t))
        noop $encode(&secret_chat_digest,bm)
        var %session_key $bvar(&secret_chat_digest,12,56).text , %text $encode($1-,mcli,%session_key,%iv)
        var %msg $+(=,%msg.salt,%text) | msg # %msg | echo 3 -tc own # Channel sees Encryption of: $+(<,$nick($chan,$me).pnick,>) $1-
        halt
      }
      else {
        bset -c &secret_chat_digest 1 $regsubex(foo,$sha512($mid($1,2,12) $nick %chan.salt %main_key %chan.salt),/(..)/g,$base(\t,16,10) $chr(32))
        var -p %iv $regsubex(foo,$bvar(&secret_chat_digest,1-8),/(\d+)\s?/g,$chr(\t))
        noop $encode(&secret_chat_digest,bm)
        var %session_key $bvar(&secret_chat_digest,12,56).text , %text $decode($mid($1,14),mcli,%session_key,%iv)
        echo -tc normal # Decoded $+(<,$nick,>,:) %text
      }
    }

If using pre-v7.56 random salt, or if using 'ir|s' switches to create user-defined Salt's or IV's, you SHOULD use the $randsalt alias to salt strings from the entire valid text range of codepoints 1-255. This increases the possible combinations to as high as 255^8, which is the 96.9% of valid 8-byte strings which don't contain the 0x00 byte. This makes it much less likely where the birthday paradox produces messages with identical salt/iv's.

.. code:: text

    alias randsalt returnex $regsubex($str(x,8),/x/g,$chr($rands(1,255)))
    alias randsalt returnex $regsubex($str(x,8),/x/g,$chr($rand( 1,255)))
    alias randsalt {
    :retry | var %a $regsubex(foo,$str(x,8),/x/g,$rands(0,255) $chr(32)) , %i 1 , %j 2
    while (%i isnum 1-7) { if (($gettok(%a,%i,32) == 0) && ($gettok(%a,%j,32) > 0)) goto retry | inc %i | inc %j }
    returnex $regsubex(foo,%a,/(\d+)\s*/g,$chr(\t))
    }
    (1st variant uses $rands, 2nd uses $rand, 3rd allows salt to contain 0x00 if not preceding byte values 1-255)

.. note:: Because 'r' switch is CBC mode without authentication, the decrypted message is vulnerable to trace-less bit-flipping of the 1st 8 bytes of the message into anything the attacker wishes by simply manipulating the IV and knowing the exact contents of the 1st 8 bytes of the plaintext message. The attacker does not need to know the key, nor even need to see how the message has been encrypted. This is not a Blowfish weakness, as the same thing would happen with AES where the larger blocksize would expose 16 bytes instead of 8. As an example, use any message where the 1st 8 bytes are all alpha characters and which do NOT contain a space character. Then encrypt with any lower-case text salt, and decrypt with the upper-case equivalent. This results in the decrypted message having the upper/lower case of each text character flipped, but the remainder of the message is NOT affected:

.. code:: text

    //var -s %iv $regsubex($str(x,8),/x/g,$rand(a,z)) , %msg $encode(BitFlipping Example,mci,key,$upper(%iv)) | echo -a $decode(%msg,mci,key,$lower(%iv))
    result: bITfLIPPing Example

Solution: If worried about this, you should avoid using the 'i' and/or 'r' switches, and always use either a random or user-defined salt. Using a 'salt' would then hash key_parameter+salt into binary_56_byte_hashed_key+hash_derived_IV, which shields the IV from someone who doesn't know the key. If they tried to bit-flip the salt, the generated encryption key and IV would be completely different, and the message would decrypt to garbage. Another way would be to include 8 garbage bytes preceding the actual message. The garbage bytes would be thrown away and only bytes 9+ of the decoded message are used.

.. note:: If using v7.52-7.55, beware of non-literal key parameter silently chopped to 56 bytes. The following examples always produce identical output in those versions each time the command is repeated, demonstrating silent ignore of key beyond byte 56.

.. code:: text

    CBC hashed-key with salt:
    //echo -a $version $encode(testtest,mcs,$str(a,55) $+ $chr($rand(192,255)) ,saltsalt)
    CBC literal key with IV:
    //echo -a $version $encode(testtest,mcirl,$str(a,55) $+ $chr($rand(192,255)) , (8)bytes)
    ECB literal key:
    //echo -a $version $encode(testtest,me,$str(a,55) $+ $chr($rand(192,255)) )
    CBC hashed-key with IV:
    //echo -a $version $encode(testtest,mcir,$str(a,55) $+ $chr($rand(192,255)) , (8)bytes)

.. note:: 'mc' or 'mcr' or 'mcrl' switch combos also silently ignored the 57th-and-later bytes in those versions, as demonstrated by being able to decode those messages without the full key:

.. code:: text

    //var -s %msg $encode(testtest,mc,$str(a,56) $+ key) | echo -a $version : $decode(%msg,mc,$str(a,56) )

Security flaws remaining with v7.56:

.. code:: text

    1. Allows encrypting where the key parameter is $null:
    //echo -a $encode(message,mc,$null)
    Your script must check to verify that %key is not null, or possibly halt the script such as with $$+(%key).
    2. Silently ignores invalid salt and IV parameters longer than 8, producing identical outputs, such as when using $ctime as the IV during a 100-seconds interval:
    /timer 110 1 echo -sg $ctime : $encode(message,mcs,$null,$ctime)
    (Only difference between 'i' and 'ir' is that 'ir' stuffs the IV parm into the header as if it's random. The extra 16 byte header lengthens the encrypted string. Your script must verify that $len(%saltparameter) is not greater than 8.
    3. Padding is broken because $decode does not let you recover the original message by specifying the 1 of 4 types of padding to remove. Also, other than scripting to check the length a decrypted &binvar, $decode does not warn you that the message did not contain valid padding, and even then it does not warn you if the wrong kind of padding was matched. For every message encoded using 'z' padding that's not a multiple of 8 bytes and which ends with a codepoint that's a multiple of 64 greater than 64 ends with the byte value 128: $decode makes a false match with 'n' padding, causing the final byte of the last character's encoding to be stripped, resulting in the final character of the text being displayed incorrectly. Your script should encode use the 'n' switch or using none of the n|p|z switches. By not warning whether the padding was wrong/missing, this makes it hard to detect whether the string has been maliciously truncated intransit.
    //bset -t &v 8 0 | while ($bvar(&v,0) == 8) { bset -tc &v 1 $str(.,$rand(1,7)) $+ $chr($calc(64*$rand(3,1023))) } | echo -a original: = $bvar(&v,1-) $bvar(&v,1-).text | noop $encode(&v,bmcz,key) $decode(&v,bmcz,key) | echo 4 -a decrypted = $bvar(&v,1-) $bvar(&v,1-).text

.. note:: Your key should be long enough to make it difficult for someone to brute-force guess it. You can't count on the guesser using a mIRC script which contains overhead which slows down the guessing. Beginning v7.56, you can use a longer key parameter up to 612 bytes, and 7.72 increases to 2148 bytes, and that string will be hashed to generate the key, instead of the hashing looking at only the 1st 56 bytes of the key parameter. When using 'r' without 'l', the key parameter is hashed in a way which does not generate more than 2^128 possible keys. The hash is derived using the $md5 function, so $encode(string,mcir,%key,iv) generates identical encryption passwords from all %key which have matching MD5 hash.

When using a salted key ('c' without 'r' or 'i' switches) the hash method has some 448-bit keys which can never be generated from every salt string, but all possible long key parameter strings against a fixed salt can generate well over 2^400 different encryption keys.

While the encryption does not include authentication, that issue can be largely mitigated. Authentication would involve a lengthening of the ciphertext which can make it less likely that the encoded encrypted string can fit within the limited length of an IRC message. However, when using a salt, both the per-message key and per-message IV are a hash result that's shielded from trivial tampering. To defend against the ciphertext being chopped short, if the ciphertext is in a &binvar, you can determine the decrypted padded-message-length inside the ciphertext based on the length of the mime string, so if the decoded string length indicates that no padding was removed, that indicates that the ciphertext was not created by $encode. There is still a small chance that padding can be removed from a truncated message without containing spurious characters, but you can also do something like ending your plaintext always with a string that you never put into the message, like XYZ, and then can check that your decrypted message ends with your magic label.

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$decode </identifiers/decode>`
    * :doc:`$rand </identifiers/rand>`
    * :doc:`$rands </identifiers/rands>`
