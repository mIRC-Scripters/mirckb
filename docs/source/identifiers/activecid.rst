$activecid
==========

$activecid returns the connection id related to the active window. This means that if the window was created on connection 1, the $activecid for that window would be ''1''.

Synopsis
--------

.. code:: text

    $activecid

Parameters
----------

None

Example
-------

Echo to the currently active window the connection ID it is related to

.. code:: text

    //echo -a $activecid

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cid </identifiers/cid>`
    * :doc:`$lactivecid </identifiers/lactivecid>`
    * :doc:`$scid </identifiers/scid>`
    * :doc:`$scon </identifiers/scon>`
    * :doc:`/scid </commands/scid>`

