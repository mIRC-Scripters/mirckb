$dllcall
========

$dllcall call a function of a dll, just like :doc:`$dll </identifiers/dll>`, but is 'multithreaded', it won't halt the script and will call the specified alias once the call returns. $dllcall does not return a value.

Synopsis
--------

.. code:: text

    $dllcall(name.dll,alias,procname,data)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name.dll
      - the filename to the dll
    * - alias
      - The alias to be called once the function call returns, the alias is called with one parameter: the dll complete filename
    * - procname
      - procname, the name of the function in the dll
    * - data
      - a string/parameter passed to the function

Example
-------

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dll </identifiers/dll>`
    * :doc:`/dll </commands/dll>`

