/titlebar
=========

The **/titlebar** command can be used to change the titlebar of a window, either the main mIRC window, or a custom @window.

Synopsis
--------

.. code:: text

    /titlebar -m [@window] <text>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -m
      - change the titlebar of the main application even if you pass a window's name

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [@window]
      - if specified, the window's name, otherwise the main mIRC's window is used.
    * - <text>
      - the new text for the titlebar, all control codes are stripped from the text.

Example
-------

.. code:: text

    alias refresh_win {
    ; create a window if it doesn't exist
    if (!$window($1)) window $1
    ; refresh the titlbar of that window
    titlebar $1 Position: $window($1).x $window($1).y
    ; refresh mIRC's main window's titlebar
    titlebar Active : $1
    }

Compatibility
-------------

Added: mIRC vmIRC 4.5 ()

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/$window>`
    * :doc:`$titlebar </identifiers/$titlebar>`
