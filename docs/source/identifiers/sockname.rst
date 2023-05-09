$sockname
=========

$sockname It is the name given to a connection to identify it. This identifier can be used in events to know which connection an event is related to.

Synopsis
--------

.. code:: text

    $sockname

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:sockread:*:echo -a $sockname

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockbr </identifiers/sockbr>`
    * :doc:`$sockerr </identifiers/sockerr>`

