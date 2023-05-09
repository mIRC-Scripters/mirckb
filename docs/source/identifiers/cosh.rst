$cosh
=====

$cosh returns the hyperbolic cosine of an angle of N radians.

Synopsis
--------

.. code:: text

    $cosh(<N>)[.deg]

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
      - This is the angle in radians for which you wish to retrieve the hyperbolic cosine.

.. note:: You can use the letter 'e' or 'd' as ``*10^N, <source lang="mIRC">$cosh(5e6) = $cosh($calc(5*10^6))</source>``

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .deg 
      - Sees N as degrees in a 360 degree circle instead of radians.

Example
-------

.. code:: text

    //echo -a $cosh(30).deg

Compatibility
-------------

.. compatibility:: 7.33

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$acos </identifiers/acos>`
    * :doc:`$cos </identifiers/cos>`
    * :doc:`$sin </identifiers/sin>`
    * :doc:`$asin </identifiers/asin>`
    * :doc:`$sinh </identifiers/sinh>`
    * :doc:`$tan </identifiers/tan>`
    * :doc:`$atan </identifiers/atan>`
    * :doc:`$atan2 </identifiers/atan2>`
    * :doc:`$tanh </identifiers/tanh>`

