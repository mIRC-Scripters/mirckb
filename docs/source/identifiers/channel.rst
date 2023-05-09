$channel
========

.. attention:: This feature has essentially been replaced by :doc:`$chan </identifiers/chan>`

$channel returns informations about channels.

Synopsis
--------

.. code:: text

    $channel(N/#)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N/#
      - The channel or the Nth channel.
:: if N is 0, returns the total numbers of channels

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
See :doc:`$chan </identifiers/chan>` for more informations.

Example
-------

.. code:: text

    //echo -a $channel(3).mode

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chan </identifiers/chan>`
    * :doc:`$query </identifiers/query>`
    * :doc:`$window </identifiers/window>`
