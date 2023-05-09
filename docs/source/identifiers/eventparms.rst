$eventparms
===========

$eventparms returns the event-specific parameters passed by the script parser to an executed command. This is nothing but a version of $parms that is 'local', it only exists during an event and it has a global scope: you can access the value from an alias called from the event.

Synopsis
--------

.. code:: text

    $eventparms

Parameters
----------

None

Examples
--------

.. code:: text

    on *:text:*:#:echo -s $parms -- $eventparms | testpm
    alias testpm echo -s $parms -- $eventparms

Compatibility
-------------

coming soon

.. compatibility:: 7.53

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$parms </identifiers/parms>`

