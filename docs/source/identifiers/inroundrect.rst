$inroundrect
============

$inroundrect returns :doc:`$true </identifiers/true>` if the specified point is inside the specified rounded rectangle, :doc:`$false </identifiers/false>` otherwise

Synopsis
--------

.. code:: text

    $inroundrect(x1,y1,x,y,w,h,w1,h1)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - x1
      - the x coordinate of the point
    * - y1
      - the y coordinate of the point
    * - x
      - the x coordinate of the rectangle
    * - y
      - the y coordinate of the rectangle
    * - w
      - the width of the rectangle
    * - h
      - the height of the rectangle
    * - w1
      - the width of the rounded part for the rectangle
    * - h1
      - the height of the rounded part of the rectangle

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $inroundrect(50,50,10,10,100,100,5,5)

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inrect </identifiers/inrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$onpoly </identifiers/onpoly>`

