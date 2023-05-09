On Dns
======

The ON DNS event triggers when a :doc:`$dns </commands/dns>` command query either succeeds or fails, including when a user does not exist on the server.

Synopsis
--------

.. code:: text

    ON <level>:DNS:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$dns </identifiers/dns>`
      - This identifier can be used to return all the address found.
    * - :doc:`$iaddress </identifiers/iaddress>`
      - Returns the ip address.
    * - :doc:`$naddress </identifiers/naddress>` 
      - Returns the host address.
    * - :doc:`$raddress </identifiers/raddress>`
      - Returns the resolved address.

Although these identifiers work now, it is strongly advised that migration to using the :doc:`$dns </identifiers/dns>` is made.

$nick
^^^^^

If :doc:`$dns </commands/dns>` was performed on a nickname rather than an address, then :doc:`$nick </identifiers/nick>` is filled with that nickname. Otherwise, :doc:`$nick </identifiers/nick>` is filled with your own name.

Examples
--------

Echo to the active window the results of the DNS:

.. code:: text

    ON *:DNS:echo -a $iif($1,$iif($dns(1).nick,$v1 has been resolved to) Hostmask: $dns(1).addr IP: $dns(1).ip,Could not resolve DNS query.)

The above example makes use of multiple :doc:`$iif </identifiers/iif>` to ensure that we get proper results, without unforeseen issues. The first surrounding :doc:`$iif </identifiers/iif>` checks to make sure any data has been returned. If no data is returned, then the :doc:`$dns </commands/dns>` obviously failed; therefore, we have it return a statement which says that a resolution could not be made. If data has been returned, the second :doc:`$iif </identifiers/iif>` checks to see if a .nick value can be extracted from the :doc:`$dns </identifiers/dns>`. This is filled if a nickname was the target of the :doc:`$dns </commands/dns>` request. If the nickname is filled, return the portion containing the nickname. If, however, the nickname is not present, only return the hostmask and ip address.

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dns </identifiers/dns>`

