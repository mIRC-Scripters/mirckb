/tray
=====

The /tray command can be used to change the tray settings for mIRC. The tray command can also be used to change the mIRC tray icon to the icon located at index N in the specific file. For all switches, N can be 0 for disabled or 1  for enabled.

Synopsis
--------

.. code:: text

    /tray -iN <ico/exe/dll>
    /tray -mNsNtNaNcN

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -iN
      - The index of the icon in the file
    * - -mN
      - Always show mIRC icon in system tray
    * - -sN
      - Minimize mIRC to tray upon startup
    * - -tN
      - When minimized, place mIRC in the system tray
    * - -aN
      - Animate icon when there is activity
    * - -cN
      - Single click on tray icon to open

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <ico/exe/dll>
      - The file with the icon to use

Example
-------

.. code:: text

    alias example {
      ; always show the mIRC icon
      tray -m1
      ; change the icon to a computer chip icon
      tray -i13 C:\Windows\System32\shell32.dll
    }

Compatibility
-------------

.. compatibility:: 5.5

See also
--------