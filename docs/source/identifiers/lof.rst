$lof
====

$lof(filename) returns the bytes size information about the specified file, same as ``$file().size`` identifier.

Synopsis
--------

.. code:: text

    $lof(filename)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Filename
      - The filename that you want to check for.

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $lof($mircexe)

It will return the bytes size of the mirc.exe file that you already using.

.. code:: text

    //echo -a $lof(mirc.ini)

It will return the bytes size (e.g: 14056) of the mirc.ini file that you already using.

.. code:: text

    //echo -a $bytes($lof($mircini)).suf

It will return the original size (e.g: 14KB) of the mirc.ini file that you already using.

.. note:: It will return "$null" if the file doesn't exists to the path.

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$bytes </identifiers/bytes>`
    * :doc:`$file </identifiers/file>`
    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$mircini </identifiers/mircini>`
    * :doc:`$null </identifiers/null>`

