/aline
======
The **aline command** is used to add a single line of text to a custom window. This command is limited to custom @windows, If you need a more general command that is able to print to both custom windows, channel, and query consider using the **/echo** command instead.

.. note:: If the main window is sorted (text or listbox and /window -s has been used), lines added with /echo to that window won't be sorted, only lines added with /aline will.

Synopsis
--------

.. code:: text

    /aline -sahpinl [c] <@name> <text>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Clears the old selection in a listbox and selects the newly added item 
    * - -a
      - Selects the newly added item while keeping the old selection in a listbox
    * - -h
      - Highlights the window's node in the treebar/switchbar is the window is minimized
    * - -p 
      - Forces the line to be wrapped if it's too long to fit in on one line (does not apply to listboxes)
    * - -i
      - Indent the newly added line (does not apply to listboxes)
    * - -n
      - Prevent the line from being added if it already exists
    * - -l
      - Specify the action to take place on the side-listbox
    * - -t
      - Forces a re-wrap of all lines in a window that have not yet been wrapped to the current window size.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [c]
      - An optional color number for the line.
    * - <@name>
      - The name of the window.
    * - <text>
      - The text to be added.

Example
-------

.. code:: text

    Alias Example {
      ;open a desktop custom window (main window is a listbox, no side-listbox and with an editbox)
      window -lde @Foo

      ;Add a line, line colored in yellow (8)
      aline 8 @Foo Line A

      ;Add a line, color Dark Green (3), selected, clear old selection
      aline -s 3 @Foo Line B
    }

Compatibility
-------------

Added: mIRC v5.0 (02 Apr 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$line </identifiers/line>`
    * :doc:`$fline </identifiers/fline>`
    * :doc:`$sline </identifiers/sline>`
    * :doc:`/cline <cline>`
    * :doc:`/dline <dline>`
    * :doc:`/echo <echo>`
    * :doc:`/iline <iline>`
    * :doc:`/rline <rline>`
    * :doc:`/sline <sline>`
    * :doc:`/window <window>`