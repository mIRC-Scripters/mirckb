/linesep
========

The /linesep command prints the line separator at a specified target. With no arguments, the line separator is printed to the active window. A line separator is only added if it would not be the first line and if the last line is not already the line separator.
The line separator can be changed by going into the options dialog (:kbd:`Alt+O`) -> Other -> Line separator. If this option dialog shows the line separator is blank, /linesep does not add a blank line. You can also set the line separator to multiple characters like -/- and the entire string is used as the line separator.

If your goal is to simply enclose your text with a pair of line separator:

Note that:

.. code:: text

    //linesep @x | echo @x Example Line. | linesep @x

Is equivalent to:

.. code:: text

    //echo -e @x Example Line.

Synopsis
--------

.. code:: text

    /linesep [ @window | #channel | query | -s | -a ]

.. note:: default is -a if no parameter is used.

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Print the line separator in the status window
    * - -a
      - Print the line separator in the active window

.. note:: This is an echo, so if active window is a -l listbox @window, the echo appears in Status Window.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [window]
      - The target @window, #channel, or query

Example
-------

A simple line separator between two lines:

.. code:: text

    alias example {
      ; create our example window
      window -de @example -1 -1 400 400
    
      ; print a simple line
      aline @example Line A.
    
      ; add a line separator
      linesep @example
    
      ; print another simple line
      aline @example Line B.
    
    The following /linesep command does nothing because the last line is already the line separator character.
    //echo -a $readini($mircini,text,linesep) | /linesep -a
    
    }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/aline </commands/aline>`
    * :doc:`/dline </commands/dline>`
    * :doc:`/echo </commands/echo>`

