$calc
=====

$calc can be used to perform mathematical calculations from the mIRC editbox line, or from inside of a custom script. The accuracy of results is limited to that of the 53-bit 'doubles' range, including the bits representing any fraction. The results are returned with any fraction rounded to the 6th decimal place, with the period or any zeroes-within-the-fraction stripped from being the rightmost digit of the output.

Synopsis
--------

.. code:: text

    $calc(operations)

The $calc identifier adheres to mathematical standards set forth by the PE(MD)(AS) order of operations, but also includes Floor Divide and Modulo. Therefore, a combination of brackets and parentheses can be used in order to manipulate the order of operations or to make a mix of operators easier to view. $calc can also be used to calculate variables in mIRC, as well as other custom identifiers that return numerical values.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - operations
      - These are a specific set of mathematical operations for $calc to perform.

Operators
---------

The TLDR version of most of this is: Use plenty of parenthesis, which improves readability as well as ensuring the operations are performed in the order you wish.

When parenthesis are not used to override the order of evaluation, these are the operators and the order in which they are used in calculating the result:

<span style="display: inline-block; width: 30px;">()</span>1. Parenthesis
<span style="display: inline-block; width: 30px;">^</span>2. Exponent
<span style="display: inline-block; width: 30px;">//</span>3. Floor division, X // Y same as $floor($calc(X / Y)) (Added v7.41)
<span style="display: inline-block; width: 30px;">%</span>3. Modulus X % Y is remainder when dividing X / Y
<span style="display: inline-block; width: 30px;">*</span>3. Multiplication
<span style="display: inline-block; width: 30px;">/</span>3. Division
<span style="display: inline-block; width: 30px;">+</span>4. Addition
<span style="display: inline-block; width: 30px;">-</span>4. Subtraction

Parenthesis used to demonstrate the order. Operations at the same level are executed left-to-right:

.. code:: text

    //echo -a $calc( 99 - 77 * 2 // 4 ^ .5 ^ 3 + 11 % 3 * 2 + 1) is same as $calc( 99 - (((( 77 * 2) // ((4 ^ .5) ^3)))) + (( 11  % 3) * 2) + 1)
    This first performs exponentiation left-to-right, so 4^.5^3 is 4 raised to .5 and that result of '2' is then cubed.
    Then it splits the formula into separate groups delimited by either + add or - subtract.
    Then the level#3 operations within each group are performed left-to-right.
    Finally the + and - groups groups are added/subtracted together from left-to-right order. 

Examples
--------

Echo a simple addition calculation to the active window

.. code:: text

    //echo -a $calc(3 + 5)

Echo a manipulated order of operations calculation to the active window

.. code:: text

    //echo -a $calc(3 * 4 * (3 + 5)))

Note that the extra closing parenthesis doesn't cause an error, but best practice is to avoid this, because future versions may not be as forgiving.

Echo the remainder of the calculation, by invoking the modulus operator, to the active window

.. code:: text

    //echo -a $calc(10 % 3)

Create a simple alias to take in two parameters, then raise the first to the power of the second, and return the value

.. code:: text

    alias power {
    
      ; Make sure both inputs are numbers
      if (($1 isnum) && ($2 isnum)) {
        return $calc($1 ^ $2)
      }
    }

The above $power alias can now be used like so:

.. code:: text

    //echo -a $power(5,2)

The result of the above command would be:

.. code:: text

    25

.. code:: text

    Modulus of N1/N2 is often seen as a number 0 through (N2 less 1), but that applies only to integers. It's the remainder (not the fraction) when dividing the numerator by the denominator.
    //var %x -10 , %y 3.14 | echo -a $calc(%x - %y * $int($calc( %x / %y))) vs $calc(%x % %y)
    * Shows -0.58 vs -0.58
    
    Order of Operation PEMDAS means Multiplication and Division and Floor Divide and Modulo are applied at the same time, as do Addition and subtraction together. It does not mean doing all multiplications before any divisions, nor doing all additions before doing any subtractions.
    
    //echo -a $calc( 2 / 4 * 5 )
    yields 2.5 because it goes left-to-right performing multiplies and divides. It divides 2/4 to obtain 0.5 before multiplying by 5, not multipling 4*5 before dividing that into 2.
    //echo -a $calc( 2 - 3 + 5 )
    yields 4 because it goes left-to-right performing adds and subtracts. It subtracts 3 from 2 = -1, then adds 5.
    
    //echo -a $calc( 0-2^8*3-1 ) vs $calc( -2^8*3-1 ) calc like $calc( (-2)^8*3-1 )
    produce 2 different answers because the presence of the 0 changes the meaning of the hyphen. In the 1st example it's -2 to the 8th power which is +256. That's then multiplied by 3, before having 1 subtracted from it. In the 2nd example, it starts by taking 2 to the 8th power, then multiplying by 3 to obtain the 2nd term 768. Then it starts with zero, subtracts the 768, then subtracts another 1.
    
    Any formula where any term reaches the undefined value returns zero for the entire result, and does not simply treating the individual operation's result as zero then continue operating.
    //echo -a $calc( 2 + ((-1) ^ .5) + 2 ) or $calc(2 + (1/0) + 2 ) are both zero

Limits and Quirks
-----------------

.. code:: text

    Integers outside the range -2^53 through +2^53 lose precision. Some of those 53 bits are used by the fraction, so adding a fraction shrinks the range where $calc returns accurate results.
    
    //echo -a $calc(9007199254740992 + 1) and $calc(9007199254740993) both return 9007199254740992
    //echo -a $calc(4294967296.000031) returns 4294967296.000032
    //echo -a $calc(9007199254740993) vs $calc(900719925474099.3) returns 9007199254740992 vs 900719925474099.25
    
    $calc has reduced accuracy for larger integers, and even lower accuracy for fractions of smaller numbers. This inaccuracy is often reflected in other identifiers which use same stored values used by $calc.
    
    For example, $base can't be trusted to be accurate when handling values larger than 2^53.
    //echo -a $base($str(f,14),16,16) returns 100000000000000
    
    Even numbers much smaller than 2^53 can return inaccurate results in their fraction, if the number to the left of the decimal is at least as large as 2^33:
    
    //echo -a $calc( 8589934592 + .999999) => 8589934592.999998
    
    if() can sometimes return inaccurate results for values larger than 2^53. For example, this executes as if $true:
    //if (18014398509481984 == 18014398509481985) echo match
    
    The 'doubles' math also applies to the if() statement, where it can accurately discern whether 2^53 is greater than 2^53-1, but considers 2^53 to be the same as 1+2^53.
    
    $calc rounds output to 6 decimals, with trailing zeroes dropped.
    //echo -a $pi vs $calc($pi)
    
    It can operate on terms who have more than 6 places, but the value with more than 6 decimal places is then rounded to 6:
    //var %x 0.1111111 , %y 6 |  echo -a $calc(%x * %y)) vs $calc($calc(%x) * %y) is 0.666667 vs 0.666666
    
    //echo -a $calc( 123 + 1abc + 2def )
    $calc stops processing when it encounters non-numerics, so this undocumented feature has often been used to strip text labels attached to a number:
    //var %a $md5(abc) | echo -a %a vs $calc(%a) returns 900150983cd24fb0d6963f7d28e17f72 vs 900150983
    
    //echo -a $calc( number + text ) returns number
    //echo -a $calc( text + number ) returns 0
    //var %a | echo -a $calc($1) vs $calc(%a) vs $calc($null) all evaluate to 0 when %var or $identifier is null
    
    You can use [ ] to force evaluation out of the normal order, but $calc has problems handling $+ as shown by:
    //echo -a $calc( 123 + 1 $+ 23 + 456 ) vs $calc( 123 + ( 1 $+ 23 ) ) vs $calc( 123 + $+ + 456 )
    In the first example, it causes everything after the $+ to be ignored, as if $+ is a text string with no special meaning except when preceded and followed by operators.
    //echo -a $calc( 5 ^ $+ + .1)
    
    When the $+ is inside additional parenthesis, the entire result is zero:
    //echo -a s $calc( 123 + ( 1 $+ 23 ) )
    
    You should use $+() instead of $+ inside the $calc string.
    //var %a 7 | echo -a $calc( %a $+ 000 ) vs $calc(%a * 1000) vs $calc( $+(7,000) )
    result: 7 vs 7000 vs 7000
    
    Because of the rounding of $calc output, it's not always accurate to use the $calc output as the argument inside $int() or $floor.
    
    //var %i 0 | while (%i isnum 0-99) { echo -a %i : $calc( $+(%i,.9999995) ) | inc %i }
    In the above example, sometimes the result is rounded up to the next integer, and other times it's rounded down to having the .999999 fraction.
    //var -s %top 2000000 , %div %top + 1 | echo -a $calc(9 + (%top / %div) ) vs $calc(9 + (%top // %div) ) vs $calc(9 + (%top - (%top % %div)) / %div)
    result: 10 vs 9 vs 9
    In this case, the first result rounded to the nearest 9 decimal places is 10.000000, so the fraction and the decimal were stripped. The input for $int would have been 10, so the wrong result would not be caused by $int. The accuracy of the 'floor divide' operator provides the accurate result because the floor divide happens before the result is rounded to 6 decimal places. The last method is a way to return accurate results without using the floor divide.
    

See also the $calc section at :ref:`injection-calc`

Compatability
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$base </identifiers/base>`
    * :doc:`$abs </identifiers/abs>`,     * :doc:`$int </identifiers/int>`,     * :doc:`$ceil </identifiers/ceil>`,     * :doc:`$floor </identifiers/floor>`,     * :doc:`$round </identifiers/round>`
    * :doc:`$and </identifiers/and>`,     * :doc:`$not </identifiers/not>`,     * :doc:`$or </identifiers/or>`,     * :doc:`$xor </identifiers/xor>`
    * :doc:`$sqrt </identifiers/sqrt>`
    * :doc:`$pi </identifiers/pi>`
    * :doc:`$rand </identifiers/rand>`
    * :doc:`$log </identifiers/log>`,     * :doc:`$log10 </identifiers/log10>`
    * :doc:`$sin </identifiers/sin>`,     * :doc:`$asin </identifiers/asin>`,     * :doc:`$sinh </identifiers/sinh>`
    * :doc:`$cos </identifiers/cos>`,     * :doc:`$acos </identifiers/acos>`,     * :doc:`$cosh </identifiers/cosh>`
    * :doc:`$tan </identifiers/tan>`,     * :doc:`$atan </identifiers/atan>`,     * :doc:`$atan2 </identifiers/atan2>`,     * :doc:`$tanh </identifiers/tanh>`
    * :doc:`$biton </identifiers/biton>`,     * :doc:`$bitoff </identifiers/bitoff>`,     * :doc:`$isbit </identifiers/isbit>`
    * :doc:`$hypot </identifiers/hypot>`,     * :doc:`$intersect </identifiers/intersect>`
    * :doc:`$inrect </identifiers/inrect>`,     * :doc:`$inroundrect </identifiers/inroundrect>`,     * :doc:`$inellipse </identifiers/inellipse>`,     * :doc:`$inpoly </identifiers/inpoly>`,     * :doc:`$onpoly </identifiers/onpoly>`,
