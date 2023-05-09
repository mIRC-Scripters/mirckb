On Disconnect
=============

The ON DISCONNECT event triggers when mIRC has disconnected from an IRC server.

Synopsis
--------

.. code:: text

    ON <level>:DISCONNECT:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access level </intermediate/events>` for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - $N
      - Returns the server disconnect message that is passed to mIRC.

Examples
--------

.. code:: text

    ; Echo network, and time
    ; when mIRC disconnected
    ON *:DISCONNECT:echo -a Disconnected from $network on $asctime(dddd mmmm $+(ddoo,$chr(44), yyyy)) at $asctime(hh:mmtt) $+ . Server disconnect reason: $1-

The following is an example of what will be displayed when mIRC has disconnected from a server:

.. code:: text

    Disconnected from DALnet on Tuesday June 24th, 2014 at 02:06pm.

The :doc:`$asctime </identifiers/asctime>` identifier has been used here in order to specifically format the current date and time.

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on connect </events/on_connect>`
    * :doc:`on connectfail </events/on_connectfail>`
    * :doc:`$network </identifiers/network>`
    * :doc:`$server </identifiers/server>`

