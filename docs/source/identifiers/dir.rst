$dir
====

.. attention:: This feature has essentially been replaced by :doc:`$sdir </identifiers/sdir>`

$dir displays the select folder dialog and returns the selected folder.

Synopsis
--------

.. code:: text

    $dir="title" <dir>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - title
      - The optional title of the dialog, the quote are optional if your title does not have space
    * - <dir>
      - the directory/file to be opened, can be a :ref:`matching_tools-wildcard`

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $dir='select dir' c:\

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sdir </identifiers/sdir>`
    * :doc:`$sfile </identifiers/sfile>`
    * :doc:`$hfile </identifiers/hfile>`
    * :doc:`$file </identifiers/file>`

