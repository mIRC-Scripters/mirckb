$lactivecid
===========

$lactivecid returns the connection id related to the last active window. For instance if the you have more than one connection, let's say connections ''2'' and ''55'', and you activate a window in connection ''55'' and then switch back to connection ''2'', $lactivecid is now set to ''55''.

Synopsis
--------

.. code:: text

    $lactivecid

Parameters
----------

None

Example
-------

Echo to the currently active window the connection ID of the last active window

.. code:: text

    //echo -a $lactivecid

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$activecid </identifiers/activecid>`
    * :doc:`$cid </identifiers/cid>`
    * :doc:`$scid </identifiers/scid>`
    * :doc:`$scon </identifiers/scon>`
    * :doc:`/scid </commands/scid>`

