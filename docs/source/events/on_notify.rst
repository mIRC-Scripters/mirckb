On Notify
=========

The ON NOTIFY event triggers when a user in the /notify command - mIRC|notify list connects to the same server.

Synopsis
--------

.. code:: text

    ON <level>:NOTIFY:<commands>

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

Send a notice to the user when they connect:

.. code:: text

    ON *:NOTIFY:notice $nick Hey there! Glad to see you again!

Compatibility
-------------

.. compatibility:: 3.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on unotify </events/on_unotify>`

