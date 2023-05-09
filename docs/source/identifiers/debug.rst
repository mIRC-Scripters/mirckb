$debug
======

$debug will return either the window name or the filename of the current connection's debug output target.

Synopsis
--------

.. code:: text

    $debug

Parameters
----------

None

Example
-------

Echo to the active screen the current, if any, debug target:

.. code:: text

    //echo -a $iif($debug,$v1,None)

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/debug </commands/debug>`

