$finddir
========

$finddir Searches the specified directory (and optionally its subdirectories) for the Nth directory matching the :ref:`matching_tools-wildcard` specification and returns the path if it is found.

.. note:: You can stop the $finddir search using /halt inside the command parameter, /halt won't halt the script execution in this case.

Synopsis
--------

.. code:: text

    $finddir(dir, wildcard , N , [depth , [@window | command] ] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - DIR
      - Name of the starting folder name.
    * - wildcard
      - directory being searched for. A list of folder names or :ref:`matching_tools-wildcard` seperated by a ';'.
    * - N
      - Nth sequential directory being searched for. 0 is count of ALL directories.
    * - depth
      - optional folder depth, counting DIR as the first level. 0 or 1 is DIR level only. If depth not used, there's no depth limit.
    * - command
      - optional 5th parameter. Can use $finddirn as the sequential number for that directory, or $1- for directory. If the first token in the command is an identifier, $1- will hold the previous values it had and you can preevaluate $1- with $!1- to access the directory.
    * - @window
      - optional 5th parameter. Must be window with side listbox created with -l switch. Each $1- from matching directories is appended as a new line to the side listbox. Is equivalent to: /aline -la @window $1-

.. note:: DIR can be absolute \path or c:\path or relative to $mircdir. Does not need ending slash. Accepts forward/backward slashes interchangeably but always output backslash.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - shortfn
      - causes N > 0 or $1- within 5th parameter to return short filenames and/or foldernames when a case-insensitive evaluation of the filename is not a valid DOS filename. (Invalid characters, more than 1 period, filename prefix longer than 8, file extension longer than 4, etc)

.. note:: Returned string can contain multiple consecutive spaces if the file/folder names contain them, causing $file() and other mIRC identifiers to fail. This problem can be avoided by using .shortfn which never contains any spaces.

Example
-------

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$finddir </identifiers/finddir>`
    * :doc:`$findfilen </identifiers/findfilen>`
    * :doc:`$shortfn </identifiers/shortfn>`
    * :doc:`$sysdir </identifiers/sysdir>`
    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`$getdir </identifiers/getdir>`
