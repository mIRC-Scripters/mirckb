/ruser
======

The **/ruser** command allows you to remove the levels of an user from the users list

Synopsis
--------

.. code:: text

    /ruser [levels] <nick | address> [type]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [levels]
      - if not specified, the user is removed from the users list, otherwise the specified levels are removed, if all levels are removed, the user is also removed from the users list.
    * - <nick | address>
      - the nick or address you want to remove the level from. You can end a nickname with a '!' and all users with an address beginning with it are removed.
    * - [type]
      - If specified, the user address is looked up with /userhost and the levels of any user in the users list matching this address are removed

Example
-------

None

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/auser </commands/auser>`
    * :doc:`/guser </commands/guser>`
    * :doc:`/iuser </commands/iuser>`
    * :doc:`/rlevel </commands/rlevel>`
    * :doc:`/ulist </commands/ulist>`
