$regml
======

$regml returns the Nth backreference from a regex match.

If you use the /g modifier with an expression containing two backreferences and there are three matches, $regml(0) will return 6, it's a list of all backref accross all matches.

Synopsis
--------

.. code:: text

    $regml([name], N, [&binvar])

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
    * - &binvar
      - If you pass a binvar as the last parameter, the result is copied to that binvar and $regml() returns the length of the capture

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .pos
      - returns the starting position of the backrefence
    * - .bytepos
      - returns the UTF-8 byte positions matched within a string.
    * - .group
      - returns the () group number for a match
    * - .match
      - returns the match number in the case of a /g global match that returns multiple matches.

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

