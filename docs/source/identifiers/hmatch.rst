$hmatch
=======

.. attention:: This feature has essentially been replaced by :doc:`$hfind </identifiers/hfind>`

$hmatch Searches an hash table for the Nth item name which matches the :ref:`matching_tools-wildcard` text. Returns item name.

Synopsis
--------

.. code:: text

    $hmatch(name/N, wildtext, N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name/N
      - the Nth hash table or the name of it
    * - text
      - the :ref:`matching_tools-wildcard` expression to use to find a match
    * - N
      - The Nth match, use 0 to get the total number of match

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .data
      - instead of looking for matches against item, matches against data, but the item name is still returned.

Example
-------

Compatibility
-------------

.. compatibility:: 5.81

see also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake </commands/hmake>`
    * :doc:`/hadd </commands/hadd>`
    * :doc:`/hload </commands/hload>`
    * :doc:`/hfree </commands/hfree>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`/hinc </commands/hinc>`
    * :doc:`$hget </identifiers/hget>`

