/drawcopy
=========

The **/drawcopy** command copies part of a picture to a different position in the same window or to another window.

Synopsis
--------

.. code:: text

    /drawcopy -ihmnt <@win> [color] <x y w h> <@win> <x y [w h]>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -t
      - indicates that you have specified the [color] RGB value as a transparent color in the source bitmap
    * - -m
      - changes the stretch mode quality when the picture is resized
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
      - the window's name to copy from
    * - [color]
      - if -t is used, the RGB color used for transparency
    * - <x y w h>
      - portion to copy
    * - <@win>
      - the window's name to copy to
    * - <x y [w h]>
      - the coordinate where to draw, if [w h] are specified, the picture is squeed/stretched to fit, they can be negative value to get a mirror effect:

@win has a bitmap area of 16*16 pixels containing this picture:

.. image:: img/Drawpic&copy_negative.png

@win1 has a bitmap area of 48*16 pixels

If you copy the whole @win over @win1 at coordinate - 16,0 you would get (drawcopy @win 0 0 @win1 16 0):

.. image:: img/Drawpic&copy_negative1.png

Now we use a negative width of -16 to flip horizontally the bitmap (drawcopy @win 0 0 16 16 @win1 16 0 -16 16):

.. image:: img/Drawpic&copy_negative2.png

.. note:: The flipped bitmap is drawn at x + 1 instead of x, you have to draw at x - 1 or y - 1 when you flip.

Example
-------

None

Compatibility
-------------

Added: mIRC v5.3

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------