On Op
=====

The ON OP event triggers whenever a user on a channel has been elevated to a Channel operator - IRC|channel operator.

This event also fills the :doc:`$opnick </identifiers/opnick>` identifier with the nickname of the user who was added to Channel operator - IRC|Channel operator status. The :doc:`$nick </identifiers/nick>` identifier points to the user who added them.

Synopsis
--------

.. code:: text

    ON <level>:OP:<#[,#]>:<commands>

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

Acknowledge when a user has been elevated to a channel operator:

.. code:: text

    ON *:OP:#:msg # Congratulations, $opnick $+ ! $nick has made you a channel operator!

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on deop </events/on_deop>`
    * :doc:`on deowner </events/on_deowner>`
    * :doc:`on devoice </events/on_devoice>`
    * :doc:`on help </events/on_help>`
    * :doc:`on owner </events/on_owner>`
    * :doc:`on serverop </events/on_serverop>`
    * :doc:`on voice </events/on_voice>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

