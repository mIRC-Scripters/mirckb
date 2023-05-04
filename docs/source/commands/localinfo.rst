/localinfo
==========

The **/localinfo** command looks up and sets your Local settings.

Synopsis
--------

.. code:: text

    /localinfo -uhp [host] [ip]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -u
      - performs a /userhost lookup (use the server you are connected to)
    * - -h
      - performs a normal lookup
    * - -p
      - performs a UPnP lookup through your router, if available, depending on the router, might freeze mIRC for a short period

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [host]
      - if specified, set the host with that value
    * - [ip]
      - if specified, set the ip with that value

Example
-------

Compatibility
-------------

Added: mIRC v5.81 (09 Nov 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$ip </identifiers/$ip>`
    * :doc: `$host </identifiers/$host>`
