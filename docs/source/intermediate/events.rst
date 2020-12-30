Events
======

Access Levels
-------------

**Access levels** in mIRC are a mechanism by which events can be restricted to certain user levels or named groups. Almost all events have a level parameter that specifies the event's access level.

User List
~~~~~~~~~

The list of users and their access is stored in the "users" tab of the script editor. Only a single address is stored per line and must follow the following syntax:

.. code:: text

  <levels>:<address> <additional info>

Access levels are comma-delimited values that define the levels of the user. Although usually, the levels are numeric, you can use a name instead like "botAdmin" or "friends".

The parameter is an optional parameter that can be used to store some additional information about the user or other useful miscellaneous data.

.. code:: text

  10,20:some!one@example.com
  friend:dan!z@some.isp.net high school friend

Adding Users
^^^^^^^^^^^^

There are two commands that can be used to add a user to the access list, /auser and /guser. They follow this syntax:

.. code:: text

   /auser [-a] <levels> <name|address> [info]
   /guser [-a] <levels> <name> [addressType] [info]

Both /auser and /guser do the same thing, they add a specific user to the user list with the access levels specified (Comma delimited). The -a switch can be used to simply add additional access levels to an existing user, otherwise all the old levels gets replaced with the new ones. The fundamental difference between /auser and /guser is that /guser can be used to look up the address of a user while /auser requires you to provide it beforehand.

.. code:: text

   ;Add joe (address mask type 2), access level 'friend'
   /guser friend joe 2 neighbor

Removing Users
^^^^^^^^^^^^^^

The /ruser command can be used to remove a user completely from the access list or simply remove one of his levels.

.. code:: text

   /ruser [levels] <name|address> [type]

For example:

.. code:: text

   /ruser madman 2
   /ruser 2,10 foobar

Changing Users' Info
^^^^^^^^^^^^^^^^^^^^

The user info parameter can be changed at any time using the /iuser command:

.. code:: text

   /iuser <name|address> [info]

Event Prefixes
--------------

mIRC offers a lot of prefixes to slightly alter how the event activates.

\* Prefix
~~~~~~~~~

The \* prefix is the most commonly used prefix, and allows any user to activate the event regardless of their access level.

For example:

.. code:: text

   on *:text:!time:#:{
     notice $nick the time for me is $time
   }

Numeric Prefixes
~~~~~~~~~~~~~~~~

Numeric prefixes allow any user with an access level >= the prefix to activate the event.

For example:

.. code:: text

   on +5:text:.h:#myChan:{
     mode $chan +h $nick
   }

can be executed by any user with access level 5 or greater.

^ Prefix
~~~~~~~~

By default, your event is triggered after mIRC has processed this event itself. For example if someone talks to you in a query, mIRC will display the text in that window, triggers the various beep and flash option if any, and only then trigger on TEXT.

The ^ prefix tells mIRC to process your event before it processes the event itself. This prefix typically only works with IRC event but here is a full list of supported events: on ACTION, on BAN, on CHAT, on DEHELP, on DEOP, on DEVOICE, on HELP, on INVITE, on JOIN, on KICK, on MODE, on NICK, on NOTICE, on OP, on OPEN, on PART, on PING, on TEXT, on UNBAN, on USERMODE, on VOICE, on QUIT, on SERV, on SERVERMODE, on SERVEROP, on SNOTICE, on TABCOMP, on TOPIC, on wallops.

This prefix, coupled with /halt or /haltdef, allows you to display your own message for a given event, or it allows you to prevent a query window from opening with on OPEN, or to prevent a nick completion in on tabcomp.

\+ Prefix
~~~~~~~~~

By default, the numeric prefix means that level and any level higher can trigger that event. Using the + prefix, you can limit the event to be exactly the level specified.

For example:

.. code:: text

   on +5:text:.h:#myChan:{
     mode $chan +h $nick
   }

will only work for users with access level of exactly 5. Any user with higher access level will not activate that event.

! Prefix
~~~~~~~~

The exclamation mark prefix can be used to prevent an event from being activated by you (if ($nick != $me)).

For example:

.. code:: text

   on !1:join:#support:{
     msg $chan Hello $nick $+ , do you need help?
   }

will never get activated by you joining #support, only other people.

@ Prefix
~~~~~~~~

The @ symbol can be used as a prefix to indicate that the event can only be activated if you are an operator in the channel. You can think of it as "if ($me isop $chan) {"

For example:

.. code:: text

   on @10:text:.op:#myChan:{
     mode $chan +o-v $nick $nick
   }

will only work if you are an operator in #myChan at the time the user typed ".o".

& Prefix
~~~~~~~~

The **& prefix** can be used to prevent the event from being executed if the previous event called the /haltdef or /halt commands (if $halted is $true).

For example, given the following two on TEXT events placed in separate files...

script1.mrc

.. code:: text

   on *:TEXT:!test:?:haltdef

script2.mrc

.. code:: text

   on &*:TEXT:*:?:echo -ga I triggered because $!halted == $halted $+ !

The second event will trigger upon recieving any msg sent via query *except* **!test**, because the first event calls the *haltdef* command upon receiving **!test**.

$ Prefix
~~~~~~~~

This event prefix means the matchtext of the event is a regular expression, the delimiter are required.

.. code:: text

   on $*:text:/^([!@.])test$/:#myChan:{
     msg $chan $nick triggered test with $regml(1)
   }

Named Access Levels
~~~~~~~~~~~~~~~~~~~

Sometimes it's beneficial to give an access group a name instead of a numeric value. A good example is bot admins, friends, or even channel members. You can define such groups using the normal /guser and /auser commands:

.. code:: text

   /guser BotAdmin Mike123 2
   /guser BotAdmin Joe73 2
   /guser BotAdmin Dave12 2

With that you can use the named group level in events, for example:

.. code:: text

   on BotAdmin:text:!example:#:{
     msg $chan Hello Bot Admin!
   }

me Prefix
~~~~~~~~~

The 'me' prefix can be used to get an event to trigger when you meet the criteria (only if $nick == $me). The 'me' prefix is a bit special; it requires a new colon before other prefixes.

For example:

.. code:: text

   on me:*:join:#support:{
     msg $chan Hello $chan $+ , I need help!
   }

.. note:: Many events are **not** triggered when you meet the criteria and you need to code a separate 'me' event to handle it.

**Raw events** allow you to handle IRC event in their native, unmodified, format. Every message you receive from the server before mIRC processes it is called a **raw message**. And it might look a little different from the one you see after it gets parsed.

RAW Events
----------

Raw Messages
~~~~~~~~~~~~

Below is an example of a typical raw irc message that is received when a user talks in a channel:

.. code:: text

   :Kevin!bncworld@I-Have.a.cool.vhost.com PRIVMSG #mIRC :I feel lucky today

What most of us would see would look a little different. In my case it looks like this:

.. code:: text

   15:43 <@Kevin> I feel lucky today

As you can see, mIRC has processed the raw message and displayed it in a convenient manner. There are many occasions where we might want to override this behavior or even handle messages that mIRC might not natively support. In this article we will see at least two such cases.

/debug
~~~~~~

Before we can talk about the actual events themselves it's important that we get a better understanding on what these raw messages look like. mIRC provides a continent way to do just that with the use of the /debug command. The **/debug command** can be used to display all the raw messages that gets passed between you and the server. The debug command can be called using the following syntax:

.. code:: text

   /debug <@window>

We suggest you create a window with an editbox so that you can execute commands from within the same window.

.. note:: The message are shown undecoded (utf8)

.. code:: text

   //window -e @raw | debug @raw

Raw Numeric
~~~~~~~~~~~

Using the debug window we have open. Let’s execute a /whois command on someone in our channel. You might see something similar to this:

.. code:: text

    -> :irc.server.name WHOIS foo
    <- :irc.server.name 311 bar foo ~Ident name-B21D62.lolhat.com :Foo Jenkins
    <- :irc.server.name 319 bar foo :+#foobar @#kekelar %#scripting
    <- :irc.server.name 312 bar foo irc.server.name :Server Description
    <- :irc.server.name 307 bar foo :has identified for this nick
    <- :irc.server.name 335 bar foo :is a Bot on name 
    <- :irc.server.name 671 bar foo :is using a Secure Connection
    <- :irc.server.name 318 bar foo :End of /WHOIS list.

You may have noticed that following the server’s name there is a strange number: 311, 319, 312, 307... These numbers are known as **raw numeric**. Most, but not all, raw messages will have a number that we can use to uniquely identify the message. For example **318** will always mean "End of /WHOIS list." Raw **numeric 319** will always give us a list of channels the user is on. That number will prove to be invaluable in writing scripts that deal with raw message.

Numeric Raw Event
~~~~~~~~~~~~~~~~~

The syntax for the raw event is:

.. code:: text

   raw <numeric>:<matchtext>:{
      ; code to handle the message
   }

.. note:: The on raw event triggers every time a raw numeric and a pattern matched, regardless of who or what caused the event to happen.

You can see how the numeric is a very important part of a raw event. The matchtext can be a wildcard pattern by which mIRC will try to match against.

Recall that raw 319 is the list of channels the user you whoised is on:

.. code:: text

   :irc.my-irc-network.net 319 <myname> <nick> :<[mode]#channel> <[mode]#channel2> <[mode]#channel3>...

Our raw event will look like this:

.. code:: text

   raw 319:*:{
     ; $1 = <myname>
     ; $2 = <nick>
     ; $3 = <[mode]#channel 1>
     ; $4 = <[mode]#channel 2>
     ; $5 = <[mode]#channel 3>
     ; $6 ...
   }

Example: Channels-On-Join
~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we will create a script that will message all the channels a user is on. Our example will be composed of two parts: an on join event and an on raw event.

We will need to use the on join event to be able to know when the user joins a channel. Recall that the raw event will trigger whenever any matching raw message is received. To ensure our raw event only happens when we want it to we will set a variable to indicate it.

The on join part:

.. code:: text

   on *:join:#:{
      ; make a variable called "%whois.nick" to the channel's name 
      ; We will use this variable later on in the raw event. 
      set %whois. $+ $nick $chan 
      ; whois the user
      whois $nick
   }

Recall that $2 is the user we whoised. We will need that to check if %whois.nick is set. Our code will look like this:

.. code:: text

   raw 319:*:{
      ;We indicated that the event should trigger on the server's numeric value of 319
      if (%whois. [ $+ [ $2 ] ]) {
        ;In the if statement we check if we actually /whoised this user 
        msg %whois. [ $+ [ $2 ] ] [WHOIS] $2 is on $3-.
        unset %whois. $+ $2
      } 
    }

Non-Numeric Raw Event
~~~~~~~~~~~~~~~~~~~~~

As we have seen, not every raw event has a numeric value. The syntax for such events are:

.. code:: text

   raw <event>:<matchtext>:{
      ; code to handle the message
   }

An example of using it is for SASL authentication. Where the following events will be used (on a network like FreeNode):

.. code:: text

   raw cap:* ack sasl *:{ }
   raw cap:* ls *:{ }
   raw authenticate:*:{ }

CTCP Events
-----------

CTCP stands for Client-To-Client-Protocol which is a special type of communication between IRC Clients. By creating CTCP events, you can make your mIRC react to commands or requests from other users.

For example when you want to know the version of the client used by an user, you type /ctcp version, this actually sends a privmsg

Format
~~~~~~

The CTCP event has the following format:

.. code:: text

   ctcp <level>:<matchtext>:<*|#|?>:<commands>

-  **<level>** - The corresponding access levels for the event to trigger.
-  **<matchtext>** - The corresponding matchtext for the event to trigger.
-  **<*><?><#>** - The place, or places where the event listens, you can specify specific name of window, seperate them by comma.

   -  **\*** - Any query/channel window
   -  **?** - Any query windows
   -  **#** - Any channel window

-  **<commands>** - The commands to be performed when the event triggers

Examples
~~~~~~~~

.. code:: text

   ctcp *:test:?:ctcpreply $nick success

triggers when someone sends a private ctcp "test", which is a privmsg, and then use /ctcpreply, which sends a notice, this will trigger the ON CTCPREPLY event for that user.

.. code:: text

   ctcp *:version:?:ctcpreply $nick mIRC 12.5!!

would send a second reply to the standard ctcp version.