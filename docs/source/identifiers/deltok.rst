$deltok
=======

$deltok deletes the Nth token from text.

Synopsis
--------

.. code:: text

    $deltok(list,N-N2,C)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <list>
      - The list of tokens (can be empty)
    * - <N-N2>
      - The Nth to delete, if you pass $null here, the original list is returned, it doesn't return an error. N can be negative, so can N2. -1--2 means from the last token to the second last token.
    * - <C>
      - The ascii number (or code point) of the character seperating the tokens

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $deltok(a b,1,32)

Would display "b"

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtokcs </identifiers/addtokcs>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$wildtok </identifiers/wildtok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`

