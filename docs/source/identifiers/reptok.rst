$reptok
=======

$reptok replaces the Nth matching token in text with a new token. If N = 0, applies to all matching items. $reptokcs is a case sensitive version

Synopsis
--------

.. code:: text

    $reptok(<list>,token,new,N,C)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <list>
      - The list of tokens (can be empty)
    * - token
      - the token used to match
    * - new
      - the token used to replace the matching token.
    * - N
      - The Nth matching token, default to 1, if N is 0, applies to all matching tokens.
    * - <C>
      - The ascii number (or code point) of the character seperating the tokens

Properties
----------

None

Example
-------

.. code:: text

    $reptok(one two three, two, four, 32) returns one four three

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptokcs </identifiers/reptokcs>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

