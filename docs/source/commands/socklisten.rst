/socklisten
===========

The **/socklisten** command allows mIRC to listen for specific connections on a specified host port.

Synopsis
--------

.. code:: text

    /socklisten [-dpun] [bindip] <name> [port]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - d
      - Indicates that an IP address has been specified as the bind address.
    * - p
      - Enables UPnP support for the listening socket, if that is available.
    * - u
      - Enables dual stack socket to support both ipv4 and ipv6 for the listening socket, if that is available, you must bind to an ipv6 ip address
    * - n
      - Disable nagle algorithm for the socket, the :doc:`accepted </commands/sockaccept>` socket will have nagle disabled. You can disable nagle per accepted socket by using /sockaccept's -n switch

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name to give the new listening socket.
    * - [port]
      - The port number to listen on for this socket. If not specified, mIRC attempts to use a random port specified in the DCC port range options.

Example
-------

Open a listening socket named **mySocket** and listen on port **31781**:

.. code:: text

    /socklisten mySocket 31781

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See Also
--------

.. hlist::
    :columns: 4

    * :doc:`$sock </identifiers/$sock>`
    * :doc:`$sockname </identifiers/$sockname>`
    * :doc:`$sockerr </identifiers/$sockerr>`
    * :doc:`$sockbr </identifiers/$sockbr>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/sockclose </commands/sockclose>`
    * :doc:`/socklist </commands/socklist>`
    * :doc:`/sockmark </commands/sockmark>`
    * :doc:`/sockopen </commands/sockopen>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockrename </commands/sockrename>`
    * :doc:`/sockudp </commands/udp-socket>`
    * :doc:`/sockwrite </commands/sockwrite>`
