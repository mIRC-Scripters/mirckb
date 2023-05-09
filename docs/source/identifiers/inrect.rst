$inrect
=======

$inrect returns :doc:`$true </identifiers/true>` if the specified point is inside the specified rectangle, :doc:`$false </identifiers/false>` otherwise

Synopsis
--------

.. code:: text

    $inrect(x1,y1,x,y,w,h)

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

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $inrect(50,50,10,10,100,100)

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$onpoly </identifiers/onpoly>`

