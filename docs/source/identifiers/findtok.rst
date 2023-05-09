$findtok
========

$findtok returns the position of the Nth matching token in text. $findtokcs is a case sensitive equivalent.

Synopsis
--------

.. code:: text

    $findtok(<list>,token,N,C)

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
      - The Nth matching token, default to 1, if N is 0, returns the total number of matching tokens.
    * - <C>
      - The ascii number (or code point) of the character seperating the tokens

Properties
----------

None

Example
-------

.. code:: text

    $findtok(one two three, two, 32) return 2

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$findtokcs </identifiers/findtokcs>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

