/fclose
=======

The **/fclose** command closes a file open that was previously opened via the **/fopen** command. This command supports a wildcard pattern for its handle name.

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
      - A wildcard handle pattern

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

Added: mIRC v6.1 (29 Aug 2003)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fopen </aliases/fopen>`
    * :doc:`$fread </aliases/fread>`
    * :doc:`$fgetc </aliases/fgetc>`
    * :doc:`$feof </aliases/feof>`
    * :doc:`$ferr </aliases/ferr>`
    * :doc:`$file </aliases/file>`
    * :doc:`/flist <flist>`
    * :doc:`/fopen <fopen>`
    * :doc:`/fseek <fseek>`
    * :doc:`/fwrite <fwrite>`