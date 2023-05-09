$rawbytes
=========

$rawbytes return the raw line for IRC server event prior to any parsing/decoding.

See :doc:`$rawmsg </identifiers/rawmsg>` for the raw line once decoded.

Synopsis
--------

.. code:: text

    $rawbytes

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:text:*:#:echo -a $rawbytes

Compatibility
-------------

.. compatibility:: 7.03

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$rawmsg </identifiers/rawmsg>`

