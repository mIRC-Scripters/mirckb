/sockopen
=========

The **/sockopen** command initiates a connection to the specified addresses and port; a named address can be substituted for an IP address (which will get resolved to an IP address eventually). On success, the on sockopen event should get executed.

Synopsis
--------

.. code:: text

    /sockopen [-de[swap]tn46] [bindip] <name> <address> <port>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -d
      - the specified IP address is the bind IP address
    * - -e
      - creates an SSL connection, with this switch you can also use:

** **-s** - skip invalid certificates

** **-w** - display warning dialog

** **-a** - accept invalid certificates

** **-p** - prevent certificate caching

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -t
      - initiates an SSL negotiation on a non-SSL connection (STARTTLS feature), this is not meant to be used when creating the socket but later after the connection has been established, trigger on sockopen a second time with $sock().starttls set to $true
    * - -4
      - specify the IPv4 context when resolving address (enforce ipv4 when it is disabled entirely because your status window is in 'ipv6 mode'
    * - -6
      - specify the IPv6 context when resolving address (enforce ipv6)
    * - -n
      - disable Nagle algorithm on socket

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [bindip]
      - bind ip to be used
    * - <name>
      - socket name (for future reference)
    * - <address>
      - ip address or server name of the end point
    * - <port>
      - port of the end point

Example
-------

.. code:: text

    Alias irc_connect {
    ;Initiate a connection with "irc.freenode.org" on port 6669, Secured connection
    sockopen -e IRC irc.freenode.org +6697
    }

    On *:sockopen:IRC:{
    ;Send our USER and NICK irc commands
    sockwrite -n IRC USER Tester $+ $rand(1,100) Test Test:mSL Testing $+ $crlf
    sockwrite -n IRC NICK Tester $+ $rand(1,100) $crlf
    }

    ;Show all receiving data in a window
    On *:sockread:IRC:{
    window -de @IRC
    var %x
    sockread %x
    aline -p @IRC $iif(%x,$v1,-)
    }

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$sockname </identifiers/$sockname>`
    * :doc: `$sock </identifiers/$sock>`
    * :doc: `/socklist </commands/socklist>`
    * :doc: `/sockmark </commands/sockmark>`
    * :doc: `/sockpause </commands/sockpause>`
    * :doc: `/sockread </commands/sockread>`
    * :doc: `/sockrename </commands/sockrename>`
    * :doc: `/sockwrite </commands/sockwrite>`
    * :doc: `on sockopen </events/on_sockopen>`
