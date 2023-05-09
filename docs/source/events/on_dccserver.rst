On Dccserver
============

The ON DCCSERVER event triggers a connection attempt is made on mIRC's DCC Server. This event allows easy monitoring of connections and the ability to prevent someone from connecting to mIRC by invoking the :doc:`$halt </commands/halt>` command.

When triggered by a Send, this event fills the :doc:`$filename </identifiers/filename>` identifier with the file name attempting to be received.

Synopsis
--------

.. code:: text

    ON <level>:DCCSERVER:<Chat|Send|Fserve>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.s
    * - <Chat|Send|Fserve>
      - The text that to be matched. Can also be a :ref:`matching_tools-wildcard`.
        * Chat - Triggers if the event is caused by a DCCSERVER Chat.
        * Send - Triggers if the event is caused by a DCCSERVER Send.
        * Fserve - Triggers if the event is caused by a DCCSERVER Fserve.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

Echo to the active screen some information when a :doc:`dcc send </commands/dcc>` is being received:

.. code:: text

    ON *:DCCSERVER:Send:echo User $nick ( $+ $address $+ ) is attempting to send: $filename

The ON DCCSERVER event can also prevent certain events from happening, based on a certain criteria. For instance, the following event will decline a :doc:`dcc send </commands/dcc>` if the file extension is .exe file type - Windows|.exe:

.. code:: text

    ON *:DCCSERVER:Send:if ($right($filename,4) == .exe) { echo -a User $nick just tried to send a file with an .exe extension. It has been declined. | halt }

The use of the :doc:`$halt </commands/halt>` command in this instance prevents any further action, even from any confirmation windows from popping up. /halt can also be used on the other ON DCCSERVER events to prevent anything from happening.

Echo when a user attempts to initiate a :doc:`DCC Chat </commands/dcc>`:

.. code:: text

    ON *:DCCSERVER:Chat:echo User $nick ( $+ $address $+ ) is attempting to initiate a DCC Chat.

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on chat </events/on_chat>`
    * :doc:`on sendfail </events/on_sendfail>`

