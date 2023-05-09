$zip
====

$zip creates/tests/extracts/lists zip using optional AES-256 encryption

.. note:: You cannot edit an existing zip file currently.

Synopsis
--------

.. code:: text

    $zip(file.zip,c[po],<filename/folder>[,password])
    $zip(file.zip,l,N)[.size]
    $zip(file.zip,t[p,password])
    $zip(file.zip,e[po],<extractdir> [,password])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - file.zip
      - the zip filename you want to create/test/list/extract from
    * - p
      - specify that the [password] parameter has been provided and should be used for the zip file
    * - o
      - overwrite the zip file when creating, overwrite the existing files and folder when extracting. It is also required if you extract into an empty existing folder (watch out)

* c - create a zip file and add a file name <filename> or the folder <folder> and all its subfolders.
* l - list the content of the zip file, returns the Nth file/folder or the total of elements in the zip
* t - test the zip file
* e - extract all the content of the zip to the <extractdir> folder

* N - used with l only, lists the Nth file/folder, or the total number of items with N = 0
* <file/folder> - used with c, the file/folder to add to the created zip file
* <extractdir> - used with e, the folder to extract the zip's content to
* [password] = password used to encrypt or decrypt each file added to zip. Can contain spaces. Valid only when using the 'p' switch.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .size
      - used with l only, makes $zip returns the size of the file (or 0 for a folder) instead of the filename
    * - .mtime
      - used with l only, makes $zip returns the timestamp of the file instead of the filename, as an integer which can be changed to date format using $asctime
    * - .crc
      - used with l only, makes $zip returns the crc32 of the file instead of the filename, as an integer instead of the hex format of $crc32()
    * - .em
      - used with l only, makes $zip returns 128 or 256 indicating the type of AES encryption. For non-encrypted files returns 0

If l is not used, $zip returns 1 for success and 0 for failure.

.. note:: If .zip contains a potentially dangerous filename such as containing '../' then 'e' and 'l' return 0 and refuse to extract or list contents.

Warning: Using the 'o' switch when extracting should NOT be used when extracting into $mircdir or any folder having important files in that folder or in any subfolders below it, especially if the zip was not created by YOU. $zip does not permit you to extract from the .zip into an existing foldername, even if it's empty. However, once you do use the 'o' switch, it allows you to extract into an existing foldername AND it also overwrites all matching files.

Example
-------

These examples assume TESTDIR contains filenames test1.txt and test2.txt and a subfolder named Backup beneath TESTDIR contains test3.bak

.. code:: text

    //echo -a $zip(test,cp,testdir\test1.txt,foo bar)

returns 1=success:
Creates zip filename "test" without the .zip extension. If you want the filename as test.zip, you must use 'test.zip' instead of 'test'.
The zip contains the filename as test1.txt without the foldername. File is encrypted using the 7-character passphrase "foo bar" including the space.

Error "* File exists: $zip" -> trying to create a .zip using a string which already exists as filename/foldername
Error "* Invalid parameters: $zip" file/folder being added does not exist.

.. code:: text

    //echo -a $zip(test,cpo,testdir\test1.txt,foo bar)

Same except creates zip named 'test' by overwriting it if it already exists.

.. code:: text

    //echo -a $zip(test.zip,tp,foo bar)

Tests contents of test.zip zipfile
Error "* Invalid parameters: $zip" if test.zip filename does not exist
Returns 1=success: contents of test.zip either use this password or are not encrypted
Returns 0=fail: At least 1 file in test.zip not able to be decrypted, or test.zip is not a valid zip file.

.. code:: text

    //echo -a $zip(test3.zip,cp,TESTDIR,foo bar)

adds to test3.zip the contents of TESTDIR and all contents of any of its subfolders. In this example, the .zip contains 5 items:

DIR entry for TESTDIR
filename TESTDIR\test1.txt
filename TESTDIR\test2.txt
DIR entry for TESTDIR\Backup
filename TESTDIR\Backup\test3.bak

.. note:: If TESTDIR uses a different case than the existing folder, the files are added using the spelling as used in the $zip parameter. Foldernames for any empty subfolders beneath TESTDIR are also added.

.. code:: text

    //echo -a $zip(test.zip3,ep,F:\ExtractDir,foo bar)

extract contents of test.zip to F:\ExtractDir. If no path were listed, subfolder below $mircdir.
Error "* Invalid parameters: $zip" if ExtractDir foldername already exists, even if empty
If this is the test3.zip created above, it extracts test1.txt and test2.txt into F:\ExtractDir\TESTDIR folder and extracts test3.bak into F:\ExtractDir\TESTDIR\Backup folder.

.. note:: After extraction, you can also use

.. code:: text

    //echo -a $findfile(F:\ExtractDir\,*,0,echo -a $1-)

to discover which files were extracted from the .zip, which does not require repeatedly using $zip() to list the contents.

.. note:: If the password is missing/wrong for a file inside the zip, any foldernames in the zip are created.

Create logs.zip containing contents of logs subfolder beneath $mircdir, returns 1 if successful. If log.zip already exists, returns 0 failure because it will not overwrite the .zip without using the 'o' switch.

.. code:: text

    //echo -a $zip(logs.zip,c,logs)

.. code:: text

    You can use the 'l' switch to confirm whether there are more than 1 file inside the .zip, and can use the .mtime and .crc properties to compare against other files to compare whether the file inside the .zip is the same. You cannot selectively unzip 1 file out of the zip, so if you need mIRC to extract 1 file for you, you must extract everything into a dummy folder in order to access just the 1 file you need.
    
    List contents of logs.zip:
    //var %i 1 | while ($zip(logs.zip,l,%i)) { echo -a $ord(%i) item: $base($zip(logs.zip,l,%i).crc,10,16,8) $asctime($zip(logs.zip,l,%i).mtime,yyyy/mm/dd HH:nn:ss) $v1  | inc %i }
    Note that the 1st item was the name of the folder, indicated by the trailing backslash

Notes
-----

Note how the files are contained inside the zip as 'logs\filename', and the only way to extract those files to the original path is to make $mircdir be the extract-to folder, which of course you should not do without examining the .zip's contents to ensure that there are no files which would extract to another folder outside the 'logs' folder. To extract safely, you should extract from the zip to a DUMMY folder, which will make these files extract to DUMMY\logs\filenames from where you can copy or move files to where you want them to be, and then delete the DUMMY folder when finished.<br>

If the 'l' switch confirms that a file exists inside the .zip and extraction fails, be sure whether you need to use the 'o' switch to both extract to a foldername which already exists, as well as to overwrite any files existing within that folder.<br>

Also note that the return value of 0 indicates that it failed to extract ALL files from the zip. If you extract without a password and the .zip contains a mix of passworded and unpassworded files, the unpassworded ones will extract while the passworded ones will not, causing the '0' return value.<br>

You can also use $zip(zipfile.zip,l,1).em to verify whether the 1st file in a zip has been encrypted, which requires using the 'p' password switch to extract it. While $zip cannot create files with AES-128 level of encryption, it can extract them from such a .zip created elsewhere. However, note that a .zip can contain files encrypted using the old PKZIP 2.0 encryption method, and .em returns 0 as if they're not encrypted, but $zip cannot extract using the encryption methods other than AES.<br>

$zip cannot add any file attribute to the files it adds, including hidden/read-only, and if these file attributes were added to files in a .zip created elsewhere, $zip extracts them without any attributes except the 'a' archive flag.

Compatibility
-------------

.. compatibility:: 7.55

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$isfile </identifiers/isfile>`
    * :doc:`$isdir </identifiers/isdir>`
    * :doc:`$exists </identifiers/exists>`
    * :doc:`$findfile </identifiers/findfile>`
    * :doc:`$finddir </identifiers/finddir>`
