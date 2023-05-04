/socklist
=========

The **/socklist** command allows mIRC to list all sockets that are currently open open.

Synopsis
--------

.. code:: text

    /socklist [-tul] [name]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -tul
      - These can be a single, or combination, of switches to list open TCP, UDP or listening sockets, respectively.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [name]
      - The name of the socket to search for. This parameter can also be a :doc: `wildcard </intermediate/matching_tools.html#wildcard>` match.

Example
-------

List all TCP sockets that have the begin with **mySock**:

.. code:: text

    /socklist -t mySock*

Compatibility
-------------

Added: mIRC v5.71 (07 May 2000)

See Also
--------

.. hlist::
    :columns: 4

    * :doc: `$sock </identifiers/$sock>`
    * :doc: `$sockname </identifiers/$sockname>`
    * :doc: `$sockerr </identifiers/$sockerr>`
    * :doc: `$sockbr </identifiers/$sockbr>`
    * :doc: `/sockaccept </commands/sockaccept>`
    * :doc: `/sockclose </commands/sockclose>`
    * :doc: `/socklisten </commands/socklisten>`
    * :doc: `/sockmark </commands/sockmark>`
    * :doc: `/sockopen </commands/sockopen>`
    * :doc: `/sockpause </commands/sockpause>`
    * :doc: `/sockread </commands/sockread>`
    * :doc: `/sockrename </commands/sockrename>`
    * :doc: `/sockudp </commands/udp-socket>`
    * :doc: `/sockwrite </commands/sockwrite>`
