On Voice
========

The ON VOICE event triggers whenever a user on a channel has been elevated to Voice channel - IRC|voice.

This event also fills the :doc:`$vnick </identifiers/vnick>` identifier with the nickname of the user who was added to Channel voice - IRC|Channel voice status. The :doc:`$nick </identifiers/nick>` identifier points to the user who added them.

Synopsis
--------

.. code:: text

    ON <level>:VOICE:<#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger..
    * - <matchtext>
      - The text to match in the event..
    * - <#[,#]>
      - The channel, or channels where the event listens.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Target
      - Description
    * - #
      - Any channel if left by itself, otherwise refers to a specific channel
    * - [,#]
      - List of specific channel names

Example
-------

Acknowledge when a user has had their user level elevated to voice:

.. code:: text

    ON *:VOICE:#:msg # $vnick now has a voice, thanks to $nick $+ .

Compatibility
-------------

.. compatibility:: 4.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on deop </events/on_deop>`
    * :doc:`on deowner </events/on_deowner>`
    * :doc:`on devoice </events/on_devoice>`
    * :doc:`on help </events/on_help>`
    * :doc:`on op </events/on_op>`
    * :doc:`on owner </events/on_owner>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

