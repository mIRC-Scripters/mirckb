On Kick
=======

The ON KICK event is triggered when the local mIRC client, or remote users, are kicked from a channel.

This event fills the :doc:`$chan </identifiers/chan>`, :doc:`$knick </identifiers/knick>`, and :doc:`$nick </identifiers/nick>` identifiers.

Synopsis
--------

.. code:: text

    ON <level>:KICK:<#[,#]>:<commands>

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
      - The channel, or channels, for the event to listen for. Can also be a :ref:`matching_tools-wildcard`.
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

Identifiers
-----------

This event fills the following identifiers:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - $chan
      - Channel where the event took place
    * - $knick
      - The kicked user's name
    * - $nick
      - The name of the person who kicked the user

Examples
--------

If local mIRC client is kicked, automatically rejoin the channel:

.. code:: text

    ON ME:*:KICK:#:join #

Send a notice to a kicked user with information about the kick:

.. code:: text

    ON *:KICK:#: {
      .notice $knick You were kicked from $chan by $nick for the following reason: $iif($1-,$1-,No reason given)
    }

The following is an example of the above code:

.. code:: text

    You were kicked from #BreakingBad by WalterWhite for the following reason: Stop mass-highlighting!

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on ban </events/on_ban>`
    * :doc:`on join </events/on_join>`
    * :doc:`on part </events/on_part>`
    * :doc:`on unban </events/on_unban>`
    * :doc:`$chan </identifiers/chan>`
    * :doc:`$knick </identifiers/knick>`
    * :doc:`$nick </identifiers/nick>`

