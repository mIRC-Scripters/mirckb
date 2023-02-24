/did
====

The **/did** command allows you to modify the values of controls in a dialog.

Synopsis
--------

.. code:: text

    /did -ftebvhnmcukradiogjslz <name> <id> [n] [text | filename | start [end] ]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -f
      - set focus on <id>, use -fu to set a tab on focus
    * - -t
      - set <id> as default button 
    * - -e
      - enable <id>
    * - -b
      - disable <id>
    * - -v
      - make <id> visible
    * - -h
      - hide <id>
    * - -n
      - enables editbox
    * - -m
      - disables editbox
    * - -c
      - check a checkbox/radio/list/combo/ line, can be used to set the selected text in an edibox/combo drop control
    * - -u
      - uncheck a checkbox/radio/list/combo line, used with -c, can be used to mark a 3dstate checkbox as indeterminate, used with -f, sets the focus on a tab control
    * - -k
      - used with -c and -u, keeps other selections in a listbox
    * - -s
      - checks the checkbox of an item in a listbox control that uses checkboxes
    * - -l
      - unchecks the checkbox of an item in a listbox control that uses checkboxes
    * - -r
      - clears all text in <id>
    * - -a
      - appends text to the end of a control or adds an item to a menu
    * - -d
      - deletes the Nth line in a listbox/combo
    * - -i
      - insert line in a listbox/combo or inserts an item to a menu
    * - -o
      - overwrite the Nth line in a listbox/combo with text
    * - -g
      - set a new icon/bmp to an icon control
    * - -z
      - resets the width of horizontal scrollbar in listbox, or set the range of a scrollbar control
    * - -j
      - resets the edited setting in an editbox

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - name of the dialog
    * - <id>
      - id of the controls, you can use the form N-N1,N2-N3 to change multiple ids at once, 1-5,6,9 would change the following ids: 1,2,3,4,5,6,9
    * - [n]
      - usually a line number, it can also be an id number with menus, use 0 if you want to access the editbox of a combo control.
    * - [text]
      - the text parameter if applicable
    * - [filename]
      - used with -g
    * - [start [end]]
      - used with -z to set the range of a scrollbar, or with -c to set a selection

Example
-------

You can check the dialog components page for examples of /did per control.

Compatibility
-------------

Added: mIRC v5.5 (08 Jan 1999)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$did </identifiers/did>`
    * :doc:`$didtok </identifiers/didtok>`
    * :doc:`$dialog </identifiers/dialog>`
    * :doc:`$didwm </identifiers/didwm>`
    * :doc:`$didreg </identifiers/didreg>`
    * :doc:`/dialog <dialog>`