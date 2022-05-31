/fupdate
========

The **/fupdate** command's setting is the maximum display update delay. So if you specify 100, it will display less frequently than 10. That said, with the latest algorithm, even if you specify 100, it may not reach that since it is adjusting automatically to the maximum value that makes a significant difference.

Higher numbers can reduce delay while a large number of text lines scroll down the window, but may also cause the screen display to update in unexpected ways. Users will need to benchmark different N values until they find one that works for them.

If used with no parameter, it displays the current setting.

Synopsis
--------

.. code:: text

    /fupdate [N]

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
    * - N
      - The algorithm setting, where 0 is disabled, or is on a scale from minimum 1 to maximum 100.

Example
-------

.. code:: text

    ;Display current setting:
    /fupdate
    ;Set to 10 within range 1-100:
    /fupdate 10
    ;Disable fupdate feature:
    /fupdate 0

Compatibility
-------------

Added: mIRC v7.52 (28/02/2018)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
---------
