/server
=======

The **/server** command can be used to initiate a new server connection. Using /server with no parameters will connect to the last server you used. If you use the server command while still connected, you will be disconnected with your normal quit message and will then connect to the specified server. It can also be used to manage the mIRC servers list

Synopsis
--------

.. code:: text

    /server -sar [server] [-p port] [-g group] [-w password] [-d description] [-l method password]
    /server [-46demnpfocztu] <server/groupname/N> [port] [password] [-l method password] [-key file] [-i nick anick email name] [-jn #channel pass]

Switches
--------

If any of the -sar switches are used:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - sorts the servers list
    * - -a
      - adds a server to the server list, if it exists, it is updated: mIRC tries to find a match for either the server address or the description in the existing servers list
    * - -r
      - removes a server from the server list
    * - -g
      - changes the group
    * - -w
      - changes the server password
    * - -d
      - changes the description

Otherwise:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -4
      - allows a connection to an IPv4 server
    * - -6
      - allows a connection to an IPv6 server
    * - -d
      - allows setting the current status window's connection details without connecting
    * - -e
      - initiates a secure connection to an SSL capable server, alternatively you can prefix the port number with a plus sign
    * - -m
      - creates a new server window for that connection and connects to the server
    * - -n
      - creates a new server window for that connection but does not connect to the server
    * - -p
      - prevents the perform from being applied
    * - -f
      - prevents the favorites folder from poping up
    * - -o
      - prevents the autojoining of channels from being applied
    * - -c
      - prevents the on connect from being triggered
    * - -z
      - minimizes the new server window
    * - -t
      - initiates a secure connection to a STARTTLS capable server
    * - -u
      - prevent the STS secure connection feature from IRCv3 to be used

Parameters
----------

if any of the -sar switches are used:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [server]
      - if specified, mIRC use that information to match for existing server entry
    * - [-p port]
      - specified the port number to be used, you can put different ports by seperating them with commas, prefix the port with a **+** for **SSL**, and prefix it with ***** for a STARTTLS capable server
    * - [-g group]
      - specifies the group for the server, if the value is 'none', it clears the setting
    * - [-w pass]
      - specifies the password for the server, if the value is 'none', it clears the setting
    * - [-d desc]
      - specifies the description for the server, if the value is 'none', it clears the setting
    * - [-l method password]
      - changes the login method and the password field corresponding to the login method (even if the given method won't be using that corresponding password field, if you use "pass" for example). See below for more information about the **-l** method parameter

Otherwise:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <server/groupname/N>
      - either a server address, or if you give a groupname, it will cycle through all the servers in the server list which have that group name until it connects to one of them, if you give a number, mIRC will try to connect to the Nth server in the server list in the connect dialog
    * - [port]
      - if specified, the port number, you can put different ports by seperating them with commas, prefix the port with a + for SSL, and prefix it with * for a STARTTLS capable server
    * - [password]
      - if specified, the password of the server, if any.
    * - [-i [nick [anick [email [name]]]]]
      - if specified, tells mIRC the different parameters to be used for the USER login sequence, parameters are in order and can't be ommited unless they are last: you cannot specify [anick] without specifying [nick] (see examples)
    * - [-jn <#channels> [passwords]]
      - if -j is specified, it will join the channels, if -n is specified, it will join them minimized. The [passwords] syntax depends on the IRC server you are using, it will simply use '/join <#channel> [passwords]', but typically, it's a comma seperated list of password where * can be used to specify that no password should be used for that channel.
    * - [-key file]
      - specify the private key file to use for SSL
    * - [-l method password]
      - specify the method to be used to identify to nickserv/service, **method** can be:

** <code>pass</code> - using this method means that the **[password]** parameter (the server password) is what contains your nickname's password (default if you don't use -l, typically IRC server will try to identify you to service such as nickserv using your current nickname and the server password provided)

** <code>sasl</code> - using this method means that mIRC will use SASL to identify you. The next parameter can be:

*** **nick:password** - nick is the registered nick/account and password is the password for that account (this indeed means that you can connect to IRC server with a nickname that is different from the nickserv nickname/account and still be logged to that account)

*** **password** - a password only, mIRC will use your current nickname to auth you

*** mIRC will first interpret this parameter as nick:pass if a ':' is present and only if that fails it will try that value as a password only, using your current nickname to auth.

** <code>external</code> - This method uses a TLS certificate and have services recognize it automatically. You must connect over SSL.

** <code>msg</code> - This method means that mIRC will use '/msg nickserv identify' once the raw 001 is received. You must specify your password (without a nickname/account of the form nick:pass, just the password) after the method

** <code>nickserv</code> - This method means that mIRC will use '/nickserv identify' once the raw 001 is received. You must specify your password (without a nickname/account of the form nick:pass, just the password) after the method

Example
-------

.. code:: text

    ;Specify the [nick] and [anick]
    /server irc.someirc.com -i nick anick
    ;Impossible: specifying the [email] without specifying [nick] and [anick] first
    /server irc.someirc.com -i * * emailtouse

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$server </identifiers/$server>`
