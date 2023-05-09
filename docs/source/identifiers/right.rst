$right
======

$right is a :doc:`string manipulation </beginner/string_and_token_manipulation>` identifier used to return characters from the right side of a string.

Synopsis
--------

.. code:: text

    $right(<string>, <length>)

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
      - The length or number of characters to remove from the original string. <length> can be a positive or negative. It cannot be 0.

If the length provided is positive, $right will return the <length> characters from the right of the string.

.. code:: text

    $right(abcdefg, 4)
    ; defg

If the length provided is negative, $right will return the characters in the string minus <length> on the left.

.. code:: text

    $right(abcdefg, -2)
    ; cdefg

More Examples
-------------

.. code:: text

    $right(appleseed, -4)
    ; eseed

.. code:: text

    $right([AB]BotName, 4)
    ; Name

See also
--------

.. hlist::
    :columns: 4

    * :doc:`string manipulation </beginner/string_and_token_manipulation>`
    * :doc:`$left </identifiers/left>`
    * :doc:`$mid </identifiers/mid>`

