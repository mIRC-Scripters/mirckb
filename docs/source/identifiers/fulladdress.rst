$fulladdress
============

$fulladdress returns the full address of the user triggering an event in the form nick!user@host.

Synopsis
--------

.. code:: text

    $fulladdress

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:text:*:#:echo -a $fulladdress

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$site </identifiers/site>`
    * :doc:`$wildsite </identifiers/wildsite>`
    * :doc:`$address </identifiers/address>`
