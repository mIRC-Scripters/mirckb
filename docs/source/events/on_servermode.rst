On Servermode
=============

The ON SERVERMODE event triggers when a server changes channel modes on a channel.

This event fills the :doc:`$chan </identifiers/chan>`, and $1- identifiers with details relative to this event.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - $chan
      - The channel where modes were changed.
    * - $1
      - The new channel modes.

Synopsis
--------

.. code:: text

    ON <level>:SERVERMODE:<#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <#[,#]>
      - The channel, or channels, to match the event listener. Can also be a :ref:`matching_tools-wildcard`.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Target
      - Description
    * - #
      - Channel where the event took place
    * - [,#]
      - Specific channel names

Example
-------

Notice the channel when the server changes channel modes, and the local mIRC client is a channel operator:

.. code:: text

    ON @*:SERVERMODE:#:notice # $nick has modified the channel modes to: $1-

It is important to note that sending a channel notice to everyone at once is generally frowned upon unless one is an operator on the channel, or a bot has been instructed to do so.

Compatibility
-------------

.. compatibility:: 3.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on mode </events/on_mode>`
    * :doc:`access levels </intermediate/events>`
    * :doc:`/mode </commands/mode>`

