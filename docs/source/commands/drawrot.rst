/drawrot
========

The **/drawrot** command rotates an area of a bitmap by the specified angle.

Synopsis
--------

.. code:: text

    /drawrot -hmnpbfc <@win> [color] <angle> [x y w h]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -b
      - indicates that you have specified the background color value
    * - -f
      - fits the newly rotated bitmap into the original width/height
    * - -c
      - centers the rotated image if -f is not specified
    * - -m
      - changes the stretch mode quality when the picture is resized
    * - -h
      - highlights the windows icon if it is minimized
    * - -n
      - prevents the display from being updated immediately
    * - -p
      - When centering, clip the rotated bitmap: only pixels inside the original bitmap are affected

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
      - the background color if -b is used, WATCH OUT, there's no -r switch on /drawrot, the color has to be RGB format.
    * - <angle>
      - the angle of the rotation
    * - [x y w h]
      - the area to rotate

Example
-------

None

Compatibility
-------------

Added: mIRC v5.3 (13 Dec 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------
