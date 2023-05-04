/dline
======

The **dline** command is used to delete lines of text from a custom window.

Synopsis
--------

.. code:: text

    /dline -hlcNt <@name> <N[-N2]>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Highlights the window's node in the treebar if the window is minimized
    * - -l
      - Specify the action to take place on the side-listbox
    * - -t
      - forces a re-wrap of all lines in a window that have not yet been wrapped to the current window size.
    * - -c[N]
      - as using the [c] parameter to change the color, but via a switch

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <@name>
      - The name of the window
    * - <N[-N2]>
      - The range to be deleted, (negative values are NOT accepted)

Example
-------

.. code:: text

    Alias Example {
    ;open a desktop custom window (listbox and with an editbox)
    Window -lde @Foo

    ;Add a line, line colored in yellow (8)
    Aline 8 @Foo Line A

    ;Add a line, color Dark Green (3), selected, clear old selection (x3)
    Aline -s 3 @Foo Line B
    Aline -s 3 @Foo Line C
    Aline -s 3 @Foo Line D
    ;Delete line 2 and 3 with range 2-3, only A D remain
    Dline @Foo 2-3
    }

Compatibility
-------------

Added: mIRC v5.0 (21 Apr 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$line </identifiers/$line>`
    * :doc: `$fline </identifiers/$fline>`
    * :doc: `$sline </identifiers/$sline>`
    * :doc: `/cline </commands/cline>`
    * :doc: `/dline </commands/dline>`
    * :doc: `/echo </commands/echo>`
    * :doc: `/iline </commands/iline>`
    * :doc: `/rline </commands/rline>`
    * :doc: `/sline </commands/sline>`
    * :doc: `/window </commands/window>`
