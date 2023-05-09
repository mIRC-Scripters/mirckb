$samepath
=========

$samepath evaluates whether the pair of [path\]filenames resolve to the same path\filename.

Synopsis
--------

.. code:: text

    $samepath( <string1> , <string2> )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - String1
      - first path to be compared
    * - String1
      - first path to be compared

you can use relative path for both parameters.

Example
-------

.. code:: text

    //echo -a This returns $true $samepath( $mircexe , $nopath($mircexe) )
    //echo -a This very likely returns $true $samepath( c:\program files\ , c:\progra~1\ )
    //echo -a Returns $true if at least 1 subfolder: $samepath( $finddir($mircdir,*,1,1) , $remove($finddir($mircdir,*,1,1),$mircdir) )
    //echo -a $true doesn't guarantee filename actually exists: $samepath( $mircdir $+ nosuchfile , nosuchfile )
    //var %i delete_me.txt | write %i test | echo -a %i $shortfn(%i) returns $true : $samepath( %i , $shortfn(%i) )

Compatibility
-------------

.. compatibility:: 7.46

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$shortfn </identifiers/shortfn>`

