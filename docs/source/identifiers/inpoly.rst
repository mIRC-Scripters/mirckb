$inpoly
=======

$inpoly returns :doc:`$true </identifiers/true>` if the specified point is inside the specified polygon, :doc:`$false </identifiers/false>` otherwise

Synopsis
--------

.. code:: text

    $inpoly(x,y,x1,y1,x2,y2,x3,y3,...)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - x
      - the x coordinate of the point
    * - y
      - the y coordinate of the point
    * - x1
      - the x coordinate of the first point
    * - y1
      - the y coordinate of the first point
    * - x2
      - the x coordinate of the second point
    * - y2
      - the y coordinate of the second point
    * - xN
      - the x coordinate of the Nth point
    * - yN
      - the y coordinate of the Nth point

Properties
----------

None

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.41

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inrect </identifiers/inrect>`
    * :doc:`$onpoly </identifiers/onpoly>`

