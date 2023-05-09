$did
====

The $did identifier allows you to get the settings and values of controls in a dialog and use them to assist in performing the functions of buttons, radio boxes, etc.

Synopsis
--------

 $did(<name>,<id>,[N])[.property]

.. note:: Inside the on dialog event, you can omit the whole dialog <name> parameter:

 $did(<id>,[N])[.property]

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - text
      - returns line or Nth line
    * - len
      - returns length of line or length of Nth line 
    * - lines
      - returns number of lines
    * - sel
      - returns line number of Nth selected line
    * - seltext
      - returns selected text in an editbox, or first selected item in a listbox
    * - selstart
      - returns selected start character in the editbox
    * - selend
      - returns selected end character in editbox line
    * - edited
      - returns $true if text in editbox was changed, and is not empty.
    * - state
      - returns state of checkboxes, radio buttons, 0 = off, 1 = on, 2 = indeterminate (for 3stage checkbox)
    * - next
      - returns id of next control in order of tab keypress.
    * - prev
      - returns id of previous control in order of tab keypress.
    * - visible
      - returns $true if control is visible, otherwise $false
    * - enabled
      - returns $true if control is enabled, otherwise $false
    * - isid
      - returns $true if id exists in the dialog, otherwise $false
    * - csel
      - returns line number of Nth checked box in a listcb control, if N = 0, returns number of checkmarked lines
    * - cstate
      - returns 0 = off, 1 = on for item in a listcb control

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
      - id of the controls
    * - [N]
      - usually a line number, it can also be an id number with menus, use 0 if you want to access the editbox of a combo control.
    * - [.property]
      - used to check features of the dialog id, such as button state, selected line in a combo control, or number of lines in an editbox.

Example
-------

This example will monitor what events are triggering, what event ID is triggering the event, and any current captions or titles of the event ID which triggered an event. Created a custom Aliases - mIRC|alias called ''/whatEvents'' which will open up the local Dialogs - mIRC|dialog ''whatEvents'':

.. code:: text

    alias whatEvents dialog - $+ $iif($dialog(whatEvents),v,m) whatEvents whatEvents
    dialog -l whatEvents {
      title "Events? What Events?"
      size -1 -1 136 112
      option dbu
      text "Event Type", 1, 8 8 73 8
      text "", 2, 82 8 49 8
      text "Event Item ID", 3, 8 18 73 8
      text "", 4, 82 18 49 8
      text "Event Item Caption/Value", 5, 8 28 73 8
      text "", 6, 82 28 49 7
      button "Click me", 7, 8 40 37 12
      edit "Type in me", 8, 48 40 66 13
      check "Check/Uncheck Me", 9, 8 64 58 10
      text "0", 10, 8 73 58 10
      text "Scroll Me", 11, 72 64 57 8, center
      scroll "", 12, 72 72 58 8, range 0 100 horizontal bottom
      button "&Close", 13, 93 90 37 16, ok
    }
    ON *:DIALOG:whatEvents:*:*: {
      did -ra $dname 2 $devent
      did -ra $dname 4 $did
      did -ra $dname 6 $iif($did == 0,NA,$iif($did($did),$v1,$iif($did($did).sel,$v1,$iif($did($did) == 0,0,NA))
      did -ra $dname 10 $did(9).state
    }

Once saved into a script file inside of the mIRC remotes, the above example can be executed by typing the following command:

.. code:: text

    /whatEvents

Almost all events are accounted for. The dialog properly tracks mouse movements, the ID of the elements being altered/used, and any other sorts of attainable event information.

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dname </identifiers/dname>`
    * :doc:`$devent </identifiers/devent>`
    * :doc:`$didwm </identifiers/didwm>`
    * :doc:`$didreg </identifiers/didreg>`
    * :doc:`$didtok </identifiers/didtok>`
    * :doc:`/dialog </commands/dialog>`
    * :doc:`/did </commands/did>`
    * :doc:`/didtok </commands/didtok>`

