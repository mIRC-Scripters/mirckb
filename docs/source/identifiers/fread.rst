$fread
======

$fread returns the next $crlf delimited line from an open file in file handling.

Synopsis
--------

.. code:: text

    $fread(N/name) returns the next line
    
    $fread(N/name,M,&binvar) reads M bytes into the binvar

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
    * - M
      - if M is specified then you must specify a binary variable name as the third parameter, it reads M bytes into the binary variable
    * - &binvar
      - the name of the binary variable

Properties
----------

None

Example
-------

.. code:: text

    //fopen test $qt($mircini) | echo -a > $fread(test) | fclose test

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
    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$feof </identifiers/feof>`
    * :doc:`$fgetc </identifiers/fgetc>`
    * :doc:`$ferr </identifiers/ferr>`
