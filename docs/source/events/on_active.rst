On Active
=========

The ON ACTIVE event monitors when a certain window, or window type, is activated or has had its active status changed.

Synopsis
--------

.. code:: text

    ON <level>:ACTIVE:<*#?=!@>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <*><?><#[,#]>
      - The place, or places where the event listens, you can specify specific name of window, seperate them by comma.
        * \* - Any query/channel window
        * ? - Any query windows
        * # - Any channel window
        * = - Any DCC chat
        * ! - Any DCC server
        * @ - Any custom window
    * - <commands>
      - The commands to be performed when the event triggers

Examples
--------

.. code:: text

    ; Listen for any window becoming active,
    ; then display information about that window and the previous active window
    
    ON *:ACTIVE:*:echo -a * $active is now active, took over for $lactive

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
