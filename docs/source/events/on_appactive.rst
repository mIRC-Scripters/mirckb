On Appactive
============

The ON APPACTIVE event monitors when the mIRC application has had its active status changed.

Synopsis
--------

.. code:: text

    ON <level>:APPACTIVE:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

.. code:: text

    ; Listen for mIRC's appactive event, then echo 
    ; some information to the active window.
    
    ON *:APPACTIVE:echo -a * mIRC now has an appactive status of $appactive $+ .

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$active </identifiers/active>`
    * :doc:`$activecid </identifiers/activecid>`
    * :doc:`$activewid </identifiers/activewid>`
    * :doc:`$lactive </identifiers/lactive>`
    * :doc:`$lactivecid </identifiers/lactivecid>`
    * :doc:`$lactivewid </identifiers/lactivewid>`

