/drawsave
=========

The **/drawsave** command saves the content of the specified picture @window to a file (bmp or jpeg).

Synopsis
--------

.. code:: text

    /drawsave -bNqN <@win> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -bN
      - allows you to specify the bit depth of the saved file, which can be 1, 4, 8, 16, 24, or 32.
    * - -qN
      - allows you to specify the quality of the jpeg file that is being saved, where N is between 1 and 100.

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

Added: mIRC v5.3

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/drawpic <drawpic>`