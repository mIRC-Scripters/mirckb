$floor
======

The $floor identifier will calculate and return a numerical value rounded to the next lowest integer.

Synopsis
--------

.. code:: text

    $floor(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The number to be rounded down. Decimals cause the value to round down, while integers are returned the same.

.. note:: You can use the letter 'e' or 'd' as ``*10^N, $floor(5e6) = $floor($calc(5*10^6))``

.. note:: $floor(N) is the same as $int(N) for N >= 0.

Example
-------

Echo to the active window 9.318 rounded to the next lowest integer:

.. code:: text

    //echo -a $floor(9.318)
    
    //var %a $pi | echo -a floor: $floor(%a) int: $int(%a) ceil: $ceil(%a) abs: $abs(%a)
    result: floor: 3 int: 3 ceil: 4 abs: 3.141593
    //var %a -1.5 | echo -a floor: $floor(%a) int: $int(%a) ceil: $ceil(%a) abs: $abs(%a)
    result: floor: -2 int: -1 ceil: -1 abs: 1.5

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$abs </identifiers/abs>`
    * :doc:`$ceil </identifiers/ceil>`
    * :doc:`$int </identifiers/int>`
    * :doc:`$round </identifiers/round>`
    * :doc:`$calc </identifiers/calc>`
