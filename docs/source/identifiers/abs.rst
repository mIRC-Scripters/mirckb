$abs
====

$abs returns the absolute value of a number.

Synopsis
--------

.. code:: text

    $abs(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The number that you want to retrieve the absolute value for.

.. note:: You can use the letter 'e' or 'd' as ``*10^N, $abs(5e6) = $abs($calc(5*10^6))``

Example
-------

Echo the absolute value of ``-7`` to the active window

.. code:: text

    //echo -a $abs(-7)

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$calc </identifiers/calc>`
    * :doc:`$floor </identifiers/floor>`
    * :doc:`$round </identifiers/round>`

