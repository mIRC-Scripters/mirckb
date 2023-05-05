/sockrename
===========

The **/sockrename** command allows mIRC to assign a new name to an existing socket connection.

Synopsis
--------

.. code:: text

    /sockrename <name> <newname>

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
      - The name of the original socket to rename.
    * - <newname>
      - The new name to give to the original socket.

Example
-------

Rename the socket **mySocket** to **newSockName**:

.. code:: text

    /sockrename mySocket newSockName

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See Also
--------

.. hlist::
    :columns: 4

    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockname </identifiers/sockname>`
    * :doc:`$sockerr </identifiers/sockerr>`
    * :doc:`$sockbr </identifiers/sockbr>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/sockclose </commands/sockclose>`
    * :doc:`/socklist </commands/socklist>`
    * :doc:`/socklisten </commands/socklisten>`
    * :doc:`/sockmark </commands/sockmark>`
    * :doc:`/sockopen </commands/sockopen>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockudp </commands/udp-socket>`
    * :doc:`/sockwrite </commands/sockwrite>`
