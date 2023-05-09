$longip
=======

$longip converts an IP address into a long value and vice-versa

Synopsis
--------

.. code:: text

    $longip(ip)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - ip
      - The ip address to convert, if you pass a long value, it will return the ip address back

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $longip(158.152.50.239) -- $longip(2660774639) 

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$iptype </identifiers/iptype>`

