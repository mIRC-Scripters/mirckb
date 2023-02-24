/bindip
=======

The **/bindip** command sets IP binding on or off. Additionally, an IP address or an adapter name to be used can be specified. When used without parameters mIRC indicates if it's on or off.

Synopsis
--------

.. code:: text

    /bindip [on [Ip|Adapter] | off]

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
    * - [on]
      - Sets IP binding on, if [Ip/Adapter] is given, it binds to that Ip/Adapter.
    * - [off]
      - Sets the IP binfing off.

Example
-------

.. code:: text

    ;Check if IP binding is on or off
    /bindip

    ;Turn binding on, set IP
    /bindip on 74.123.54.13

    ;Turn IP binding off
    /bindip off

The above example will output:

.. code:: text

    * Binding is off

    * Binding is on (74.123.54.13)

    * Binding is off

Compatibility
-------------


See also
--------

.. hlist::
    :columns: 4

    * :doc:`$bindip </identifiers/bindip>`
    * :doc:`$ip </identifiers/ip>`
    * :doc:`/dns <dns>`
    * :doc:`/server <server>`
    * :doc:`/sockaccept <sockaccept>`
    * :doc:`/sockopen <sockopen>`
