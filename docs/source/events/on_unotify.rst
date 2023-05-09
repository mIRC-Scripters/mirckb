On Unotify
==========

The ON UNOTIFY event triggers when a user in the :doc:`/notify </commands/notify>` command list disconnects from the same server.

Synopsis
--------

.. code:: text

    ON <level>:UNOTIFY:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Halt mIRC's default notice and echo the event to the active window:

.. code:: text

    ON ^*:UNOTIFY: {
      echo -a * $nick just left $network
      haltdef
    }

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on notify </events/on_notify>`

