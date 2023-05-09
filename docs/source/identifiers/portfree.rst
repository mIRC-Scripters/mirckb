$portfree
=========

$portfree returns $true if the specified port is free, $false otherwise

Synopsis
--------

.. code:: text

    $portfree(N,[ipaddress])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The port number
    * - ipaddress
      - if you specify an ip address (can also be an adapter name), only the interface with that ip address is checked for used ports.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $portfree(6667)

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

