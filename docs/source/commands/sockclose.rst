/sockclose
==========

The **/sockclose** command allows the closing of any open socket connections, either specifically or by :doc: `wildcard </intermediate/matching_tools.html#wildcard>` .

.. note:: if you close a socket inside a socket event, all infos on the socket are lost and $sockname will be set to $null as well.

Synopsis
--------

.. code:: text

    /sockclose <name>

Switches
--------

None

Parameters
----------

**<name>**: The specific socket name to be closed. This parameter can also be a :doc: `wildcard </intermediate/matching_tools.html#wildcard>` match.

Example
-------

.. code:: text

    /sockclose mySock

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
    * :doc: `/sockaccept </commands/sockaccept>`
    * :doc: `/socklist </commands/socklist>`
    * :doc: `/socklisten </commands/socklisten>`
    * :doc: `/sockmark </commands/sockmark>`
    * :doc: `/sockopen </commands/sockopen>`
    * :doc: `/sockpause </commands/sockpause>`
    * :doc: `/sockread </commands/sockread>`
    * :doc: `/sockrename </commands/sockrename>`
    * :doc: `/sockudp </commands/udp-socket>`
    * :doc: `/sockwrite </commands/sockwrite>`
