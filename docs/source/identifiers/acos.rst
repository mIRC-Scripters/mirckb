$acos
=====

$acos returns the arccosine of N.

Synopsis
--------

.. code:: text

    $acos(N)[.deg]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The cosine in radians for which you want the arc cosine.

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

    //echo -a $acos(5)
    ; returns $null because cosine can only be in range of -1.0 through +1.0

.. code:: text

    //echo -a In right triangle where opposite side is 4 and hypotenuse is 5, angle is $acos( $calc(4/5) ).deg degrees
    ; Returns: In right triangle where opposite side is 4 and hypotenuse is 5, angle is 36.869898 degrees

.. code:: text

    //var %i 60 | echo -a %i degrees / cosine $cos(%i).deg / acos $acos( $cos(%i).deg ).deg
    //var %i 45 | echo -a %i degrees / cosine $cos(%i).deg / acos $acos( $cos(%i).deg ).deg
    ; returns 44.999982 instead of 45 because the $cos fraction is limited to 6 places
    //var %i 270 | echo -a %i degrees / cosine $cos(%i).deg / acos $acos( $cos(%i).deg ).deg
    ; returns angle in the range of 0-180 degrees (0-pi radians)

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cos </identifiers/cos>`
    * :doc:`$cosh </identifiers/cosh>`
    * :doc:`$sin </identifiers/sin>`
    * :doc:`$asin </identifiers/asin>`
    * :doc:`$sinh </identifiers/sinh>`
    * :doc:`$tan </identifiers/tan>`
    * :doc:`$atan </identifiers/atan>`
    * :doc:`$atan2 </identifiers/atan2>`
    * :doc:`$tanh </identifiers/tanh>`

