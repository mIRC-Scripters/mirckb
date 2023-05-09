On Ping
=======

The ON PING event is triggered when the server sends you a Ping - IRC|PING to see if you are still connected. The ON PING event does not trigger if mIRC's option is checked "Hide ping! pong! event"

Synopsis
--------

.. code:: text

    ON <level>:PING:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Halt mIRC's default display, and echo the ping message to the active window:

.. code:: text

    ON *:PING: {
      echo -a Server PING: $1-
      haltdef
    }

You can mimic mIRC's default display with:

.. code:: text

    ON ^*:PING:{ echo -ctgs info2 Ping? Pong! | haltdef }

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on pong </events/on_pong>`

