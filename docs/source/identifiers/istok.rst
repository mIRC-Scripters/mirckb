$istok
======

$istok returns $true if a matching token exists, or $false if it does not.

Synopsis
--------

.. code:: text

    $istok(<LIST>,<Token>,<C>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - LIST:
      - Text list delimited by a character into tokens
    * - Token: 
      - The token searched for in LIST
    * - C: 
      - The :doc:`$asc </identifiers/asc>` value which splits TEXT into tokens

The search is for entire token, not partials, and the search is NOT case-sensitive. If you need the token search to be case-sensitive, use :doc:`$istokcs </identifiers/istokcs>` which has the same syntax}}

Properties
----------

None

Examples
--------

.. code:: text

    //if ($event isin DISCONNECT JOIN) goto LABEL

If this alias is executed in the :doc:`on connect </events/on_connect>` and :doc:`on disconnect </events/on_disconnect>` events, this triggers on BOTH events because isin matches on CONNECT being a substring of DISCONNECT. Better is:

.. code:: text

    //if ($istok(CONNECT JOIN,$event,32)) goto LABEL
    ; searches for exact match of the value of the $event string against the tokens in the space-delimited list of tokens.

.. code:: text

    //var %filename spreadsheet.xls | var %filetype $gettok($noqt(%filename),-1,46) | echo -a %filetype $istok(xlsx xlsm,%filetype,32)
    ; returns false because $istok does not match the substring xls against the token xlsx

.. code:: text

    //echo -a $asctime($ctime,dddd) $istok(SUNDAY MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY,$asctime($ctime,dddd),32)
    ; returns $true because match is case-insensitive

Compatibility
-------------

.. compatibility:: 5.5

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

