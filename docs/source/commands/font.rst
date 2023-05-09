/font
=====

The /font command allows you to change the font for the current window. If no parameters are specified, the font dialog pops up, otherwise the specified parameters are used.

Synopsis
--------

.. code:: text

    /font [-asbegilunkdmz|window] <fontsize> <fontname>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - applies the setting to the active window
    * - -s
      - applies the setting to the status window
    * - -b
      - makes the font bold
    * - -i
      - makes the font italic
    * - -l
      - applies the setting to the channel list window
    * - -u
      - applies the setting to the url list window
    * - -n
      - applies the setting to the notify list window
    * - -k
      - applies the setting to the links window (/links)
    * - -g
      - applies the setting to the finger window (old feature that has been removed)
    * - -m
      - applies the setting to the message window (/dqwindow)
    * - -d
      - makes the font the default for that type of window
    * - -e
      - clears the font entry for that window
    * - -z
      - clears all font settings and sets all windows to the specified font. If no font is specified, all windows are set to default font settings

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [window]
      - if none of the -azs switch is used, you must provide the name of a window instead
    * - <fontsize>
      - the size of the font, can be negative: it will then match the size of fonts in the font dialog
    * - <fontname>
      - the name of the font

Example
-------

.. code:: text

    /font -z -8 verdana
    /font -d "Status Window" -8 fixedsys
    /font -s 12 verdana

Compatibility
-------------

.. compatibility:: 3.92

See also
--------