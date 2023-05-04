/savebuf
========

The **/savebuf** command saves the specified number of lines from the end of the buffer of the specified window into the specified filename.

Synopsis
--------

.. code:: text

    /savebuf -sgaolp [lines] <window | dialog id> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Appends the lines to the output file
    * - -s
      - Saves the status window buffer
    * - -g
      - Saves the finger window buffer (removed feature)
    * - -o
      - Indicates that you have specified the [dialog id] parameters instead of a window name in order to load lines into a custom dialog control
    * - -p
      - Strip control code from saved lines
    * - -l
      - Save the content of the side listbox of the window if there is one (can be used to save the nicklist of a channel quickly)
    * - -n
      - Treat the wrapped lines as a single line

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [lines]
      - If specified, the number of lines to add from the end the file or a range of lines N-N2, otherwise the whole content of the file is added.
    * - <window | dialog id>
      - The window's name or the dialog's name and an id to adds the lines to.
    * - <filename>
      - The filename you want to add lines from.

Example
-------

None

Compatibility
-------------

Added: mIRC v5.0 (21 Apr 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/loadbuf </commands/loadbuf>`
