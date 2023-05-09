/ctcpreply
==========

The /ctcpreply command can be used to send a reply to a CTCP request

Synopsis
--------

.. code:: text

    /ctcpreply <nick> <ctcp> [message]

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
    * - <nick>
      - Nickname of the person to send a response to
    * - <ctcp>
      - Reply type
    * - [message]
      - response message

Example
-------

.. code:: text

    ;Listen to a TIME CTCP request
    ctcp *:TIME:*:{
    
      ;Send two CTCP replays
      ctcpreply $nick TIME Current time: $time(hh:nn:ss TT (ZZZ))
      ctcpreply $nick TIME Current Data: $time(dddd $+ $chr(44) mmmm dd $+ $chr(44) 2009)
    
      ;Stop the standard mIRC\'s CTCP replay
      halt
    }

Compatibility
-------------

.. compatibility:: 5.02

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ctcp </commands/ctcp>`
    * :doc:`/ctcps </commands/ctcps>`

