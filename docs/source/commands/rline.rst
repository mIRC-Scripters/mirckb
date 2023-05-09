/rline
======

The /rline command replaces a line in a custom @window.

Synopsis
--------

.. code:: text

    /rline -ahsltc[N] [c] <@name> <N> <text>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Clears the old selection in a listbox and selects the newly added item.
    * - -a
      - Selects the newly added item while keeping the old selection in a listbox
    * - -h
      - Highlights the window's node in the treebar is the window is minimized
    * - -l
      - Specify the action to take place on the side-listbox
    * - -t
      - forces a re-wrap of all lines in a window that have not yet been wrapped to the current window size.
    * - -c[N]
      - Same as using the [c] parameter to change the color of the line, but via a switch

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [c]
      - An optional color number for the line
    * - <@name>
      - The name of the window
    * - <N>
      - The number of the line you want to replace
    * - <text>
      - The text replacing the Nth line

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/aline </commands/aline>`
    * :doc:`/iline </commands/iline>`
    * :doc:`/dline </commands/dline>`
    * :doc:`/cline </commands/cline>`
    * :doc:`/sline </commands/sline>`
    * :doc:`$line </identifiers/line>`
    * :doc:`$fline </identifiers/fline>`
    * :doc:`$sline </identifiers/sline>`
    * :doc:`$window </identifiers/window>`

