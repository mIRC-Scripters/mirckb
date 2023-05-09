$findtokcs
==========

$findtokcs returns the position of the Nth matching token in text using case sensitivity.

Synopsis
--------

.. code:: text

    $findtokcs(<list>,token,N,C)

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

    $findtokcs(one two three twO, twO, 32) return 4

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
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

