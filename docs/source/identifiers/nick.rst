$nick
=====

$nick can be called in two ways:

# $nick will return the nickname associated with an IRC event.
# $nick(#channel,index) retrieves information about nicknames on a specific channel.

Synopsis
--------

.. code:: text

    $nick

.. code:: text

    $nick(#,N/nick,aohvr,aohvr)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #
      - The channel name to look up nickname information.
    * - N/nick
      - Can be either a number to look up a particular Nth user (if N is 0, returns total matching users based on criteria), or can be a nickname to target a specific user.
    * - aohvr
      - Optional: The first aohvr characters target all users of a specific type, while the second aohvr excludes a specific type from the target list.

Specific Types
^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Type
      - Description
    * - a
      - All users
    * - o
      - Operators
    * - h
      - Helpers
    * - v
      - Voiced
    * - r
      - Regular users

Except for Type 'a' which has been defined as all users in the channel, channel modes given to users and pnick characters can also be used as nick types. This includes networks where channel owner is given mode +q and pnick character ! or ~, and superop is given mode +a and pnick character &. This next table assumes channel is at a network supporting the additional channel modes given to nicks.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Additional Type
      - Description
    * - q
      - Channel Owner having mode +q
    * - ~
      - Channel Owner having pnick character ~
    * - &
      - SuperOp (a.k.aa Protected Op)  having pnick character &
    * - @
      - Operators
    * - %
      - Helpers
    * - +
      - Voiced

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .pnick
      - Returns the target result with their elevation level, eg: @,+,%. Regular users display normal.
    * - .idle
      - Returns the current idle time for the nickname on the channel specified
    * - .color
      - Returns the color for that user as set up in the Nick color dialog

Examples
--------

Echo to the active screen the total amount of users in the channel:

.. code:: text

    //echo -a Total users: $iif($active ischan,$nick(#,0))

Echo to the active screen the number of operators in the channel:

.. code:: text

    //echo -a Total users: $iif($active ischan,$nick(#,0,o))

Echo to the active screen all elevated users only, excluding regular users:

.. code:: text

    //echo -a Total users: $iif($active ischan,$nick(#,0,a,r))

Create an alias that will open a Custom windows - mIRC|custom @window, and detail the user list:

.. code:: text

    alias getUserDetails {
    
      ; Make sure the active window is a channel
      if ($active ischan) {
    
        ; Set the %c variable to the channel name
        var %c = $active
        window @getUserDetails 350 350 650 300
    
        ; Clear the window justin in case it
        ; was already opened previously
        clear @getUserDetails
    
        ; Echo all of the user details
        echo @getUserDetails Channel: %c
        echo @getUserDetails $crlf $crlf
        echo @getUserDetails Total Users: $nick(%c,0)
        echo @getUserDetails Operators: $nick(%c,0,o)
        echo @getUserDetails Voices: $nick(%c,0,v)
        echo @getUserDetails Helpers: $nick(%c,0,h)
        echo @getUserDetails Regular Users: $nick(%c,0,r)
        echo @getUserDetails $crlf $crlf
    
        ; Below lists elevated users, whom are the ops/voices/helpers
        echo @getUserDetails Total Elevated Users: $nick(%c,0,a,r)
        echo @getUserDetails $crlf $crlf
    
        ; Lastly, list the nickname of the first nickname in the
        ; op list, voice list, helper list, and regular user list
        echo @getUserDetails First operator/voice/helper/regular users:
        echo @getUserDetails $lf $iif($nick(%c,1,o),$v1,NONE)
        echo @getUserDetails $lf $iif($nick(%c,1,v),$v1,NONE)
        echo @getUserDetails $lf $iif($nick(%c,1,h),$v1,NONE)
        echo @getUserDetails $lf $iif($nick(%c,1,r),$v1,NONE)
      }
    }

The above command is executed in a channel command-line by typing:

.. code:: text

    /getUserDetails

The results from the above will look something like this:

File:$nick identifer example results - mIRC.png|Shows the example results.

.. note:: A nick can have several channel modes, and the nicklist will display only the highest level. To have an exact count of the nicks displaying a certain nick type, you should have the 3rd parameter be the list of all types of that level and greater, then have the 4th parameter be the nick types greater than the specified level. For example, networks supporting levels above @Operator also give +o. ~ChannelOwner is given modes +qo and &ProtectedOp is given mode +ao. Some networks allow the Founder to give +q to several other users, so the ~ prefix isn't always an indication that someone is the channel owner/founder.

.. code:: text

    //echo -a There are $nick($chan,0,~&o,~&) nicks at the @operator level excluding Owners and SuperOps

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chan </identifiers/chan>`