$atan2
======

$atan2 returns the arctangent of the 2 short sides of a right triangle.

Synopsis
--------

.. code:: text

    $atan2(<O>,<A>)[.deg]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - O
      - The length of the Opposite side of the right triangle.
    * - A
      - The length of the Adjacent side of the right triangle.

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

    //var %opposite 3, %adjacent 4 | echo -a In right triangle where opposite side is length %opposite and adjacent side is length %adjacent - angle is $atan2( %opposite , %adjacent ).deg degrees
    ; Returns: In right triangle where opposite side is length 3 and adjacent side is length 4 - angle is 36.869898 degrees

.. code:: text

    //var %opposite 4 | var %adjacent 3 | echo -a except for rounding $atan2(%opposite,%adjacent).deg is the same as $atan( $calc( %opposite / %adjacent ) ).deg
    ; ATAN2 accepts the side lengths while ATAN accepts the tangent ratio of those sides

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
    * :doc:`$tan </identifiers/tan>`
    * :doc:`$atan </identifiers/atan>`
    * :doc:`$tanh </identifiers/tanh>`
