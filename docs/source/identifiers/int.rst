$int
====

$int Returns the integer part of a floating point number with no rounding.

Synopsis
--------

.. code:: text

    $int(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The number you want the integer part of

.. note:: You can use the letter 'e' or 'd' as ``*10^N, $int(5e6) = $int($calc(5*10^6))``

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $int(1.9)

will return 1, the integer part

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$round </identifiers/round>`
    * :doc:`$calc </identifiers/calc>`
    * :doc:`$floor </identifiers/floor>`
    * :doc:`$ceil </identifiers/ceil>`

