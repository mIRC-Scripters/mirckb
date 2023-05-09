$raddress
=========

.. attention:: This feature has essentially been replaced by :doc:`$dns </identifiers/dns>`

$raddress returns the resolved address of a /dns request in an :doc:`on dns </events/on_dns>` event.

Synopsis
--------

.. code:: text

    $raddress

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:dns:{
      echo -a $raddress
    }

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dns </identifiers/dns>`
    * :doc:`$iaddress </identifiers/iaddress>`
    * :doc:`$naddress </identifiers/naddress>`

