/fwrite
=======

The **/fwrite** command writes text or the specified binary variable to the file.

Synopsis
--------

.. code:: text

    /fwrite [-bn] <name> <text | &binvar>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -b
      - indicates that a &binvar is being specified
    * - -n
      - appends a $crlf to the line being written

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - name of the file handle
    * - <text | &binvar>
      - the text or the binvar to be written

Example
-------

Compatibility
-------------

Added: mIRC v6.1 (17 Feb 2006)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$feof </identifiers/feof>`
    * :doc:`$ferr </identifiers/ferr>`
    * :doc:`/fclose </commands/fclose>`
    * :doc:`/fopen </commands/fopen>`
    * :doc:`/fseek </commands/fseek>`
