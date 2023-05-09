$sin
====

$sin returns the sine of an angle of N radians.

Synopsis
--------

.. code:: text

    $sin(<N>)[.deg]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
* N -This is the angle in radians for which you wish to retrieve the sine.

.. note:: You can use the letter 'e' or 'd' as ``*10^N, $sin(5e6) = $sin($calc(5*10^6))``

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

Sine is the ratio of the Opposite Side / Hypotenuse of a right triangle, so in a right triangle from the position of an angle of 60 degrees, the length of the Opposite side is .866025 as long as the hypotenuse. As with :doc:`$calc </identifiers/calc>`, the returned fraction is limited to 6 decimal places.

.. code:: text

    //echo -a There are 2x pi radians in a circle, so a radian is $calc(360 / (2*$pi) ) degrees
    //var %i 60 | echo -a $sin(%i).deg is the same as $sin( $calc(%i * $left($pi,8) / 180) )

$sin accepts numbers larger than 1 rotation of a circle, as if the angle loops past the origin and continues. Assuming you are using the .deg property, angles above 360 degrees return the same result of the angle modulo 360.

.. code:: text

    //var %i 400 | echo -a $sin(%i).deg is the same as $sin( $calc(%i % 360) ).deg

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cos </identifiers/cos>`
    * :doc:`$acos </identifiers/acos>`
    * :doc:`$cosh </identifiers/cosh>`
    * :doc:`$asin </identifiers/asin>`
    * :doc:`$sinh </identifiers/sinh>`
    * :doc:`$tan </identifiers/tan>`
    * :doc:`$atan </identifiers/atan>`
    * :doc:`$atan2 </identifiers/atan2>`
    * :doc:`$tanh </identifiers/tanh>`

