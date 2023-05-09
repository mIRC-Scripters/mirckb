$ulevel
=======

$ulevel returns the matching user level for any triggered {{mirc|on event|on events}}.

Synopsis
--------

.. code:: text

    $ulevel

Parameters
----------

None

Properties
----------

None

Example
-------

When a user speaks in a channel, echo the user level that is triggered:

.. code:: text

    ON *:TEXT:*:#:echo -a User level triggered: $ulevel

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`events </events/index_events>`
    * :doc:`$clevel </identifiers/clevel>`
    * :doc:`$dlevel </identifiers/dlevel>`
    * :doc:`$event </identifiers/event>`

