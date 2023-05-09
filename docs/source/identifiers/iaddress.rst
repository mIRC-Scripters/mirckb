$iaddress
=========

$iaddress returns the ip address, if avaible, inside an :doc:`on dns </events/on_dns>` event.

Synopsis
--------

.. code:: text

    $iaddress

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:dns:echo -a $iaddress

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dns </identifiers/dns>`
    * :doc:`$raddress </identifiers/raddress>`
    * :doc:`$maddress </identifiers/maddress>`
    * :doc:`$naddress </identifiers/naddress>`

