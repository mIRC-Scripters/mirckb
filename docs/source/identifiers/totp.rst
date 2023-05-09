$totp
=====

$totp returns  a TOTP (Time-based One-time Password) based on the specified parameters.

See the Wikipedia page for TOTP for more details.

TOTP allows proving that you know a pre-shared secret in a public communications path without actually sending the secret. It assumes that both parties have a clock that is reasonably well in synch, which allows them both to calculate a value based on the secret and the current time, with little better than random chance of replying with the correct number unless you have the 'secret'. This method is most commonly used by Google Authenticator where the most common secret is a randomly generated 160-bit value. While a 6 digit number has only 20 bits of strength against a lucky guess, knowledge of 6 digit numbers within past or future time intervals does not help an observer determine the correct digits for the current interval, except for knowing which of the 2^160 possible keys didn't work in the past.

For security, the verifier should limit how many retries are accepted within each timestep interval, and also limit how many nearby timestep responses are accepted when allowing for the other clock being out of synch. Because the secret is based on $calc(time//timestep), changing the timestep should not be allowed without changing the key and/or hashname. i.e. allowing timestep to change from 30 to 31 seconds means someone observing the timestep=30 response made now would be able to make a correct response at $asctime($calc($ctime * 31/30)) in the future. If both parties need to prove themselves to each other, either both parties should use separate unrelated pre-shared secrets to prove themselves, or if they need to use the same secret, each should use different hashnames in making their response.

Due to a slight bias toward the smallest numbers, it is not appropriate to consider this to be a random N digit number, with the bias increasing as 'digits' increases. The number is created from an :doc:`$hmac </identifiers/hmac>` digest based on combining a secret and the time interval, and reduces a 31-bit portion of the digest to a base10 integer. Because the max 31-bit value is 2147483647, there is a slight bias in an N-digit number toward the numbers <= the rightmost N digits of the 31-bit max. For this reason, digits <= 9 offers 10^digits of security, while digits=10 offers 2^31.

Also causing bias is choosing to use MD5 as the hashname. HOTP/TOTP were originally designed using SHA1 as the hashname, which happened to be the mimimul length where the same bit is never used by the 31-bit value and by the byte used to determine which bytes to use as the 31-bit value. Example below demonstrates this.

Because this uses HMAC to generate the secret, a longer key is not always better. The internal block length for sha256 and shorter hashes is 512 bits, and is 1024 bits for sha384 and longer (32 or 64 binary bytes). If the secret is longer than that 512 or 1024 bits, the secret is then replaced by the binary hashdigit of that longer secret, which reduces the strength. HMAC always pads keys shorter than the 512 or 1024 by appending 0x00 bytes, so all hex keys shorter than the 512 or 1024 are equivalent to longer keys created by '0' right-padding the shorter key. To prevent equivalent keys, either always consistently use the same shorter length, or if allowing for a variable length key, then always include a length-byte with your key while staying within the 512/1024 limit.

Because hex lengths 128 and 256 support the 512 and 1024 bit block lengths, and the longest base32 length of 32 is a 160-bit key, hex format is a universal encoding format, and base32 keys longer than 160 bits must be translated to hex format as described below.

The description here applies to changes as of v7.72, where there were key changes to how key format was guessed and interpreted. Prior versions had timestep range 1-3600, digits range 3-9, lengths for hex and base32 included optional spaces, with hex lengths being 40,64,128 and base32 lengths being all multiples of 8 >= 16. Hex keys were modified by stripping all 0x00 bytes then UTF8 encoding the remaining bytes individually even if the string was already UTF8 text. For prior versions, base32 was the universal key format where hex keys needed to be translated to base32 then having enough 'A' digits appended to make the string length be a multiple of 8.

The /help description states that the key is required, but $totp($null) is accepted, even though the purpose of TOTP is to prove that you know a secret. To defend against %key being accidentally blank, see example below. Also, timestep is restructed to max 48 hours, so using larger valid timesteps requires using timestep=1 then calculating the 'time' parameter as demonstrated below.

You can prevent your text passphrase from being interpreted as base-insensitive base32 by avoiding having the 3 counts of base32 symbols, or by using at least 1 non-space character that is not in the base32 alphabet (A-Za-z2-7). Base32 and hex keys ignore spaces and are case-insensitive, so you can confirm your text key is not seen otherwise by changing the case on one of the letters or moving a space to a different position, and verify this cause the code to change (use a fixed 'time' because the TOTP code changes every 'timestep' seconds)

Synopsis
--------

.. code:: text

    $totp(key[, time[, hash[, digits[, timestep]]]])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - key
      - the key is optional and can be hex or base32 format where the key parameter, excluding spaces, is either a hex string of 40, 64, 128 or 256 digits - or is a base32 string of either 16, 26 or 32 length; otherwise the key parameter is plain UTF8 text. (base32 cannot have '=' padding)
    * - time
      - optional integer [0,2^64-1], default to $ctime
    * - hash
      - optional, hashing algorithm, default to sha1 (Other possibles: sha256, sha384, sha512, md5 )
    * - digits
      - optional, number of digits of output, default to 6 (Valid: 3 thru 10) (The return string is always 'digits' length, left-padded with 0's if needed)
    * - timestep
      - optional floor divisor for the 'time' integer, which causes the result to remain constant for the 'timestep' duration of time. default to 30 when parameter is not a number 1-172800 (48 hours)

.. note:: "Optional" parameters other than the key are not allowed to be $null when defining later parameters, and cause the return string to be $null.

* Output number is the same for all "time" values where $calc(time // timestep) is the same. A script allowing a "grace period" for recognizing digits for multiple timestep intervals must calculate additional results where time=time+timestep and time=time-timestep.

* $totp is equivalent to $hotp(key , $int( $calc(time / $iif(timestep isnum 1-172800,($v1 //1),30))) , hash , digits)

Properties
----------

None

Example
-------

.. code:: text

    //var -s %key example key, %digits $totp(%key) , %ctime $calc($ctime //30*30 + 30) | while ($totp(%key,%ctime) != %digits) inc %ctime 30 | echo -a the digits %digits currently valid will next be valid in a 30 seconds window beginning at $asctime(%ctime)
    
    $totp is a specific usage of $hotp, using the number of timestep intervals as the counter, and using 'timestep' as a floor divisor to ensure the result remains the same throughout a time interval.
    //var %key password , %ctime $ctime , %timestep 30 , %digits 9 , %hash sha256 , %interval $int($calc($ctime / %timestep)) | echo -a interval %interval ctime %ctime $totp(%key,%ctime,%hash,%digits,%timestep) same as $hotp(%key,%interval,%hash,%digits)
    
    Password changing every hour on-the-hour (long intervals are NOT recommended for most usage)
    //echo -a $totp(Secret case-sensitive Pass Key,$ctime,sha512,9,3600)
    
    Because password is short, allowed number of retries and length of interval should be short enough to deter brute-force attempts.
    
    Recognize password reply for the current 30-sec interval plus the prior or following intervals. Uses defaults sha1, 6 digits, and 30 sec interval:
    //var -s %t1 $ctime , %t2 = $ctime + 30 , %t3 = $ctime - 30 , %totp1 $totp(Secret Key,%t1) , %totp2 $totp(Secret Key,%t2) , %totp3 $totp(Secret Key,%t3) , %reply $rand(100000,999999) | if ($istok(%totp1 %totp2 %totp3,%reply,32)) echo Accepted $v1
    
    For internal use only because $ticks is different for everyone, password changes every 2.5 seconds, but not necessarily at :00 seconds rollovers.
    $totp(Secret Key,$ticks,sha256,9,2500)
    
    The RFC does not restrict timestep other than being an integer in the range [0,2^64-1]. However $totp limits the timestep range to [1,172800], and defaults to 30 if the parameter is not used, or is outside that range - valid or not. Because timestep outside the range 1-172800 defaults to 30, must calculate larger intervals separately, by changing timestep=1 and then calculating the adjusted 'time' value.
    
    //echo -a $totp(secret,$ctime,sha256,9,604800) changes every 30 seconds because a weekly timestep is not accepted while $totp(secret,$calc($ctime //604800),sha256,9,1) returns the expected result.
    
    * If you want a daily or weekly digits code, you may want to also adjust for the timezone and possibly the day of the week or the daylight setting.
    * Digits that changes daily at 9am local clock:
    //var -s %interval $int($calc(($ctime -9*3600)  // 86400))
    * Digits that changes daily at 9am UTC:
    //var -s %interval $int($calc(($ctime -$timezone -$daylight -9*3600)  // 86400))
    * Digits that changes weekly on Tuesday at 6pm UTC (where Sunday=0 Tuesday=2 Saturday=6 and 6pm is the 18th hour):
    //var -s %interval $int($calc(($ctime +86400*4 -$timezone -$daylight -86400*2 -18*3600)  // 604800)) | echo -a password for week %interval is $totp(secret,%interval,sha256,9,1)
    
    Since $totp does not quit with an error if the key is blank, your script can prevent using $totp without the valid key:
    * halt script with no message if %key is blank: $totp($$+(%key))
    * halt script with syntax error if %key is blank - requires finding a parameter where it quits with an error message, and 'time' or 'timestep' is not that, as it always returns a result based on *some* number unless it is blank, in which case it returns $null. However you can get it to halt with a syntax error message if the hash parameter is a string not containing a valid hashname, or if the digits parameter is a string that's not an integer in the 3-10 range:
    $totp(%key,$ctime,$iif(%key == $null,foobar,sha1))
    
    This next example should be read before using MD5 as the hashname. Because of the HOTP/TOTP design, using MD5 results in the effect that 1/16th of the time the return value will always be 1 of 8 specific digit values, rather than the expected where using digits 3-9 has close to 1 per 10^digits chance for each number, and using digits=10 having each number returned 1 per 2^31 chance. The alias below calculates 1 million random TOTP codes using sha1 as the hashname, to see how many times any of these 8 10-digit numbers is returned. As expected, the number of matches is most likely zero, with a 1 per 2147 chance of there being 1 match. However changing the hashname to md5 results in the number of matches being approximately 1/16th of the number of tests, or 62500.
    
    //echo -a WARNING: SLOW | var %list 0251658240 0520093696 0788529152 1056964608 1325400064 1593835520 1862270976 2130706432 , %i 0 , %c 0 | while (%i < 1000000) { if ($istok(%list,$hotp($rand(1,999999999999),$rand(1,999999999999),sha1,10),32)) inc %c | inc %i } | echo -a %c matches out of %i results
    
    The above problem cannot be solved by rejecting these 8 results and requiring different ones, because there are other groups of digits which also have the same bias preference, though to a lesser degree. For example, a different 1/16th of the time the result can only be from a different group of 2048 numbers.
    
    If a hex key is shorter than 128 digits (or 256 if hash is sha384 or sha512) and is not one of the magic hex lengths of 40 64, you can make the key be seen as hex by appending enough '0' digits to make it be length 128:
    
    //var -s %key1 $base($rand(0,4294967295),10,16,8) , %key40 $left(%key1 $+ $str(0,128),40)  , %key64 $left(%key1 $+ $str(0,128),64) , %key128 $left(%key1 $+ $str(0,128),128) | echo -a $totp(%key40) same as $totp(%key64) same as $totp(%key128)
    
    Demonstrates that keys longer than the 64 or 128 bytes are replaced by the shorter hash digest of the key. %key1 is seen as text, and %key2 is seen as hex:
    
    //var -s %key1 $str(x,64) $rand(1,999999999) , %key2 $sha1(%key1) | echo -a $totp(%key1) same as $totp(%key2)
    
    The equivalent base32 lengths for the hex lengths 128 and 256 are 103 and 205. However the only 3 base32 lengths are 16,26,32. If you have a base32 key any length up through 103, you can translate it to a hex key of 128 digits and it will return the correct result:
    
    //var -s %base32 $regsubex($str(x,99),/x/g,$rand(a,z)) | bset -t &v 1 %base32 | noop $decode(&v,ba) | var -s %hexkey $regsubex($bvar(&v,1-),/([0-9]+)/g,$base(\t,10,16,2)) | while ($numtok(%hexkey,32) < 64) var %hexkey %hexkey 00 | var -s %hexkey2 $remove(%hexkey,$chr(32)) | echo -a spaces optional in hex key: $totp(%hexkey) same as $totp(%hexkey2)

If you enabled 2FA at Undernet, below is an example of using $totp to provide the needed 6 digit code for it. If you already have Undernet TOTP set up with your phone, if the phone app does not have the ability to show your TOTP secret to you, you can go to the website and disable 2FA, then enable it again, and this time click on 'enter your secret key manually' which will show you a 32-digit base32 string that's split into 8 groups of 4. You can paste them into this example, along with replacing your actual Undernet accountname and password, and this will automatically login to X and add your address cloak. (Versions prior to v7.72 need to delete the spaces)

.. code:: text

    ON *:CONNECT:{
      if ($network == Undernet) {
        .msg x@channels.undernet.org login YourAccountName YourPassword $totp(abcd efgh ijkl mnop qrst uvwx yz23 4567)
        .mode $me +x
      }
    }

Compatibility
-------------

.. compatibility:: 7.42

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$hotp </identifiers/hotp>`
    * :doc:`$hmac </identifiers/hmac>`
    * :doc:`$encode </identifiers/encode>`
    * :doc:`$sha1 </identifiers/sha1>`
    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha512 </identifiers/sha512>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$md5 </identifiers/md5>`
