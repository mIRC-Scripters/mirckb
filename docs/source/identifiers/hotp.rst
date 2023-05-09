$hotp
=====

$hotp returns an HOTP (HMAC-based One-Time Password) based on the specified parameters.

Synopsis
--------

.. code:: text

    $hotp( [key] , count [, hash [, digits ]])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - key
      - The can be in a base16 format of either 40, 64 or 128 chars; or in a base32 format (not containing the '=' character) of any length that's a multiple of 8 greater than length 8; or plain text. The "Google Authenticator format" is implemented by allowing the base32 and base16 lengths to be upper/lower case-insensitive and optionally contain spaces, where the string length is evaluated before removing spaces, instead of the correct method where the string length is verified after spaces are removed. Also incorrect is allowing the spaces to be present when not following exactly 4 encoding characters. If the 40/64/128 lengths of base16 contain an odd number of non-space hex digits, the decoding method is undiscovered. For even-number count of hex digits, the hex is decoded to binary, with 0x00 bytes discarded. The remaining bytes are individually UTF-8 encoded. The correct method should have been to use these 3 lengths are the hex encoding of binary strings of length 20/32/64 bytes.
    * - count
      - required. The 'counter' should never be used more than once with the same key, as it always returns the same number for the same number value. This is a 64-bit number with valid range 0 through 2^64-1. Non-numeric are removed from the end, and "+" removed from the beginning.
    * - hash
      - optional, hashing algorithm, default to sha1. Also allowed: sha256, sha512, sha384, md5
    * - digits
      - optional, number of digits, default to 6. Valid range 3 through 9.

.. note:: /help says the key is required, but $hotp(,0) is valid syntax and returns same as when the key is all 0x00's.

Properties
----------

None

Details
-------

The /help describes 4 formats for the key. Here is the sequence of parsing:.

Rule #1. If key is a length 40/64/128 case-insensitive string that's a mix of spaces and/or case-insensitive hex digits, spaces are removed then the remaining pairs of hex digits are translated into a byte value. If the pair of hex digits is value 00, it is not added to the key. Otherwise, the byte values 1-255 are individually UTF-8 encoded and added to the key string. When there are an odd number of space characters causing an odd number of hex digits, the key is created in an un-discovered way where shifting the location of the spaces in the original string doesn't alter the output.
Rule#2. Else: If key length is 16 or greater and a multiple of 8 (except for matching rule #1) containing only A-F 2-7 a-f or spaces, and if removing spaces results in a valid case-insensitive Base32 encoded string, the spaces are stripped from the string, and the key is the binary decoded contents whose length is approximately 5/8ths the length of the remaining Base32 string. The decoded binary bytes are used as the key, with no 0x00's stripped and no UTF-8 encoding as done in #1 for hex-encoded strings.
Rule #3. Else: Any remaining strings not matching the 1st 2 patterns are considered literal case-sensitive text keys, and the input is assumed to already be UTF-8 encoded where necessary.

.. note:: The actual Google Authenticator format should be: Case-insensitive base32 string of length 16/26/32 encoding a key of 80/128/160 bits, not the 16/24/32 lengths decribed in /help. Base32 string can optionally have spaces inserted into that 16/26/32 character string only if immediately preceded by exactly 4 base32 characters. The purpose of adding spaces is to improve accuracy when entering the key by hand into a 2nd device while viewing the encoded string on a 1st device. $hotp is not recognizing the 128-bit key because 26 isn't a multiple of 8, unless it's padded with 6 spaces so the key length is 32 and becomes a multiple of 8. $hotp is not supporting the base32 encoded string padded by spaces into being divided into groups of 4 because that space-padded string isn't a multiple of 8, so you must $remove(key,$chr(32)) before $hotp correctly recognizes the 16 and 32 character strings as 80-bit or 160-bit keys. Instead of supporting length 16/26/32 AFTER spaces are removed, $hotp is incorrectly using base32 strings of lengths 16/24/32 BEFORE spaces are removed, then extended that same behavior to strings whose length including spaces is any multiple of 8 greater than 8.

.. note:: Because $hotp uses decoded base16 strings after deleting 0x00 bytes and then UTF-8 encoding byte values 128-255 into 2 bytes, keys are replaced by UTF-8 encoded text strings an average of 50% longer, and hex strings with 0x00's in different positions produce matching keys. Because the $hmac format appends 0x00's to a key shorter than 512 bits, all strings which decode into the $null string or a string entirely consisting of 1-128 0x00's or have differing number of trailing 0x00's produce identical outputs.

The count parameter should be in the range 0 to 2^64-1. All values greater than 2^64-1 return the same password as when 2^64-1 is used. For 64-bit negative numbers, negative N returns the same password as when 2^64 is added to the negative number. If using a count value greater than 2^53, $hotp correctly translates it to binary, but $calc() does not perform accurate integer math for all values above 2^53.

The OTP in HOTP stands for One Time Password, which is only 'one time' if the application makes sure that the same 'count' value is never used twice. Either the server and the client keep track of the last count used with each key, or each use the current time for a very short interval as defined for $totp().

* This alias shows how $hotp calculates the output number when the key parameter is handled as a literal string and not handled as if it needs to be decoded out of base16 or base32 text. If the outputs are different, that should be because $hotp is handling them as if they're hex-encoded or base32-encoded keys. The HOTP password is calculated as follows:

1. key should be any text string that doesn't match the above rules #1/#2
2. count should be any integer from 0-2^53-1 supported by $calc ($hotp supports up to 2^64-1 but the alias below doesn't)
3. hashname should be any of sha1/sha512/sha256/sha384/md5 - defaults to sha1
4. digits should be any integer 3-9 - defaults to 6

.. code:: text

    ;syntax: //noop $fake_hotp(key,count,hashname,digits)
    alias fake_hotp {
      var %count $gettok($2,1,46) , %hash $3 , %digits $gettok($4,1,46)
      if (%digits !isnum 3-9) var %digits 6 | if (!$istok(md5 sha1 sha256 sha512 sha384,%hash,32)) var %hash sha1
      if ((%count !isnum 0-) || ($1 == $null) || !$isid) { echo -stc info *$fake_hotp(<key>,<count>[[,hashname],digits3-9]) | return }
      bset &count 1 $regsubex($base(%count,10,16,16),/(..)/g,$base(\t ,16,10) $chr(32))
      var %hmac $hmac(&count,$1,%hash,1) , %offset $calc(1+2*$base($right(%hmac,1),16,10)) , %truncate $mid(%hmac $+ 000000,%offset,8) , %divisor 1 $+ $str(0,%digits) , %num $and($base(%truncate,16,10),$calc(2^31-1))
      echo -a key: $1 keylen $len($1) count: %count hash: %hash digits: %digits hmac %hmac offset %offset truncate: %truncate num: %num calculated hotp: $right(000000000 $+ $calc(%num % %divisor ) , %digits) compare to $ $+ hotp: $hotp($1,%count,%hash,%digits)
    }
    
    * Note: Even though HOTP supports hash=md5, you should avoid using md5 because HOTP was not designed for hashes shorter than 160 bits, and a few values are returned a high percentage of the time. When the hmac string ends with 'f', md5 gives only 8 possible passwords. When the output is 6 digits, each output number should appear approximately once per 1 million random tests. Below is a very slow alias that calculates a 'random' $hotp number. It shows there are 8 outputs which appear over 60000 times in a million tests when using md5 as the hash:
    
    //var %list 658240 093696 529152 964608 400064 835520 270976 706432 , %i 0 , %x 0 | while (%i < 1000000) { if ($istok(%list,$hotp($rand(1,9999999),$rand(1,9999999),md5,6),32)) inc %x | inc %i } | echo -a 8 passwords appeared %x out of %i times
    
    This is not due to the weakness in the hash output of md5, but instead is caused by how the 32-bit 'truncate' value is chosen from within the shorter md5 hash, often at offsets where - not only are there not 8 hex digits available at that position, but often one of the 8 hex digits used is the same digit used to determine the location of the 31-bit value. When using md5 as the hash, every implementation of HOTP i've seen appends hex digit 0's when there are only 2/4/6 hex digits available at that offset in the hash digests, causing some outputs to appear much more often than they should. SHA1 is a long enough hash digest which doesn't need to append the 0's and doesn't ever re-use the locator hex-digit as part of the 31-bit value. 

Examples
--------

.. code:: text

    ; //noop $handshake($nick,#channel)
    
    alias handshake {
      inc %handshake_counter
      var %a $hotp(%secret_key,%handshake_counter,sha256,6)
      if ($1 ison $2) /notice $1 password is %a for counter %handshake_counter
    }
    
    In a perfect world, both sides of the handshake keep track of the last counter used, then increment it to create a new output value without publicly sharing that counter. If one side of the transaction loses the data, there needs to be a mechanism for both sides to agree on a new counter without reusing a counter. Probably the best method is to either select a new key+counter, or select a new counter that's guaranteed to be greater than the previously used counters, such as using $ctime.
    
    //var %a 1234567890 , %a2 $encode(%a,a) | echo -a key %a is $hotp(%a,1,sha512) key %a2 is $hotp($encode(%a,a),1,sha512)
    Both return identical passwords because the 2nd usage identifies the key as a valid Base-32 encoded string that's a multiple of 8 greater than 8.
    
    //var %a $str(A,16) | echo -a $hotp($upper(%a),1) $hotp($lower(%a),1)
    These return the same value because they are recognized as valid Base32 encoded strings, regardless of upper/lower case. To ensure your key cannot be mistaken for a case-insensitive Base16 or Base32 encoding, you should prevent your key from having a length that's a multiple of 8 and which also matches rules #1 or #2 above.
    
    //var %a A , %b $base($asc(%a),10,16,2) , %key1 $str(%a,20) , %key2 $str(%b,20) | echo -a key %key1 is $hotp($str(%a,20),1,sha256) - key %key2 is $hotp($str(%b,20),1,sha256)
    Both return identical passwords because the 2nd usage identifies the key as a valid Base-16 encoded string of length 40,64, or 128 which decodes to the identical string.
    
    Both above encoded strings return the same value regardless whether the encoded string contains upper or lower or a mix of upper/lower characters.
    
    //var %a $str($chr(233),20) | var %b $str($base($asc(%a),10,16,2),20) | echo -a key %a is $hotp(%a,1,sha256) key %b is $hotp(%b,1,sha256)
    This pair also return identical passwords, showing that HOTP UTF8-encodes the underlying decoded hex strings before including them in the key.
    
    //echo -a $hotp(11223344556677889900aabbccddeeff11223344,1)
    //echo -a $hotp(112233445566778899aabbccddee00ff11223344,1)
    In addition to UTF8-encoding bytes in a hex string of length 40/64/128, $hotp also removes decoded 0x00's from the decoded output. The above keys are identical except the '00' was cut/pasted to another byte position in the key. Since 0x00's are not added to the key when decoding hex-encoded keys, the output remains unchanged.
    
    //var %digits 3 | while (%digits isnum 3-9) { echo -a %digits $hotp(password,123,sha1,%digits) | inc %digits }
    All passwords are similar, differing only in the number of digits displayed.
    
    //var %a CuRiOsItY KiLlEd ThE CaT | echo -a length $len(%a) $hotp($upper(%a),1) $hotp($lower(%a),1) $hotp(%a,1)
    Mistakenly decodes as if this is a case-insensitive base32 string. Changing any character to the number 1 while retaining the length 24 changes this into a case-sensitive literal string because the string no longer contains only case-insensitive characters from the base32 alphabet. Even though $decode handles the number 1 as the letter L and number 8 as the letter B, $hotp/$totp do not.
    
    //echo -a $hotp(test,123) $hotp(test,123abc456)
    Identical results because mIRC removed non-numeric string front the end of the 'counter' parameter.
    
    //echo -a $hotp(test,abc) $hotp(test,def) $hotp(test,0)
    Identical because non-numeric count parameters are treated as if count is zero.
    
    //var %key $regsubex($str(x,40),/x/g,$iif(\n <= 24,$chr($calc(97+ (\n % 6))) $+ $chr( 0),$chr($calc(97+ (\n % 6))))) | echo -a $len(%key) key %key $hotp(%key,123,sha256,9) / $hotp($upper(%key),123,sha256,9)
    //var %key $regsubex($str(x,40),/x/g,$iif(\n <= 24,$chr($calc(97+ (\n % 6))) $+ $chr(32),$chr($calc(97+ (\n % 6))))) | echo -a $len(%key) key %key $hotp(%key,123,sha256,9) / $hotp($upper(%key),123,sha256,9)
    Both produce the same output because both are hexadecimal-or-space strings of length 40-or-64-or-128, and after the spaces are removed they have the same case-insensitive hex string.
    
    //echo -a $hotp($str(0,40),9,sha1,9) / $hotp($str(0,64),9,sha1,9) / $hotp($str(0,128),9,sha1,9)  
    //var %key 00 0 00000000000000000000000000000000000 | echo -a $hotp(%key,9,sha1,9) $len(%key) key %key 
    These show that all keys entirely consisting of all 0x00 bytes...
    //var %key 33 0 00000000000000000000000000000000000 | echo -a $hotp(%key,9,sha1,9) $len(%key) key %key 
    //var %key 330 0 0000000000000000000000000000000000 $+ $str(0,24) | echo -a $hotp(%key,9,sha1,9) $len(%key) key %key 
    ... or keys identical except ending with different number of 0x00 bytes produce identical output (hex encoded keys of length 40/64/128)
    
    //var %key 00 0000000000000000000000000000000000000 | echo -a $hotp(%key,9,sha1,9) $len(%key) key %key 
    //var %key 000 000000000000000000000000000000000000 | echo -a $hotp(%key,9,sha1,9) $len(%key) key %key 
    //var %key 000 00 0 0 0 000000000000000000000000000 | echo -a $hotp(%key,9,sha1,9) $len(%key) key %key 
    These produce a different string than the all-zeroes hex string does, showing that keys of length 40/64/128 containing an odd number of hexadecimal digits do strip the spaces before decoding the remaining string, but they do not append or prepend the 0 digit to handle the not-paired hex digit, so they are processing the string in an unknown manner. Moving the space to a different position shows the spaces are stripped before decoding the string into identical keys. Having an odd-number of zeroes in the 40-byte string always returns the same number that's different than the number returned when there's an even number of zeroes. But so far I have not been able to figure out how mIRC decodes a hex string containing an odd number of hex digits.

Warning
-------

Through v7.53, $hmac and $hotp and $totp using hash method sha512 or sha384 and a key whose length is 65-128 returned an incorrect value due to replacing the key with its own hash for lengths 65+ instead of only for 129+.

.. code:: text

    //echo -a $hotp($str(z,65),0,sha512,9) should be 187092660

Compatibility
-------------

.. compatibility:: 7.42

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$totp </identifiers/totp>`
    * :doc:`$hmac </identifiers/hmac>`
    * :doc:`$encode </identifiers/encode>`
    * :doc:`$decode </identifiers/decode>`
    * :doc:`$sha1 </identifiers/sha1>`
    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha512 </identifiers/sha512>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$md5 </identifiers/md5>`
