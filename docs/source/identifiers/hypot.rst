$hypot
======

$hypot returns the hypotenuse for the other 2 sides of a right triangle.

Synopsis
--------

.. code:: text

    $hypot(<A>,<B>)

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
    * - A
      - One of the shorter sides of the right triangle
    * - B
      - The other of the shorter sides of the right triangle

Doesn't matter which order the short sides are given. You can use the letter 'e' or 'd' as *10^N, $hypot(5e6,1) = $hypot($calc(5*10^6),1)

Properties
----------

None

Example
-------

.. code:: text

    //var %a 3 | var %b 4 | echo -a $hypot(%a,%b) is the same as $sqrt( $calc( %a ^2 + %b ^2 ) )

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
    * :doc:`$atan2 </identifiers/atan2>`
    * :doc:`$tanh </identifiers/tanh>`

