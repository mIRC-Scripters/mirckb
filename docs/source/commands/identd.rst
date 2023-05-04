/identd
=======

The **/identd** command can be used to enable or disable your Identd server in mIRC. Enabling the Identd server greatly increases the speed with which you connect to most modern IRC servers, in that the information the server requests, in order to identify your connection, is more readily available.

What Is Identd?
---------------

Identd is enabled as a server in order for mIRC to send your required Ident/Identification, which is part of the connection initiation to a lot of IRC servers. The server then checks to see whether you have an Identd running and uses the Ident (*UserID+System*) reported by that in your hostmask. If the server does not find Identd running on your machine, it adds the tilde (~) to your Ident.

Hostmask? Tilde (~)?
^^^^^^^^^^^^^^^^^^^^

The hostmask is combined with the information you see when you */whois* someone on an IRC server. It looks like the sample below:

 hostmaskhere@somewhere.com

If Identd is not enabled on your client, or the client you try to */whois*, then the hostmask has a preceding tilde (**~**) attached to it, much like the sample below:

 ~hostmaskhere@somewhere.com

Synopsis
--------

.. code:: text

    The basic break-down of how to use the */Identd* command is shown below:

.. code:: text

         /identd [on/off] [userid]

Switches
--------

None

Parameters
----------

: **ON**

:: *Enables the Identd server.*

: **OFF**

:: *Disables the Identd server.*

: **userid**

:: *This will be the UserID you want to use for your IRC connections, and it can be any alphanumeric character sets, eg: 0-9, A-Z & a-z. Most servers have a 10-character limit set for the maximum length of your custom UserID.*

.. note:: If no parameter is specified, mIRC will simply echo to the main screen the status of your Identd, such as: ** Identd is on (IdentdUserIDHere).*

Examples
--------

**Enable Identd**

.. code:: text

    /identd on

**Enable Identd With Custom UserID**

.. code:: text

    /identd on CustomUser

[[File:Identdscreen2.jpg|/identd example]]

**Disable Identd**

.. code:: text

    /identd off

Compatibility
-------------

Added: mIRC v3.3 - 3.4 ()

See also
--------
