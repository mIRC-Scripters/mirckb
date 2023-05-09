$longfn
=======

$longfn(path) returns long pathname\filename version of a short filename.

Synopsis
--------

.. code:: text

    $longfn( < path | filename | path\filename > )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
* Path = ''The absolute/relative directory/path and/or filename that you want to ensure is a long filename.''

NOTE:
* Looks for target the same way $isfile does: If relative path or no-path is provided, it assumes the location is relative to $mircdir
* In order to return the long version of the path, the path MUST exist.
* $longfn alters upper/lower case of individual folders and the filename only when the token needs to be changed
* To ensure foldernames+filename are all the correct case-sensitive spellings, must use $longfn($shortfn(target))

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $shortfn($mircdir) -> $longfn($shortfn($mircdir))

It returns the long path version of the specified directory. "C:\Users\westor\Documents\mIRC\" 

.. code:: text

    Assuming folder C:\PROGRA~1\ is the short alias of C:\Program Files\ and these filenames exist:
    C:\Program Files\7-Zip\readme.txt
    C:\Program Files\7-Zip\Uninstall.exe
    
    //echo -a $longfn( C:\Progra~1\7-ZIP\README.txt )
    returns: C:\Program Files\7-Zip\readme.txt
    The case of '7-ZIP' and 'README' were fixed because they were the case-insensitive equivalents of their values within $shortfn
    
    //echo -a $longfn( C:\ProgRam fiLes\7-ZIP\UnInStall.eXe )
    returns: C:\ProgRam fiLes\7-Zip\UnInStall.eXe
    The case of 'program files' and 'uninstall.exe' were not changed because they were already the case-insensitive equivalents of the long filename
    
    To ensure the entire path\filename has the correct case-sensitive spelling, use the $lonfn of the $shortfn of the target:
    //echo -a $Longfn($shortfn( C:\ProgRam fiLes\7-zIP\UnInStall.eXe ))
    Returns: C:\Program Files\7-Zip\Uninstall.exe

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$exists </identifiers/exists>`
    * :doc:`$isdir </identifiers/isdir>`
    * :doc:`$isfile </identifiers/isfile>`
    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$shortfn </identifiers/shortfn>`

