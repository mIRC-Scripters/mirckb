/firewall
=========

The /firewall command changes the firewall settings.

Synopsis
--------

.. code:: text

    /firewall [on|off]
    /firewall [-cmN[+|-]d] <server> <port> <userid> <password>
    /firewall [-cmN[+|-]d] <server:port> <userid> <password>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - clears the userid and password values
    * - -mN
      - sets the connection type, where N is 4 or 5 for Socks4 or Socks5, or p for proxy
    * - +d
      - turns dccs through a firewall on.
    * - -d
      - turns dccs through a firewall off.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <server>
      - the server
    * - <port>
      - the port
    * - <userid>
      - the username
    * - <password>
      - the password

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/proxy </commands/proxy>`

