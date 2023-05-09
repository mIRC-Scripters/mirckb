$nofile
=======

$nofile returns the directory path in a full filename without the name of the file itself.

Synopsis
--------

.. code:: text

    $nofile(full-filename)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - full-filename
      - the filename you want the path of

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $nofile($mircexe)

will return the directory of the mIRC executable that is running.

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$nopath </identifiers/nopath>`

