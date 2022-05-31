/flushini
=========

The **/flushini** command flushes the specified INI file to the hard disk. INI files are cached in memory, so you may want to do this to make sure that your INI is updated properly. It is advised that you do not use this command to modify any INI file currently being used by mIRC.

Synopsis
--------

.. code:: text

    /flushini <filename>

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - the INI file to be flushed

Example
-------

.. code:: text

    /flushini myini.ini

Compatibility
-------------

Added: mIRC v4.52 (06/07/1996)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------
