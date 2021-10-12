/close
======

The **/close** command is used to close all the windows of a specified type and matching a specific name. If no name is used, all the windows with the specified type will close. Names support wildcard characters. You can also close the Nth window for -cfsg, with -cNfNsNgN, if you specify a name, the Nth window matching that name will be closed.

Synopsis
--------

.. code:: text

    /close [-ticfgms@[ID]axdnu] [name1] ...[nameN]
    /close [-cNfNsNgN] [name1] ...[nameN]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -i
      - Inactive DCC windows (send, get, chat, fserv)
    * - -it
      - Inactive Status window (not connected nor connecting)
    * - -t
      - Status Window
    * - -l
      - Channel list windows
    * - -k
      - Link windows
    * - -c
      - DCC Chat windows
    * - -f
      - DCC fserve windows
    * - -g
      - DCC Get windows
    * - -s
      - DCC Send windows
    * - -m
      - Query windows 
    * - -@[ID/name]
      - A custom window's name or a window ID
    * - -cN
      - Nth DCC chat window
    * - -fN
      - Nth DCC fserve windows
    * - -gN
      - Nth DCC Get windows
    * - -sN
      - Nth DCC Send windows
    * - a
      - apply to all server connections
    * - x
      - apply to current server connection
    * - d 
      - apply to single message window
    * - n
      - apply to notify list
    * - u
      - apply to urls list

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [nick1]
      - A nickname for the window to close 
    * - [nickN]
      - Additional nicknames 

Example
-------

.. code:: text

    ;Close all query windows
    /close -m

    ;Close all custom windows containing \"#\" in their name
    /close -@ @*#*

    ;Close the 2nd DCC chat window with Dave
    /close -c2 Dave

Compatibility
-------------

Added: mIRC v4.6 (07 Sep 1996)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/clear <clear>`
    * :doc:`/clearall <clearall>`
    * :doc:`/debug <debug>`
    * :doc:`/window <window>`
