$lines
======

$lines returns the total number of lines in the specified text file.

Synopsis
--------

.. code:: text

    $lines(filename)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
filename - The complete filename you want to know the total number of lines.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $lines(readme.txt)

 will return the total number of lines in the relative filename readme.txt.

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$read </identifiers/read>`

