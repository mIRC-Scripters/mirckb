On Deowner
==========

The ON DEOWNER event triggers whenever a user on a channel has been released of their owner (-q) status.

Synopsis
--------

.. code:: text

    ON <level>:DEOWNER:<#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <*><#>
      - The place, or places where the event listens, you can specify specific name of window, seperate them by comma.
        * \* - Any channel window
        * # - Any channel window
    * - <commands>
      - The commands to be performed when the event triggers

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$opnick </identifiers/opnick>`
      - Returns the nickname of the user being deowned.

Example
-------

Message the channel where the event occurs:

.. code:: text

    ON *:DEOWNER:#:msg # $nick $+ : You're not an owner of # anymore? :-o

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on deop </events/on_deop>`
    * :doc:`on devoice </events/on_devoice>`
    * :doc:`on help </events/on_help>`
    * :doc:`on op </events/on_op>`
    * :doc:`on owner </events/on_owner>`
    * :doc:`on voice </events/on_voice>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

