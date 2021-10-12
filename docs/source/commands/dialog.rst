/dialog
=======

The **/dialog** command is used to create a dialog using a given table. The name is what the script/you will use to refer to the table. The standard dialog created using the /dialog command can be used to create model or modeless dialogs. Modeless it does not return a value when the dialog closes. As a result it does not halt the mIRC scripting engine, letting other script to keep processing. Dialogs can be kept open for as long as you want.

Synopsis
--------

.. code:: text

    /dialog -mhbpardievon <name> [table]
    /dialog -kcx <name>
    /dilaog -g <name> <newName>
    /dialog -t <name> [text]
    /dialog -s <name> [x y w h]
    /dialog -mhbpardievonts <name> [table] [x y w h] [text]

Switches
--------

Mode:
~~~~~

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -m
      - Modeless dialog
    * - -b
      - Size Mode: DBU
    * - -p
      - Size Mode: Pixels
    * - -h
      - Dialog work with active server connection

Modes Used with -m:
~~~~~~~~~~~~~~~~~~~

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Uses the current window as parent
    * - -d
      - opens the dialog on the desktop

Modes Used with -d:
~~~~~~~~~~~~~~~~~~~

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -i
      - Minimize dialog
    * - -e
      - Restores dialog

Close:
~~~~~~

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -k
      - clicks the ok button
    * - -c
      - clicks the cancel button
    * - -x
      - closes the dialog without triggering any event

Change:
~~~~~~~

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -t
      - Sets the dialog's title
    * - -s
      - Sets the dialog's size [X Y W H]
    * - -o
      - Sets the dialog on top of all windows
    * - -n
      - Unset -o
    * - -r
      - Centers the dialog
    * - -v
      - Sets the dialog as the active window
    * - -g
      - Renames dialog <name> <new name>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - Dialog Name
    * - [table]
      - Table Name
    * - [x y w h]
      - (x,y) coordinates, width and height
    * - [text]
      - Text

Example
-------

Consider:

.. code:: text

    Dialog Example1 {
      title "This is Example 1"
      size -1 -1 172 129
      option dbu
      tab "Tab A", 14, 2 0 165 123
      tab "Tab B", 15
      tab "Tab C", 16
      edit "", 17, 8 16 154 104, tab 16 multi return autohs vsbar
      menu "&File", 1
      item "&New", 6, 1
      item "&Open", 7, 1
      item break, 8, 1
      item "&Save", 9, 1
      item "Save &as", 10, 1
      menu "&Edit", 2
      item "&Copy", 11, 2
      item "P&aste", 12, 2
      menu "&view", 3
      item "&All", 13, 3
      menu "&Help", 4
      item "&About", 5, 4
    }

Example 1:

.. code:: text

    ;Modeless, Desktop
    /dialog -md Example1 Example1

Example 2:

.. code:: text

    ;Change the title of the dialog
    /dialog -t Example1 This is Example 2!

Example 3:

.. code:: text

    ;Rename the dialog
    /dialog -g Example1 Example3

Example 4:

.. code:: text

    ;Close the dialog, don't trigger any event
    /dialog -x Example3

Compatibility
-------------

Added: mIRC v5.5 (08 Jan 1999)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dialog </aliases/dialog>`
    * :doc:`$dname </aliases/dname>`
    * :doc:`$devent </aliases/devent>`
    * :doc:`$did </aliases/did>`
    * :doc:`$didwm </aliases/didwm>`
    * :doc:`$didreg </aliases/didreg>`
    * :doc:`$didtok </aliases/didtok>`
    * :doc:`/did <did>`
    * :doc:`/didtok <didtok>`
