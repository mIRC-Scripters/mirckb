$font
=====

$font returns the Nth font available on the system

Synopsis
--------

.. code:: text

    $font(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth font, if N = 0 returns the total number of font available

Without a property, returns the name of the font

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .size
      - return a comma separated list of size supported by the font
    * - .pitch
      - returns "variable" or "fixed" depending on the font's pitch
    * - .type
      - returns the type of the font "truetype", "raster", "vector", "unknown" or "device"

Example
-------

.. code:: text

    //echo -a $font(0)

Compatibility
-------------

.. compatibility:: 7.44

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/font </commands/font>`

