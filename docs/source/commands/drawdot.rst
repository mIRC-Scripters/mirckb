/drawdot
========

The **/drawdot** command draws a dot to the specified coordinates with a specific color in a specific picture window

Synopsis
--------

.. code:: text

    /drawdot -ihnr @ <color> <size> <x y> [<x y>...]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
- use RGB color instead of the mIRC standard colors
    * - -i
      - draws in inverse color mode. You can find the final color based on the two color by using $xor($xor(currentcolor,16777215),drawncolor). Drawing the same color gives white and may be used to create transparency effect.
    * - -h
      - highlights the windows icon if it's minimized.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <color>
      - mIRC Color to draw with (unless -r is used, then RGB color is used)
    * - <size>
      - radius
    * - <x y>
      - coordinates
    * - [<x y>...]
      - more optional coordinates

Example
-------

.. code:: text

    ;draws a small black dot in the top left of the window
    /drawdot @PicWin 1 1 10 10

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/$window>`
    * :doc:`$click </identifiers/$click>`
    * :doc:`$mouse </identifiers/$mouse>`
    * :doc:`$inellipse </identifiers/$inellipse>`
    * :doc:`$inrect </identifiers/$inrect>`
    * :doc:`$inroundrect </identifiers/$inroundrect>`
    * :doc:`$inpoly </identifiers/$inpoly>`
    * :doc:`$onpoly </identifiers/$onpoly>`
    * :doc:`$rgb </identifiers/$rgb>`
    * :doc:`$getdot </identifiers/$getdot>`
    * :doc:`$height </identifiers/$height>`
    * :doc:`/drawcopy </commands/drawcopy>`
    * :doc:`/drawfill </commands/drawfill>`
    * :doc:`/drawline </commands/drawline>`
    * :doc:`/drawpic </commands/drawpic>`
    * :doc:`/drawrect </commands/drawrect>`
    * :doc:`/drawreplace </commands/drawreplace>`
    * :doc:`/drawsave </commands/drawsave>`
    * :doc:`/drawscroll </commands/drawscroll>`
    * :doc:`/drawtext </commands/drawtext>`
