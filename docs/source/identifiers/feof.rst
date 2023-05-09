$feof
=====

$feof returns 1 if the end of the file was reached from the last file access attempt in any script, 0 otherwise.

Synopsis
--------

.. code:: text

    $feof

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //write -c test.txt test | fopen test test.txt | echo -a $fread(test) | echo -a $feof | echo -a > $fread(test) | echo -a $feof | fclose test | remove test.txt

Note that when reading a file line by line with $fread, you need one extra evaluation so that $feof is set to 1

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ferr </identifiers/ferr>`
    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$fgetc </identifiers/fgetc>`
    * :doc:`/flist </commands/flist>`
    * :doc:`/fopen </commands/fopen>`
    * :doc:`/fclose </commands/fclose>`
    * :doc:`/fwrite </commands/fwrite>`
    * :doc:`/fseek </commands/fseek>`

