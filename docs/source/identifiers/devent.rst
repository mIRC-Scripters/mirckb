$devent
=======

$devent returns the name of the dialog inside an on dialog event.

Synopsis
--------

.. code:: text

    $devent

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:dialog:*:*:*:{
    echo -a $devent
    }

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dialog </identifiers/dialog>`
    * :doc:`$did </identifiers/did>`
