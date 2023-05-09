$onpoly
=======

$onpoly returns :doc:`$true </identifiers/true>` if two polygon overlap, :doc:`$false </identifiers/false>` otherwise

Synopsis
--------

.. code:: text

    $onpoly(n1,n2,x1,y1,xN1,yN1,x2,y2,xN2,yN2,...)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - n1
      - the number of points defining the first polygon
    * - n2
      - the number of points defining the second polygon
    * - x1
      - the x coordinate of the first point for the first polygon
    * - y1
      - the y coordinate of the first point for the first polygon
    * - xN1
      - the x coordinate of the Nth point for the first polygon
    * - yN1
      - the y coordinate of the Nth point for the first polygon
    * - x2
      - the x coordinate of the first point for the second polygon
    * - y2
      - the y coordinate of the first point for the second polygon
    * - xN2
      - the x coordinate of the Nth point for the second polygon
    * - yN2
      - the y coordinate of the Nth point for the second polygon

Properties
----------

None

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$inrect </identifiers/inrect>`

