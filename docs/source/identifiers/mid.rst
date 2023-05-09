$mid
====

$mid is a :doc:`string manipulation </beginner/string_and_token_manipulation>` identifier used to return a sub-string portion of a string.

Synopsis
--------

.. code:: text

    $mid(<text> ,S [, N ] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - String from which to return a portion
    * - S
      - Position within Text. If S is negative, position is relative to the end of Text instead of the beginning. Using Zero behaves same as position 1.
    * - N
      - Optional Length. If Length parameter not used, returns entire remainder of the string. If N is zero, returns the numeric length of the string. If N is negative, returns the string beginning at position S except for the LAST $Abs(N) characters.

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $mid(abcdefghij,2,3)
    returns 3 characters beginning at position 2

.. code:: text

    //echo -a $mid(abcdefghij,2)
    //echo -a $mid(abcdefghij,2,9999)
    both return ALL characters beginning at position 2. Omitting N avoids the need to use N as a too-large number like 9999

.. code:: text

    //echo -a $mid(abcdefghij,-6,2)
    returns 2 characters beginning at position 6th from the end. Is equivalent to:
    //echo -a $left($right(abcdefghij,6) ,2)

.. code:: text

    //echo -a $mid(abcdefghij,-6)
    returns ALL characters beginning at position 6th from the end.

.. code:: text

    //echo -a $mid(abcdefghij,3,-2)
    returns ALL characters beginning at position 3 EXCEPT for the last 2 characters.

.. code:: text

    //echo -a $mid(abcdefghij,3,0)
    returns the length of the string beginning at position 3.

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`string manipulation </beginner/string_and_token_manipulation>`
    * :doc:`$left </identifiers/left>`
    * :doc:`$right </identifiers/right>`
    * :doc:`$pos </identifiers/pos>`
    * :doc:`$str </identifiers/str>`
