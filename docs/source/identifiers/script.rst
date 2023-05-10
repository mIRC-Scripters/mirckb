$script
=======

$script can be used to return the filename of the Nth loaded script file or the script file the identifier is being called from. If you specify a filename, it returns $null if the file is not loaded; otherwise it returns the file's name.

Synopsis
--------

.. code:: text

    $script(N/filename)

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
      - The Nth script file you want to check. If N is 0, this will return the total number of script files currently loaded.
    * - filename
      - Specify an actual filename if you want to explicitly check if a script file is loaded. This will return $null if no file is loaded, otherwise it returns the file name.

Example
-------

Echo script files this identifier is being called from:

.. code:: text

    alias test {
      echo -a $script
    }
    /test

Echo the total number of script files currently loaded to the active window:

.. code:: text

    //echo -a $script(0)

Echo the 2nd script file name to the active window:

.. code:: text

    //echo -a $script(2)

Echo if ``myfile.mrc`` is currently a loaded script to the active window:

.. code:: text

    //echo -a $script(myfile.mrc)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$alias </identifiers/alias>`

