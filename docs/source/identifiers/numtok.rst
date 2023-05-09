$numtok
=======

$numtok returns the number of $asc(C)-delimited token in a list.

Synopsis
--------

.. code:: text

    $numtok(<LIST>,<C>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
LIST: - Text list delimited by a character into tokens
C: - The :doc:`$asc </identifiers/asc>` value which splits LIST into tokens

Properties
----------

None

Examples
--------

Echo to the active window, the number of tokens delimited by the $chr(45) hyphen:

.. code:: text

    //echo -a $numtok(a-b-c-d-e,45)
    ; returns 5

.. code:: text

    //echo -a $numtok(1x2x3x4,120)
    ; returns 4 because $chr(120) is lower-case x
    //echo -a $numtok(x1xxxx2x3x4x,120)
    ; also returns 4 because duplicate, leading, and trailing delimiters are stripped before $numtok processes the LIST
    //echo -a $numtok(1x2X3x4,120)
    ; returns 3 because the C token is case-sensitive, so capital X isn't a delimiter

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

