/clear
======

The /clear command is used to clears the buffer of the current window. If a window name is specified that window's buffer will be cleared.

Additionally, the clear command can also be used to erase the history of the editbox as well as the clicks history of the picture window.

You can use "Status Window" and =nick for the status window and dcc chat windows.

Synopsis
--------

.. code:: text

    /clear -sghlcn [windowName]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - clears the status window
    * - -g
      - clears the finger window
    * - -h
      - clears the editbox command history for a window.
    * - -l
      - clears the side-listbox in a custom window
    * - -c
      - clears the click history in a picture window
    * - -n
      - delay update of display untill a forced redraw (pic window)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [windowName]
      - Window name

Example
-------

.. code:: text

    ;Clear the status window
    /clear -s
    
    ;Clears a custom window called "@Highlight_Log"
    /clear @Highlight_Log

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$line </identifiers/line>`
    * :doc:`$fline </identifiers/fline>`
    * :doc:`/clearall </commands/clearall>`
    * :doc:`/loadbuf </commands/loadbuf>`
    * :doc:`/savebuf </commands/savebuf>`
    * :doc:`/window </commands/window>`

