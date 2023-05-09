IPv6
====

This page has been written to describe how IPv6 support has been provided in mIRC v7 onwards and the quirks of the current implementation, and to provide guidance to scripters on how to code /dns and /sockopen commands so that they work reliably regardless of the IPv4/v6 connectivity of the local and remote systems and regardless of the IP version used by the current IRC connection.

This page is most relevant if your PC has both IPv4 and IPv6 connectivity to the internet as it describes issues related to the way mIRC handles domain lookups and consequent connections if you have connectivity using both IP versions.

It has been written both to provide non-technical users with the practical information that they need to fix issues when they experience them, and also to explain in the simplest way possible how mIRC works and why this sometimes creates unexpected issues. Unfortunately this does make the page lengthy and a little repetitive, and for this we apologise.

Background
----------

mIRC was first conceived in 1995, when the Internet was in its infancy and IP version 4 seemed like it would easily scale to cope with global usage. But that was before mobile phones became IP based and the Internet of Things joined the fray.

Eventually it became clear that IP version 4 would run out of addresses at some point, and a new IP version 6 Internet was launched in parallel. The IPv4 Internet and IPv6 Internet share a lot of concepts and technologies, but they are essentially separate networks, with end-points (users or servers) residing either on the IP v4 network **or** the IP v6 network **or** both. (There are some technologies that provide some co-existence functionality, but these are probably not relevant at this point.)

Versions of mIRC up to v6.x supported only IP v4. Version 7.0 in April 2010 introduced the first support for IPv6 and as IPv6 started to be supported by both IRC servers and IRC users, mIRC's IPv6 functionality was tweaked through to c. 2016 and is now considered to be mature and stable. There are, however, a few quirks with how mIRC handles coexistence between IPv4 and v6, and this page will attempt to explain them.

It should be recognised that mIRC's IPv6 support was implemented before there was widespread real-world usage of IPv6, and with the benefit of hindsight there are some areas in DNS name resolution where questionable decisions were made - the consequence is that mIRC (currently) has some implementation oddities that both scripters and some users need to be aware of.

This page has been written to explain how mIRC's support for IPv6 works, and what you need to know to make it work when the quirks would otherwise create difficulties.

DNS primer
----------

Firstly a quick reminder about the purpose of DNS - if you already understand this, please feel free to skip the rest of this section. 

Both IPv4 and v6 use numeric addresses to identify computers and how they are connected in order to route information between them - when we humans need to use these numeric addresses we represent them as 1.2.3.4 for IPv4 and 1234:5678:90AB:CDEF:1234:5678:90AB:CDEF for IPv6. Whilst these numeric addresses are great for computers to route packets, they are not so good for giving a computer a name or for identifying the services it provides, and of course the number used to route packets can change over time even if it is still the same computer you are trying to talk to. (In other words "I am a name not just a number".) 

The names given to computers on the Internet (like www.wikichip.org or irc.undernet.org) are called Domain Names or hostnames, and the service provided to convert Domain Names to IP addresses is called DNS. 

mIRC's quirks
-------------

Although mIRC can make IPv6 connections to explicitly specified IPv6 addresses out of the box without **any** mIRC configuration settings needing to be set, unfortunately this is **not** the same as mIRC fully supporting IPv6 without any configuration. Whilst you **can** connect using an explicit IPv6 address if you wanted to (presumably having looked it up yourself manually from a hostname), we almost always prefer to use hostnames and allow programs like mIRC to lookup the associated IP addresses.

mIRC does have a configuration setting for IPv6 - though it is not easy to find in mIRC's Options dialog, and even when you find it the description is not accurate. The configuration setting can be found at :menuselection:`Tools --> Options --> Connect --> Options --> Ports...` and is called "Enable IPv6 support and prioritize IPv6 over IPv4 connections" - but despite the description, this option is not needed to be set to "enable IPv6" and it only "prioritizes" IPv6 over IPv4 in some circumstances, whilst in other circumstances mIRC is effectively only supporting either IPv6 or IPv4 but not both. *If you have IPv6 connectivity to the Internet, you should read and understand this page before deciding to set or unset this configuration option.*

Another quirk in mIRC's implementation of IPv6 is that whilst it is capable of looking up both the IPv4 and IPv6 numeric addresses for a hostname, often by default (i.e. if you have both IPv4 and IPv6 internet addresses but are not explicit about wanting it to look up both IPv4 & IPv6 addresses) it limits the lookup to only one version. *If* the version that *isn't* queried then happens to be the *only* version that the other computer supports then mIRC will tell you that it is "* Unable to resolve server" and will *not* make the connection. 

Additionally whilst we would expect mIRC's IPv6 functionality to work consistently for the same commands or for connections to the same servers, unfortunately the IPv6 implementation can deliver different results not only depending on which IP version you are currently using to connect to IRC with, but indeed also based on what connections you may previously have made hours or even days ago in the same status window (so long as you haven't closed and reopened mIRC in the mean time). In other words, even though you may have made a connection successfully before, and even though the status window may look the same, for reasons that are not immediately obvious by looking at the screen, this time the connection doesn't work.

These are the gotchas that you need to be aware of! And in the remainder of this page we are going to attempt to provide you with an explanation of what is happening and how to avoid any difficulties.

mIRC's DNS lookups
------------------

As described above, for a domain name you can lookup either the IPv4 addresses or the IPv6 addresses or both types of address.

**mIRC decides which versions to query based on an internal state associated with the status window of the connection.**

A status window has 3 possible states regarding the version(s) of IP it uses for DNS lookups: 

* IPv4
* IPv6
* Both - IPv6/v4. 

mIRC will only lookup domain names on both IP versions **by default** when the status window state is IPv6/v4. 

When the status window state is either IPv4 or IPv6, it will only lookup IP addresses by default on that IP version and will not lookup IP addresses on the other IP version. If IP addresses for the host name only exist on the other IP version, you will get "Unable to resolve server" and, even though your computer is capable of connecting to the hostname using the other IP version, mIRC will not try that and your connection will not be made. 

Only when the internal state is IPv6/v4 will mIRC reliably make connections regardless of which IP version you are (or were previously) connected to IRC with, and which IP version the computer you are trying to connect to now is on.

The internal state of the status window is set as follows:

* When a new status window is opened, the IP version state is set to IPv4 if the mIRC option **Enable IPv6 support and prioritize IPv6 over IPv4 connections** is **not** enabled, and v6/v4 if it **is** enabled. (This setting can be found at Tools Options... (:menuselection:`Tools --> Options --> Connect --> Options --> Ports...`)
* Making a connection via a host name without specifying the IP version explicitly (i.e. you don't user /server -4 or -6 and don't specify an explicit IP address) does not change the status windows DNS lookup state.
* Making a connection using an explicit IP address or the -4 or -6 switches, changes the DNS lookup state to that IP version. 
* It is not possible to change the DNS lookup state for an existing status window back to v6/v4 once it has changed to v4 or v6. It can only be reset by opening a new status window.

Without knowing how the previous or current connections have been made, it is not possible for a human looking at the status window or for a script to know precisely which IP version state the status window is in (even if you can tell which IP version is currently being used to connect to to an IRC server), and it is therefore not possible to determine with absolute certainty how default DNS lookups (without switches) will behave.

IPv6/v4
^^^^^^^

This is the state a status window starts with if you have enabled the mIRC option for IPv6 priority. 

.. note:: If you use /server -m6 for example, you can still view it as a short ipv4 state and then ipv6, again you cannot go back to that state once you change from it.

In this state, mIRC will resolve a hostname to both IPv6 and IPv4 without explicitly telling mIRC to check both versions; IRC connections (e.g. using the connect button or /server), /sockopen and /dns without -4 and -6 switches will correctly work in all cases. In this state, this is equivalent to using these commands with the -64 switch.

If mIRC resolves a hostname to **both** IPv6 and IPv4 addresses, it will use the IPv6 address to try to make the IRC or socket connection - this is what is meant by "IPv6 Priority".

To stay in this state, you must always connect to IRC via a hostname, and never by using either /server -4 or -6 switches or an explicit IP address.

Scripts using /server, /dns or /sockopen which were written for mIRC v6 (i.e. before IPv6 support) generally continue to work in this state because calls to these commands are equivalent to having specified -64.

**Summary:** If your status window is IPv6/v4 state, then you should be able to connect to IPv4 and IPv6 hosts without any issues. But there is no easy way for a user or a script to determine when the IPv6/v4 state has been changed to IPv4 or IPv6, and then things may start to break.

IPv6
^^^^

This is the state you are in if you used /server -6 or used /server with an explicit IPv6 address.

In this state, mIRC does not resolve hostname to an IPv4 address without explicitly requesting mIRC to do so using a -4 switch. IPv4 using hostnames is effectively disabled for this status window.

If you want mIRC to resolve hostnames to IPv4 addresses and make connections over IPv4 for a status window that is IPv6, you need to use either an explicit IPv4 address or use a -4 switch on the command (i.e. /server -4, /dns -4, /sockopen -4).

Scripts using /server, /dns or /sockopen which were written for mIRC v6 (i.e. before IPv6 support) will not use -4 switches (because they didn't exist when the script was written) and consequently if they are run in a status window that is IPv6 they will fail to connect to an IRC or socket server that is IPv4 only - but the script would have worked if the status window was IPv4. For scripts to work reliably they need to code -46 on all /server, /dns and /socket calls.

**Summary:** If your status window is IPv6 state, then if you want to lookup or connect to an IPv4-only hostname, you need to explicitly code -4 on the /server, /dns or /sockopen command.

IPv4
^^^^

This is the state you are if you opened the status window with IPv6 priority not enabled or if you made a connection to an IRC server using either an explicit IPv4 address or used /server -4.

In this state, mIRC does not resolve hostname to an IPv6 address without explicitly requesting mIRC to do so using a -6 switch. IPv6 using hostnames is effectively disabled for this status window.

If you want mIRC to resolve hostnames to IPv6 addresses and make connections over IPv6 for a status window that is IPv4, you need to use either an explicit IPv6 address or use a -6 switch on the command (i.e. /server -6, /dns -6, /sockopen -6).

Scripts using /server, /dns or /sockopen which were written for mIRC v6 (i.e. before IPv6 support) will not use -6 switches (because they didn't exist when the script was written) and consequently if they are run in a status window that is IPv4 they will fail to connect to an IRC or socket server that is IPv6 only. At present almost all servers have IPv4 connections so this is not a frequent issue, but in the future when IPv4 addresses are exhausted and many more computers will be IPv6 only this may become a far more frequent problem.

**Summary:** If your status window is IPv4 state, then if you want to lookup or connect to an IPv6-only hostname, you need to explicitly code -6 on the /server, /dns or /sockopen command.

Some examples
-------------

The following examples are for users who have both IPv4 and IPv6 internet connectivity:

Manual server connection
^^^^^^^^^^^^^^^^^^^^^^^^

* User connects to irc.ipv4only.net using Options dialog - connects just fine using.
* User does /server -6 irc.ipv6.net - connects just fine.
* User tries to connect again to irc.ipv4only.net using Options dialog - connection fails - it worked only a few minutes earlier, now it doesn't - user is flummoxed.

This is true regardless of the "IPv6 priority" setting.

IPv6 priority not set
^^^^^^^^^^^^^^^^^^^^^

* User connects to irc.net by IPv4.
* Script to connect to www.ipv4only.com by IPv4 works just fine.
* For some reason user connects to irc.net by IPv6 (for whatever reason).
* Same script to connect to www.ipv4only.com by IPv4 breaks for no reason apparent to the user.

Additional SockOpen restriction
-------------------------------
When using /sockopen -d to bind to a specific network card IP address on your own PC (i.e. to make the socket connection originate from a specific IP address when you have several), mIRC will base its DNS resolution and subsequent connection on the IP version of the IP address you specify to bind to.

If you bind to an IPv6 address (e.g. /sockopen -d 1234:5678:90AB:CDEF:1234:5678:90AB:CDEF hostname), then mIRC will only do an IPv6 lookup on the hostname (because the bind address is IPv6 and so the connection has to be IPv6, so no point in looking up IPv4 addresses).

If you bind to an IPv4 address (e.g. /sockopen -d 1.2.3.4 hostname), then mIRC will only do an IPv4 lookup on the hostname (because the bind address is IPv4 and so the connection has to be IPv4, so no point in looking up IPv6 addresses). 

To prioritise or Not to prioritise? That is the question!
---------------------------------------------------------

Assuming that you have IPv6 connectivity of some sort on your PC, you are (or perhaps should be) worrying about whether you should set the IPv6 priority option or not.

As described above, setting IPv6 priority gives you the best chance of network connections succeeding (particularly if you ensure that you preserver the IPv6/v4 state of your status window), but it also means that your hostname-based connections will all be IPv6 where possible, and only IPv4 when an IPv6 address is not available for the hostname.

If your IPv6 internet connection is native, then it is likely that the performance of your IPv6 connections will be on a par with your IPv4 connections, and you are recommended to set IPv6 priority. There should be no real down-side to this - in the event that you switch your status window from IPv6/v4 to IPv6 or IPv4, the situation would be no different had you not set this option.

On the other hand, if your IPv6 internet connectivity is delivered using a gateway protocol like Teredo on your individual PC or 6to4 as part of your network infrastructure, then it is likely that your the performance of your IPv6 connections will be substantially slower than your IPv4 connections because the traffic from your PC to the server doesn't go via the shortest/quickest route but instead is sent via a gateway. In this situation, you are recommended **not** to set IPv6 priority, continue to connect via IPv4 and live with the occasions when connections to IPv6 are not made - which at present, whilst servers generally still all have IPv4 addresses, should be fairly rare. If you do set IPv6 priority in this situation, your IRC connections will default to IPv6 and be slower, but your ability to connect to both types of server is enhanced.

Recommendations for scripters
-----------------------------

To ensure that connections are made whenever they are possible, regardless of the IP version used by the status window's state, scripts should explicitly use the -46 switch on every /dns and /sockopen command in order to make a connection on the opposite IP version when needed. Scripts that have been written without this (e.g. written before IPv6 was implemented in mIRC) will not have backward compatibility and will not work reliably.

Including these switches will make your script work in all circumstances regardless of the IP state of the status window:

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - IPv6/v4 state 
      - there's no problem in this mode, you already DNS lookup on both IP versions, adding -46 won't change anything;
    * - IPv6 state
      - -6 is already implied, and the -4 will additionally ensure that IPv4 DNS lookups will also be done;
    * - IPv4 state
      - -4 is already implied, and the -6 will additionally ensure that IPv6 DNS lookups will also be done.


Impact of quirks in the future
------------------------------

At present, almost all users and servers have IPv4 connections. Users connecting via IPv4 will be able to make connections to almost all servers over IPv4. Users who have IPv6 connectivity and set IPv6 priority will still get IPv4 connectivity by default unless they have explicitly connected a status window to a specific version.

However with IPv4 addresses now officially exhausted, it will become increasingly likely that users and servers will be IPv6 only. Whilst IPv6 users can still set IPv6 priority and connect automatically to IPv4-only servers, IPv4-only users will NOT be able to connect to IPv6-only servers and will be forced to implement a gateway protocol like Teredo to get IPv6 connectivity for these situations. But as identified above, with the the current mIRC implementation it is **not** recommended to set IPv6 priority for gateway IPv6 which is substantially slower, and we can therefore reasonably expect the number of mIRC users experiencing connection difficulties of this form to increase substantially in the near future.

Potential mIRC enhancement
--------------------------

As the number of IPv6 connected mIRC users increases substantially over the next few years, this issue is likely to become more frequent. In particular as IPv4/v6 connected users still connecting to IRC primarily over v4 increasingly try to make connections to end points that are IPv6 only, this incompatibility for older scripts may become a much more significant issue. 

It would be nice if mIRC were to recognise this likelihood and make this change now despite the potential for occasional backward compatibility issues, and in the knowledge that this change would balance these backward compatibility issues with avoiding a potentially far greater level of backward compatibility issues from existing scripts failing.

The decision seems a little odd to limit mIRC's DNS lookups by default to the IP version state of the status window, rather than always to do DNS lookups for all versions that the user has Internet connectivity for - but this easy to say with the benefit of hindsight.

The question for mIRC is whether to:
* Retain the current implementation, preserving backwards compatibility with modern v7 scripts (if there are any) that have explicitly been written to expect that e.g. /dns or /socket calls will sometimes be limited to the IP version of the IRC connection (and sometimes won't) - but which breaks any existing scripts which use /server, /dns or /sockopen but which haven't explicitly been coded with -64 switches on any /server, /dns or /sockopen commands; OR
* Change mIRC's DNS lookup behaviour, preserving backwards compatibility with any existing scripts which use /server, /dns or /sockopen but which haven't explicitly been coded with -64 switches on any /server, /dns or /sockopen commands, but breaking backwards compatibility with modern v7 scripts (if there are any) that have explicitly been written to expect that e.g. /dns or /socket calls will sometimes be limited to the IP version of the IRC connection (and sometimes won't).

At present, with most servers having IPv4 connectivity, this does not cause widespread connectivity issues. However as more servers become IPv6 only due to exhaustion of IPv4 addresses, IPv4 only users will be pushed into using IPv6 transition technologies to get IPv6 connectivity, and we should then expect the number of occasions when scripts fail because of the quirky DNS implementation to increase substantially.

If the authors decide to change mIRC's behaviour, the recommended changes are as follows:

* Change the IPv6 Priority setting (and the description) to mean exactly that - for connections to hostnames with both IPv6 and IPv4 addresses, to use IPv6 rather than IPv4.
* Make /server, /dns and /socket commands without -4 or -6 work as if -46 or -64 had been specified.
* Make re-connections in the same window to the same server hostname as the last connection use the same IP version i.e. if you were previously connected by IPv6, then reconnect using IPv6.