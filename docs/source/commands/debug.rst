/debug
======

The **/debug** command outputs raw server messages to a file or a custom window  Incoming messages are prefixed with **<-** and outgoing messages are prefixed with **->**

Synopsis
--------

.. code:: text

    /debug [-cinptrNoN] [color_index] [on | off | @window | filename] [identifier]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Turns off debugging (close associated window as well)
    * - -i
      - Call a specific $identifier and use the returned value as the debug lines
    * - -n
      - Minimize the custom @window
    * - -p
      - Wrap the debug lines if it is too long for the @window
    * - -t
      - Adds timestamp to the debug lines
    * - -rN
      - Uses the N color index as the line color for received debug lines.
    * - -oN
      - Uses the N color index as the line color for outbound debug lines.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [color]
      - Optional text color for the debug window (Partly overridden by -rN and/or -oN) Can be color index 0-99
    * - [on|off]
      - Turns debug on or off
    * - [@window|filename]
      - outputs to a custom @window or a file
    * - [identifier]
      - Calls an identifier before logging the debugged line (the returned value if used for the logging)

Example
-------

.. code:: text

    ;Opens @raw debug window (wrap text+
    //debug -p @Raw

.. code:: text

    ;The line can be 'piped' through an alias on its way to the log file.
    From editbox: /debug -i Log.txt $console
    From script: /debug -i Log.txt $!console

    Alias console {
    ; split by spaces
    tokenize 32 $1-

    ; open window if not already opened
    if (!$window(Console)) window -e @Console

    if (<- == $1) aline -p 9 @Console >> $2-
    else aline -p 4 @Console << $2-

    ; return the line back to mIRC's log
    return $1-
    }

.. code:: text

    .. note:: the identifier is listed on command line instead of calling an alias. The yellow 8 is overridden by defining in/out colors with -rNoN. Alias uses $time to display seconds without forcing all windows to show seconds in their $timestamp too

    on *:CONNECT:{ debugg }

    alias debugg {
    window -ze2Dj2000k @debug
    titlebar @debug active= $+ $scid($window(@debug).cid).network logging: $addtok($gettok($window(@debug).titlebar,3-,32),$network,32)
    debug -pir44o52 8 @debug $!+([,$time,],[,$network,] $!1-)
    } ; Raccoon's altered by maroon

Compatibility
-------------

Added: mIRC v6.0 (16 Aug 2002)
See also
--------

.. hlist::
    :columns: 4

    * :doc: `$debug </identifiers/$debug>`
    * :doc: `$rawmsg </identifiers/$rawmsg>`
