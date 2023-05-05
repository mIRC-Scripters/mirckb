/dns
====

The **/dns** command resolves an address. If mIRC sees a "." in the name you specify it assumes it is an address and tries to resolve it. Otherwise it assumes it is a nickname and performs a :doc:`/userhost </commands/userhost>` to find the user's address and then resolves it. If you specify an IP address, it looks up the host name. You can queue multiple /dns requests, and you can view the current queue by using /dns with no parameters.

Synopsis
--------

.. code:: text

    /dns [-46ch] [nick|address]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -4
      - allows IPv4 results to be returned (enforce ipv4 for status window which are in ipv6 mode)
    * - -6

.. note:: that you can't connect to it, not so useful)

    * - -c
      - clears all currently queued DNS requests, except for the one currently in progress
    * - -h
      - forces /dns to treat the parameter as a hostname

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [nick|address]
      - the nick or address you want to look up

Example
-------

.. code:: text

    ;using default setting for ipv6
    /dns Ouims
    ;specifically allowing for ipv4 results
    /dns -4 Ouims
    ;specifically allowing for ipv6 results
    /dns -6 Ouims
    ;both
    /dns -46 Ouims
    ; beginning v7.58 returns all resolved IP addresses instead of only the 1st, such as for IRC network's round-robin name
    /dns chat.freenode.net

Compatibility
-------------

Added: mIRC v3.8 (25 Nov 1995)
See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dns </identifiers/dns>`
