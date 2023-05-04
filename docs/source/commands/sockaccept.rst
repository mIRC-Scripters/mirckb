/sockaccept
===========

The **/sockaccept** command allows mIRC the ability to accept incoming connections on a port that has been opened with the :doc: `/socklisten </commands/socklisten>` commmand.

Synopsis
--------

.. code:: text

    /sockaccept -n <name>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - Disable nagle algorithm on the accepted socket, you can disable nagle algorithm for any accepted socket by using :doc: `/socklisten </commands/socklisten>` -n

Parameters
----------

**Name**: The name that should be assigned to the accepted connection in order to reference it later.

Example
-------

.. code:: text

    ; Listen for connections on the socket named mySock
    ON *:SOCKLISTEN:mySock: {

    ; Accept incoming connection on this socket and name them
    ; with a combination of the socket's name and the current $ctime
    sockaccept $+($sockname,$ctime)
    }

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See Also
--------

.. hlist::
    :columns: 4

    * :doc: `$sock </identifiers/$sock>`
    * :doc: `$sockname </identifiers/$sockname>`
    * :doc: `$sockerr </identifiers/$sockerr>`
    * :doc: `$sockbr </identifiers/$sockbr>`
    * :doc: `/sockclose </commands/sockclose>`
    * :doc: `/socklist </commands/socklist>`
    * :doc: `/socklisten </commands/socklisten>`
    * :doc: `/sockmark </commands/sockmark>`
    * :doc: `/sockopen </commands/sockopen>`
    * :doc: `/sockpause </commands/sockpause>`
    * :doc: `/sockread </commands/sockread>`
    * :doc: `/sockrename </commands/sockrename>`
    * :doc: `/sockudp </commands/udp-socket>`
    * :doc: `/sockwrite </commands/sockwrite>`
