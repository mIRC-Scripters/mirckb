On Help
=======

The ON HELP event triggers whenever a user on a channel has been elevated to helper/halfop (mode +h) status in a channel.

Synopsis
--------

.. code:: text

    ON <level>:HELP:<#[,#]>:<commands>

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

    * - Parameter
      - Description
    * - :doc:`$hnick </identifiers/hnick>`
      - Returns the nickname of the user being helped.

Example
-------

Acknowledge when a user has been elevated to helper:

.. code:: text

    ON *:HELP:#:msg # Congratulations, $hnick $+ ! You are now a helper thanks to $nick $+ .

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
    * :doc:`on op </events/on_op>`
    * :doc:`on owner </events/on_owner>`
    * :doc:`on voice </events/on_voice>`
    * :doc:`/mode </commands/mode>`
    * :doc:`$mode </identifiers/mode>`

