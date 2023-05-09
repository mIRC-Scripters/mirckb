$biton
======

$biton returns N with the Bth bit set to 1.

Synopsis
--------

.. code:: text

    $biton(<N>,<B>)

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
      - The Bth bit to be set

Properties
----------

None

Example
-------

.. code:: text

    //var %n 10 | echo -a $biton(%n,3)
    ; returns 14

Here's how the answer was calculated:
# Convert base-10 N to binary.
# Count 3 from the right
# that bit is set to 1.
# Return the possibly altered number

.. code:: text

    //var %n 10 | echo -a $base(%n,10,2,32) | echo -a $str(-,24) $+ 87654321 | echo -a $base($biton(%n,3),10,2,32) $base(1110,2,10)
    ; returns:
    00000000000000000000000000001010
    ------------------------87654321
    00000000000000000000000000001110 14

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

.. code:: text

    ; $biton can be simulated by using $or to set the appropriate bit to 1
    //var %n 10 | var %b 3 | echo -a within the valid number range, %n $biton(%n,%b) is the same as $or( %n , $calc( 2^ (%b -1) ) )

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
    * :doc:`$bitoff </identifiers/bitoff>`
    * :doc:`$isbit </identifiers/isbit>`

