$server
=======

$server can be used to return the current server name if you don't provide any parameter, or informations about servers in your IRC server list if you provide one. You can use $server(-1) to get informations about the current connection without relying on the server list

Synopsis
--------

.. code:: text

    $server
    $server(N/address,[group])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N/address
      - references the Nth server or use the name you provided, if N = 0, returns total number of server. If N = -1, it identifies the current connection
    * - [group]
      - If you specify a group name, returns only servers for that group

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
If parameters are used, you can use the following properties:
    * - .desc
      - returns the description of that server (returns Random server if N = -1 and you're not connecting using the server list)
    * - .pass
      - returns the server password 
    * - .port
      - returns the port parameter (same as $port if you're not using the server list)
    * - .group
      - returns the group name (returns the $network value if N = -1 and you're not connecting using the server list)
    * - .method
      - returns the login method (used in conjunction with :doc:`/server -l </commands/server>`)
    * - .methodpass
      - returns the password associated with the login method
    * - .keytype
      - returns the type/mode of the SSL certificate, "global" or "local", depending on if you're using the global certificate or a specific certificate
    * - .key
      - returns the the private certificate filename for SSL
    * - .itype
      - returns the type/mode of the user informations, "global" or "local", depending on if you're using the global user infos (nick, email, ident etc) or specific infos per server (via /server -i or by editing the server list)
    * - .nick
      - return the nickname associated with the connection (editing server list or /server -i), return $null if you connect without the server list and without /server -i
    * - .anick
      - return the alternative nickname associated with the connection (editing server list or /server -i), return $null if you connect without the server list and without /server -i
    * - .email
      - return the email address associated with the connection (editing server list or /server -i), return $null if you connect without the server list and without /server -i
    * - .user
      - return the username associated with the connection (editing server list or /server -i), return $null if you connect without the server list and without /server -i
    * - .encoding
      - return the encoding's ID associated with the connection (editing server list or /server -i), return 0 if you connect without the server list and without /server -encoding

Examples
--------

Echo the active connection's server to the active window'''

.. code:: text

    //echo -a $server

Echo the number of Dalnet servers in the server list to the active window'''

.. code:: text

    //echo -a $server(0,Dalnet)

Echo the domain name of the first server in the Dalnet group in the server list to the active window'''

.. code:: text

    //echo -a $server(1,Dalnet)

Compatibility
-------------

.. compatibility:: 3.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/server </commands/server>`

