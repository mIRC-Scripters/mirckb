$isdde
======

$isdde(text) returns $true if the specified dde name is in use, $false otherwise.

Synopsis
--------

.. code:: text

    $isdde(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Text
      - The DDE name you want to check for.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $isdde(mIRC)

It will return $true if the currently mIRC using DDE name is the one that you specified, otherwise will be $false.

.. note:: The default mIRC dde name is "mIRC", if you would never change that from the options then is gonna be that for ever.

Compatibility
-------------

.. compatibility:: 5.41

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dde </identifiers/dde>`
    * :doc:`$ddename </identifiers/ddename>`
    * :doc:`/dde </commands/dde>`
    * :doc:`/ddeserver </commands/ddeserver>`

