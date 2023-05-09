On Action
=========

The ON ACTION event triggers on an action (:doc:`$me </commands/me>` or :doc:`$describe </commands/describe>`) events inside of a channel, or a query window.

Synopsis
--------

.. code:: text

    ON <level>:ACTION:<matchtext>:<*><?><#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <matchtext>
      - The corresponding matchtext for the event to trigger.
    * - <*><?><#[,#]>
      - The place, or places where the event listens, you can specify specific name of window, seperate them by comma.
    * - <commands>
      - The commands to be performed when the event triggers

Examples
--------

Listens for if anyone uses the word ''slap'' anywhere in an action inside of any channel

.. code:: text

    ON *:ACTION:* slap *:#:msg # $nick $+ ! Why would you slap anyone?!?!?

The above code listens for the action event, looks for if the user used the word ''slap'' in any channel, and then responds accordingly.

.. note:: The :ref:`matching_tools-wildcard` search, with a space between them and the word, means this event will not trigger if any other characters are touching the word ''slap''. This includes words such as: ''slaps'', ''slapper'', ''myslap'', etc.

Listen for any action inside of a private message and responds

.. code:: text

    ON *:ACTION:*:?:msg $nick Well, I have no idea why I'm responding to this automatically, $nick $+ . You said: $1-

This code will listen for ''any'' action event in a private message, and respond with a silly message.

Compatibility
-------------

.. compatibility:: 3.5

See also
--------