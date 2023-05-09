$editbox
========

The $editbox identifier is used to get the contents of editboxes in any mIRC window that contains an editbox.

Synopsis
--------

.. code:: text

    $editbox(window[,N])[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - window
      - The target window to get the editbox contents from
    * - N
      - Retrieves the data from the second editbox in a window (Note: Can only be the value of 1)

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - selstart
      - Returns the character location in the string of the start of a highlight selection
    * - selend
      - Returns the character location where the highlighted text ends

Example
-------

Echo the contents of the status window:

.. code:: text

    //echo -a $editbox(Status Window)

Echo the start and end locations of selected text in the status window editbox:

.. code:: text

    //echo -a Selection start: $editbox(Status Window).selstart --- Selection end: $editbox(Status Window).selend

.. note:: If no highlighted selection exists, both selstart and selend will return the location of the cursor in the text.

Compatibility
-------------

.. compatibility:: 6.2

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/editbox </commands/editbox>`

