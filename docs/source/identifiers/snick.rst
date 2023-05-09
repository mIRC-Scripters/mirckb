$snick
======

$snick returns the Nth selected nickname on the specified channel

Synopsis
--------

.. code:: text

    $snick(#chan,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #chan
      - The channel name you want to know the selected nickname from
    * - N
      - The Nth selected nickname on that channel.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $snick(0)

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$snicks </identifiers/snicks>`

