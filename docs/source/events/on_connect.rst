On Connect
==========

The ON CONNECT event triggers when mIRC has successfully connected to an IRC server and that IRC server has displayed its MOTD.

Synopsis
--------

.. code:: text

    ON <level>:CONNECT:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <commands>
      - The commands to be performed when the event triggers

Examples
--------

.. code:: text

    ; Echo the server and network
    ; names to the active window
    ON *:CONNECT:echo -a Server: $server -- Network: $network

If a successful connection is made to an IRC server, the above code will display something similar to the below example:

.. code:: text

    Server: chicago.il.us.undernet.org -- Network: UnderNet

.. code:: text

    ; Join a single channel,
    ; #myChannel, upon successful connection
    
    ON *:CONNECT:join #myChannel

When a successful connection is made to a server, mIRC will now join the channel #myChannel.

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on connectfail </events/on_connectfail>`
    * :doc:`on disconnect </events/on_disconnect>`
    * :doc:`$network </identifiers/network>`
    * :doc:`$server </identifiers/server>`

