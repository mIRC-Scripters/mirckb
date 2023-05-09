$lactive
========

$lactive will return the full name of the last window that was active.

Synopsis
--------

.. code:: text

    $lactive

Switches
--------

None

Example
-------

.. code:: text

    ; Echo the value of $lactive to the active window
    
    //echo -a $lactive

.. code:: text

    ; Listen for an active window change, then 
    ; echo the last active window
    
    ON *:ACTIVE:*:echo -a * Active window is now $active $+ . Previous active window was $lactive

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`events </events/index_events>`
    * :doc:`on active </events/on_active>`
    * :doc:`$active </identifiers/active>`
    * :doc:`$activecid </identifiers/activecid>`
    * :doc:`$activewid </identifiers/activewid>`
    * :doc:`$lactive </identifiers/lactive>`
    * :doc:`$lactivecid </identifiers/lactivecid>`
    * :doc:`$lactivewid </identifiers/lactivewid>`

