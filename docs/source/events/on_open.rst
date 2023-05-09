On Open
=======

The ON OPEN event triggers within mIRC when a specific window type is opened, either locally, through server interaction, or due to a scripted circumstance. This event can be used to trigger scripted situations for actions to perform when a certain window is opened.

Much like the On close - mIRC|ON CLOSE event, the ON OPEN event triggers the :doc:`$target </identifiers/target>` identifier, and fills it with the window name related to the event. During the ON OPEN events, :doc:`$target </identifiers/target>` now refers to the window the event is dealing with.

Synopsis
--------

.. code:: text

    ON <level>:OPEN:<?|@|=|!|*>:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <?|@|=|!|*>
      - The window type that the event should trigger for:
    * - ?
      - Private messages/query windows.
    * - @
      - Custom Windows - mIRC|Custom @windows
    * - =
      - DCC Chat windows.
    * - !
      - DCC Fileserv windows.
    * - *
      - All window types.
    * - <matchtext>
      - The text that should be matched. Can be a :ref:`matching_tools-wildcard`. Specifically for this event, this text will most-likely be from a private message query window opening up. The reason is that this will allow interaction with the text, during the event of a query window opening, immediately, rather than waiting for an On text - mIRC|ON TEXT event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

.. code:: text

    ; When a query window opens, recognize if
    ; the user has typed the !yourserver command, which will
    ; relay to the user the current server for the mIRC client
    
    ON *:OPEN:?:!yourserver:msg $nick Current IRC Server: $server $+ .

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on close </events/on_close>`
