/auto
=====

Auto-OP is a feature that can be used to manage access for a channel. Whenever a user whose address matches an address in the auto-op list joins the channel, mIRC will automatically OP them.

The **auto** command can also be used to disable or enable this feature as well as add and remove users from and to the list.

**This** commands been superseded by the :doc: `/aop </commands/aop>` command.'''

Synopsis
--------

.. code:: text

    /auto -rw <nick/address> [#channel1,#channel2,...] [type] [network]
    /auto <on/off>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Indicates address/nick to should be removed
    * - -w
      - Auto-OP apply to any network

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
      - The nickname or address of the person to be added to the auto-op list. Both nickname and addresses are acceptable. Addresses can be :doc: `wildcard </intermediate/matching_tools.html#wildcard>` addresses.
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
    /auto on

    ;Add Madgoat to the auto-op list. Address type 2, network Undernet
    /auto MadGoat 2 Undernet

    ;Remove Madgoat from the auto-op list
    /auto -r MadGoat 2 Undernet

    ;Turn off auto op
    /auto off

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

Added: mIRC v2.5a (08 Mar 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$aop </identifiers/$aop>`
    * :doc: `$avoice </identifiers/$avoice>`
    * :doc: `$auto </identifiers/$auto>`
    * :doc: `/aop </commands/aop>`
    * :doc: `/avoice </commands/avoice>`
    * :doc: `/ignore </commands/ignore>`
    * :doc: `/pop </commands/pop>`
    * :doc: `/pvoice </commands/pvoice>`
