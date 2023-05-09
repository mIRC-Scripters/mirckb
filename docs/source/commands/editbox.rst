/editbox
========

The /editbox command provides the ability to edit the editbox of a window according to the switches. To specify a dcc chat window, prefix the nickname with an equal sign '='.

Synopsis
--------

.. code:: text

    /editbox [-saf[N]nopbNeNvqN] [window] <text>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - specifies the Status window
    * - -a
      - specifies the Active window
    * - -fN
      - if N = 1 sets focus, if N = 2 uses editbox with focus
    * - -p
      - indicates that a space should be appended to text
    * - -n
      - fills the editbox and presses the enter key in the editbox
    * - -o
      - applies the command to the second editbox in a channel window
    * - -bN
      - set the start of the selection
    * - -eN
      - set the end of the selection
    * - -v
      - used with -f and -q, prevents the editbox contents from being changed
    * - -qN
      - disables the second editbox with N = 0, enables it with N = 1, and toggles the state if N = 2

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [window]
      - if the switch doesn't involve a window to be used, you must provide it
    * - <text>
      - the text used for the edition

Example
-------

A popup example

Add a smileyface to the second edit box:

.. code:: text

    /editbox -oq ☺ $+ editbox($chan,1)

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$editbox </identifiers/editbox>`

