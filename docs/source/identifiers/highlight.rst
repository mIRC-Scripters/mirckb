$highlight
==========

The $highlight identifier, if used without parameters, returns a $true/$false value depending on if you have the highlight features enabled in mIRC, otherwise returns informations about the highlight entries.

Synopsis
--------

.. code:: text

    $highlight - return $true/$false depending on if highlighting is turned on in the highlight mIRC dialog

.. code:: text

    $highlight(N/text) - return the Nth line in the highlight mIRC dialog's list, or return the value of the corresponding entry in mIRC's highlight dialog list, if any, for that string

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - if N is passed, return the Nth line in the highlight mIRC dialog's list
    * - text
      - if non-number parameter is passed, return the value of the corresponding entry in mIRC's highlight dialog list in option for that string.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .text
      - returns the matching text of the entry
    * - .color
      - returns the color of the line being highligted
    * - .sound
      - returns the sound associated with the highlight if any ("beep" or a filename)
    * - .flash
      - returns 0 if flash is not set, otherwise it returns the corresponding number of repeat time
    * - .message
      - returns $true/$false depending on if the highlight is set for messages
    * - .nicks
      - returns $true/$false depending on if the highlight is set for nicks
    * - .regex
      - returns $true/$false depending on if the text should be compared using a regular expression
    * - .cs
      - returns $true/$false depending on if the text should be compared using case sensitivity
    * - .chans
      - returns the list of channels and nicknames required to trigger an highlight for that entry, if any.

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.11

See also
--------

.. hlist::
    :columns: 4

