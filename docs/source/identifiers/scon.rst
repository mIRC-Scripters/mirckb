$scon
=====

$scon allows you to get the server id for a connection, or specific details regarding the properties of a certain connection id. It is important to note that unlike :doc:`$scid </identifiers/scid>`, $scon works on the Nth connection, not the actual connection ID.

Synopsis
--------

.. code:: text

    $scon(N)[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Returns the connection ID for the Nth connection. If you specify N as ''0'', the total number of connections is returned.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - [.property]
      - If you specify a compatible List of identifiers - mIRC|identifier here, it returns the value of that identifier evaluated on that connection. See the examples below for more details.

Example
-------

Echo the total number of connections to the active window

.. code:: text

    //echo -a $scon(0)

Use the optional identifier-supported property to echo the server name of connection number 1 to the active window

.. code:: text

    //echo -a $scon(1).server

Use the optional identifier-supported property to echo the network name of connection number 4 to the active window

.. code:: text

    //echo -a $scon(4).network

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
    * :doc:`$scid </identifiers/scid>`
    * :doc:`/scid </commands/scid>`

