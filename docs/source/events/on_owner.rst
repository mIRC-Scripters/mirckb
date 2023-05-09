On Owner
========

The ON OWNER event triggers whenever a user on a channel has been elevated to the level of channel owner. You can use :doc:`$opnick </identifiers/opnick>` to get the nickname being given owner status.

Synopsis
--------

.. code:: text

    ON <level>:OWNER:<#[,#]>:<commands>

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

Example
-------

Message the channel where the event occurs:

.. code:: text

    ON *:OWNER:#:msg # $opnick $+ : Congratulations on becoming an owner of # $+ !

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on deop </events/on_deop>`
    * :doc:`on deowner </events/on_deowner>`
    * :doc:`on devoice </events/on_devoice>`
    * :doc:`on help </events/on_help>`
    * :doc:`on op </events/on_op>`
    * :doc:`on voice </events/on_voice>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

