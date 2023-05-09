$alias
======

$alias can be used to return the filename of the Nth loaded alias file. If you specify a filename, it returns $null if the file is not loaded; otherwise it returns the file's name.

Synopsis
--------

.. code:: text

    $alias(N/filename)

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
    * - N
      - The Nth alias file you want to check. If N is 0, this will return the total number of alias files currently loaded.
    * - filename
      - Specify an actual filename if you want to explicitly check if an alias file is loaded. This will return $null if no file is loaded, otherwise it returns the file name.

Example
-------

Echo the total number of alias files currently loaded to the active window

.. code:: text

    //echo -a $alias(0)

Echo the 3rd alias file name to the active window

.. code:: text

    //echo -a $alias(3)

Echo if ''myfile.mrc'' is currently a loaded alias to the active window

.. code:: text

    //echo -a $alias(myfile.mrc)

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$script </identifiers/script>`

