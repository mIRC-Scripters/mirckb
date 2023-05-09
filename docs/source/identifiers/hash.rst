$hash
=====

The $hash identifier calculates a simple hash of the supplied text. The hash is shown as an integer in the range from 0 to 2^N-1 where N is the number of bits ranging from 2-32. Except for compatibility with legacy scripts, you should probably avoid using this hash for reasons explained in the Notes section. It's possible that $hash() was once the method used by /hadd to put an item into one of the hash table's "buckets", but that was not the case at the point when it was changed to use 'modified FNV-1A'. Alternate solutions are suggested below.

Synopsis
--------

.. code:: text

    $hash(<text>,<N>)

Switches
--------

None
Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - text
      - text string or %variable to be hashed
    * - B
      - Bit length for the returned hash. $hash returns $null if B is a number outside the range 2-32, and returns the original string if the B parameter isn't used. Returned hash is an integer in the range 0 to 2^B -1.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a The hash is $hash(test,32)
    returns: The hash is 1702094848

Notes
-----

The 'fakehash' alias below is based on the code posted here: https://forums.mirc.com/ubbthreads.php/topics/98371/Re:_$hash_function#Post98371

I have not been able to find a string where 'fakehash' returns a different number than $hash.

$hash uses a hash function that is very weak for several reasons. The weaknesses are more easily seen by inspecting the 'fakehash' alias which mimics $hash output, and by showing $hash output as hex instead of a base-10 number. These weaknesses could be why $hash was not also extended to accept binary variables as input when $crc was given this ability. Some weaknesses in $hash include:

* 1. Similar input have similar output hash. Strings of 1-3 bytes are most obvious:

.. code:: text

    //echo -a $base($hash(abc,32),10,16) is $+($base($asc(a),10,16,2),$base($asc(b),10,16,2),$base($asc(c),10,16,2),00)
    returns: 61626300 is 61626300
    
    (i.e. 0x61 0x62 and 0x63 are the hex format for $asc() of the 3 characters a b and c.

* 2. When N is greater than 24, the rightmost extra bits above 24 are always zero, making it effectively a 24-bit hash not a 32-bit. Only 2^24 of the 2^32 values within the range of 0 - 2^32-1 can possibly be hashes. i.e. the least-significant 3 bits of a 27-bit hash are always zero:

.. code:: text

    //var %a $hash($rand(1,999999999),27) | echo -a %a is the same as $and(%a,-8)
    or ...
    //var %i 99999 | while (%i) { var %n $rand(1,99999999) , %bits $rand(25,32) | if ( $right( $base($hash(%n,%bits),10,2,%bits) , $calc(%bits -24) )) echo -a this message will never show | dec %i }

* 3. One of the properties of good hash functions is that each changed bit of the input should change close to half the output bits in a seemingly-random pattern. Changing 1 bit of the input string has minimal change of the bits in the $hash output, often changing output by just 1 bit. $hash() processes the input string 1 byte at a time, and it often takes several additional bytes before the bits altered by the first byte are altered again by another byte.

.. code:: text

    Here, 3 bits changed in the input changes only 1 bit of the output:
    
    //echo -a $base($hash(mIRC,32),10,16) vs $base($hash(mIRD,32),10,16)
    returns: 4952B000 vs 4952B100

* 4. It's easy to create duplicate hashes from different inputs:

.. code:: text

    //echo -a $base($hash(ABCDEF,32),10,16) / $base($hash(ABDDEE,32),10,16)

These collisions are so easy to create that they can be scripted very simply. What you do is change one of the characters of the string by changing the $asc() codepoint of that character by N in either direction. You then find another character in that string whose distance from the changed character is a multiple of 3. You then change that 2nd character's $asc() codepoint in the opposite direction by the same N. So, if someone knows your script is depending on $hash($nick,32) being different for everyone in the channel, they can use this to easily change their nick to have a matching hash as someone else's nick. For example, take the nick 'mastadon', where you can subtract 3 from the 'm' to begin the nick with the letter 'j'. Since the characters 't' and 'o' are 3 and 6 characters distant from the 'm', you can then add 3 to either of their codepoints, and 'jaswadon' or 'jastadrn' will have the same $hash result. In fact, you can split these changes and change the 't' by +2 and the 'o' by +1, and 'jasvadpn' also has the matching $hash.<br>

* 5. One of the properties of a good hash function is that it should be reasonably fast. However $hash is excruciatingly slow compared to $crc.

.. code:: text

    //var %string $str(a,8192), %reps 1000, %t $ticks | while (%reps) { noop $crc(%string,0) | dec %reps } | echo -a ticks: $calc($ticks - %t)
    //var %string $str(a,8192), %reps 1000, %t $ticks | while (%reps) { noop $hash(%string,32) | dec %reps } | echo -a ticks: $calc($ticks - %t)

As of v7.56, on a computer where the 1000 repetitions takes $crc approx 1/10th of a second, the same work using $hash takes longer than 30 seconds.

Instead of using $hash, you would be better off using other substitutes. For example, if you need it to be an integer with a variable 1-32 number of bits, use $crc then use $base to convert from base16 hex to base10 integer then reduce the number of bits:

.. code:: text

    alias crchash { return $calc( $base($crc($1,0),16,10) % (2^$iif($$2 isnum 1-32,$gettok($2,1,46),32)) ) }
    
    //echo -a $base($crchash(mIRC,32),10,16) vs $base($crchash(mIRD,32),10,16)
    returns: F01B6971 vs 6E7FFCD2

If all that's needed is a reasonably unique fast string and the hex output from $crc is ok, then can simply replace $hash(parameter,32) with $crc(parameter,0). While $crc does not provide crypto level ability to make it difficult to create collisions, it does have the property that trivially related strings do not have identical hashes. Based on the 'birthday paradox', it should be expected that out of 2^(32/2) (65536) different strings, that there should be a 50/50 chance of a matching hash pair among them. However because only the 1st 24 bits of the result are ever non-zero, that reduces the number of strings needed for a collision to 2^(24/2) (4096), and since strings actually being hashed tend to be related, the odds of collisions are even higher.<br>

If you want to reduce the chance of collision even further below the ability of the 32-bit result from $crc, beginning with v7.68 the $crc64 identifier can return a 64-bit CRC variant similar to the 32-bit result from $crc, which means the birthday collision property means there would need to be 4 billion strings in order to have a 50/50 chance of a collision.<br>

If the hash needs to be based on a crypto-level hash, or needs more than 32 bits, use up-to-52 bits from $sha1 or $sha512 instead of from $crc. Note that beginning with v7.72 the .bigfloat mode allows accuracy for integers above 2^53, but that can carry extra time cost.

.. code:: text

    alias sha1hash {
      var %sha1 $sha1($1) , %offset $base($right(%sha1,1),16,10) + 1 , %hash13 $base($mid(%sha1,%offset,13),16,10)
      return $calc( %hash13 % (2^$iif($2 isnum 1-52,$gettok($2,1,46),32)) )
    }
    
    //echo -a $base($sha1hash(mIRC,52),10,16) vs $base($sha1hash(mIRD,52),10,16)
    returns: 9AB6235ED89DF vs D2F9CD20CA42B

The above borrows code from $hotp which uses the final digit of the hash to determine which digits within the SHA* hash are used. This next variant is faster, because it doesn't calculate the offset, and it also uses the faster MD5. Because of the 2^53 accuracy limit for $calc, this allows the hash to be up to 52 bits instead of the 32 bits for $hash, and you can easily substitute any of the SHA* identifiers in place of $md5.

.. code:: text

    alias md5hash { return $calc( $base($right($md5($1),13),16,10) % (2^$iif($$2 isnum 1-52,$gettok($2,1,46),32)) )

When the fakehash alias is in a remotes script, you should get the same answers from $fakehash as from $hash:

.. code:: text

    //var %i 999 | while (%i) { var %input $rand(1,999999999) , %bits $rand(2,32) | if ($hash(%input,%bits) != $fakehash(%input,%bits)) echo -a this should never show: %input %bits | dec %i }
    
    alias fakehash {
      if ( ($1 == $null) || ($2 !isnum 2-32) ) return $null
      var %i 1 | var %len $len(%string) | var %x 0 | var %bits $int($2)
      while (%i <= $len($1)) {
        var %y $int($calc( $and(%x,$base(ff000000,16,10)) / 2^24 ))
        var %x = $calc( %x + %y + $asc($mid($1,%i,1)) )
        var %x = $calc( (%x * 256) % (2^32) )
        inc %i
      }
      var %y = $base(%x,10,2,32)
      var %z = $base($left(%y,%bits),2,10)
      if ($mid(%y,$calc(1+%bits))) inc %z
      return $calc( %z % (2^%bits) )
    }

Having good distribution of hash output is not proof that a hash is good, but having bad distribution is evidence of a bad hash. This next alias shows that $hash has a bad distribution:

.. code:: text

    ;syntax: /hash_distribution BITS STRINGLEN [1stOfRandom Range] [LastOfRandomRange]
    alias hash_distribution {
      var %bits $iif($1 isnum 1-32,$1,4) , %stringlen $iif($2,$2,9)
      var %numstrings 10000 , %i %numstrings , %tokens $str(0 $+ $chr(32),$calc(2^%bits))
      var %first $iif($3,$3,a) , %last $iif($4,$4,z)
      while (%i) {
        var %a $regsubex($str(x,%stringlen),/x/g,$r(%first,%last))
        var %h 1 + $hash(%a,%bits) , %tokens $puttok(%tokens,$calc(1+$gettok(%tokens,%h,32)),%h,32)
        dec %i
      }
      echo -ag bits: %bits #randoms: %numstrings stringlen: %stringlen input range $+(%first,-,%last) distribution: %tokens
    }

The first parameter tells the number of bits in the output hash, which means there should be 2^N possible outputs.
The 2nd number is the length of random strings to be hashed.
The 3rd and 4th parameters give the option of changing the first and last characters of the random range away from being the range a-z.

Using "/hash_distribution 4 N a z" where N ranges from 8 through 12 shows a very uneven frequency count of hash output, and the quality of the distribution depends greatly on the string length. In this example, because the output is a 4-bit hash, there are 2^4=16 possible outputs, and this alias shows most of the 16 numbers never happen for this length of a-z input, while other outputs happen too frequently:

.. code:: text

    /hash_distribution 4 8 a z
    bits: 4 #randoms: 10000 stringlen: 8 input range a-z distribution: 300 0 0 0 0 0 0 0 0 0 0 0 0 1342 4954 3404
    bits: 4 #randoms: 10000 stringlen: 9 input range a-z distribution: 0 0 0 232 2056 4404 2852 456 0 0 0 0 0 0 0 0
    bits: 4 #randoms: 10000 stringlen: 10 input range a-z distribution: 0 0 0 212 2127 4390 2839 432 0 0 0 0 0 0 0 0
    bits: 4 #randoms: 10000 stringlen: 11 input range a-z distribution: 0 0 0 213 2122 4371 2837 457 0 0 0 0 0 0 0 0
    bits: 4 #randoms: 10000 stringlen: 12 input range a-z distribution: 0 0 0 0 0 0 0 0 0 23 580 2525 3869 2486 498 19

Increasing the number of bits above 4 helps smooth the distribution, and increasing the string length also helps, but even when the string is as long as 100 characters the distribution of hashing lower-case letters is uneven. Also helping to smooth the distribution is to change first/last characters in the random range to increase that range size. But even for using ! and ~ as the first/last characters of the range, which includes a lot of characters unlikely to be in real-world item names, it still has an uneven distribution until  the string length increases sufficiently.

.. code:: text

    /hash_distribution 4 10 ! ~
    bits: 4 #randoms: 10000 stringlen: 10 input range !-~ distribution: 1256 1167 962 737 409 284 121 52 40 133 292 476 673 1006 1197 1195

The 1024 outputs of a 10 bit hash of a length-100 input fits onto a length-4150 mIRC line, but only because too many of the tokens are single digits:

(Warning: This is slow, and is too long to display here. There's a very large area where consecutive outputs happen 0-3 times. 11 bit instead of 10 bit can be used in a length-8292 line, but is even SLOWER.)

.. code:: text

    /hash_distribution 10 100 a z

As you shorten the hash, the distribution gets worse:

.. code:: text

    /hash_distribution 2 8 a z
    bits: 2 #randoms: 10000 stringlen: 8 distribution: 10000 0 0 0
    /hash_distribution 2 9 a z
    bits: 2 #randoms: 10000 stringlen: 9 distribution: 0 2265 7735 0

If you edit the fakehash alias to use the above $crchash alias instead of $hash, the distribution is much better for all input lengths and range of characters. Repeating the a-z range with $crchash gives a much smoother distribution.

.. code:: text

    /hash_distribution 4 8 a z (using $crchash)
    bits: 4 #randoms: 10000 stringlen: 8 input range a-z distribution: 624 618 617 627 610 638 624 626 602 635 612 650 632 600 627 658

$crc is not of cryptographic quality, but at least it has a good distribution, and hash functions don't always need a 1-way feature, they just need to be fast. A good distribution is not proof of a good hash, since even a repeating pattern of 1-through-10 has that.
Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$crc </identifiers/crc>`
    * :doc:`$crc64 </identifiers/crc64>`
    * :doc:`$md5 </identifiers/md5>`
    * :doc:`$sha1 </identifiers/sha1>`
    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$sha512 </identifiers/sha512>`
    * :doc:`/hadd </commands/hadd>`
