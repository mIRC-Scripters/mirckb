/me
===

The /me command is used to send an action message to the active window. Because this command does not take a target parameter, it cannot be used within events that are triggered by anything other than the user directly from a given channel. For example: it can be used within the on input or hotlink events but not within the on text. To be able to generate an action message from any event to any window, consider using the /describe command instead.

An action message is simply a regular PRIVMSG that follows a client-dependent format - usually different to that of a normal message. The raw format for an action message is:

.. code:: text

    //raw PRIVMSG $active $+(:, $chr(1), ACTION) [message] $+ $chr(1)

Where [message] is the actual message to be displayed.

Synopsis
--------

.. code:: text

    /me <message>

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
      - The message to be sent to the channel

Example
-------

.. code:: text

    ;Send an action message to the active window
    /me brings the cookie jar

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$me </identifiers/me>`
    * :doc:`$nick </identifiers/nick>`
    * :doc:`/ame </commands/ame>`
    * :doc:`/amsg </commands/amsg>`
    * :doc:`/action </commands/action>`
    * :doc:`/describe </commands/describe>`
    * :doc:`/msg </commands/msg>`
    * :doc:`/qme </commands/qme>`
    * :doc:`/qmsg </commands/qmsg>`
    * :doc:`/say </commands/say>`

