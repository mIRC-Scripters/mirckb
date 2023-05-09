On Signal
=========

The ON SIGNAL event triggers after a call to the :doc:`$signal </commands/signal>` command. This is a mechanism used to signal events in multiple script at the same time

You can use :doc:`$signal </identifiers/signal>` to refer to the name of signal triggering the event and you can use :doc:`$1- </identifiers/dollar1dash>` to refer to the parameters passed to /signal

Synopsis
--------

.. code:: text

    ON <level>:signal:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <matchtext>
      - The matchtext for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

.. code:: text

    ON *:signal:*:echo -s $signal -- $1-

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$signal </identifiers/signal>`
    * :doc:`/signal </commands/signal>`
