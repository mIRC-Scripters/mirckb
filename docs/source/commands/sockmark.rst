/sockmark
=========

The **/sockmark** command assigns temporary data to a socket to be referenced later using :doc: `$sock </identifiers/$sock>` (<name>).mark. Leaving the [temp data] parameter :doc: `$null </identifiers/$null>` will clear the socket mark. The sockmark command can be used to assign the same data to multiple sockets using a <wild_name> :doc: `wildcard </intermediate/matching_tools.html#wildcard>` pattern.

Limitations
-----------

The [temp data] is limited to (4,141 - [length of <sock_name>]) characters. I.e. with a socket named "x", you can store up to 4140 characters.

Synopsis
--------

.. code:: text

    /sockmark <name> [temp data]
    /sockmark <wild_name> [temp data]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The handle name of the socket
    * - <wild_name>
      - A :doc: `wildcard </intermediate/matching_tools.html#wildcard>` pattern to match
    * - [temp data]
      - The temporary socket's data

Example
-------

The example below is a demonstration of how you would use it. It does not actually function.

.. code:: text

    ; Non-functioning example, shows practical usage only
    on $*:text:/^!foo (\S+)$/Si:#:{
    ; if ( .. validate input .. ) {
    sockopen sock1 www.example.com 80
    sockmark sock1 $regml(1)
    }
    on *:sockopen:sock1:{
    ; submit the information we got from the user
    sockwrite -nt $sockname GET /foobar.php?q= $+ sock($sockname).mark HTTP/1.0
    sockwrite -nt $sockname Host: www.example.com
    sockwrite -nt $sockname $crlf
    }
    ; on *:sockread:sock1: {
    ; ....
    ; }

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$sock </identifiers/$sock>`
    * :doc: `$sockname </identifiers/$sockname>`
    * :doc: `$sockerr </identifiers/$sockerr>`
    * :doc: `$sockbr </identifiers/$sockbr>`
    * :doc: `/sockaccept </commands/sockaccept>`
    * :doc: `/sockclose </commands/sockclose>`
    * :doc: `/socklist </commands/socklist>`
    * :doc: `/socklisten </commands/socklisten>`
    * :doc: `/sockopen </commands/sockopen>`
    * :doc: `/sockpause </commands/sockpause>`
    * :doc: `/sockread </commands/sockread>`
    * :doc: `/sockrename </commands/sockrename>`
    * :doc: `/sockudp </commands/udp-socket>`
    * :doc: `/sockwrite </commands/sockwrite>`
