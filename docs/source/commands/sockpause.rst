/sockpause
==========

The /sockpause command allows mIRC to pause/restart the reading from winsock.

The packet are not lost, it's just that on sockread will stop triggering until you restart the reading.

Synopsis
--------

.. code:: text

    /sockpause [-r] <name>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - r
      - Restarts the reading for the socket.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name of the socket to reference.

Example
-------

Resume the incoming data reading for mySocket:

.. code:: text

    /sockpause -r mySocket

Compatibility
-------------

.. compatibility:: 5.3

See also
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
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockrename </commands/sockrename>`
    * :doc:`/sockudp </commands/sockudp>`
    * :doc:`/sockwrite </commands/sockwrite>`

