$comerr
=======

$comerr return 1 if an error occured with a :doc:`com </advanced/com>`, 0 otherwise. This identifier should be checked after any :doc:`$com </identifiers/com>`/:doc:`$comcall </identifiers/comcall>` call.

Synopsis
--------

.. code:: text

    $comerr

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //comopen a nonexistant | echo -a $comerr

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/comopen </commands/comopen>`
    * :doc:`$com </identifiers/com>`
    * :doc:`$comcall </identifiers/comcall>`
