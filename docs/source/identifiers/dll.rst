$dll
====

$dll call a function of a dll, and eventually returns a value if the function is made to return a value. More informations about dll :doc:`here </advanced/dll>`

Synopsis
--------

.. code:: text

    $dll(name[.dll],procname,data)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name.dll
      - the filename to the dll. If filetype not used, assumes filename.dll
    * - procname
      - procname, the name of the function in the dll
    * - data
      - a text string/parameter passed to the function, which .dll sees as 0x00-terminated, even if procname does not require a data string, you must still pass a null or dummy string. If data should contain a comma, best to place it in a %var or use $chr(44) instead of trying to pass as a literal string.

Properties
----------

None

Notes
-----

1. Beginning v7.56, filename and filename.dll are both loaded into the $dll(N) list once as filename.dll. Previously they were loaded as 2 different $dll(N) items with 2 different filenames, yet referencing both filename|filename.dll used the memory image associated with the lowest Nth item in the $dll(N) list of the pair.
Example
-------

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dllcall </identifiers/dllcall>`
    * :doc:`/dll </commands/dll>`
