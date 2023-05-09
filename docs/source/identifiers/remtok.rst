$remtok
=======

$remtok removes the Nth matching token in text. $remtokcs is a case sensitive equivalent.

Synopsis
--------

.. code:: text

    $remtok(<list>,token,N,C)

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

    $remtok(one two three, two, 32) returns one three

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$remtokcs </identifiers/remtokcs>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

