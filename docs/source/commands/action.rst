/action
=======

The **/action** command is now deprecated in favour of the  identical **/me** command and is used to send an action message to the active window. Since it does not take a target parameter, that command is the kind of command that is mostly used manually, it cannot be used within events that are triggered by anything other than the user directly from a given channel. For example: it can be used within the on input or hotlink events but not within the on text. To be able to generate an action message from any event to any window, consider using the /describe command instead.

An action message is simply a regular PRIVMSG that follows a client-dependent format - usually different to that of a normal message. The raw format for an action message is:

.. code:: text

    //raw PRIVMSG $active $+(:, $chr(1), ACTION) [message] $+ $chr(1)

Where [message] is the actual message to be displayed.

Synopsis
--------

.. code:: text

    /action <message>

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
      - The message to be sent to the channel.

Example
-------

.. code:: text

    ;Send an action message to the active window
    /action brings the cookie jar

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$me </identifiers/me>`
    * :doc:`$nick </identifiers/nick>`
    * :doc:`/amsg </commands/amsg>`
    * :doc:`/describe </commands/describe>`
    * :doc:`/me </commands/me>`
    * :doc:`/msg </commands/msg>`
    * :doc:`/qme </commands/qme>`
    * :doc:`/qmsg </commands/qmsg>`
    * :doc:`/say </commands/say>`
