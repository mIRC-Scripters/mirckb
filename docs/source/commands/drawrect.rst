/drawrect
=========

The **/drawrect** command can be used to draw a rectangle in a picture window. Multiple rectangles can be drawn at once.

Synopsis
--------

.. code:: text

    /drawrect [-ihnrfecd] <@win> <color> <size> <x y w h> [x y w h [...]]

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
      - Highlights the windows icon if it is minimized.
    * - -n
      - Prevents the display from being updated immediately.
    * - -r
      - Indicates that the color is in RGB format.
    * - -f 
      - Draws a filled rectangle.
    * - -e
      - Draws an ellipse instead of a rectangle.
    * - -c 
      - Draws a focus rectangle.
    * - -d 
      - Draws a rounded rectangle, using the format "/drawrect -d x y w h [w h]" where w and h are the width and height of the ellipse used to draw the corners.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <@win> 
      - Name of the Picture Window to draw to.
    * - <color>
      - A mIRC colour value from 0 to 15, or if the -r switch is used, an RGB value.
    * - <size> 
      - Thickness of the border in pixels.
    * - <x y w h>
      - Co-ordinates for a rectangle in pixels, x and y are the top left corner.

Example
-------

.. code:: text

    ;Draws a rectangle that is blue (colour 2) with border thickness of 7, at co-ordinates 15,10 with a width of 200 and height of 150.
    /drawrect @window 2 7 15 10 200 150

    ;Same as above but the corners are drawn using a 5x5 ellipse.
    /drawrect -d @window 2 7 15 10 200 150 5 5

    ;Draws a filled green rectangle using an RGB colour value.
    /drawrect -fr @window 65280 1 5 5 20 20

Compatibility
-------------

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$rgb </identifiers/rgb>`
    * :doc:`$window </identifiers/window>`
    * :doc:`/drawcopy <drawcopy>`
    * :doc:`/drawdot <drawdot>`
    * :doc:`/drawfill <drawfill>`
    * :doc:`/drawline <drawline>`
    * :doc:`/drawpic <drawpic>`
    * :doc:`/drawreplace <drawreplace>`
    * :doc:`/drawrot <drawrot>`
    * :doc:`/drawsave <drawsave>`
    * :doc:`/drawscroll <drawscroll>`
    * :doc:`/drawtext <drawtext>`