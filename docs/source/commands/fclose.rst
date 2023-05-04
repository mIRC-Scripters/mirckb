/fclose
=======

The **/fclose** command closes a file open that was previously opened via the :doc: `/fopen </commands/fopen>` command. This command supports a :doc: `wildcard </intermediate/matching_tools.html#wildcard>` pattern for its handle name.

Synopsis
--------

.. code:: text

    /fclose <handle>
    /fclose <wild_handle>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - <handle>
      - The name of the handle
    * - <wild_handle>
      - A :doc: `wildcard </intermediate/matching_tools.html#wildcard>` handle pattern

Parameters
----------

None

Example
-------

.. code:: text

    alias example {
    ;open the file
    .fopen -o x example.txt
    ;write to it
    .fwrite x Print this line.
    ;close the file handle
    .fclose x
    }

Compatibility
-------------

Added: mIRC v6.1 (17 Feb 2006)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$fopen </identifiers/$fopen>`
    * :doc: `$fread </identifiers/$fread>`
    * :doc: `$fgetc </identifiers/$fgetc>`
    * :doc: `$feof </identifiers/$feof>`
    * :doc: `$ferr </identifiers/$ferr>`
    * :doc: `$file </identifiers/$file>`
    * :doc: `/flist </commands/flist>`
    * :doc: `/fopen </commands/fopen>`
    * :doc: `/fseek </commands/fseek>`
    * :doc: `/fwrite </commands/fwrite>`
