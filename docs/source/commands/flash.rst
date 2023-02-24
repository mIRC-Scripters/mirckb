/flash
======

The **/flash** command flashes the mIRC titlebar and tray icon. The title of the window can be set if the parameter is provided. mIRC or the window specified must not be the active window for this to work. The N parts of the switches are optional, if not specified the flashing and beeping will repeat continuously.

Synopsis
--------

.. code:: text

    /flash -wNbNrNc [windowName] [titleText]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -wN
      - play the flash sound, limit to N times
    * - -bN
      - beep, limit to N times
    * - -rN
      - repeat the flashing N times
    * - -c
      - clear the flash for all windows

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [titleText]
      - The text to show up in the titlebar
    * - [windowName]
      - The window name to flash

Example
-------

.. code:: text

    alias example {
      ; create a new desktop window, minimize it
      window -den @example
      ; flash the window, beep
      flash -b @example
    }

Compatibility
-------------

Added: mIRC v5.3 (13 Dec 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/window>`
    * :doc:`$ebeeps </identifiers/ebeeps>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/beep <beep>`
    * :doc:`/ebeeps <ebeeps>`
    * :doc:`/vol <vol>`
    * :doc:`/window <window>`
