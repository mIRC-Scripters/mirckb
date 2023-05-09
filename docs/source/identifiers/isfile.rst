$isfile
=======

$isfile(path) returns $true if the specified file exists, otherwise $false, (same as $exists).

Synopsis
--------

.. code:: text

    $isfile(path)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
* Path = ''The direction/path of the filename you want to check for.''

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $isfile($mircexe)

It will return $true because is checking if the mirc.exe exists or not, as you using the mIRC it always be true.

.. code:: text

    //echo -a $isfile($mircdirtest.txt)

It will return $true if inside your mIRC direction there is an file named as "test.txt", otherwise will be $false.

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$exists </identifiers/exists>`
    * :doc:`$isdir </identifiers/isdir>`
    * :doc:`$true </identifiers/true>`
    * :doc:`$false </identifiers/false>`

