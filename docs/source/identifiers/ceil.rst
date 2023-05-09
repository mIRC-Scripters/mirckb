$ceil
=====

The $ceil identifier will calculate and return a numerical value rounded to the next highest integer.

Synopsis
--------

.. code:: text

    $ceil(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The number to be rounded up. Decimals cause the value to round up, while integers are returned the same.

.. note:: You can use the letter 'e' or 'd' as ``*10^N, $ceil(5e6) = $ceil($calc(5*10^6))``

Example
-------

Echo to the active window 3.14 rounded to the next highest integer:

.. code:: text

    //echo -a $ceil(3.14)

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$abs </identifiers/abs>`
    * :doc:`$acos </identifiers/acos>`
    * :doc:`$asin </identifiers/asin>`
    * :doc:`$atan </identifiers/atan>`
    * :doc:`$base </identifiers/base>`
    * :doc:`$calc </identifiers/calc>`
    * :doc:`$cos </identifiers/cos>`
    * :doc:`$floor </identifiers/floor>`
    * :doc:`$sin </identifiers/sin>`
    * :doc:`$tan </identifiers/tan>`

