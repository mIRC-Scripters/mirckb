On Socklisten
=============

The ON SOCKLISTEN event triggers when a connection is made on a listening :ref:`tcp_sockets` created with :doc:`$socklisten </commands/socklisten>`

Synopsis
--------

.. code:: text

    ON <level>:SOCKLISTEN:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <matchtext>
      - The name of the socket you want event to trigger on.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Accepting a connection
----------------------

.. note:: By design, you cannot prevent a socket from being accepted, as in, Windows accepts the connection even before mIRC.

You can use /sockaccept <newsocket> to accept a socket, mIRC create the new socket.

.. note:: If a new connection occurs on a listening socket but there is no on socklisten event matching that socket, the connection is rejected.

You should be checking for $sockerr before accepting the connection to see if an error occured, here is a list of the possible value for $sockerr in the on SOCKLISTEN event:

* 0 - New socket successfuly accepted.
* 1 - Error occurred on listening socket, $sock().wsmsg will contain a more specific error message. Note that getting this error is considered rare.
* 2 - Error accepting new socket, $sock().wsmsg will contain a more specific error message.
* 4 - Not enough memory for new socket. Note that getting this error is considered rare.

Examples
--------

.. code:: text

    on *:socklisten:name:{
      if (!$sockerr) sockaccept myprefix $+ $ticks
      else {
        echo -s An error occured while trying to accept a connection: $sock($sockname).wsmsg
      }
    }

Compatibility
-------------

.. compatibility:: 3.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on sockopen </events/on_sockopen>`
    * :doc:`on sockread </events/on_sockread>`
    * :doc:`on sockwrite </events/on_sockwrite>`
    * :doc:`on sockclose </events/on_sockclose>`
    * :doc:`/sockwrite </commands/sockwrite>`
    * :doc:`/sockclose </commands/sockclose>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockbr </identifiers/sockbr>`
    * :doc:`$sockerr </identifiers/sockerr>`
