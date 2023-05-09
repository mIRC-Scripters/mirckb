/drawtext
=========

The /drawtext command draws text at the specified co-ordinates. If you use a negative number for the font size, it will match the size of fonts in the font dialog. The /drawtext command will use some default options for anti-aliasing that you cannot change (yet), meaning that a text drawn in black may not be drawn only using the expected color, this can be a real concern when using :doc:`/drawfill </commands/drawfill>` to fill an area with text inside it.

Synopsis
--------

.. code:: text

    /drawtext -hnrpbocv <@win> <color> [color] [fontname fontsize] <x y [w h]> <text>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -p
      - processes and interprets control codes in the text
    * - -b
      - indicates that you have specified the second color parameter as the background color for the text
    * - -c
      - means that you have specified the [w h] values as the rectangle in which text should be printed. Text will be clipped if it extends beyond this rectangle
    * - -h
      - highlights the windows icon if it is minimized
    * - -n
      - prevents the display from being updated immediately
    * - -r
      - indicates that the colors are in RGB format
    * - -o
      - Attempt to draw the text in bold. A $chr(2) is inserted at the beginning of the string and is interpreted (but the others control codes won't be). If you use -p as well as -o, control code will be interpreted and having a $chr(2) in your text will break the bold.
    * - -i
      - Same as -o but for italic with $chr(29)
    * - -v
      - Draw text from a binvar

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
      - the foreground color
    * - [color]
      - the background color, if -b has been specified
    * - [fontname fontsize]
      - the name of the font and the size of the font
    * - <x y [w h]>
      - the coordinate of the text
    * - <text>
      - the text to be drawn

Example
-------

.. code:: text

    drawtext -rn @mygame 0 verdana 20 30 30 the fps is: 60

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$width </identifiers/width>`
    * :doc:`$height </identifiers/height>`

