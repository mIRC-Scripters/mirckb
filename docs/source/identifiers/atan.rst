$atan
=====

$atan returns the arctangent of N.

Synopsis
--------

.. code:: text

    $atan(N)[.deg]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The tangent in radians for which you want the arc tangent.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .deg
      - Returns the angle as degrees, default is radians.

Example
-------

.. code:: text

    //echo -a In right triangle where opposite side is 3 and adjacent is 4, angle is $atan( $calc(3/4) ).deg degrees 
    ; Returns: In right triangle where opposite side is 3 and adjacent is 4, angle is 36.869898 degrees

.. code:: text

    //var %i 60 | echo -a %i degrees / tangent $tan(%i).deg / atan $atan( $tan(%i).deg ).deg
    ; returns 60.000003 instead of 60 because the $tan fraction is limited to 6 places
    //var %i 45 | echo -a %i degrees / tangent $tan(%i).deg / atan $atan( $tan(%i).deg ).deg
    //var %i 240 | echo -a %i degrees / tangent $tan(%i).deg / atan $atan( $tan(%i).deg ).deg
    ; returns angle in the range of -90 - +90 degrees (-pi/2 - +pi/2 radians)
    //var %i 90 | echo -a %i degrees / tangent $tan(%i).deg / atan $atan( $tan(%i).deg ).deg
    ; for 90 degrees, returns a VERY BIG NUMBER instead of infinity

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
    * :doc:`$sin </identifiers/sin>`
    * :doc:`$asin </identifiers/asin>`
    * :doc:`$sinh </identifiers/sinh>`
    * :doc:`$tan </identifiers/tan>`
    * :doc:`$atan2 </identifiers/atan2>`
    * :doc:`$tanh </identifiers/tanh>`

