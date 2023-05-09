$iptype
=======

$iptype returns "ipv4" or "ipv6" if the parameter is a valid IP address format.

Synopsis
--------

.. code:: text

    $iptype(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The string you want to know the ip type of

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
If an ipv6 is given, you can use the following properties:
    * - .compress
      - returns the compressed version of the ip address
    * - .expand
      - returns the expanded version of the ip address

Example
-------

.. code:: text

    //echo -a $iptype(5.6.7.8)

Compatibility
-------------

.. compatibility:: 7.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ip </identifiers/ip>`

