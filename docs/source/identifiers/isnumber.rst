$isnumber
=========

$isnumber Returns $true if text is a number, otherwise returns $false.

.. note:: switches affects the range number parameters, see the examples

Synopsis
--------

.. code:: text

    $isnumber(text,[sd],[I,J])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The input string to be checked
    * - s
      - also permits +- sign to be used
    * - d
      - also permits the decimal, allowing numbers with fractions
    * - [I,J]
      - If you pass a third and fourth parameters, they must be valid number (with respect to the switches used) and are used to validate the number in a range.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $isnumber(564)

will return $true

.. code:: text

    //echo -a $isnumber(abcdefG)

will return $false because not all the characters are digits

.. code:: text

    //var %a -123 | echo -a $isnumber(%a) vs $isnumber(%a,s)

result: $false vs $true (using a sign requires 's')

.. code:: text

    //echo -a $isnumber(3,d,2.1,4) vs $isnumber(3,,2.1,4)

result: $false vs error, the d switches is required not only to allow decimal in the input, but in each range parameter as well

Compatibility
-------------

.. compatibility:: 7.58

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$calc </identifiers/calc>`
    * :doc:`$isnum </identifiers/isnum>`
