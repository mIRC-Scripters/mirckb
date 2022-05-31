/drawline
=========

The **/drawline** command draws a line from the first <x y> coordinate to the second, if more coordinates are specified, the line is continued.

Synopsis
--------

.. code:: text

    /drawline -ihnr <@win> <color> <size> <x y> <x y> [<x y>...]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -i
      - draws in inverse color mode. You can find the final color based on the two color by using $xor($xor(currentcolor,16777215),drawncolor). Drawing the same color gives white and may be used to create transparency effect.
    * - -h
      - highlights the windows icon if it is minimized
    * - -n
      - prevents the display from being updated immediately
    * - -r
      - indicates that the color is in RGB format

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <@win>
      - the window's name
    * - <color>
      - the color of the line
    * - <size>
      - the size of the line (thickness)
    * - <x y>
      - the first point
    * - <x y>
      - the second point
    * - [<x y>...]
      - if you gives more points, it will draw a line from the previous point to that point

Example
-------

None

Compatibility
-------------

Added: mIRC v5.3 (13 Dec 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------
