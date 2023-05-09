On Devoice
==========

The ON DEVOICE event triggers whenever a user on a channel has had their voice privileges (mode -v) removed.

Synopsis
--------

.. code:: text

    ON <level>:DEVOICE:<#[,#]>:<commands>

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
    * - :doc:`$vnick </identifiers/vnick>`
      - Returns the nickname of the user being devoiced.

Example
-------

Acknowledge when a user has had their voice user level removed:

.. code:: text

    ON *:DEVOICE:#:msg # Uh oh, looks like $vnick no longer has a voice, thanks to $nick $+ .

Compatibility
-------------

.. compatibility:: 4.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on deop </events/on_deop>`
    * :doc:`on deowner </events/on_deowner>`
    * :doc:`on help </events/on_help>`
    * :doc:`on op </events/on_op>`
    * :doc:`on owner </events/on_owner>`
    * :doc:`on voice </events/on_voice>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

