On Playend
==========

The ON PLAYEND event triggers when mIRC has finished /play command - mIRC|playing a text file to a channel, or user.

This event fills the :doc:`$filename </identifiers/filename>` identifier with the file that just finished playing.

Synopsis
--------

.. code:: text

    ON <level>:PLAYEND:<commands>

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

Examples
--------

Echo the name of the file that finished playing to the active window:

.. code:: text

    ON *:PLAYEND:echo -a * $filename has just finished playing.

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/play </commands/play>`

