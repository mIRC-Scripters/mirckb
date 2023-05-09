On Deop
=======

The ON DEOP event triggers whenever a user on a channel has had their op privileges (mode -o) removed.

Synopsis
--------

.. code:: text

    ON <level>:DEOP:<#[,#]>:<commands>

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
      - Returns the nickname of the user being deopped.

Example
-------

Let the channel know when a user's operator privilege has been removed:

.. code:: text

    ON *:DEOP:#:msg # Oh no, $opnick has had their operator privilege removed :(

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on deowner </events/on_deowner>`
    * :doc:`on devoice </events/on_devoice>`
    * :doc:`on help </events/on_help>`
    * :doc:`on op </events/on_op>`
    * :doc:`on owner </events/on_owner>`
    * :doc:`on voice </events/on_voice>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

