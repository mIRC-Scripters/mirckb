$fgetc
======

$fgetc returns the next character from an open file in file handling.

Synopsis
--------

.. code:: text

    $fgetc(name/N)

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
      - The name of the handle to be used

Properties
----------

None

Example
-------

.. code:: text

    //fopen test $qt($mircini) | echo -a > $fgetc(test) | fclose test

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/fopen </commands/fopen>`
    * :doc:`/fclose </commands/fclose>`
    * :doc:`/fseek </commands/fseek>`
    * :doc:`/flist </commands/flist>`
    * :doc:`/fwrite </commands/fwrite>`
    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$feof </identifiers/feof>`
    * :doc:`$ferr </identifiers/ferr>`

