On Join
=======

The ON JOIN event triggers when the mIRC client, or a remote user, joins a channel.

.. note:: When you join a channel yourself, $nick($chan,0) is always 1 inside the on join event because mIRC has to send /names to get the nickname; if you want to undertake some processing once the channel user list is complete, then use RAW 366 which indicates the end of the user list. Similarly, if you're an operator on the channel, you won't be opped inside the on join event, and should use ON OP event instead.

Synopsis
--------

.. code:: text

    ON <level>:JOIN:<#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <#,[,#]>
      - The text that to be matched. Can also be a :ref:`matching_tools-wildcard`.
    * - [,#]
      - Specific channel names
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

The following example makes use of the on me - mIRC|ON ME event, which triggers only when the local mIRC client triggers the event, not remote users.

.. code:: text

    ON ME:*:JOIN:#testing: { msg $chan Hello $chan - Today is $day and time is $time }

The following example works for everyone else who joins but except your self.

.. code:: text

    ON !*:JOIN:#mychan: { msg $chan Hey $nick $+ ! Welcome in our channel. }

Who ever joins, send them a greeting:

.. code:: text

    ON *:JOIN:#:msg # Welcome to # $+ , $nick $+ !

Override the join event to print a custom text and then tell mIRC to ignore it's own text.

.. code:: text

    on ^*:JOIN:*:{
      echo -tcbf join $chan * $nick ( $+ $fulladdress $+ ) join $chan
      halt
    }

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on part </events/on_part>`

