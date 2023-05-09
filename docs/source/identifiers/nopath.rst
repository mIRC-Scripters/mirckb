$nopath
=======

$nopath(path) returns filename without a path if it has one.

Synopsis
--------

.. code:: text

    $nopath(filename)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - filename
      - the filename you want the path of

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $nopath($mircexe)

It will return the "mirc.exe" filename without the "path" direction into it.

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$nofile </identifiers/nofile>`

