$fopen
======

$fopen returns information about an open file in file handling

Synopsis
--------

.. code:: text

    $fopen(N/name)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth handle to be used
    * - name
      - The handle name to be used

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .fname
      - returns the complete filename opened
    * - .pos
      - returns the position of the pointer in the file
    * - .eof
      - returns 1 if the end of the file was reached, 0 otherwise
    * - .err
      - returns 0 if an error occured from the last file access
    * - .bom
      - returns the encoding of the file, "utf16le", "utf16be", "utf8", or "ascii"

Example
-------

.. code:: text

    //fopen test $qt($mircini) | echo -a > $fread(test) $fopen(test).pos | fclose test

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/fclose </commands/fclose>`
    * :doc:`/fseek </commands/fseek>`
    * :doc:`/flist </commands/flist>`
    * :doc:`/fwrite </commands/fwrite>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$feof </identifiers/feof>`
    * :doc:`$fgetc </identifiers/fgetc>`
    * :doc:`$ferr </identifiers/ferr>`
