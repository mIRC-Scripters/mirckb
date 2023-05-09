/drawreplace
============

The /drawreplace command replaces <color1> with <color2> in the specified area of the picture window.

Synopsis
--------

.. code:: text

    /drawreplace -nr <@win> <color1> <color2> [x y w h]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
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
    * - <color1>
      - the color to be replaced
    * - <color2>
      - the color you replace with
    * - [x y w h]
      - the area of the picture you want to replace in

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.3

See also
--------