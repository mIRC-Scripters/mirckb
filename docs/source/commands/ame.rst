/ame
====

The **ame** command is used to send an action message to all the channels you are currently on in a specific network.  This command behaves the same as the /me command with the addition of multiple channels.

An action message is simply a regular PRIVMSG that follows a client-dependent format - usually different to that of a normal message. The raw format for an action message is:

.. code:: text

    //raw PRIVMSG #ChanA,#chanB,#chanC $+(:, $chr(1), ACTION) [message] $+ $chr(1))

Where [message] is the actual message to be displayed.

.. note:: As of mIRC v7.1 the /ame command will split long messages into smaller messages so no part of the message will be truncated.

Synopsis
--------

.. code:: text

    /ame <message>

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <message>
      - The action message to be sent.

Example
-------

.. code:: text

    /ame gives away cookies

    ; The ame command can be used in conjunction with
    ; the scon command to generate a multi-network ame:
    /scon -at1 ame gives away cookies

Compatibility
-------------

Added: mIRC v3.2 (02 May 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/amsg </commands/amsg>`
    * :doc:`/describe </commands/describe>`
    * :doc:`/me </commands/me>`
    * :doc:`/msg </commands/msg>`
    * :doc:`/qme </commands/qme>`
    * :doc:`/qmsg </commands/qmsg>`
    * :doc:`/say </commands/say>`
