$sinh
=====

$sinh returns the hyperbolic sine (hypersine) of an angle of N radians.

Synopsis
--------

.. code:: text

    $sinh(<N>)[.deg]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - This is the angle in radians for which you wish to retrieve the hypersine.

.. note:: You can use the letter 'e' or 'd' as ``*10^N, $sinh(5e6) = $sinh($calc(5*10^6))``

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

    //echo -a There are 2x pi radians in a circle, so a radian is $calc(360 / (2*$pi) ) degrees
    //var %e 2.718281 | var %angle $calc( 30 * $pi / 180)   | echo -a $sinh(%angle) same as $calc( ((%e ^ %angle) - (%e ^ (0 - %angle) )) /2 )
    //var %angle 30 | echo -a $sinh(%angle).deg same as $sinh( $calc( %angle * $pi / 180) ) except for rounding

Unlike :doc:`$sin </identifiers/sin>`, <source lang="mIRC">$sinh(N degrees).deg</source> is not the same as <source lang="mIRC">$sinh( N + 360 degrees).deg</source>

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
    * :doc:`$tan </identifiers/tan>`
    * :doc:`$atan </identifiers/atan>`
    * :doc:`$atan2 </identifiers/atan2>`
    * :doc:`$tanh </identifiers/tanh>`

