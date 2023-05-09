$regmlex
========

$regmlex returns the Mth backreference of the Nth match from a regex match.

Synopsis
--------

.. code:: text

    $regmlex([name], N, M, [&binvar])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The optional name given to the regex match
    * - M
      - The Mth match, if M = 0, returns the total number of match
    * - N
      - Optional, the Nth capturing group, default to 1
    * - &binvar
      - If the last parameter is a binvar, the result is copied to the binvar and $regmlex() returns the length of the result.

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

    * :doc:`$regex </identifiers/regex>`
    * :doc:`$regsubex </identifiers/regsubex>`
    * :doc:`$regmlex </identifiers/regmlex>`

