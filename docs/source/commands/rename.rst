/rename
=======

The **/rename** command can be used to rename and/or move a file or a directory. If the path contains spaces, you must enclose the path in a pair of double quotes ( :doc:`$qt </identifiers/$qt>` ).

Synopsis
--------

.. code:: text

    /rename -fo <filename> <new_filename>
    /rename <dirname> <new_dirname>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -f
      - Flush the renamed file to the disk
    * - -o
      - when renaming a file, allow to overwrite any existing file with the new filename

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - The path of the file or directory to rename or move
    * - <new_filename>
      - The new path of the file or directory

Example
-------

.. code:: text

    /rename E:\example.txt E:\renamed.txt

Will produce the following result:

.. code:: text

    * Renamed 'E:\example.txt' to 'E:\renamed.txt'

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$read </identifiers/$read>`
    * :doc:`$readini </identifiers/$readini>`
    * :doc:`$fopen </identifiers/$fopen>`
    * :doc:`/copy </commands/copy>`
    * :doc:`/fclose </commands/fclose>`
    * :doc:`/fopen </commands/fopen>`
    * :doc:`/mkdir </commands/mkdir>`
    * :doc:`/remove </commands/remove>`
    * :doc:`/rmdir </commands/rmdir>`
    * :doc:`/write </commands/write>`
    * :doc:`/writeini </commands/writeini>`
