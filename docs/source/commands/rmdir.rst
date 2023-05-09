/rmdir
======

The /rmdir command deletes an empty directory. If the directly contains either files or other directories, an error will occur.

Synopsis
--------

.. code:: text

    /rmdir <dirname>

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <dirname>
      - The path/name of the directory to delete

Example
-------

.. code:: text

    ; Create a directory
    /mkdir example
    
    ; Delete it
    /rmdir example

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$scriptdir </identifiers/scriptdir>`
    * :doc:`$read </identifiers/read>`
    * :doc:`$findfile </identifiers/findfile>`
    * :doc:`$finddir </identifiers/finddir>`
    * :doc:`/copy </commands/copy>`
    * :doc:`/mkdir </commands/mkdir>`
    * :doc:`/remove </commands/remove>`
    * :doc:`/rename </commands/rename>`
    * :doc:`/run </commands/run>`
    * :doc:`/write </commands/write>`

