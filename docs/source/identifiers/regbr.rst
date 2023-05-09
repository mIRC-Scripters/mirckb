$regbr
======

.. attention:: This feature has essentially been replaced by :doc:`$regml </identifiers/regml>`

$regbr used to return the Nth backreference from a regex match.

Synopsis
--------

.. code:: text

    $regbr([name], N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The optional name given to the regex match
    * - N
      - The Nth backreference, if N is 0, returns the total number of backreference/capturing group

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .pos
      - returns the starting position of the backrefence

Example
-------

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$regml </identifiers/regml>`
    * :doc:`$regex </identifiers/regex>`
    * :doc:`$regsubex </identifiers/regsubex>`
    * :doc:`$regmlex </identifiers/regmlex>`

