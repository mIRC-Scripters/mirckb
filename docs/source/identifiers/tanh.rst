$tanh
=====

$tanh returns the hyperbolic tangent of an angle of N radians

Synopsis
--------

.. code:: text

    $tanh(<N>)[.deg]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - This is the angle in radians for which you wish to retrieve the hyperbolic tangent.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - deg
      - Sees N as degrees in a 360 degree circle instead of radians.

Example
-------

.. code:: text

    echo -a $tanh(1).deg

Compatibility
-------------

.. compatibility:: 7.33

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cos </identifiers/cos>`
    * :doc:`$acos </identifiers/acos>`
    * :doc:`$cosh </identifiers/cosh>`
    * :doc:`$sin </identifiers/sin>`
    * :doc:`$asin </identifiers/asin>`
    * :doc:`$sinh </identifiers/sinh>`
    * :doc:`$atan </identifiers/atan>`
    * :doc:`$atan2 </identifiers/atan2>`
    * :doc:`$tan </identifiers/tan>`

