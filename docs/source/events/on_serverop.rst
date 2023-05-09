On Serverop
===========

The ON SERVEROP event triggers when a server ops a user on a channel.

This event also fills the :doc:`$opnick </identifiers/opnick>` identifier with the nickname of the user who was added to channel operator status. The :doc:`$nick </identifiers/nick>` identifier points to the server.

Synopsis
--------

.. code:: text

    ON <level>:SERVEROP:<#[,#]>:<commands>

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
      - The channel, or channels to listen on. Can be # to target all channels.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Acknowledge when a user has been elevated to channel operator by the server:

.. code:: text

    ON *:SERVEROP:#:msg # Congratulations, $opnick $+ ! The server, $nick $+ , just made you an operator!

Compatibility
-------------

.. compatibility:: 3.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on deop </events/on_deop>`
    * :doc:`on op </events/on_op>`

