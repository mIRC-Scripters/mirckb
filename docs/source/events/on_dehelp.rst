On Dehelp
=========

The ON DEHELP event triggers whenever a user on a channel has had their helper status (mode -h) removed in a channel.

Synopsis
--------

.. code:: text

    ON <level>:DEHELP:<#[,#]>:<commands>

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
    * - :doc:`$hnick </identifiers/hnick>`
      - Returns the nickname of the user being dehelped.

Example
-------

Acknowledge when any user has been dehelped on all channels

.. code:: text

    ON *:DEHELP:#:msg # Sorry to see the helper privilege removed from $hnick $+ .

Compatibility
-------------

.. compatibility:: 5.4

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
    * :doc:`on voice </events/on_voice>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

