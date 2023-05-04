/part
=====

The **/part** command is used when you want to depart/leave a specific channel, or the current active channel. This command also allows you to specify a parting message, which will display to the remaining users a custom message in the server's PART message.

Synopsis
--------

.. code:: text

    /part [[#][PartMessage]] [PartMessage]

.. note:: All parameters are optional.*

Switches
--------

None

Parameters
----------

: **#**

:: *The optional name of a channel you wish to part from. If left blank, mIRC will attempt to part from the active channel.*

: **PartMessage**

:: *Specifies the part message you want the server to display to the remaining users.''

.. note:: If you do not specify a channel, the part message can be typed in place of the channel name; whereas if you specify a channel, you can also, optionally, include a part message.

Examples
--------

**Part Active Channel**

.. code:: text

    /part

**Part Active Channel With Part Message**

.. code:: text

    /part See ya!

**Part Specific Channel**

.. code:: text

    /part #ChannelName

**Part Specific Channel With Part Message**

.. code:: text

    /part #ChannelName See ya!

Compatibility
-------------

Added: mIRC v3.3 - 3.4 ()

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/partall </commands/partall>`
