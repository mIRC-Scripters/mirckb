/mode
=====

The /mode command changes the mode of the specified channel or nick.

Channel modes can typically only be changed by a channel operator. Nick modes can typically only be changed for your own nick, though some are set by the server and cannot be changed.

Some Channel and Nick modes are standard across all servers, whilst some are unique to particular IRC networks.

Synopsis
--------

.. code:: text

    /mode <channel|nickname> [[+|-]modechars [parameters]]

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
    * - <channel|nickname>
      - the nick/channel you want to change the mode
    * - [[+|-]modechars [parameters]]
      - the syntax of a mode change.

.. note:: modechars are almost always case sensitive. Be sure to use the correct upper or lower case.

Modes
-----

Channel Modes
^^^^^^^^^^^^^

Channel modes can either apply to the channel as a whole, or can apply particular rules to specific users in the channel (such as Op, Voiced, Banned etc.)

You are normally only able to set Channel modes if you are a channel Op.

The list of ''Channel'' modes below are those that are commonly available on most IRC networks. Some (or many) IRC networks have additional modes (see individual network help pages), and this list should not be considered definitive.

Channel-wide Modes
~~~~~~~~~~~~~~~~~~

* A - For an invite only channel by default only Ops and Half-Ops can invite users to join. /mode $chan +A allows any channel member to invite others to join the channel.
* C - Blocks users from sending CTCP requests to channel: /mode $chan +C
* F - Restrict channel users from changing nicks (with /nick) more than X times in Y seconds: /mode $chan +F X:Y
* Q - Only Chanserv (or equivalent) can kick users, not Ops: /mode $chan +Q
* R - Only registered users can join the channel: /mode $chan +R
* S - Strip Control codes for colours etc from channel messages: /mode $chan +S
* c - Disallow messages containing control codes for colours: /mode $chan +c
* d - Make users wait X seconds after joining before being able to speak in channel - can help prevent drive-by spam: /mode $chan +d X
* i - Make the channel invite only - existing users will need to invite new users before they can join the channel: /mode $chan +i
* j - Only allow X users to join the channel every Y seconds: /mode $chan +j X:Y
* k - Give the channel a password or key - users will need to provide the key to join the channel: /mode $chan +k key
* l - Set a limit to the number of users allowed in the channel - this is typically used to prevent DoS attacks by hundreds of users attempting to join a channel at once, and is reset by a bot as the number of valid users increases as they join or decreases as they part: /mode $chan +l n
* m - Make the channel moderated - only users who have been 'voiced' with mode v are able to say anything in channel: /mode $chan +m
* n - No external messages - only people who have joined the channel can send messages to it: /mode $chan +n
* p - Make the channel private i.e. it will not appear in the server's channel list: /mode $chan +p
* s - Make the channel secret i.e. it will not appear in the server's channel list or in /whois responses for users already in channel: /mode $chan +s
* t - Only Ops and Half-Ops can change the topic: /mode $chan +t
* z - Only users connected via SSL can join the channel: /mode $chan +z

User specific channel modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* I - Allows users matching the mask to join the channel without needing an invite first: /mode $chan +I nick!host@address
* b - Ban users matching the mask from the channel: /mode $chan +b nick!host@address
* e - Allows users matching the mask to join the channel even if a ban mask would otherwise ban them: /mode $chan +e nick!host@address
* h - Give a user Half-Op status in the channel - usually indicated with nick prefixed with a %: /mode $chan +h nick
* o - Give a user Op status in the channel - usually indicated with nick prefixed with an @: /mode $chan +o nick
* v - Give a user Voiced status in the channel - usually indicated with nick prefixed with a +: /mode $chan +v nick

User Modes
^^^^^^^^^^

The list of ''User'' modes below are those that are commonly available on most IRC networks. Some (or many) IRC networks have additional modes (see individual network help pages), and this list should not be considered definitive.

* i - Mark yourself invisible from /who: /mode $me +i 

.. note:: This does NOT make you invisible inside a channel - nor does it stop someone doing a /whois for your nick if they know it. But it does stop your nick being listed using /who or /names commands.

* r - Indicates that your nick is registered and identified with Chanserv or equivalent.
* w - Allows you to receive walluser messages about the status of the network from IRCOPS: /mode $me +w
* x - Replace the IP address in your IRC hostname with a hashed/encrypted version: /mode $me +x
* B - Mark yourself as being a bot: /mode $me +B
* R - Allows only other nicks who are registered and identified with Chanserv or equivalent to send you private messages: /mode $me +R

Example
-------

None

Compatibility
-------------

.. compatibility:: 2.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mode </identifiers/mode>`
    * :doc:`on mode </events/on_mode>`
    * :doc:`on rawmode </events/on_rawmode>`
    * :doc:`$modespl </identifiers/modespl>`

