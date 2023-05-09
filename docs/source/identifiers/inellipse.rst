$inellipse
==========

$inellipse returns :doc:`$true </identifiers/true>` if the specified point is inside the specified ellipse, :doc:`$false </identifiers/false>` otherwise

Synopsis
--------

.. code:: text

    $inellipse(x1,y1,x,y,w,h)

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
      - the x coordinate of the ellipse
    * - y
      - the y coordinate of the ellipse
    * - w
      - the width of the ellipse
    * - h
      - the height of the ellipse

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $inellipse(50,50,10,10,100,100)

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$inrect </identifiers/inrect>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$onpoly </identifiers/onpoly>`

