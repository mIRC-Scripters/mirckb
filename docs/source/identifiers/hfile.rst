$hfile
======

.. attention:: This feature has essentially been replaced by :doc:`$sfile </identifiers/sfile>`

$hfile could be used in the past to display a selection file dialog just like the old ":doc:`$file </identifiers/file>`" identifier, but would lay out the file in the dialog horizontally. Nowadays it returns the same :doc:`$sfile </identifiers/sfile>`

Synopsis
--------

.. code:: text

    $hfile="title" dir

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - title
      - the title of the dialog, the quote are optional if you don't use space, this parameter is optional: //echo -a $hfile c:\*.txt
    * - dir
      - the directory you want to display, you can put a file at the end which will be used to fill the 'filename' field in the dialog

Example
-------

.. code:: text

    //echo -a > $hfile="select" c:\

Compatibility
-------------

.. compatibility:: 4.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sfile </identifiers/sfile>`

