$dns
====

The $dns identifier becomes filled and has the ability for reference whenever an :doc:`on dns </events/on_dns>` event occurs.

Synopsis
--------

.. code:: text

    $dns(N)[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Used to reference the resolved address, or total number of addresses

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - addr
      - Return the resolved hostmask address
    * - ip
      - Return the IP Address
    * - nick
      - Return the nicknames used when :doc:`/dns </commands/dns>`'ing on a nickname

Example
-------

Echo to the active window the results of the DNS:

.. code:: text

    ON *:DNS:echo -a $iif($1,$iif($dns(1).nick,$v1 has been resolved to) Hostmask: $dns(1).addr IP: $dns(1).ip,Could not resolve DNS query.)

The above example makes use of multiple :doc:`$iif identifiers </identifiers/iif>` - to ensure that we get proper results, without unforeseen issues. The first surrounding $iif identifier checks to make sure any data has been returned. If no data is returned, then the :doc:`/dns command </commands/dns>` obviously failed; therefore, we have it return a statement which says that a resolution could not be made. If data has been returned, the second $iif identifier checks to see if a .nick value can be extracted from the :doc:`$dns identifier </identifiers/dns>`. This is filled if a nickname was the target of the DNS request. If the nickname is filled, return the portion containing the nickname. If, however, the nickname is not present, present only the hostmask and IP address.

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on dns </events/on_dns>`