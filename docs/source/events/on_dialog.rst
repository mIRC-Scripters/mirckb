On Dialog
=========

The ON DIALOG event listens for events which take place inside of custom Dialogs - mIRC|dialog windows.

Synopsis
--------

.. code:: text

    ON <level>:DIALOG:<name>:<event>:<id>:{}

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <name>
      - The dialog name that this event triggers for, :ref:`matching_tools-wildcard` accepted.
    * - <event>
      - The dialog event that this event triggers for, :ref:`matching_tools-wildcard` accepted.
    * - <id>
      - The id name of the dialog item to listen for, :ref:`matching_tools-wildcard` accepted. Multiple IDs can be specified in the form: 1,2,3,4-8,9

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$dname </identifiers/dname>`
      - Returns the name of the dialog.
    * - :doc:`$devent </identifiers/devent>`
      - Returns the name of the event.
    * - :doc:`$did </identifiers/did>`
      - Returns the ID of the control.

Events
------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Event
      - Description
    * - active
      - Triggers when the dialog is made active.
    * - close
      - Triggered when a dialog has been closed.
    * - dclick
      - Occurs when a double left-click has occurred in a list box or combo box, as well as on the dialog itself.
    * - drop
      - Triggers when an item has been dragged and dropped with the mouse.
    * - edit
      - When text in an editbox or a combo box has changed.
    * - init
      - This event ID is 0, and triggers before a dialog is displayed. This allows initialization time for the dialog and its items.
    * - menu
      - Whenever a menu-item is selected.
    * - mouse
      - When the mouse is moved.
    * - rclick
      - Works when the mouse right-clicks.
    * - sclick
      - Occurs during a single-click in a list box/combo box, during check/uncheck of radio/check buttons, or during the click of a button.
    * - scroll
      - A scroller control position has changed.
    * - uclick
      - Left mouse button has been released/gone up.

Examples
--------

Here we will create an alias that launches a dialog. This dialog has a mouse event listener that will track mouse movements in the dialog, and write them to specific dialog components:

.. code:: text

    ; To use this example, simply type: /mouseListener
    alias mouseListener dialog - $+ $iif($dialog(mouseListener),v,m) mouseListener mouseListener
    dialog -l mouseListener {
      title "Mouse Listener"
      size -1 -1 184 120
      option dbu
      text "Move Your Mouse In Here!", 1, 56 32 73 8
      text "X", 2, 56 48 5 8
      text "0", 3, 64 48 25 8
      text "Y", 4, 95 48 5 8
      text "0", 5, 103 48 25 8
      button "&Close", 6, 139 99 37 16, ok
    }
    ON *:DIALOG:mouseListener:mouse:*: {
      did -ra $dname 3 $mouse.x
      did -ra $dname 5 $mouse.y
    }

In the example above, we have created an alias, mouseListener, to handle a local dialog, which cannot be seen outside of the scope of whatever script file it is saved to. This will help make sure no other dialogs collide with this dialog and its events.

This example can be triggered by typing the following command:

.. code:: text

    /mouseListener

Once the demo has begun, the mouse event will now listen. When the mouse begins moving around inside of the dialog, the X and Y positions of the mouse are represented inside of the ''text'' components of ID 3, and 5, respectively.

Clicking the ''Close'' button will close the dialog and halt event listening.

Below is another, more thorough example. This example will monitor what events are triggering, what event ID is triggering the event, and any current captions or titles of the event ID which triggered an event. Created a custom alias called whatEvents which will open up the dialog whatEvents:

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
    * :doc:`$did </identifiers/did>`
    * :doc:`$didwm </identifiers/didwm>`
    * :doc:`$didreg </identifiers/didreg>`
    * :doc:`$didtok </identifiers/didtok>`
    * :doc:`/dialog </commands/dialog>`
    * :doc:`/did </commands/did>`
    * :doc:`/didtok </commands/didtok>`

