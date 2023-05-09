$ignore
=======

$ignore returns the Nth address in the ignore list. 

Synopsis
--------

.. code:: text

    $ignore(N|address)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth address in the ignore list, if N = 0, returns the total number of ignored addresses.
    * - address
      - An address that is currently ignored, the first matching address is used.

.. note:: without a parameter, $ignore returns $true if ignore is on $false otherwise

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .type
      - returns the ignore flag for the ignored address
    * - .secs
      - returns the number of seconds until ignore is removed if /ignore -uN were used.
    * - .network
      - returns the network associated with the ignored address

Example
-------

.. code:: text

    //echo -a $ignore(0)

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ignore </commands/ignore>`

