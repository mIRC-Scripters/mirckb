$base
=====

The $base identifier converts numbers between different number bases, or zero-pads numbers to the desired length.

Synopsis
--------

.. code:: text

    $base(<N>,<InBase>,<OutBase>[,Zero-pad][,Precision])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Number being converted.
    * - InBase
      - The Number Base in which N is being expressed.
    * - OutBase
      - The Number Base to which N is being converted. Can be same as InBase.
    * - ZeroPad
      - The output's minimum number of non-fraction digits by adding 0's if needed. Accepts up to 100.
    * - Precision
      - Shortens the output's maximum number of fraction digits, limited by mIRC's base-10 precision of 6.

.. note:: Beginning v7.72 $base supports the larger integer accuracy of bigfloat mode without needing to use %varname.bf or /bigfloat on, and no longer limits zero padding to 100 digits. But extra precision for fractional input requires bigfloat mode.

.. note:: InBase & Outbase can be any integer from 2-36, with Base 17-36 extending hexadecimal to use as many letters as needed from the G-Z range. Letters A-Z used by number bases 11 through 36 accept case-insensitive input, but always outputs uppercase.

.. note:: All 36 inbases accept all 36 characters of the base36 alphabet, so $base(ZZ,2,10) = 35*2+35=105.

.. note:: Prefix 0x or 0X is stripped from N for base 16. (Prior to v7.53 only base36 did not strip the 0x. To prevent this, such as in base 34-35 where X is a valid character, it was necesary to prefix inputs with 00.)

.. note:: Base 32 is NOT the same as the base32 encoding method used by $encode(). $base assigns the values 0-31 to characters 0-9 and A-V, while the Base32 encoding method assigns values 0-31 to A-Z and 2-7 then stores them differently.

Properties
----------

None

Example
-------

.. code:: text

    Without changing number base, can use $base to left-zero-pad and/or truncate (not round) fractions to fewer digits:
    //echo -a $base(123.456,10,10,6,2)
    returns: 000123.45
    
    //var %n $color(8) | echo -a %n $base(%n,10,16,6)
    converts the color rgb number index 8 from decimal to hexadecimal, zero padded to 6 digits.
    Default Output is 00FFFF not FFFF00 because mIRC stores colors as GBR not RGB.
    
    //var %n $pi  | echo -a %n $base(%n,10,16,0,12) $base($calc(%n * 16^6),10,16,6,12) 
    ; returns: 3.14159265358979323846 3.243F7 3243F6A.8885A
    ; precision of output is input rounded to 6 fraction digits
    //echo -a $base(1.0000005,10,10) returns 1.000001  
    
    //var %n $crc(abc,0) | echo -a %n $base(%n,16,36,7)
    ; Converts 8-digit hexadecimal
    ; Base 36 extends the hexadecimal alphabet so the characters G-Z have decimal values 16-35
    
    //var %n $str(F,9) | echo -a converts 9-digit hex number %n to 7-digit base-36 $base(%n,16,36,7)
    ; returns: converts 9-digit hex number FFFFFFFFF to 7-digit base-36 VKHSVLR

.. code:: text

    You should not attempt to input numbers greater than decimal 2^53 prior to v7.72. For N=1+2^n, this shows that even though $base failed to convert back to the original number starting with N=55, $calc failed to create an odd-numbered number at N=53. But starting v7.72 the $base output is accurate as long as the input is too
    
    //if ($version >= 7.72) bigfloat on | var %i 1 | while (%i isnum 1-64) { var %n $calc(1+2^%i ) | echo -a %i %n $base(%n,10,16) $base($base(%n,10,16),16,10) | inc %i }
    
    $base allows invalid letters to be used in the input, assigning them values as they have in Base 36.
    
    //echo -a $base(mIRC,10,10) is same as $calc(22*1000 + 18*100 + 27*10+ 12*1)
    
    The exception to the above is skipping the 0x prefix for hexadecimal notation. Converting from base-16 to base10 results in 255 for both 0xFF and FF. The 0x or 0X prefix is ignored only when tranlating to base16. (Prior to v7.53 it was ignored in every base except 36):
    
    //var %i 2 , %a , %value F | while (%i isnum 2-36) { var %a %a $+(base,%i,=,$base(0x $+ %value,%i,10),vs,$base(%value,%i,10)) | inc %i } | echo -a %a
    
    Prior to v7.53, if using base 34 or 35 where X is a valid character, you must prepend the from-value with 00 to prevent 0x from being stripped:
    //if ($version < 7.53) { var %value 0xF | echo -a $base(%value,35,10) vs $base(00 $+ %value,35,10) }
    returned: 15 vs 1170
    
    To store the 128 hexadecimal digits of the sha512 hash digest in fewer digits, you can't use $base to accurately translate more than 13 digits at a time, until v7.72.
    //var %digits 13 , %from_base 16 , %to_base 36 | echo -a $calc( %digits * $log(%from_base) / $log(%to_base) )
    //var %digits  9 , %from_base 16 , %to_base 36 | echo -a $calc( %digits * $log(%from_base) / $log(%to_base) ) 
    These show that base36 requires 10.05 digits to store 13 hex digits, or 6.96 digits to store 9 hex digits. Rounding up, this means both methods shrink the strings by the same 4 digits. (13->11 vs 9->7) It's more efficient to translate the string 9 digits at a time into 14 groups of 9, then translate the remaining 2 digits separately, for a total length of 14*7+2=100:
    
    alias short_hash {
      var %long $sha512($1) , %short , %hash %long | while ($len(%hash) >= 9) {
        var %temp $right(%hash,9) , %hash $left(%hash,-9) , %short $base(%temp,16,36,7) $+ %short
        echo -a %hash %temp -> $left(%short,7)
      }
      var %short $base(%hash,16,36,2) $+ %short
      echo -a shortened $len(%long) %long to $len(%short) %short
      return %short
    }
    
    /short_hash abc
    returns:
    shortened 128 d8022f2060ad6efd297ab73dcc5355c9b214054b0d1776a136a669d26a7d3b14f73aa0d0ebff19ee333368f0164b6419a96da49e3e481753e7e96b716bdccb6f to 100 6009P25MYQI73NNEMLHK0MTBF48SUD996MZJE2E6ZVTED4R1VM7E9HEQ5NVGI65GZ6Q7J6FFCCDZ2ZE9413JTJACHSWXJ2SYIR1R

But beginning v7.72 the above is not needed as the accurate results are obtained from both:

.. code:: text

    //echo -a $base($base($sha1(abc),16,10),10,16) is A9993E364706816ABA3E25717850C26C9CD0D89D
    //echo -a $base($sha1(abc),16,36) is JT72FO5T4YOBF0QUGWUCZBWJ07MAX7H

starting v7.72 the accuracy for large integers is always enabled by default, but precision for fractions is only enabled if in bigfloat mode:

.. code:: text

    //var -s %var.bx 10000000000000000000000000001 | echo -a $base(%var.bx,10,10) 
    result: 10000000000000000000000000001
    //var -s %var.bf 0.10000000000000000000000000001 | echo -a $base(%var.bf,10,10) 
    result: 0.10000000000000000000000000001
    //var -s %var.bx 0.10000000000000000000000000001 | echo -a $base(%var.bx,10,10) 
    result: 0.1

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$calc </identifiers/calc>`
    * :doc:`$encode </identifiers/encode>`
    * :doc:`$bytes </identifiers/bytes>`
