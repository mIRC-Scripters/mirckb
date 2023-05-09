$bitoff
=======

$bitoff returns N with the Bth bit set to 0.

Synopsis
--------

.. code:: text

    $bitoff(<N>,<B>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - the number, in base10/decimal
    * - B
      - The Bth bit to turn off

Properties
----------

None

Example
-------

.. code:: text

    //var %n 10 | echo -a $bitoff(%n,2)
    ; returns 8

Here's how the answer was calculated:
# Convert base-10 N to binary.
# Count 2 from the right
# That bit is set to 0
# Return the possibly altered number

.. code:: text

    //var %n 10 | echo -a $base(%n,10,2,32) | echo -a $str(-,24) $+ 87654321 | echo -a $base($bitoff(%n,2),10,2,32) $base(1000,2,10)
    ; returns:
    00000000000000000000000000001010
    ------------------------87654321
    00000000000000000000000000001000 8

If N is 2^32 or greater, returns 2^32 -1
If N is less than -2^31+1, returns 2^(B-1) +1

Using $biton and $bitoff, you can store several variables as bits within a single variable, instead of creating a separate variable for each.
The /window switch -wN uses bit settings, with default 3 if N not used.

.. code:: text

    var %treebarsetting $true
    var %switchbarsetting $true
    var %n
    if (%switchbarsetting) var %n $biton(%n,1)
    if (%treebarsetting) var %n $biton(%n,2)
    if (%n == $null) var %n 3

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
    * :doc:`$not </identifiers/not>`
    * :doc:`$biton </identifiers/biton>`
    * :doc:`$isbit </identifiers/isbit>`

