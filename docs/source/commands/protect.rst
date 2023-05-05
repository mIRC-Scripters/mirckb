/protect
========

The **/protect** command can be used to manage the protect list, which allows you to protect nicknames (deop the user if the protected nickname is deopped, and kicked back if kicked)

Synopsis
--------

.. code:: text

    /protect [-rwal] <on|off|nick> [#channel1,#channel2,...] [type] [network]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Removes the entry from the list.
    * - -w
      - Makes the protect apply to all network.
    * - -a
      - add the entry (default)
    * - -l
      - list all of the protect entries.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <on|off|nick>
      - If you specify on/off, turns the feature on/off. Otherwise you must give a nickname.
    * - [#channel1,#channel2]
      - If specified, a list of channels you want to protect the nickname on, otherwise the protect apply on all channels.

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

    * :doc:`$protect </identifiers/protect>`
