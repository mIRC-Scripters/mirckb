$ferr
=====

$ferr return 1 if a file error of some kind occured from the last file access attempt in any script, 0 otherwise

Synopsis
--------

.. code:: text

    $ferr

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //fopen test noexist | echo -a $ferr | fclose test

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$feof </identifiers/feof>`
    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$fgetc </identifiers/fgetc>`
    * :doc:`/flist </commands/flist>`
    * :doc:`/fopen </commands/fopen>`
    * :doc:`/fclose </commands/fclose>`
    * :doc:`/fwrite </commands/fwrite>`
    * :doc:`/fseek </commands/fseek>`

