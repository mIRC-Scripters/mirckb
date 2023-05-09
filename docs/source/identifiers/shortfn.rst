$shortfn
========

$shortfn(path) returns short version of a long filename.

Synopsis
--------

.. code:: text

    $shortfn(path)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Path
      - The direction/path that you want to check for.

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $shortfn($longfn($mircdir))

It will return for example the "C:\Users\westor\DOCUME~1\mIRC\" short path version of the specified direction.

.. code:: text

    //echo -a $shortfn(C:\Users\westor\Documents\mIRC\)

It will return "C:\Users\westor\DOCUME~1\mIRC\" short path version of the long version one that you have specified.

.. note:: In order to return the short version of the path, the path MUST exist.

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$longfn </identifiers/longfn>`
    * :doc:`$exists </identifiers/exists>`
    * :doc:`$isdir </identifiers/isdir>`
    * :doc:`$mircdir </identifiers/mircdir>`

