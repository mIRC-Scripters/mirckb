On Pong
=======

The ON PONG event is triggered when the server replies with a PONG after the local mIRC client sent a Ping - IRC|PING response.

Synopsis
--------

.. code:: text

    ON <level>:PONG:<commands>

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

Halt mIRC's default display, and echo the pong message to the active window:

.. code:: text

    ON *:PONG: {
      echo -a Server PONG: $1-
      haltdef
    }

.. code:: text

    You can Trigger the ON PONG event with:
    //raw ping $ctime X
    
    If X is $null or $server, the displayed reply will be:
    * PONG from YourServerName: sent_ctime_value
    
    When the ON PONG event sees the reply, it can use $calc($ctime - $2) to find the number of seconds between PINGing the server and receiving the reply. If X is a valid Server Name different than the $server you are connected to, the reply substitutes your nick in place of the ctime value. A replacement of mIRC's display is:
    
    on ^*:PONG:{ echo -ctgs info * PONG from $1 $+ : $2 | haltdef }

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on ping </events/on_ping>`

