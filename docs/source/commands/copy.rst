/copy
=====

The **/copy** command can be used to copy a file or an entire directory to another location. Both the source and the destination parameters support directory names. If the source is a directory the entire directory will be copied. The source parameter also supports wildcard characters.

This command is verbose by default.

Synopsis
--------

.. code:: text

    /copy -aof <nowiki><source></nowiki> <destination>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -o
      - If the file exists, override it
    * - -a
      - If the file exists, append to it
    * - -f
      - Flush the copied file to the disk

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <source>
      - The name of the directory or file to be copied (can be a wildcard name)
    * - <destination>
      - Destination filename (or directory)

Example
-------

You can use the copy command to move the content of entire directories:

.. code:: text

    ;Copy all the files in directory 'aaa' into directory 'bbb'
    copy aaa bbb

Below is a simple backup script:

.. code:: text

    ;A simple backup script to back up all currently loaded script file.
    ; /backup
    Alias backup {
      var %dir = backup\bkup. $+ $ctime

      ;make sure the user wants to backup
      if ($input(Are you sure you want to backup all loaded the scripts?, y, Backup Scripts?)) {

        ;make sure the backup directory exists
        if (!$isdir(backup)) mkdir backup

        ;create the new backup directory, timestamped
        mkdir %dir
        echo -ac info [backup] %dir created!

        var %x = 1
        ;while there is another script file
        while ($script(%x)) {
          ;backup the file
          .copy $qt($v1) %dir
          echo -ca info [backup] copying $qt($v1)
          inc %x 
        }

        ;done!
        echo -ac info [backup] Backup is complete!
      }
    }

Compatibility
-------------

Added: mIRC v5.3 (13 Dec 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$file </identifiers/file>`
    * :doc:`/mkdir <mkdir>`
    * :doc:`/remove <remove>`
    * :doc:`/rename <rename>`
    * :doc:`/rmdir <rmdir>`