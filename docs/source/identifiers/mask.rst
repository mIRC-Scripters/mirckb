$mask
=====

$mask returns the address with a mask of the specified type.

Synopsis
--------

.. code:: text

    $mask(address,type)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - address
      - The address you want the mask of.
    * - type
      - The type of address, a positive integer between 1-19

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Type
      - Address Mask
    * - 0
      - \*!user@host
    * - 1
      - \*!\*user@host
    * - 2
      - \*!\*@host
    * - 3
      - \*!\*user@\*.host
    * - 4
      - \*!\*@\*.host
    * - 5
      - nick!user@host
    * - 6
      - nick!\*user@host
    * - 7
      - nick!\*@host
    * - 8
      - nick!\*user@\*.host
    * - 9
      - nick!\*@\*.host

Type 10-19 are same as types 0-9 except asterisks in host are expanded to the text they replaced, then all numbers are replaced by question marks.

Masks are case-insensitive and assigned by the internet provider, but IRC servers often provide user mode +x to help disguise them.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $mask(nick!user@host,7)

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$address </identifiers/address>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$fulladdress </identifiers/fulladdress>`
    * :doc:`$site </identifiers/site>`
    * :doc:`$wildsite </identifiers/wildsite>`

