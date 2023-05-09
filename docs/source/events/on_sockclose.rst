On Sockclose
============

The ON SOCKCLOSE event triggers when a :ref:`tcp_sockets` connection is closed by the remote host.

Synopsis
--------

.. code:: text

    ON <level>:SOCKCLOSE:<name>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <matchtext>
      - The name of the target socket. Can be a :ref:`matching_tools-wildcard`.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Connection State
----------------

The reason a socket is closed could be because of an error, rather than because the remote host closed your connection on purpose, you should check :doc:`$sockerr </identifiers/sockerr>` for error, here is a list of the possible value for $sockerr inside the on sockclose event:

* 0 - EOF from the remote host received, this actually means the remote host closed your connection successfuly.
* 3 - An error occurred while receiving data, or a SSL error occurred (most likely SSL cert cypher incompatibility), $sock().wsmsg will contain a more specific error message.
* 5 - An SSL error of some kind occurred when trying to initialize the connection. Unlikely to happen. If you get this you most likely are trying to initiate an SSL socket connection without SSL capabilities (check {mIRC|$sslready}}, which is $false if you don't have them)

Example
-------

When the socket closes, echo that the socket has closed and some details about it to the active window:

.. code:: text

    ON *:SOCKCLOSE:*: {
      if (!$sockerr) echo -ag => $sockname Connection to $sock($sockname).ip on port $sock($sockname).port closed by the remote host!
      else echo -ag => An error occured with the socket $sock($sockname).wsmsg
    }

Compatibility
-------------

.. compatibility:: 6.14

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on sockopen </events/on_sockopen>`
    * :doc:`on sockread </events/on_sockread>`
    * :doc:`on sockwrite </events/on_sockwrite>`
    * :doc:`on socklisten </events/on_socklisten>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/socklist </commands/socklist>`
    * :doc:`/sockmark </commands/sockmark>`
    * :doc:`/sockopen </commands/sockopen>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockrename </commands/sockrename>`
    * :doc:`/sockudp </commands/sockudp>`
    * :doc:`/sockwrite </commands/sockwrite>`
    * :doc:`$sock </identifiers/sock>`

