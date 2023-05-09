$freadex
========

$freadex returns the total content of the file from the pointer.

Synopsis
--------

.. code:: text

    $freadex(N/name) returns the content of the file

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

None

Example
-------

.. code:: text

    //fopen test $qt($mircini) | echo -a > $freadex(test) | fclose test

Compatibility
-------------

.. compatibility:: 7.59

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
    * :doc:`$fread </identifiers/fread>`
