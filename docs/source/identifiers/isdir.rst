$isdir
======

$isdir(path) returns $true if the specified directory exists, otherwise $false, (same as $exists).

Synopsis
--------

.. code:: text

    $isdir(path)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Path
      - The direction/path you want to check for.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $isdir($mircdir)

It will return $true because is checking if the mIRC direction is exists or not, as you using the mIRC it always be true.

.. code:: text

    //echo -a $isdir($mircdirtest)

It will return $true if inside your mIRC direction there is an folder named "test", otherwise will be $false.

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$exists </identifiers/exists>`
    * :doc:`$isfile </identifiers/isfile>`
    * :doc:`$true </identifiers/true>`
    * :doc:`$false </identifiers/false>`

