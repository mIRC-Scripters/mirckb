/drawsize
=========

The **/drawsize** command extend the bitmap size of a picture window.

Synopsis
--------

.. code:: text

    /drawsize <@win> <w> <h>

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
    * - <w>
      - new width
    * - <h>
      - new height

/window cannot be used to set the size of the bitmap (-f doesn't guarantee anything even for window area).

While /window or two /window can be used to set the bitmap correctly, /drawsize is better and more consistent.

.. note:: a bitmap cannot be sized to less than the largest point that has been drawn on it (which can be reset with /clear). Once a size has been set, changing the window size will not resize it to less than the set size. can be cleared with /clear

With /drawsize, you can extend the bitmap to make sure your draws are correctly made beyond the size of the window without having the size of the window (what's visible) to be the same (more or less, borders and visual effect put aside) as the size of the bitmap.

Example
-------

None

Compatibility
-------------

Added: mIRC v7.48 (15 Apr 2017)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/window>`
    * :doc:`$click </identifiers/click>`
    * :doc:`$mouse </identifiers/mouse>`
    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inrect </identifiers/inrect>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$onpoly </identifiers/onpoly>`
    * :doc:`$rgb </identifiers/rgb>`
    * :doc:`$getdot </identifiers/getdot>`
    * :doc:`$height </identifiers/height>`
    * :doc:`/drawcopy </commands/drawcopy>`
    * :doc:`/drawfill </commands/drawfill>`
    * :doc:`/drawline </commands/drawline>`
    * :doc:`/drawpic </commands/drawpic>`
    * :doc:`/drawrect </commands/drawrect>`
    * :doc:`/drawreplace </commands/drawreplace>`
    * :doc:`/drawsave </commands/drawsave>`
    * :doc:`/drawscroll </commands/drawscroll>`
    * :doc:`/drawtext </commands/drawtext>`
