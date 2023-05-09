$initopic
=========

.. attention:: This feature has essentially been replaced by :doc:`$ini </identifiers/ini>`

$initopic returns the name/Nth position of the specified topic in an ini/text file.

Synopsis
--------

.. code:: text

    $initopic(file,topic/N)

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

Properties
----------

None

Example
-------

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ini </identifiers/ini>`
    * :doc:`$readini </identifiers/readini>`

