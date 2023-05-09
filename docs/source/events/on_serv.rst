On Serv
=======

The ON SERV event, much like the On chat - mIRC|ON CHAT event, is triggered when a message is sent via an /fserve command - mIRC|FSERVE window.

This event fills the $cd identifier - mIRC|$cd identifier with the current folder that the user is in within the /fserve command - mIRC|FSERVE.

Synopsis
--------

.. code:: text

    ON <level>:SERV:<matchtext>:<commands>

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
      - The text that to be matched. Much like the On text - mIRC|ON TEXT event, this can be any combination of text letters, numbers, and wildcards.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

.. code:: text

    ; This event waits for any user on a DCC Chat to use the
    ; command !time and then relays back to them the current time
    
    ON *:SERV:!time:msg =$nick The current time is: hh:nntt

In the above example, the msg is not simply followed by the :doc:`$nick </identifiers/nick>` identifier. Instead, the {{mIRC|=$nick}} identifier has been used. This special identifier tells mIRC that the event should not simply send a private message to the user, but rather it should message the user's DCC Chat window, if there is one.

The next example will send the user the current folder they are in if they type !folder:

.. code:: text

    ; Listen for !folder on the SERV event
    ON *:SERV:!folder:msg =$nick Current Folder: $cd

Compatibility
-------------

.. compatibility:: 3.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cd </identifiers/cd>`
    * :doc:`on chat </events/on_chat>`
    * :doc:`on text </events/on_text>`

