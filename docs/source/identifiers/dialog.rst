$dialog
=======

The $dialog() identifier can be used in one of two ways:

# To create a modal dialog
# To be used as an identifier in order to get properties for a specific dialog window.

Modal vs Modeless
-----------------

mIRC has the ability to create a special kind of dialog, known as a modal dialog. Modal dialogs can be called from within a script using the $dialog() identifier. These dialogs are special in that they stop a script from continuing until one of the following conditions are met:

# The dialog is closed
# The dialog returns a value

Modal dialogs are different from modeless dialogs for a variety of reasons, but the most important ones are:

# They don't allow users to do anything else in mIRC until their conditions are met.
# They return information via the $dialog() identifier inside the script.
# They are generally only used when immediate action is necessary.

Modal dialogs should never be used unless absolutely necessary; they are mainly for critical user input. While modeless dialogs can be executed and navigated away from, or even minimized, it should be noted that modal dialogs do not have these abilities.

Creating A Modal Dialog
-----------------------

We can take a quick look at how to create a modal dialog via the following piece of code:

.. code:: text

    %modalvar = $dialog(name,table[,parent])

Here we can break down what we are looking at:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Name
      - The name you will give to the dialog and use to refer to it later.
    * - Table
      - The table name used to create the dialog
    * - Parent
      - The parent window of the dialog, this can be a window name or one of the following as documented in the next table.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Parent window description
    * - -1
      - Desktop window
    * - -2
      - Main mIRC window
    * - -3
      - Currently active window
    * - -4
      - Currently active dialog (Note: If there is no dialog open, this defaults to -3)

.. note:: ''This type of dialog cannot be called from a remote script event.''

Use As An Identifier
--------------------

$dialog(), in use as an identifier, can be used to get information regarding any dialog you specify, and its properties. To get the properties of a dialog you specify, you simply append a period after $dialog() and the property name, such as $dialog(mydialog).title to get the title of the dialog named mydialog. Don't worry, this is all explained further below.

Synopsis
^^^^^^^^

.. code:: text

    $dialog(<name/N>)[.property]

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Name
      - The name of the dialog you want to reference.
    * - N
      - If you want to reference a dialog by it's ID number, you would specify the ID number here. If you specify 0, mIRC will return the number of currently open dialogs.
    * - Property
      - Here is where you would specify the property that you want to retrieve about a specific dialog.

List of Properties
^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 30 55
    :header-rows: 1

    * - Property
      - Example
      - Description
    * - x,y,w,h
      - $dialog(mydialog).x
      - Can be used to return the x/y-position of a dialog, or the width/height.
    * - cw,ch
      - $dialog(mydialog).cw
      - Returns the width and height of the client area within the dialog.
    * - title
      - $dialog(mydialog).title
      - Returns the title of the dialog that you reference.
    * - modal
      - $dialog(mydialog).modal
      - If the dialog is a modal dialog, returns $true, otherwise returns $false.
    * - table
      - $dialog(mydialog).table
      - Returns the dialog table that the dialog name you reference is using.
    * - ok
      - $dialog(mydialog).ok
      - If you specify an 'OK' button, this will allow the identifier to specify the dialog ID number of that button.
    * - cancel
      - $dialog(mydialog).cancel
      - Same as above, but specifies the cancel button ID.
    * - result
      - $dialog(mydialog).result
      - Same as above, but specifies the result button ID.
    * - focus
      - $dialog(mydialog).focus
      - Allows you to retrieve the ID of the object control, within the dialog, that currently has focus.
    * - tab
      - $dialog(mydialog).tab
      - Returns the ID of the tab that is currently being displayed.
    * - active
      - $dialog(mydialog).active
      - If the dialog is the active window, returns $true, otherwise returns $false.
    * - hwnd
      - $dialog(mydialog).hwnd
      - Returns the window handle of the current dialog window.

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

