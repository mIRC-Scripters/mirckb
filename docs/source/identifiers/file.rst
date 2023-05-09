$file
=====

$file can be used in two ways:

* $file(filename).prop return information about a specified file. If no .property is specified, the size in bytes will be returned by default.

* $file="title" dir this is an old, deprecated syntax, display the select file dialog, {{Deprecated feature|new=:doc:`$sfile </identifiers/sfile>`}}

Synopsis
--------

.. code:: text

    $file(filename).prop 
 

.. code:: text

    $file="title" dir

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - filename
      - The filename or directory to any local or networked resource, optionally including absolute or relative path (relative to :doc:`$mircdir </identifiers/mircdir>`)
    * - title
      - the title of the dialog, the quote are optional if you don't use space, this parameter is optional: //echo -a $file c:\*.txt
    * - dir
      - the directory you want to display, you can put a file at the end which will be used to fill the 'filename' field in the dialog

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
When new $file(filename) is used, you can use the following properties:
    * - .size
      - Returns the file's size in bytes. (default) (see: :doc:`$bytes </identifiers/bytes>`)
    * - .ctime
      - Returns the file's creation time. (see: :doc:`$asctime </identifiers/asctime>`)
    * - .mtime
      - Returns the file's modification time. (see: :doc:`$asctime </identifiers/asctime>`)
    * - .atime
      - Returns the file's last access time. (see: :doc:`$asctime </identifiers/asctime>`)
    * - .shortfn
      - Returns the file's short filename (if it has one).
    * - .longfn
      - Returns the file's long filename.
    * - .attr
      - Returns the file (or folder)'s attributes. the returned value is a concatenation of letters representing the attributes, it will contain a:
** a - archive flag. Is set during normal file-modifying or dir-creation as an indicator to backup programs the file has changed since the last backup, for use with incremental backups. All backups clear this flag for files they archive.
** c - if file/folder is compressed.
** d - if it is a directory.
** e - if the file/folder is encrypted
** h - if the file/folder is hidden.
** n - if the file/folder is normal, not indexed.
<!--- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-sparse --->
** o - the file data is physically moved to offline storage (Remote Storage).
** p - if the file is sparse.
** r - if the file/folder is in read only mode
** s - if the file/folder is a system file/folder
** t - a file or directory that has an associated reparse point, or a file that is a symbolic link.
** x - if you're archiving (a) but are not allowing the indexing of the file/folder's content
** y - if the file is temporary
    * - .sig
      - Checks digital signature of an executable/DLL file. (Returns: ok, fail, none)
    * - .ext
      - Returns the extention of the filename if a filename is used, $null otherwise
    * - .path
      - if a folder is passed, returns the path containing that folder ($file(C:\windows\).path is C:\), if a filename is used, returns the path containing the filename.
    * - .name
      - Returns the name of the folder if a folder is used, or the name of the file without the extention if a filename is used
    * - .version
      - Returns the file's ''file version'' if executable/DLL.
    * - .product
      - Returns the file's ''product version'' if executable/DLL.
    * - .flags
      - Returns the file's ''file flags'' if executable/DLL, the value is a combination bitmask that specifies the compile time attributes of the file:
** 1: DEBUG - The file contains debugging information or is compiled with debugging features enabled.
** 2: PRERELEASE - The file is a development version, not a commercially released product.
** 4: PATCHED - The file has been modified and is not identical to the original shipping file of the same version number.
** 8: PRIVATEBUILD - The file was not built using standard release procedures.
** 16: INFOINFERRED - The file's version structure was created dynamically; therefore, some of the members in this structure may be empty or incorrect.
** 32: SPECIALBUILD - The file was built by the original company using standard release procedures but is a variation of the normal file of the same version number.
** See: https://msdn.microsoft.com/en-us/library/windows/desktop/ms646997(v=vs.85).aspx for more informations.

Example
-------

Tells you some information about mIRC's executable.

.. code:: text

    //echo -a $mircexe is $bytes($file($mircexe),3).suf and was installed on $asctime($file($mircexe).ctime)

Some more information about mIRC's executable.

.. code:: text

    //echo -a My copy of mIRC appears to be $iif($file($mircexe).sig == ok,valid.,hacked!)

Compatibility
-------------

.. compatibility:: 5.71

See also
--------

.. hlist::
    :columns: 4

