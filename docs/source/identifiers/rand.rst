$rand
=====

$rand returns a random integer from the specified range. If you supply two strings or characters not beginning with a number, it returns a random character from that range of code points. $r is an equivalent alias for $rand

Synopsis
--------

$rand(number1,number2)
$rand(char1,char2)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
number1,number2 = starting/ending range of integers
char1,char2 = starting/ending characters in range of characters. Valid range $chr(1) through $chr(65535)

.. note:: High/Low endpoints of output range can be used in either order.

.. note:: Through v7.54 numbers must be 0 or greater. Starting v7.55 one/both number can be negative

.. note:: v6.35 returns range as large as 12 9's. Somewhere between v7.1 and 7.54 it changed to allow range 14 9's. Beginning v7.55, range can now be 2^53. Beginning v7.55 $rand returns output from Bob Jenkins' jsf64.

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $rand(1,100)

returns a random number from 1 through 100 inclusive.

.. code:: text

    //echo -a $rand(-5,20)

returns a random number from negative 5 through positive 20.

.. code:: text

    //echo -a $rand(A,Z)
    returns a random upper case from A through Z
    //echo -a $rand(A,z)
    returns upper and lower case letters, but also other ASCII characters in that range of code points, including [ \ ] ^ _ `

.. code:: text

    Random number used as index:
    //echo -a Monty Hall opens Door number 2 to reveal a $gettok(goat goat car,$rand(1,3),32)
    
    display all unique values returned within 100 random values:
    //var %i 100 | var %s | while (%i) { var %a $rand($chr(33),$chr(126)) | if (%a !isincs %s) var %s %s %a | dec %i } | echo -a $sorttokcs(%s,32)
    
    Displays frequency distribution. Random does not mean equal outcomes. It's rare for a dice to roll exactly 10K 6's in 60K rolls:
    //var %i = 60000 , %low 1 , %high 6 | var %nums $str(0 $chr(32),$calc(1+%high -%low)) | var %ticks $ticks | while (%i) { var %a $rand(%low,%high) | var %t $calc(1+%a -%low) | var %b $gettok(%nums,%t,32) | inc %b | var %nums $puttok(%nums,%b,%t,32) | dec %i } | var %c 1 | var %i %low | while ($gettok(%nums,%c,32) != $null) { var %b $gettok(%nums,%c,32) | var %nums $puttok(%nums,$+(%i,:,%b),%c,32) | inc %i | inc %c } | echo -a time: $+ $calc($ticks - %ticks) $+ ms-> %nums
    
    Valid codepoints are 1 through 65535:
    //var %i 10000 , %s , %low 9100 , %high $calc(%low +999) | while (%i) { var %a $rand($chr(%low),$chr(%high)) | if (%a !isincs %s) var %s %s %a | dec %i } | echo -a $numtok(%s,32) tokens: $sorttok(%s,32)

Notes
-----

* It does not matter which value is higher, $rand(a,z) is same as $rand(z,a) and $rand(9,1) is same as $rand(1,9)
* If either number has a fraction, it's rounded (not $int) to the nearest integer. $rand(-1.6,1.6) is $rand(-2,2)
* 'number' is allowed to have stripped trailing non-numerics only if neither number is negative
* stripped non-numerics sees to follow same rules as $int() does. $rand(1abc,1e2abc) is $rand(1,100)
* $rand(number,non-number) returns $null, so if you need ASCII range from '1' through 'Z', use $chr($rand($asc(1),$asc(Z)))
* The first character of text strings is used as the starting/ending codepoint.
* Through v7.54, if one of the numbers is negative, it's treated as if the value was the hyphen's non-numeric codepoint 45.
* $rand(foo,bar) returns codepoints from the first character of each value, 'b' through 'f'
* $rand does not claim to create cryptographically secure output. For that type of random number, you can consider using $rands and/or use up to 53 bits of the output of a $hmac digest which uses a random message and a secret key, and use $base to translate up to 53 bits of that string into a base 10 number.
* As of v6.35, valid range was 0-999999999999 (12 9's approx 2^40), and somewhere prior to v7.52 the valid range was increased to be 14 9's, 0 through 99999999999999 (slightly greater than 2^46.5). But a bug did not allow all values within that range to be returned. Even as low as a 24-bit range $rand(0,16777215), nearly a third of v7.54 outputs appear to be rarely or never returned. Those versions also had a modulo bias favoring lower numbers for some range sizes, which can be hard to detect except at large ranges or with large number of test outputs.
* Random does not mean 'equal outcomes'. While it's more likely to have 100 6's from 600 dice rolls than any other individual total-result, only a small portion of groups of 600 rolls would have 100 6's. It is possible, though extremely unlikely, for a 'fair' random $rand(1,6) to return 10 6's in a row. Unless the prior results were caused by a bias in the number generator, the odds of the 11th roll being a 6 remains 1/6th.
* The next 64-bit value output by the jsf64 number generator is 100% determined by the unknown state of the 4 64-bit variables of the RNG state, which can be any of 2^256 possible states. There should be approx 2^192 different states which could have returned the latest 64-bit value, and 2^128 possible states returning that exact combo of 64bit values. This RNG should not have a detectible bias favoring some bits being 0's or 1's, or some numbers being more/less likely when following/preceding certain other numbers. The value appears random due to lack of information needed to know the next number.

Demonstrating bias in v7.54: Paste the command below into any editbox, and the distribution within the range from low to high appears fairly random. However change the 14 9's into 14 6's and 2/3rds of the outputs are in the lower regions of the range. For older versions whose valid range is only as large as 12 9's, shorten the string of 9's to length 12.

.. code:: text

    //var -s %pockets 256 , %array $str(0 $chr(32),%pockets) , %i 25600 , %max 99999999999999 , %div %max / %pockets | while (%i) { var %t $calc(1+ ($rand(0,%max) / %div)) , %a $gettok(%array,%t,32) + 1 , %array $puttok(%array,%a,%t,32) | dec %i } | echo -a %array = $calc($replace(%array,$chr(32),+))

In v7.55+ the above alias can increase %max to $calc(2^53-1) without obvious bias.

If worried that your large range has some 'impossible' outputs, you can use the slower randpatch alias to create output which combines the output from 5 smaller ranges. You can test randpatch by substituting it in place of $rand in the above command.

The %throwaway_above calculation discards the highest values which caused modulo bias when shrinking the outputs down to the requested range, preventing 1 or more of the lowest outputs from having an extra input when allocating the 2^53 possible inputs among the possible outputs of the requested range. 

.. code:: text

    alias randpatch {
      if (($1 !isnum) || ($2 !isnum)) goto error | var %lo $int($1) , %hi $int($2)
      var %diff %hi - %lo , %out_range %diff + 1 , %max.val $calc(2^53-1)
      if ((%hi > %max.val) || (%diff > %max.val) || (%lo < $calc(-(2^53)))) goto error
      var %throwaway_above $calc(%max.val - (((%max.val % %out_range) + 1) % %out_range) )
      var %int53 $get_53bit_rand_num
      while (%int53 > %throwaway_above) { var %int53 $get_53bit_rand_num }
      return $calc(%lo + (%int53 % %out_range))
      :error | echo -sc info2 *$randpatch(Num1,Num2) MinN1:-2^53 MaxN2/range.max:+2^53-1 | halt
    }
    alias -l get_53bit_rand_num {
      return $calc($r(0,255) + $r(0,2047) * 256 + $r(0,2047) * 524288 + $r(0,2047) * 1073741824 + $r(0,4095) * 2199023255552)
    } ; 53bit value from joining bit sizes 12:11:11:11:8

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$r </identifiers/r>`
    * :doc:`$rands </identifiers/rands>`
    * :doc:`$hmac </identifiers/hmac>`
    * :doc:`$base </identifiers/base>`
