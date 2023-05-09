On Connectfail
==============

The ON CONNECTFAIL event triggers when mIRC fails to connect to an IRC server. This event will also trigger during reconnect attempt disconnections. The $1- identifier is filled with any server disconnect message that is passed to mIRC.

Synopsis
--------

.. code:: text

    ON <level>:CONNECTFAIL:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <commands>
      - The commands to be performed when the event triggers

Examples
--------

.. code:: text

    ; Stop mIRC from reconnecting
    ; after a connection failure.
    ON *:CONNECTFAIL:echo -s connection to $servertarget failed: $1- | disconnect

Compatibility
-------------

.. compatibility:: 6.02

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on connect </events/on_connect>`
    * :doc:`on disconnect </events/on_disconnect>`
    * :doc:`$network </identifiers/network>`
    * :doc:`$server </identifiers/server>`
    * :doc:`$servertarget </identifiers/servertarget>`

