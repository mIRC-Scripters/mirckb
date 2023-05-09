$left
=====

$left is a :doc:`string manipulation </beginner/string_and_token_manipulation>` identifier used to return characters from the left side of a string.

Synopsis
--------

.. code:: text

    $left(<string>, <length>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <string>
      - The string to manipulate
    * - <length>
      - The length or number of characters to remove from the original string. <length> can be a positive or negative. Using 0 returns $null (0 characters).

If the length provided is positive, $left will return the <length> characters from the left of the string.

.. code:: text

    $left(abcdefg, 4)
    ; abcd

If the length provided is negative, $left will return the string except the rightmost <length> characters.

.. code:: text

    $left(abcdefg, -2)
    ; abcde

More Examples
-------------

.. code:: text

    $left(appleseed, -4)
    ; apple

.. code:: text

    $left([AB]BotName, 4)
    ; [AB]

See also
--------

.. hlist::
    :columns: 4

    * :doc:`string manipulation </beginner/string_and_token_manipulation>`
    * :doc:`$right </identifiers/right>`
    * :doc:`$mid </identifiers/mid>`
    * :doc:`$pos </identifiers/pos>`

