/loadbuf
========

The /loadbuf command loads the specified number of lines from the end of the file of filename into the specified window.

Synopsis
--------

.. code:: text

    /loadbuf [lines] [-apiNrsglecNnomt<topic>] <window | dialog id> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - adds the lines into the active window
    * - -p
      - forces lines of text to wrap when added to the window
    * - -iN
      - makes sure that lines are indented if they wrap, if N is specified, indents by N characters
    * - -r
      - clears the contents of the output window before adding lines to it
    * - -s
      - adds the lines into the status window
    * - -g
      - adds the lines into the finger window (feature removed)
    * - -l
      - adds the lines into the side-listbox in a custom window
    * - -e
      - evaluates variables and identifiers in the line being read
    * - -h
      - hides a line if -e is specified and it doesn't evaluate anything in the line being read
    * - -cN
      - specifies the default color for lines, N is an index color
    * - -n
      - if logging is enabled for that window, logs the loaded lines
    * - -m
      - used with -n, indicates that the text shouldn't be timestamped in the log file. (the buffer text is already timestamped or you might not want it to be timestamped)
    * - -o
      - indicates that you have specified the [dialog id] parameters instead of a window name in order to load lines into a custom dialog control
    * - -t
      - loads the lines under the [topic] section in a file

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [lines]
      - If specified, the number of lines to add from the end the file, otherwise the whole content of the file is added.
    * - <window | dialog id>
      - The window's name or the dialog's name and an id to adds the lines to.
    * - <filename>
      - The filename you want to add lines from.

Example
-------

<code>//window @test | loadbuf $lines($mircini) @test $qt($mircini)</code>

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/filter </commands/filter>`
    * :doc:`/savebuf </commands/savebuf>`

