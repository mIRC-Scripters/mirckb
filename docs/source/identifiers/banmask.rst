$banmask
========

$banmask returns the current user ban through either an :doc:`on ban </events/on_ban>`, or an :doc:`on unban </events/on_unban>`. Most of the time, a banmask returns a :ref:`matching_tools-wildcard` address, generally resembling ''*user*@host.net''.

Synopsis
--------

.. code:: text

    $banmask

Parameters
----------

None

Example
-------

Message any channel where a ban has occurred, acknowledging the address the ban was placed on

.. code:: text

    ON *:BAN:#: {
      msg # Uh, oh! Looks like the address $banmask has just been banned.
    }

Message any channel where an unban has occurred, and report the address that was removed

.. code:: text

    ON *:UNBAN:#: {
      msg # Oh, look! $banmask was just removed from the channel banlist.
    }

Compatibility
-------------

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$bnick </identifiers/bnick>`
    * :doc:`$ibl </identifiers/ibl>`
    * :doc:`/ban </commands/ban>`
    * :doc:`on ban </events/on_ban>`
    * :doc:`on unban </events/on_unban>`

