$and
====

$and returns the AND operation of two numbers.

.. note:: The numbers need to be provided in decimal, and are then converted to binary, the AND operation applied, and  the answer converted back to decimal.

Valid range for N1 and N2 are -4294967295 through +4294967295. See :doc:`$xor </identifiers/xor>` for description of handling out-of-range and negative numbers.

Synopsis
--------

.. code:: text

    $and(<N1>,<N2>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <N1>, <N2>
      - The numbers, in decimal

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $and(14,27)
    ; returns 10
    ; 14 is 00001110 when converted to binary
    ; 27 is 00011011 when converted to binary
    ; AND   00001010 which is 10 when converted back to decimal

The AND operation returns a 1 when both matching binary bits are 1, otherwise returns 0

.. code:: text

    //var %n1 14 | var %n2 27 | echo -a $base(%n1,10,2,8) | echo -a $base(%n2,10,2,8) | echo -a $str(-,8) | echo -a $base($and(%n1,%n2),10,2,8) -> $and(%n1,%n2)
    returns:
    00001110
    00011011
    --------
    00001010 -> 10
    
    $and returns the answer as a decimal number, so the answer 10 is the decimal representation of binary 1010.
    
    //var %a 127 | var %bits 3 | var %b $and(%a,$calc(-2^%bits)) | echo -a $base(%a,10,16,8) $base(%b,10,16,8)
    Zeroes the lowest 3 bits, which ensures that %b is a multiple of 8.

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$not </identifiers/not>`
    * :doc:`$or </identifiers/or>`
    * :doc:`$xor </identifiers/xor>`
    * :doc:`$biton </identifiers/biton>`
    * :doc:`$bitoff </identifiers/bitoff>`
    * :doc:`$isbit </identifiers/isbit>`
