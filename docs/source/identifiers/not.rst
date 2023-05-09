$not
====

$not returns the binary NOT of a number

Synopsis
--------

.. code:: text

    $not(<N>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - the number, in base10/decimal

Properties
----------

None

Example
-------

$not returns the binary NOT of <N>. It returns 0 if the bit is 1, and returns 1 if the bit is 0. In effect, every 1-bit in the result toggles the 0/1 state of the corresponding bit of the input number

.. code:: text

    //var %n 5 | echo -a $not(%n) $base($not(%n),10,16)
    ; 4294967290 FFFFFFFA

Here's how the answer was calculated:
# Convert base-10 N to binary. If N is negative, treat as if a signed 32-bit number where the leftmost bit is a 1.
# Flip each 0-bit to 1, and each 1-bit to 0
# Convert the answer from binary to base 10.

.. code:: text

    //var %n 5 | echo -a $base(%n,10,2,32) | echo -a $str(-,32) | echo -a $base($not(%n),10,2,32) 
    ; returns:
    00000000000000000000000000000101
    --------------------------------
    11111111111111111111111111111010

.. code:: text

    //var %n1 4294967290 | var %n2 -6 | echo -a %n1 is the signed representation of %n2 so $not(%n1) is the same as $not(%n2)
    ; returns: 4294967290 is the signed representation of -6 so 5 is the same as 5

.. code:: text

    ; mIRC doesn't have the $neg function, but if it did, $not(N) would be $neg(N) less 1.
    //var %n 5 | echo -a $not(%n) is the same as $calc( -%n -1) so NOT of each is the same: $not($not(%n)) is the same as $not($calc( -%n -1))

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$xor </identifiers/xor>`
    * :doc:`$or </identifiers/or>`
    * :doc:`$and </identifiers/and>`
    * :doc:`$biton </identifiers/biton>`
    * :doc:`$bitoff </identifiers/bitoff>`
    * :doc:`$isbit </identifiers/isbit>`

