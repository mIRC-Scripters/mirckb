/cnick
======

The **/cnick** command allows you to modify items from the address book's nick color list.

Synopsis
--------

.. code:: text

    /cnick -rfaniovpylNmNsN [nick[!user@host]] [color] [modes] [levels]

    /cnick <on/off> 

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Removes the specified nick or address
    * - -f
      - Forces mIRC to add another item instead of replacing an existing one
    * - -a
      - Sets the Any Mode option
    * - -n
      - Sets the No Mode option
    * - -i
      - Sets the ignore option
    * - -o
      - Sets the op option
    * - -v
      - Sets the voice option
    * - -p
      - Sets the protect option
    * - -y
      - Sets the notify list option
    * - -lN
      - Sets the idle time
    * - -mN
      - Sets the highlight method (0-2) 
    * - -sN
      - Sorts the item into the Nth position in the list

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [nick[!user@host]]
      - Nickname or the host mask to be added
    * - [color]
      - The color to assign the nick/host
    * - [modes]
      - List of modes that is required for the nick/host (Ed. ~&@%+)
    * - [levels]
      - Access level form the user list
    * - <on/off>
      - turns nick colors on or off

Example
-------

.. code:: text

    ;Turn nick color on
    /cnick on

    ;Add color 5 for all Operators
    /cnick * 5 @

    ;Add color 3 for all half-op
    /cnick * 3 %

Compatibility
-------------

Added: mIRC v6.1 (29 Aug 2003)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.


See also
--------

.. hlist::
    :columns: 4

    * :doc:`$abook </identifiers/abook>`
    * :doc:`$cnick </identifiers/cnick>`
    * :doc:`$nick </identifiers/nick>`
    * :doc:`/abook <abook>`