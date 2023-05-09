$pic
====

$pic returns size informations about .bmp, .jpg or .png filenames

Synopsis
--------

.. code:: text

    $pic(filename)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - filename
      - The filename you want the size informations of

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .height
      - Returns the height of the picture
    * - .width
      - Returns the width of the picture
    * - .size
      - Return the product of the width by the height, this value is returned by default if no property is specified
    * - .frames
      - Returns the number of frames in a file.
    * - .delay
      - Returns the delay
    * - .icons
      - Returns the icon

Example
-------

.. code:: text

    //echo -a $pic(C:\K.png)

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/window>`
    * :doc:`$getdot </identifiers/getdot>`
    * :doc:`$width </identifiers/width>`
    * :doc:`$height </identifiers/height>`
    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inrect </identifiers/inrect>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$onpoly </identifiers/onpoly>`
    * :doc:`$rgb </identifiers/rgb>`
    * :doc:`$mouse </identifiers/mouse>`
