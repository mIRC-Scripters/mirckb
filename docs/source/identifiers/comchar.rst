$comchar
========

The $comchar identifier returns the command prefix character.

Prior to mIRC 7.39, one could generally access this value with the following code:

.. code:: text

    alias comchar return $readini($mircini, n, text, commandchar)

.. note:: Regardless of the command prefix, the slash (/) is ''always'' a valid command prefix.

.. note:: The command prefix can be changed from mIRC-Options/Other.

Synopsis
--------

.. code:: text

    $comchar

Parameters
----------

None

Example
-------

.. code:: text

    //echo -a $comchar

Compatibility
-------------

.. compatibility:: 7.39

