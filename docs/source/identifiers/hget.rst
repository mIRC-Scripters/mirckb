$hget
=====

$hget returns informations about hash tables

Synopsis
--------

.. code:: text

    $hget(name/N) - returns the name if the hash table exist or Nth name
    $hget(name/N, item, [&binvar]) - returns the data associated with the item

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name/N
      - the Nth hash table or the name of it
    * - item
      - the name of the item you want the data of
    * - &binvar
      - if you provide a binvar as a third parameter, the associated data is copied at the beginning of the binvar and the binvar is chopped at length of the associated data (what was before in the binvar is 'deleted' before copying)

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .unset
      - When passing an item, you can use the .unset property to get the unset time of the item if any
    * - .state
      - Return some internal informations about the table. The format returned is 3 tokens space separated, the first word is the number of items in the table, the second is in the format <nbr_used_buckets>/<totalnbr_buckets>, while the third consists of four number separated by a slash as well, but it's unknown what they really mean.
    * - .hash
      - Return the name of the algorithm used by the hash table, which can be passed using the -h switch in :doc:`/hmake </commands/hmake>`
    * - .data
      - returns the contents of the hash table item.

Example
-------

.. code:: text

    //hadd -m test test test | echo -a $hget(test,test) | hfree test

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake </commands/hmake>`
    * :doc:`/hadd </commands/hadd>`
    * :doc:`/hload </commands/hload>`
    * :doc:`/hfree </commands/hfree>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`/hinc </commands/hinc>`
    * :doc:`$hfind </identifiers/hfind>`

