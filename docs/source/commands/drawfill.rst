/drawfill
=========

The **/drawfill** command fills an area with the specified color starting at the specified co-ordinates.

Synopsis
--------

.. code:: text

    /drawfill -ihnrs <@win> <color> <color> <x y> [filename] [<x y>...]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - indicates that the second color parameter is the color that should be filled (surface fill), if -s is not used specified, the second color is the border color at which filling should stop (border fill)
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
      - the color used for the fill
    * - <color>
      - the color used to know how to fill (if -s, it fills as long as the color of the pixels around is the same color as the one you provide here, otherwise, it fills as long as the color of pixel is not the color you provide here)
    * - <x y>
      - the coordinate where to fill
    * - [filename]
      - if specified, a bitmap .BMP file that is 8 by 8 pixels in size and is used as a fill pattern
    * - [<x y>...]
      - more coordinates to apply the same fill on

Example
-------

None

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------
