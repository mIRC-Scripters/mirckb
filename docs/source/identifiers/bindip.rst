$bindip
=======

$bindip is used to get information regarding an available network adapter.

Synopsis
--------

.. code:: text

    $bindip(N|ipaddress)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Returns the Nth device in the network adapters list. If ''N'' is specified as ''0'', returns the total number of active network adapters.
    * - ipaddress
      - If you specify an IP address, mIRC will try to find the best network adapter to use to connect to that IP.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - name
      - The name of the network adapter.
    * - ip
      - The IP address of the network adapter.
    * - loopback
      - Returns ''$true'' if the IP/device has a loopback, otherwise ''$false''.

Examples
--------

Echo to the active window the total number of network adapters

.. code:: text

    //echo -a $bindip(0)

Echo to the active window the name of a local network adapter

.. code:: text

    //echo -a $bindip(192.168.1.1).name

Compatibility
-------------

.. compatibility:: 7.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ip </identifiers/ip>`
    * :doc:`$iptype </identifiers/iptype>`
    * :doc:`$portfree </identifiers/portfree>`
    * :doc:`/bindip </commands/bindip>`

