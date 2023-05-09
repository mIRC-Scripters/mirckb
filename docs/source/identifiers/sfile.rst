$sfile
======

$sfile displays the select file dialog and returns the selected file

Synopsis
--------

.. code:: text

    $sfile(dir, title, button)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - dir
      - The directory you want to open, can be a :ref:`matching_tools-wildcard`: it will be used as the field in the dialog selection where you can enter a file name
    * - title
      - The optional title
    * - button
      - The optional text of the 'open' button on the dialog

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $sfile($mircdir,"choose a file!,Ok!)

Compatibility
-------------

.. compatibility:: 5.81

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sdir </identifiers/sdir>`

