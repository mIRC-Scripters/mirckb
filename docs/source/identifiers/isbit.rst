$isbit
======

$isbit returns 1 if the Nth bit is turned on

Synopsis
--------

.. code:: text

    $isbit(A,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - A
      - The number, in base10/decimal
    * - N
      - The Nth bit you want to check

Properties
----------

None

Example
-------

.. code:: text

    //var %a 5 | echo -a $base(%a,10,2) $isbit(%a,2)

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$and </identifiers/and>`
    * :doc:`$or </identifiers/or>`
    * :doc:`$xor </identifiers/xor>`
    * :doc:`$not </identifiers/not>`
    * :doc:`$biton </identifiers/biton>`
    * :doc:`$bitoff </identifiers/bitoff>`

