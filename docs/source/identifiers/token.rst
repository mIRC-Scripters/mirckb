$gettok
=======

.. attention:: This feature has essentially been replaced by :doc:`$gettok </identifiers/gettok>`

$token returns the Nth $asc(C)-delimited token from a list.

Synopsis
--------

.. code:: text

    $token(<LIST>,<N>,<C>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - LIST:
      - Text list delimited by a character into tokens
    * - N:
      - The token(s) to be returned. N can also be negative or a range
    * - C:
      - The :doc:`$asc </identifiers/asc>` value which splits TEXT into tokens

If N=0, returns total number of tokens, same as :doc:`$numtok </identifiers/numtok>` 
If N is greater than the total number of tokens, returns :doc:`$null </identifiers/null>` 
If N is negative, returns tokens relative to the last token. -1 is the last token, -2 is next-to-last token, etc.
N- returns all tokens beginning with the Nth token.
N1-N2 returns all tokens in the range of those 2 numbers, including the between delimiters.

.. note:: You can reverse the order of the number: $token(a b c,3-2,32) is the same as $token(a b c,2-3,32)

.. note:: N2 can also be negative: $token(a b c d e f,-2-3,32) return the token from the 3rd token to the -2th but $token(a b c d e f,-2--3,32) return e f, from -3 to -2

.. note:: For readability you can also code this as $token(a-b-c-d-e,2,$asc(-)).

Properties
----------

None

Examples
--------

Echo to the active window, the 2nd token as delimited by the $chr(45) hyphen:

.. code:: text

    //echo -a $token(a-b-c-d-e,2,45)
    ; returns b

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

