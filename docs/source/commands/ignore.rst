/ignore
=======

The /ignore command ignores various types of messages from users, You can also manage ignore from the Control tab of the address book.

Synopsis
--------

.. code:: text

    /ignore [-lrpcntikdwxuNhysf] <on|off|nick/address> [type] [network]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -p
      - ignores the private messages (if you have a query window associated for that nick/address, it won't ignore the messages)
    * - -c
      - ignores the channel messages
    * - -n
      - ignores the notice messages
    * - -t
      - ignores the ctcp messages
    * - -i
      - ignore the invites requests
    * - -k
      - ignore the control codes from the messages (messages themselves are not ignored)
    * - -d
      - ignores the dcc requests
    * - -s
      - prevent user from triggering speech
    * - -h
      - prevent user from triggering highlight
    * - -y
      - prevent user from triggering tips
    * - -f
      - prevent user from triggering flash
    * - -a
      - ignores private, channel, notice, ctcp, dcc, invite, controls, speech, highlight, tips, flash 
    * - -l
      - lists all ignored addresses that matches the switches above if any is specified, otherwise lists all ignored addresses.
    * - -r
      - if an address/nick is specified, removes the nick/address, otherwise removes all ignored addresses.
    * - -w
      - makes the ignore apply to any network.
    * - -uN
      - specifies a delay (N) in seconds after which the ignore is automatically removed.
    * - -x
      - indicates that this address should be excluded from ignores, useful to temporarily stop ignoring an user or to allow a specific address not to be ignored after ignoring a wide range with an address.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <on|off|nick/address>
      - turns on/off the ignore feature, or if a nick/address is specified, applies the ignore that user.
    * - [type]
      - if specified, the address is looked up via the server, otherwise just ignore the nickname.
    * - [network]
      - if specified, applies the ignore on that network, otherwise applies the ignore on the current network

Example
-------

None

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ignore </identifiers/ignore>`

