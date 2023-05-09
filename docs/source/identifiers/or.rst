$or
===

$or returns the binary OR of 2 numbers.

Synopsis
--------

.. code:: text

    $or(<N1>,<N2>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <N1>/<N2>
      - The numbers, in base10/decimal

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $or(14,27)
    ; returns 31

Bits which are both 0 return 0, otherwise the bit is 1

.. code:: text

    //var %n1 14 | var %n2 27 | echo -a $base(%n1,10,2,8) | echo -a $base(%n2,10,2,8) | echo -a $str(-,8) | echo -a $base($or(%n1,%n2),10,2,8)

returns:

.. code:: text

    00001110
    00011011
    --------
    00011111

$or returns the answer as a decimal number, so the answer 31 is the decimal representation of binary 11111.

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$and </identifiers/and>`
    * :doc:`$biton </identifiers/biton>`
    * :doc:`$bitoff </identifiers/bitoff>`
    * :doc:`$isbit </identifiers/isbit>`
    * :doc:`$not </identifiers/not>`
    * :doc:`$xor </identifiers/xor>`

