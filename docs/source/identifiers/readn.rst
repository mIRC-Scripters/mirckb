$readn
======

$readn returns the number of the line matched by the last :doc:`$read </identifiers/read>` attempt.

.. note:: The value remains visible to all scripts and events until the next $read. If the read attempt fails to match, it returns 0.

Synopsis
--------

.. code:: text

    $readn

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //noop $read($mircini,tnw,*mirc*) | echo -a $readn

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$read </identifiers/read>`

