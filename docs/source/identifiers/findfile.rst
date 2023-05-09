$findfile
=========

$findfile Searches the specified directory (and optionally its subdirectories) for the Nth filename matching the :ref:`matching_tools-wildcard` file specification and returns the full path and filename if it is found.

.. note:: You can stop the $findfile search using /halt inside the command parameter, /halt won't halt the script execution in this case.

Synopsis
--------

.. code:: text

    $findfile(dir, wildcard , N , [depth , [@window | command] ] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - DIR
      - Name of the starting folder name.
    * - wildcard
      - Filename being searched for. A list of filenames or :ref:`matching_tools-wildcard` separated by a ';'.
    * - N
      - Nth sequential file being searched for. 0 is count of ALL files.
    * - depth
      - optional folder depth, counting DIR as the first level. 0 or 1 is DIR level only. If depth not used, there's no depth limit.
    * - command
      - optional 5th parameter. Can use $findfilen as the sequential number for that filename, or $1- for the space-delimited filename. If the first token in the command is an identifier, $1- will hold the previous values it had and you can pre-evaluate $1- with $!1- to access the filename.
    * - @window
      - optional 5th parameter. Must be window with side listbox created with -l switch. Each $1- from matching filenames is appended as a new line to the side listbox. Is equivalent to: /aline -la @window $1-

.. note:: DIR can be absolute \path or c:\path or relative to $mircdir. Does not need ending slash. Accepts forward/backward slashes interchangeably but always output backslash.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - shortfn
      - causes N > 0 or $1- within 5th parameter to return short filenames and/or foldernames when a case-insensitive evaluation of the filename is not a valid DOS filename. (Invalid characters, more than 1 period, filename prefix longer than 8, file extension longer than 4, etc)

.. note:: Returned string can contain multiple consecutive spaces if the file/folder names contain them, causing $file() and other mIRC identifiers to fail. This problem can be avoided by using .shortfn which never contains any spaces.

Example
-------

.. code:: text

    //noop $findfile( c:\program files\, * ,0,2,echo -s $ord($findfilen) $1-).shortfn
      echoes all filenames in c:\program files\ and 1 level beneath it. .shortfn causes all foldernames and pathnames to be converted to short filenames if necessary. The "Program Files" folder appears as PROGRA~1 regardless of the way it was spelled for DIR.
    //noop //echo -a $findfile( c:\proGra~1\, * ,0,2,echo -s $ord($findfilen) $1-)
      same, except the "Program Files" folder is displayed exactly as spelled for DIR.

.. code:: text

    //window @FileList | var %a $findfile( $sysdir(downloads),*.jpg;*.png;w* ,0,1,@FileList1)
      Loads path\filenames of files in windows username's download folder (not necessarily mIRC's download folder) but nothing from any subfolders beneath it. The list will be an alphabetical list of all *.jpg followed by all *.jpg followed by all filenames beginning with W which did not match the prior wildcards.

.. code:: text

    //echo -a Versions.txt $iif($findfile($mircdir,versions.txt,1,1),is,isn't) in the same folder as $nopath($mircini)
    
    //echo -a $findfile( $sysdir(profile),*.html,0,999,echo -s $iif($!isfile($1), There are multiple consecutive spaces in the folder\filename $1-))
      Multiple consecutive spaces in folder/file names can cause $file($1-).size to either fail to see an existing file or incorrectly see a similarly named filename without the extra spaces.

.. code:: text

    DIR can be relative path to $mircdir. \windows\ is relative to the root folder on the same drive letter where $mircdir is. If $getdir is the downloads subfolder of $mircdir, which is c:\mIRC\, the following pair of commands return the same list of files, with the only difference being that mIRC displays the same spelling of the portion of the path entered as the DIR parameter. This means that while they both incorrectly capitalize the W in downloads, the 1st one shows the true c:\mIRC\ spelling while the 2nd one displays as the lower case used in the  DIR parameter.
    
    //echo -a $findfile(doWnloads,* ,0,2,echo -s $1- )
    //echo -a $findfile(c:\mirc748\doWnloads,* ,0,2,echo -s $1- )
    
    Because relative path can include the .. alias for the parent folder, both following examples show all filenames in the c:\ root folder, differing only by the DIR string used in the example:
    
    //echo -a $findfile(c:\No Such Folder\..\,*,0,1,echo -s $1- )
    //echo -a $findfile( $getdir $+ $str(..\,$calc($numtok($getdir,92) -1)) ,*,0,1,echo -s $1- )
    
    (Even though c:\No Such Folder\ does not exist, appending the ..\ starts with c:\ which does exist.)

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$finddir </identifiers/finddir>`
    * :doc:`$findfilen </identifiers/findfilen>`
    * :doc:`$shortfn </identifiers/shortfn>`
    * :doc:`$sysdir </identifiers/sysdir>`
    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$getdir </identifiers/getdir>`
