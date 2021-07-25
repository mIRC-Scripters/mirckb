/ban
====

The **/ban** command is used to ban someone from a specific channel using their address. If no channel specified mIRC will use the active channel window. Using the -k switch mIRC will also kick the user with a kick message. mIRC uses the /userhost server command to find the user's address before applying a ban.

Synopsis
--------

.. code:: text

    /ban [-ruN] [#channel] <nickname|address> [type]
    /ban -k[ruN] [#channel] <nickname|address> [type] [kick message]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -k
      - Bans and kicks the user
    * - -r
      - Used to remove a banned address
    * - -uN
      - Unsets the ban in N amount of seconds

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [#channel]
      - A specific channel to apply the ban on.
    * - <nickname|address>
      - The nick or address to use for the ban.
    * - [type]
      - The address type to use for the ban.
    * - [kick message]
      - The optionnal kick message.

Example
--------

.. code:: text

    ;Ban Foo's address (type 2) in the active channel window 
    /ban Foo 2

    ;Ban/Kick Mike202 from the active channel with a kick message of "Owned!"
    ;Unset ban after 60 seconds
    /ban -ku60 Mike202 Owned!

    ;Ban/kick Dave3 from #FooBar with a kick message of "Cya!"
    ;ban type 2
    /ban -k #FooBar Dave3 2 Cya!

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$banmask </aliases/banmask>`
    * :doc:`$bnick </aliases/bnick>`
    * :doc:`$ibl </aliases/ibl>`
    * :doc:`$address </aliases/address>`
    * :doc:`$chan </aliases/chan>`
    * :doc:`$nick </aliases/nick>`