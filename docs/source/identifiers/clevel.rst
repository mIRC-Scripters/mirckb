$clevel
=======

$clevel will return the matching event level for any triggered :doc:`events </events/index_events>`.

Synopsis
--------

.. code:: text

    $clevel

Parameters
----------

None

Example
-------

When a user speaks in a channel, echo the event level that is triggered:

.. code:: text

    ON *:TEXT:*:#:echo -a Event level triggered: $clevel

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`events </events/index_events>`
    * :doc:`$dlevel </identifiers/dlevel>`
    * :doc:`$event </identifiers/event>`
    * :doc:`$ulevel </identifiers/ulevel>`

