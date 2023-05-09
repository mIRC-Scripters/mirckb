/mkdir
======

The /mkdir command creates a new, empty, directory.

.. note:: Since mIRC 7.46, /mkdir can create more than one directory at a time, you can now do /mkdir C:\new\new1\

Synopsis
--------

.. code:: text

    /mkdir <dirname>

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
      - The directory's path/name to create

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
    * :doc:`/remove </commands/remove>`
    * :doc:`/rename </commands/rename>`
    * :doc:`/rmdir </commands/rmdir>`
    * :doc:`/run </commands/run>`
    * :doc:`/write </commands/write>`

