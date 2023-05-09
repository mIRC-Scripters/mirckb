/cline
======

The /cline command changes the color of the Nth line/item in a custom window or channel's nicklist.

Synopsis
--------

.. code:: text

    /cline -hrmltc[N] [c] <@name/#channel> <N>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Highlights the window's button (if window is minimized)
    * - -r
      - Reset an item in the listbox to default; [c] parm must be omitted
    * - -m
      - When coloring a nick in the nicklist, also color the nick in channel messages
    * - -l
      - Apply to side listbox
    * - -t
      - forces a re-wrap of all lines in a window that have not yet been wrapped to the current window size.
    * - -c[N] 
      - Same as using the [c] parameter to change the color, but via a switch

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [c]
      - new color
    * - <@name/#channel>
      - target window/channel
    * - <N>
      - line/item number

Example
-------

.. code:: text

    ;Color your nick color number 4 (default red) in the active channel
    //cline -l 4 $chan $fline($chan,$me,1,1)

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/window>`
    * :doc:`$line </identifiers/line>`
    * :doc:`$fline </identifiers/fline>`
    * :doc:`$sline </identifiers/sline>`
    * :doc:`/aline </commands/aline>`
    * :doc:`/cline </commands/cline>`
    * :doc:`/dline </commands/dline>`
    * :doc:`/renwin </commands/renwin>`
    * :doc:`/sline </commands/sline>`
    * :doc:`/window </commands/window>`

