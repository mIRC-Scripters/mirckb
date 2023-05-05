/scid
=====

The **/scid** command can change the connection associated with the current script. When a command is not specified, mIRC changes the connection of the current script to the connection associated with the given Connecion ID. The rest of the code will continue to execute on that connection. When a command is specified, mIRC will execute the command on the connection specified by the Connection ID or the connections based on the switches provided. Any active connection changes are restored upon returning to the calling routine. A command can be executed on all or some of the connections depending on their types using the -a or -at<Type> switches.

Connection Type
---------------

* 1 = Connected
* 2 = Disconnected or Connecting
* 3 = 1+2 = Connected, Disconnected, or Connecting (Same as -a)
* 4 = Connecting
* 5 = 1+4 = Connected or Connecting
* 6 = 2+4 = 2 = Disconnected or Connecting
* 7 = 3+4 = Disconnected or Connected or Connecting
* 8 = Disconnected

Synopsis
--------

.. code:: text

    /scid -rats<type> [Connection ID] [command]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Resets the connection back to what it original was.
    * - -s
      - Prints the current connection ID or the new connection ID.
    * - -a
      - Perform on all connections.
    * - -t<type>
      - Perform on all the connections of a specific type, can only be used with -a.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <ID>
      - The connection ID.
    * - <type>
      - The connection type, used with the -t switch.

Example
-------

A simple example of using /scid to send a command to all connected connections.

.. code:: text

    /*
    ** Global amsg - performs an amsg on all the
    ** the actives connections you are on.
    **
    ** /gamsg <message>
    */
    alias gamsg {
    if (!$1) {
    echo -gtcse info * /gamsg: insufficient parameters
    halt
    }
    ; all active connections
    ; if you don't use $unsafe, $1- is evaluated twice, watch out!
    scid -at1 amsg $unsafe($1-)
    }

Print all the channels you are on from every connection you have:

.. code:: text

    alias listChans {
    var %x = 1
    while ($scid(%x)) {
    ; switch connection
    scid %x

    ; iterate over the channels
    var %c = 1, %chans
    while ($chan(%c)) {
    var %chans = $addtok(%chans, $chr(32) $v1, 44)
    inc %c
    }

    ; print channels
    ; again, safer to use $unsafe
    scon -r echo -s $unsafe(Network: $network Channels: %chans)

    ; next connection
    inc %x
    }
    }

Compatibility
-------------

Added: mIRC v6.0 (16 Aug 2002)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$status </identifiers/status>`
    * :doc:`$network </identifiers/network>`
    * :doc:`$scon </identifiers/scon>`
    * :doc:`$scid </identifiers/scid>`
    * :doc:`/scon </commands/scon>`
