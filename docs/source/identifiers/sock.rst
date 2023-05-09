$sock
=====

$sock returns information about currently opened sockets.

Synopsis
--------

.. code:: text

    $sock(name,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The name of the socket, you can use a :ref:`matching_tools-wildcard` expression and use the N parameter to get the Nth socket
    * - N
      - The Nth matching socket, to be used with a :ref:`matching_tools-wildcard` expression, default to 1

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .name
      - returns the name you give to a connection to identify it
    * - .addr
      - returns the original named address if one was used.
    * - .sent
      - returns the number of bytes sent over that connection so far
    * - .rcvd
      - returns the number of bytes received over that connection so far
    * - .ip
      - returns the IP Address the socket is connected to.
    * - .port
      - returns the Port the socket is connected to.
    * - .sq
      - returns the number of bytes queued in the send buffer
    * - .rq
      - returns the number of bytes queued in the receive buffer
    * - .ls
      - returns the number of seconds since the connection last sent data
    * - .lr
      - returns the number of seconds since the connection last received data
    * - .mark
      - returns the data marked from :doc:`/sockmark </commands/sockmark>` (data storage tied to the socket, 512 bytes max)
    * - .type
      - returns the socket type, TCP or UDP
    * - .saddr
      - returns the source address of the last received UDP packet
    * - .sport
      - return the source port of the last received UDP packet
    * - .to
      - returns the number of seconds the socket has been open
    * - .wserr
      - returns the last winsock error number that occurred on a socket
    * - .wsmsg
      - returns the last winsock error message corresponding to the .wserr error number above
    * - .ssl
      - returns $true for an SSL connection
    * - .pause
      - returns $true if a socket has been paused
    * - .starttls
      - returns $true for a STARTTLS connection
    * - .bindip
      - returns the ip address or adapter name used when binding IP
    * - .bindport
      - returns the port name used when binding IP
    * - .status
      - returns the status of the socket "listening", "active", "connecting", or "inactive"
    * - .upnp
      - return $true or $false depending on if upnp was used on the socket

Example
-------

.. code:: text

    //echo -a $sock(*,1)

Compatibility
-------------

.. compatibility:: 5.3

see also
--------

.. hlist::
    :columns: 4

    * :doc:`/sockopen </commands/sockopen>`
    * :doc:`/sockwrite </commands/sockwrite>`
    * :doc:`$sockerr </identifiers/sockerr>`
    * :doc:`$sockbr </identifiers/sockbr>`

