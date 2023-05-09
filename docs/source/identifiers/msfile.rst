$msfile
=======

$msfile Opens dialog to select 1 or more files.

Synopsis
--------

* $msfile(<path> [,title [,OpenButtonText] ] ) Opens dialog to choose 1 or multiple files. Returns N where 0 or greater is the count of returned filenames. N=-1 if error, such as one of the selected items being folder c:\windows\fonts\
* $msfile(N)	After dialog closes, for N>=1 returns the Nth selected filename. For N=0 returns the count of returned filenames.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
* path	Starting folder for the file select dialog. Can be a relative path to $mircdir. Ignores the last "\" delimited token if path doesn't end with "\" or "/". Error if path ends with \\.
* title	Optional string placed in the titlebar of the select dialog
* OpenButtonText	Optional string to replace 'Open' on that button of the select dialog. You cannot set this parameter without first defining the the title parameter to a non-null string.

* N	When N>=1, returns the Nth selected filename N=0 is the count of returned filenames. Returned filenames always include full path too.

.. note:: The returned count of filenames is limited to the number of filenames returned, which can be less than the number of files actually selected. The number of returned filenames varies, and seems to be limited to not allowing the sum of $msfile(0) plus the length of $nopath(filename) strings to be more than somewhere around 1000-1024 bytes. Longer filenames causes fewer filenames to be returned.

Properties
----------

None

Local Identifier
----------------

* $sfstate	Returns the null string or 'cancel' or 'error' after exiting the dialog.
* $msfile(N) N=0 returns the count of returned filenames. N>=1 returns the Nth returned filename.

.. note:: $sfstate and $msfile(N) are shared by $sfile and $sdir and $msfile(dir). These values are accessible by any script or from the editbox until the next time any of these 3 commands are used, when these identifiers are replaced by the new results. (Using $msfile(N) does not reset $sfstate) (Using $sdir or $sfile always causes $msfile(N>=1) to be $null. $sfile causes $msfile(0) to be either 0 or 1 depending on whether it selected a file, $sdir always sets $msfile(0) to 0 and blacks $msfile(1).)

Example
-------

.. code:: text

    //echo -ag $msfile($sysdir(profile),This shows in Titlebar,OpEn) sfstate = $sfstate | var %i 0 , %tot 0 | echo -ag sfstate $sfstate | while (%i < $msfile(0)) { inc %i | inc %tot $len($nopath($msfile(%i))) | echo -ag $calc(%i + %tot) <- this number probably won't go above 1000-1024 bytes / %i / $msfile(%i) }

The 2nd parameter puts your optional string in the titlebar. The 3rd optional parameter alters the label on the 'Open' button.

Since mIRC won't return a tokenized list of $nopath(filename) that's longer than 1000-1024, if you select more filenames than this limit, your list of returned filenames will show fewer filenames than you actually selected.

If you press ESCAPE or click cancel, $msfile(dir) returns 0 because zero files were selected. If the value returned is greater than zero, $msfile(0) is also filled with that same value, the count of returned filenames. Also, the local $sfstate identifier is filled with the string 'cancel' if you cancel or ESCAPE.

You can select multiple files and/or folders by pressing the Control key while clicking on filenames in the dialog. If the 1st (or only) item selected is a folder, clicking 'open' (or double-clicking on the folder) navigates into that folder.

Otherwise, folders are ignored in the returned count and list of filenames returned in $msfile(N>=1). You can also select a range of filenames by single-clicking on a file, then hold down the shift-key while clicking on a different filename. All files in that range will be selected. If the Control key is pressed while you click on the 1st file in that range, you can select that range without losing the earlier selection(s).

If you double-click on a file, the dialog behaves as if you selected that file and then pressed the OPEN button, returning that filename as $msfile(1). If you double-click on a file while pressing the Control key and while other files are already selected, any prior selections are not cleared, returning values as if you clicked OPEN while those multiple files are selected.

If your first selection is a folder, the dialog navigates into that folder for selecting files there, clearing selection of any files selected in the original folder. If your first selection is a filename, the identifier and $msfile(0) both return the number of selected files. It doesn't matter which order you click on files, because the returned files are filled into $msfile(N) in the order they appear in the dialog window, which could be sorted by filename, size, etc in normal or reverse order.

Once you've clicked anywhere within the dialog to set the focus there, even if you haven't selected a file, you can then press Control-A within the dialog, and it selects all the files before selecting all the folders, and $msfile(N) is filled in the dialog's sort order.

The selection window has 'mIRC" at the top of the treebar, which you can use to navigate back to the folder first opened by this command.

The values of $sfstate, $msfile(0), and any selected filenames in $msfile(N) will remain in those values until the next time any of the 3 identifiers are used, $sfile(dir) or $sdir(dir) or $msfile(dir)

.. code:: text

    //echo -a $msfile( $sysdir(profile)  ) / $sfstate / $msfile(0) / $msfile(1)

This shows the files and folders in your profile folder. Even though $finddir(c:\users\lefty\,*,0,1,echo -a $1-) lists both "Documents" and "My Documents" aliases to the same folder, the select window shows  "My Documents" but not "Documents". You can use $sysdir(profile) $+ Documents as your starting folder even though it's not shown by the parent folder.

.. code:: text

    //echo -a $msfile( $sysdir(profile) $+ My Documents\ ) / $sfstate / $msfile(0) / $msfile(1)

This displays an error message and forces you to begin selecting files in $mircdir

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sfile </identifiers/sfile>`
    * :doc:`$sdir </identifiers/sdir>`
    * :doc:`$sfstate </identifiers/sfstate>`
