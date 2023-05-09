$naddress
=========

.. attention:: This feature has essentially been replaced by :doc:`$dns </identifiers/dns>`

$naddress returns the address being resolved in an :doc:`on dns </events/on_dns>` event.

Synopsis
--------

.. code:: text

    $naddress

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
      echo -a $naddress
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
    * :doc:`$raddress </identifiers/raddress>`

