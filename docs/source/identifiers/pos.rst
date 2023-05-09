$pos
====

$pos returns the case-insensitive position of the Nth substring within a text string. $poscs is the case-sensitive version.

Synopsis
--------

.. code:: text

    $pos(text,substring [,N] )
    $poscs(text,substring [,N] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The string being searched
    * - substring
      - The string being searched for within text string
    * - N
      - The Nth occurrence of substring being searched for. Default is 1 if parameter not used, you can use N=0 to return the count of string's occurrences.

Switches
--------

None

Examples
--------

.. code:: text

    //echo -a $pos(DEADBEEF,E)
    returns: 2 (search is case-insensitive) (Default N=1 when 3rd parameter isn't used)
    //echo -a $pos(DEADBEEF,e,2)
    returns: 6
    //echo -a $pos(DEADBEEF,e,0)
    returns: 3 (count of letter 'e')
    //echo -a $pos(deadbeef,db,1)
    returns: 4
    //echo -a $pos(DEADBEEF,x,0)
    returns: $null (not found)
    //var %a a $chr(32) b | echo -a The string has length $len(%a) and contains $pos(%a,$chr(32),0) spaces
    //echo -a The path-less filename is $mid($mircexe, $calc(1+$pos($mircexe,\, $count($mircexe,\) ) ) )

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mid </identifiers/mid>`
    * :doc:`$left </identifiers/left>`
    * :doc:`$right </identifiers/right>`
