/cline
======

The **/cline** command changes the color of the Nth line/item in a custom window or channel's nicklist.

Synopsis
--------

.. code:: text

    /cline -hrml [c] <@name/#channel> <N>

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

Added: mIRC v5.1 (28 Aug 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </aliases/window>`
    * :doc:`$line </aliases/line>`
    * :doc:`$fline </aliases/fline>`
    * :doc:`$sline </aliases/sline>`
    * :doc:`/aline <aline>`
    * :doc:`/cline <cline>`
    * :doc:`/dline <dline>`
    * :doc:`/renwin <renwin>`
    * :doc:`/sline <sline>`
    * :doc:`/window <window>`