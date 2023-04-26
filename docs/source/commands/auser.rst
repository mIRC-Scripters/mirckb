/auser
======

The **/auser** command adds or edits an entry in mIRC's user list (the user tab of the script editor).

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

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ulevel </identifiers/ulevel>`
    * :doc:`$ulist </identifiers/ulist>`
    * :doc:`/flush <flush>`
    * :doc:`/guser <guser>`
    * :doc:`/iuser <iuser>`
    * :doc:`/rlevel <rlevel>`
    * :doc:`/ruser <ruser>`
    * :doc:`/ulist <ulist>`