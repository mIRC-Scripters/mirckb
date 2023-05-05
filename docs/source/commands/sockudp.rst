/sockudp
========

The **/sockudp** command allows you to send data to a specific address at a specific port destination (See :doc:`uDP sockets </advanced/sockets.html#udp-socket>` ).

.. note:: if /sockudp fails, it sets :doc:`$sock().wserr </identifiers/sock>` to the error value, and trigger on sockwrite with :doc:`$sockerr </identifiers/sockerr>` set etc.

Synopsis
--------

.. code:: text

    /sockudp -bntkduz [bindip] <name> [port] <ipaddress> <port> [numbytes] [text|%var|&binvar]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -b
      - Indicates that you are specifying the numbytes value which is the number of bytes you want send, the full line is sent otherwise
    * - -n
      - Appens a :doc:`$crlf </identifiers/crlf>` to the line being sent if it's not a &binvar or if does not already end with a $crlf
    * - -t
      - Forces mIRC to send anything beginning with a & as plain text
    * - -k
      - Keeps the socket opened
    * - -d
      - Means you have specified the ip address as the bind address
    * - -u
      - Enables dual stack socket to support both ipv4 and ipv6 for the listening socket, if that is available, you must bind to an ipv6 ip address
    * - -z
      - Wait for the data to be sent if any and then close the socket

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [bindip]
      - If -d has been specified, the ip address you want to use as the bind address.
    * - <name>
      - The sockname name.
    * - [port]
      - If specified, the local port to use, otherwise mIRC choose one randomly.
    * - <ipaddress>
      - The ip address you want to send to information to, use you localhost 127.0.0.1 with -k to create a listening socket.
    * - <port>
      - The port you want to send to information to, that's your listening port if you create a server.
    * - [numbytes]
      - If -b has been specified, indicates the number of bytes you want to send.
    * - [text|%var|&binvar]
      - If specified, the message you want to send, can be a binary variable. You don't want to specify that parameter if you create a server.

Example
-------

.. code:: text

    alias gettime {
    ; Set a NULL byte binary variable.
    bset &null 1 0

    ; Open a UDP connection to Time-a.nist.gov = 129.6.15.28
    sockudp -k gettime 129.6.15.28 37 &null
    }

    ON *:UDPREAD:gettime: {
    ; Read the reply.
    sockread -f &time

    var %time $bvar(&time,1,$bvar(&time,0))

    ; Convert to binary, remove spaces.
    var %bin $regsubex(%time, /(\d+)\s?/g, $base(\1, 10, 2, 8))

    ; Get the current unix time in decimal system.
    var %time = $base(%bin, 2, 10)

    ; Print the time.
    echo -ag Currnt Time/Date: $asctime($calc(%time - 2208988800), yyyy-mm-dd hh:nn:ss TT)

    ; Close the socket
    sockclose $sockname
    }

Compatibility
-------------

Added: mIRC v5.5 (19 Feb 1999)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on udpread </events/udp-socket>`
    * :doc:`on sockwrite </events/on_sockwrite>`
    * :doc:`$sockerr </identifiers/sockerr_idEntifiers>`
