/aop
====

Auto-OP is a feature that can be used to manage access for a channel. Whenever a user whose address matches an address in the auto-op list joins the channel, mIRC will automatically OP them.

The **AOP** command can also be used to disable or enable this feature as well as add and remove users from and to the list.

Synopsis
--------

.. code:: text

    /aop -rwal <nick/address> [#channel1,#channel2,...] [type] [network]
    /aop <on/off>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Indicates address/nick to should be removed, you can pass a channel name to remove only a channel name from the list of channel for that entry.
    * - -w
      - Auto-OP apply to any network
    * - -a
      - Add the entry (default)
    * - -l
      - list all of the auto-op entry

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <on/off>
      - Turns the auto-op feature on/off.
    * - <nick/address>
      - The nickname or address of the person to be added to the auto-op list. Both nickname and addresses are acceptable. Addresses can be :doc:`wildcard </intermediate/matching_tools.html#wildcard>` addresses.
    * - [#channel1,#channel2,...]
      - Channels to apply the auto-op to.
    * - [type]
      - Address type to be used.
    * - [network]
      - Optional network name to apply the auto-op to.

Example
-------

.. code:: text

    ;Turn on auto op
    /aop on

    ;Add Madgoat to the auto-op list. Address type 2, network Undernet
    /aop MadGoat 2 Undernet

    ;Remove Madgoat from the auto-op list
    /aop -r MadGoat 2 Undernet

    ;Turn off auto op
    /aop off

The above example will output:

.. code:: text

    * Auto-Op is on
    -
    * Added *!*@Example.com to auto-op list
    -
    * Removed *!*@Example.com from auto-op list
    -
    * Auto-Op is off

Compatibility
-------------

Added: mIRC v5.9 (15 Jun 2001)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$aop </identifiers/aop>`
    * :doc:`$avoice </identifiers/avoice>`
    * :doc:`$auto </identifiers/auto>`
    * :doc:`/avoice </commands/avoice>`
    * :doc:`/ignore </commands/ignore>`
    * :doc:`/pop </commands/pop>`
    * :doc:`/pvoice </commands/pvoice>`
