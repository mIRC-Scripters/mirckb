$puttok
=======

$puttok replaces the Nth $asc(C)-delimited token in a list.

Synopsis
--------

.. code:: text

    $puttok(<LIST>,<Token Data>,<N>,<C>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
LIST: - Text list delimited by a character into tokens
Token Data: - Replacement text which overwrites the existing Nth token
N: - The token number to be overwritten
C: - The :doc:`$asc </identifiers/asc>` value which splits TEXT into tokens

If N is negative, returns tokens relative to the last token. -1 is the last token, -2 is next-to-last token, etc.

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $puttok(a-b-c-d-e-f,TEST,3,46))
    ; returns a-b-TEST-d-e-f

Shows the unchanged path with the filename changed to TEST.TXT:

.. code:: text

    //echo -a $puttok($mircexe,TEST.TXT,-1,92))

.. code:: text

    //echo -a $puttok(x11xx33X44x55x66x,TEST,3,120)
    ; returns 11x33X44xTESTx66
    ; because leading/trailing/duplicate delimiters are removed before evaluating <LIST>. $chr(120) is lower-case x so the capital X is not a delimiter.

.. note:: Unlike CSV format, if C=44 to delimit with commas, double-quotes around filename containing a comma does not allow the entire filename to be a single token. If you want $filename to be a token in a comma-delimited list of tokens, you should use :doc:`$replace </identifiers/replace>` to change the comma in the filename into another character that cannot appear in the filename before adding as a token, then use :doc:`$replace </identifiers/replace>` on the extracted token to restore any comma(s).

Compatibility
-------------

.. compatibility:: 5.3

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
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

