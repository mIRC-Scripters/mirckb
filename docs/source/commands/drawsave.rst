/drawsave
=========

The **/drawsave** command saves the content of the specified picture @window to a file (bmp or jpeg).

Synopsis
--------

.. code:: text

    /drawsave -abNqNv [x y w h] <@win> <filename|&binvar>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - means that you specified the [x y w h] parameters, representing the region to be saved
    * - -bN
      - allows you to specify the bit depth of the saved file, which can be 1, 4, 8, 16, 24, or 32.
    * - -qN
      - allows you to specify the quality of the jpeg file that is being saved, where N is between 1 and 100.
    * - -v
      - means that you specified a binvary variable to save the content to, instead of saving to disk.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <@win>
      - the window's name
    * - <filename>
      - the filename you want to save to

Example
-------

None

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/drawpic </commands/drawpic>`
