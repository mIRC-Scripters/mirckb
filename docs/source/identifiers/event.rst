$event
======

$event will return the event name of any triggered :doc:`events </events/index_events>`. It will also be filled inside raw events with the numeric or string event's name

Synopsis
--------

.. code:: text

    $event

Parameters
----------

None

Example
-------

When a user speaks in a channel, echo the event name that is triggered:

.. code:: text

    ON *:TEXT:*:#:echo -a Event triggered: $event

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`events </events/index_events>`
    * :doc:`$clevel </identifiers/clevel>`
    * :doc:`$dlevel </identifiers/dlevel>`
    * :doc:`$ulevel </identifiers/ulevel>`

