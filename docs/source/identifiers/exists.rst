$exists
=======

The $exists identifier can be used to determine whether a specified file, or folder, exists. If the file/folder exists, or does not exist, the identifier will return :doc:`$true </identifiers/true>` or :doc:`$false </identifiers/false>`, respectively.

Synopsis
--------

.. code:: text

    $exists(File/Folder)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - File/Folder
      - The file or folder to check for

Example
-------

Echo to the active screen if mirc.ini exists

.. code:: text

    //echo -a $exists(mirc.ini)

The above executed line should return the following:

.. code:: text

    $true

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$isfile </identifiers/isfile>`
    * :doc:`$isdir </identifiers/isdir>`
* 

