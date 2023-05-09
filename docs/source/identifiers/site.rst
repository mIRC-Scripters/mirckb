$site
=====

$site returns the portion of :doc:`$address </identifiers/address>` after the @ for the user associated with an event in the form user@host.

Synopsis
--------

.. code:: text

    $site

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:text:*:#:{
      echo -a $site
    }

Compatibility
-------------

.. compatibility:: 3.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$wildsite </identifiers/wildsite>`
    * :doc:`$fulladdress </identifiers/fulladdress>`
    * :doc:`$address </identifiers/address>`

