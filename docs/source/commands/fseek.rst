/fseek
======

The /fseek command sets the read/write pointer to the specified position in the file, position starts at 0.

Synopsis
--------

.. code:: text

    /fseek -nlwrp <name> <position|N|matchtext>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -l
      - sets the pointer to the beginning of the Nth line
    * - -n
      - sets the pointer to the beginning of the next line (from the current position of the read/write pointer)
    * - -w
      - sets the pointer to the beginning of the line matching the :ref:`matching_tools-wildcard` expression
    * - -r
      - sets the pointer to the beginning of the line matching the regular expression
    * - -p
      - sets the pointer to the beginning of the current line, if the pointer is already at the beginning of a line, it sets the pointer to the beginning of the previous line

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - the name of the file handle
    * - <position|N|matchtex>
      - not required if you use -n, if -l is used: a line number, if -w is used: a :ref:`matching_tools-wildcard` expression, if -r is used: a regular expression, if no switch is used, it's the position in the file (Nth byte)

.. note:: if /fseek is not successful (can't find a match with -w or -r, can't find the Nth line with -l etc), it will set the read/write pointer to the end of the file. $fopen().err is not set, but $fopen().eof is.

Example
-------

.. code:: text

    /fseek myfile 42
    /fseek -l myfile 12
    /fseek -n
    /fseek -w *findthis*
    /fseek -r /findthat/

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fread </identifiers/fread>`
    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$ferr </identifiers/ferr>`
    * :doc:`$feof </identifiers/feof>`
    * :doc:`$fgetc </identifiers/fgetc>`
    * :doc:`/fclose </commands/fclose>`
    * :doc:`/flist </commands/flist>`
    * :doc:`/fopen </commands/fopen>`

