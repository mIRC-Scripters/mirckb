On Quit
=======

The ON QUIT event is triggered when a user quits/disconnects from the IRC network while on the same channel as the local mIRC client.

Synopsis
--------

.. code:: text

    ON <level>:QUIT:<commands>

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

When a user disconnects, stop mIRC's default message and, instead, echo to the active window a custom message:

.. code:: text

    ON ^*:QUIT: {
      echo -a * $nick just disconnected from $network
      haltdef
    }

.. code:: text

    Because ON QUIT is not associated with # or $chan, to show a quit message in all channels you share with that nick, you can use $comchan. You can simulate mIRC's default Quit message in channels with:
    
    on ^*:QUIT:{
      var %i $comchan($nick,0)
      while (%i) {
        echo -ctg quit $chan(%i) * $nick $+($chr(40),$address,$chr(41)) Quit $iif($1,$+($chr(40),$1-,$chr(41))) 
        dec %i
      }
      haltdef
    }

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on disconnect </events/on_disconnect>`
    * :doc:`on join </events/on_join>`
    * :doc:`on part </events/on_part>`

