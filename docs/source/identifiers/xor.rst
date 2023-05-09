$xor
====

$xor returns the binary XOR of 2 numbers.

Synopsis
--------

.. code:: text

    $xor(<N1>,<N2>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
* N1,N2 = the numbers, in base10/decimal

.. note:: Fractions are ignored. valid range is integers from -(2^32-1) through +(2^32-1). Negative numbers within that range are translated from signed 32bit-int to unsigned 32bit-int. i.e. Negative numbers in the range -4294967295 through -1 are replaced by N+4294967296. Numbers outside that range are replaced by the closest valid number. i.e. 4294967296+ is handled as if it's 4294967295, and -4294967296 and lower are handled as if -4294967295 which is then handled as if -4294967295+4294967296=1. This means the result is always in the range 0 thru +4294967295.

Properties
----------

None

Example
-------

XOR is "Exclusive OR" comparison of a pair of bits. For each bit position it returns 0 if BOTH or NEITHER bits are 1, and returns 1 if exactly 1 of the pair is a 1-bit. In effect, every 1-bit in the 2nd number toggles the 0/1 state of the corresponding bit of the 1st number

.. code:: text

    //echo -a $xor(21,9)
    ; returns 28

Here's how the answer was calculated:
# If either number is below -4294967295 replace it with -4294967295
# If either number is above +4294967295 replace it with +4294967295
# If either number is below zero, add 4294967296 to bring it into range of 0 through 4294967295
# Convert each number to binary, then line them up vertically so there are 2 rows, where each position pair is a single column.
# Create a 3rd row, where each column's 0 or 1 value is the XOR of the bit pair directly above it
# Convert the 3rd row from binary to base 10.

.. code:: text

    //echo -a $base(21,10,2,8) | echo -a $base(9,10,2,8) | echo -a $str(-,8) | echo -a $base($xor(21,9),10,2,8)
    ; returns:
    00010101
    00001001
    --------
    00011100

The columns where both numbers are zero remain 0. The columns where only 1 of the 2 values is 1, and the column where both values were 1 is zero.

$xor then returns the answer in base 10. Depending on which bits have changed to 0 or 1, the answer can be less than or greater than the 2 numbers:

.. code:: text

    //echo -a $base(00011100,2,10)
    ; returns 28

//echo -a $xor(-1,0)
: returns 4294967295 because -1 was translated to 4294967295 in a preliminary step. Then, the XOR of all numbers in the valid range against 0 is the same number.

//echo -a $xor(4444444444,5555555555)
: returns 0. Both numbers were outside valid range, so both were replaced with 2^32-1, and XOR of the same number against itself is always zero.

//var %a $and(%a,1) | var %b $and(%b,1) | if ($xor(%a,%b)) goto label
: Goes to label only if exactly 1 of the 2 variables is 1

//echo -a $xor($pi,2.777777)
: result is 1, because both fractions are ignored.

//echo -a $xor(1,2) = 3 and $xor(-1,-2) is same as $xor(4294967295,4294967294)

//echo -a $xor(-9999999999,0)
Invalid negative number replaced with -4294967295, which is replaced with +1. Result is 1.

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$and </identifiers/and>`
    * :doc:`$or </identifiers/or>`
    * :doc:`$not </identifiers/not>`
    * :doc:`$bitoff </identifiers/bitoff>`
    * :doc:`$biton </identifiers/biton>`
    * :doc:`$isbit </identifiers/isbit>`
