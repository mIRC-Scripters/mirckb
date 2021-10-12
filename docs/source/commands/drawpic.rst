/drawpic
========

The **/drawpic** commmand draws a picture at the specified coordinates. The picture can be a graphics file, or an ico/exe/dll file.

Synopsis
--------

.. code:: text

    /drawpic -ihmnoftsclgN <@win> [color] <x y [w h]> [x y w h] [N] [M] <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -t
      - indicates that you have specified the [color] RGB value as a transparent color in the specified bitmap
    * - -s
      - indicates that you have specified the first [w h] parameters to squeeze/stretch the bitmap
    * - -c
      - indicates that the bitmap should be cached. This greatly speeds up subsequent references to this bitmap. If you specify -c and the bitmap is already in the cache, it is loaded and used from the cache, otherwise it is reloaded from the file. You can clear the entire cache with /drawpic -c
    * - -l
      - tiles the picture
    * - -m
      - changes the stretch mode quality when the picture is resized
    * - -o
      - indicates that you have specified the [N] value before the filename, representing the index of the icon in the file, or the Nth frame in a GIF file.
    * - -f
      - used with -o, indicate that you want to use the Mth frame in the Nth icon, eg /drawpic -of [N] [M]
    * - -gN
      - attempts to load the large icon in an icon file, if none exists, it loads the small icon. If N is specified, N = 0 loads the small icon, N = 1 loads the large icon, and N = 2 loads the actual icon
    * - -i
      - draws in inverse color mode. You can find the final color based on the two color by using $xor($xor(currentcolor,16777215),drawncolor). Drawing the same color gives white and may be used to create transparency effect.
    * - -h
      - highlights the windows icon if it is minimized
    * - -n
      - prevents the display from being updated immediately

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <@win>
      - the window's name
    * - [color]
      - if -t is used, the RGB color used for transparency
    * - <x y [w h]>
      - the x y coordinates where you want to draw, if -s is used, [w h] is the width/height that will be used to squeeze/stretch the bitmap
    * - [x y w h] 
      - the area in the picture to be drawn
    * - [N]
      - if -o is used, the index number of the icon in the file
    * - [M]
      - if -fo is used, the index number of the frame in the icon.
    * - <filename>
      - the filename for the picture

Example
-------

None

Compatibility
-------------

Added: mIRC v5.3

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------