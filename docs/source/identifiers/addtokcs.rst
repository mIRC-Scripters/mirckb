$addtokcs
=========

$addtokcs adds a token to a list of token, only if the token does not already exist in the list, return the resulting list. $addtokcs is case sensitive.

Synopsis
--------

.. code:: text

    $addtokcs(<list>,<token>,<C>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <list>
      - The list of tokens (can be empty)
    * - <token>
      - The token to add, if you pass $null here, the original list is returned, it doesn't return an error.
    * - <C>
      - The ascii number (or code point) of the character seperating the tokens

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $addtokcs(A,a,32)

Would display "A a", $addtok would have returned "A".

Compatibility
-------------

.. compatibility:: 5.91

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$wildtok </identifiers/wildtok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`

