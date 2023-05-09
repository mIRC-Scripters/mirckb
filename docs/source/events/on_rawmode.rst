On Rawmode
==========

The ON RAWMODE allows a script to intercept and interpret the modes of a channel directly, avoiding mIRC's messages and notifications altogether.

Synopsis
--------

.. code:: text

    ON <level>:RAWMODE:<#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - #[,#]
      - The channel, or channel names, to listen on.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Intercept all RAWMODE events, echo them to the target window in plain text, and halt mIRC's notifications:

.. code:: text

    ON ^*:RAWMODE:*: {
      echo $target * RAWMODE: $1-
      haltdef
    }

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on mode </events/on_mode>`
    * :ref:`raw_events`