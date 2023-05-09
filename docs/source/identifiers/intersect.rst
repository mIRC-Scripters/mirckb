$intersect
==========

$intersect returns the point at which two lines/rays intersect.

.. note:: $intersect does not return a point on overlaping line/ray

Synopsis
--------

.. code:: text

    $intersect(x1,y1,x2,y2,x3,y3,x4,y4,method)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - x1
      - the x coordinate of the first point for the first line/ray
    * - y1
      - the y coordinate of the first point for the first line/ray
    * - x2
      - the x coordinate of the second point for the first line/ray
    * - y2
      - the y coordinate of the second point for the first line/ray
    * - x3
      - the x coordinate of the first point for the second line/ray
    * - y3
      - the y coordinate of the first point for the second line/ray
    * - x4
      - the x coordinate of the second point for the second line/ray
    * - y4
      - the y coordinate of the second point for the second line/ray
    * - method
      - optional, by default the method is line/line, if specified can be "lr" for line/ray (first point is line and second is ray), "rl" for ray/line and "rr" for ray/ray

"Ray" means the line defined by two points can expand infinitely in the two directions to try to cross the other line/ray whereas "line" means it doesn't expand.

.. note:: You can use the letter 'e' or 'd' as ``*10^N, for any coordinate parameters $intersect(5e6,y,x1,x1) = $intersect($calc(5*10^6),y,x1,y1)``

Properties
----------

None

Example
-------

.. code:: text

    alias test_inter {
      window -c @ti
      window -pfdoCB @ti -1 -1 400 200
      var %x 50,%y 50,%x1 64,%y1 64
      var %x2 100,%y2 25,%x3 75,%y3 75
      drawline -r @ti 0 1 %x %y %x1 %y1
      drawline -r @ti 0 1 %x2 %y2 %x3 %y3
      titlebar @ti > $intersect(%x,%y,%x1,%y1,%x2,%y2,%x3,%y3) - $intersect(%x,%y,%x1,%y1,%x2,%y2,%x3,%y3,lr) - $intersect(%x,%y,%x1,%y1,%x2,%y2,%x3,%y3,rl) - $intersect(%x,%y,%x1,%y1,%x2,%y2,%x3,%y3,rr)
    }

Compatibility
-------------

.. compatibility:: 7.33

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$inrect </identifiers/inrect>`

