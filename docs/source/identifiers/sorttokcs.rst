$sorttokcs
==========

$sorttokcs sorts the token in text using case sensitivity.

Synopsis
--------

.. code:: text

    $sorttokcs(<list>, <C> [,nrca] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <list>
      - The list of tokens (can be empty)
    * - <C>
      - The ascii number (or code point) of the character seperating the tokens
    * - ncra
      - default is alphabetical sort (ASCII sort) if 3rd parameter not used, n = numeric sort; c = channel prefix sort; r = reverse; a = alphanumeric (ASCII) sort

.. note:: See $sorttok for case-insensitive sort

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $sorttokcs(C a c b A B,32)

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sorttok </identifiers/sorttok>`
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
    * :doc:`$wildtok </identifiers/wildtok>`

