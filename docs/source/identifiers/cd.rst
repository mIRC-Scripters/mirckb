$cd
===

The $cd identifier contains the current directory/folder a user is viewing within an :doc:`/fserve </commands/fserve>`.

Synopsis
--------

.. code:: text

    $cd

Parameters
----------

None

Example
-------

This example will send the user the current folder they are in if they type !folder:

.. code:: text

    ; Listen for !folder on the SERV event
    ON *:SERV:!folder:msg =$nick Current Folder: $cd

Compatibility
-------------

.. compatibility:: 4.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on serv </events/on_serv>`
    * :doc:`/fserve </commands/fserve>`

