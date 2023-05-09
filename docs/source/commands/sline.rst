/sline
======

The /sline command is used to select a line, or a specific set of lines, in a specific window. This command works on most custom @windows, as well as channel nickname lists.

Synopsis
--------

.. code:: text

    /sline [c] -artc[N] <#channel> <N|nick>
    /sline [c] -artc[N] <@win> <N>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Causes the selection to select the new line while retaining all previous selections
    * - -r
      - Removes selections from either all lines or the Nth line (cannot unselect specific multiple lines at once).
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
    * - #channel
      - Specifies the window that you wish to target.
    * - N|nick
      - Tells mIRC which line number you wish to select, if using a channel window, you can pass a nickname to be matched against and that line number will be used

Examples
--------

.. code:: text

    /sline #example awesomePerson
    /sline -a #example John
    /sline -a #example UhOh

.. code:: text

    /sline @win 1

.. code:: text

    /sline -r #example awesomePerson

.. code:: text

    /sline -r #example 1

.. code:: text

    /sline -r #example

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/aline </commands/aline>`
    * :doc:`/window </commands/window>`

