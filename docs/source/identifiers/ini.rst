$ini
====

$ini returns the name/Nth position of the specified topic/item in an ini/text file.

Synopsis
--------

.. code:: text

    $ini(file,topic/N,item/N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - file
      - the filename you want name/position from
    * - topic/N
      - The Nth topic or a topic name, use N = 0 for the total number of topics
    * - item/N
      - the Nth item or an item name, use N = 0 for the total number of items for that topic

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $ini($mircini,0)

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$initopic </identifiers/initopic>`
    * :doc:`$readini </identifiers/readini>`

