$wildsite
=========

$wildsite returns the address of the user who triggered an event in the form *!*@host.

Synopsis
--------

.. code:: text

    $wildsite

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
      echo -a $wildsite
    }

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$site </identifiers/site>`
    * :doc:`$fulladdress </identifiers/fulladdress>`

