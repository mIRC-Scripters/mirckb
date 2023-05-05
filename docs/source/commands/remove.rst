/remove
=======

The **/remove** command can be used to delete a file permanently or sends it to the recycle bin. The filename cannot be a wildcard pattern. This command prints "* Removed '<filename>'", to avoid that message, use the dot prefix (i.e. use /.remove).

Synopsis
--------

.. code:: text

    /remove -b <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -b
      - Send the file to the recycle bin

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - the file to remove. Your filename can be case-insensitive, but cannot include ?* wildcards. In the absence of a full path, filenames are assumed to be relative to $mircdir. If the <filename> contains any spaces, it must be enclosed in quotes.

.. note:: If filename contains 2+ consecutive spaces, this command searches for a filename without the duplicate space, and deletes that file instead, if it exists.

Example
-------

.. code:: text

    create and write to a file:
    /write foo.txt Hello There
    remove the file:
    /remove foo.txt
    delete a filename containing space from downloads subfolder:
    //.remove $qt(downloads\test filename.txt)

.. note:: The dot prefix hides both the success message and the "no such file" error.

Compatibility
-------------

Added: mIRC v4.0 (20 Mar 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$scriptdir </identifiers/scriptdir>`
    * :doc:`$read </identifiers/read>`
    * :doc:`$findfile </identifiers/findfile>`
    * :doc:`$finddir </identifiers/finddir>`
    * :doc:`/copy </commands/copy>`
    * :doc:`/mkdir </commands/mkdir>`
    * :doc:`/rename </commands/rename>`
    * :doc:`/rmdir </commands/rmdir>`
    * :doc:`/run </commands/run>`
    * :doc:`/write </commands/write>`
