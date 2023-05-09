/notice
=======

/notice Sends a private message to nickname without opening a query window for either you or them.

Synopsis
--------

.. code:: text

    /notice nick|target|nick,nick,... Message

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
    * - target 
      - receiver of the private message. Usually is a nick, but some networks support target being a comma separated list of nicks, or a #channel or prefixes#channel
    * - message 
      - message sent to the target(s)

.. note:: depending how the client is configured, received notice message can appear in status window, channel shared with sender, or active window.

Properties
----------

None

Example
-------

.. code:: text

    One of the messages from the /version command is similar to:
    TARGMAX=NAMES:1,LIST:1,KICK:1,WHOIS:1,PRIVMSG:4,NOTICE:4,ACCEPT:,MONITOR: are supported by this server
    The "NOTICE:4" is the maximum number of nicks that can be combined in a single /notice command:
    /notice nick1,nick2,nick3,nick4 This message is seen by all 4 nicks
    
    Inside the :NOTICE: event you can use $target to discern between notices sent to 1+ nicks or a class of nicks. In the above, all 4 nicks see $target = $me without knowing the other 3 nicks.
    
    If the server supports additional targets, some can include:
    /notice #test This notice seen by everyone in channel #test ($target = #test)
    /notice @+#test This message received by all OP+Voice in #test ($target = @+#test)
    /notice @%+#test This message received by all OP+Voice+HalfOp in #test ($target = @%+#test)
    /notice @#test This message received by all OP in #test ($target = @#test)
    This is not the same as /onotice, which requires sender be an OP
    
    For "/onotice message" or "/notice nick message" the receiver sees: -sender- message
    but for "/notice @+#test message" the receiver sees: -sender:@+#test- message
    
    Warning: Some networks did not fully support all targets, so should test to make certain that a target is seen only by nicks having that status, and not everyone in channel, or sometimes also seen by unlisted prefixes of higher status.

Compatibility
-------------

.. compatibility:: 2.7a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on notice </events/on_notice>`
