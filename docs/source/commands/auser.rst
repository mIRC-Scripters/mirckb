/auser
======

The **/auser** command Add or edit an entry in mIRC's User List (the User tab of the Script Editor).

Synopsis
--------

.. code:: text

    /auser -a <levels> <nick|address> [info]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - If <nick|address> match an entry in the list, <levels> are added to that entry

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <levels>
      - Access level to be assigned to the nick/address.
    * - <nick|address>
      - The exact nick or address to be used.
    * - [info]
      - Can be used to add additional information about that entry.

Example
-------

.. code:: text

    ;Add an address; Info can be retrieved using $ulist(*!*@Example.com).info
    ;5:*!*@Example.com Cool people
    /auser 5 *!*@Example.com Cool people

    ;Add another level for the same address
    ;10,=5:*!*@Example.com Cool people
    /auser -a 10 *!*@Example.com

    ;Remove Address
    /ruser *!*@Example.com

The above example will output:

.. code:: text

    * Added *!*@Example.com to user list
    * Added level(s) to user *!*@Example.com
    * Removed *!*@Example.com from user list

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$ulevel </identifiers/$ulevel>`
    * :doc: `$ulist </identifiers/$ulist>`
    * :doc: `/flush </commands/flush>`
    * :doc: `/guser </commands/guser>`
    * :doc: `/iuser </commands/iuser>`
    * :doc: `/rlevel </commands/rlevel>`
    * :doc: `/ruser </commands/ruser>`
    * :doc: `/ulist </commands/ulist>`
