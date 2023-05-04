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

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/$window>`
    * :doc:`$ebeeps </identifiers/$ebeeps>`
    * :doc:`$vol </identifiers/$vol>`
    * :doc:`/beep </commands/beep>`
    * :doc:`/ebeeps </commands/ebeeps>`
    * :doc:`/vol </commands/vol>`
    * :doc:`/window </commands/window>`
