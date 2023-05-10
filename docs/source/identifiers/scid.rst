$scid
=====

$scid allows you to get the server id for a connection, or specific details regarding the properties of a certain connection id.

Synopsis
--------

.. code:: text

    $scid(N)[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Returns connection information based on a specific connection ID. Unlike $scon identifier - mIRC|$scon, $scid needs the connection id, not the Nth connection. If you specify N as ``0``, the total number of connections is returned.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - [.property]
      - If you specify a compatible List of identifiers - mIRC|identifier here, mIRC will provide you with that specific identifier property for the connection id parameter you've passed. See the examples below for more details.

Example
-------

Echo the total number of connections to the active window

.. code:: text

    //echo -a $scid(0)

Use the optional identifier-supported property to echo the server name of connection ID 39 to the active window

.. code:: text

    //echo -a $scid(39).server

Use the optional identifier-supported property to echo the network name of connection ID 39 to the active window

.. code:: text

    //echo -a $scid(39).network

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$activecid </identifiers/activecid>`
    * :doc:`$cid </identifiers/cid>`
    * :doc:`$lactivecid </identifiers/lactivecid>`
    * :doc:`$scon </identifiers/scon>`
    * :doc:`/scid </commands/scid>`

