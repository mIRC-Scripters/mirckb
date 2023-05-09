$cnick
======

$cnick returns the 'Nick or address' field from the Edit dialog of the Nth entry in the Nick Colors dialog, or if a nick/address is specified, returns the Nth position of the item in list that matches the nick. If the nick/address does not match any items, returns zero.

Synopsis
--------

.. code:: text

    $cnick(N/nick, M)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <N/nick>
      - a number representing the Nth item in the Nick Color dialog or a nickname/address used as a match against the field 'Nick or address' in Nick Color Edit dialog
    * - M
      - if you use the .color property and no item is found via a nick/address match, the 'Normal Text' color is returned, if M is 1, the 'Listbox text' is color is returned

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .color/.colour
      - return the color for that entry. if no item is found via a nick/address match, the 'Normal Text' color is returned, if the M parameter is 1, the 'Listbox text' is color is returned
    * - .modes
      - return the 'Channel modes' field
    * - .levels
      - return the 'User levels' field
    * - .method
      - return the 'Method' field
    * - .anymode
      - return the state of the 'Any mode' checkbox
    * - .nomode
      - return the state of the 'No mode' checkbox
    * - .ignore
      - return the state of the 'Ignore' checkbox
    * - .op
      - return the state of the 'Op' checkbox
    * - .voice
      - return the state of the 'Voice' checkbox
    * - .protect
      - return the state of the 'Protect' checkbox
    * - .notify
      - return the state of the 'notify' checkbox
    * - .idle
      - return the 'Idle time' field
    * - .auto
      - return the state of the 'Auto color' option (where you can use '*' as a color to enable the option)

Example
-------

.. code:: text

    //echo -a $cnick(1).color

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/cnick </commands/cnick>`

