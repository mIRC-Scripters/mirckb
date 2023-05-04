/comreg
=======

The **/comreg** command can be used to registers and unregisters a COM with windows to make themselves accessible to applications. Regsvr32 command will not register .NET assemblies because of their very nature. However if you must, [http://msdn.microsoft.com/en-us/library/tzat5yw6(vs.71).aspx Regasm Might Help].

Synopsis
--------

.. code:: text

    /comreg -u <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -u
      - Unregister

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - Filename to be registered

Example
-------

.. code:: text

    ;register example.dll file
    /comreg example.dll

Compatibility
-------------

Added: mIRC v5.1 (11 Sep 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$com </identifiers/$com>`
    * :doc:`$comcall </identifiers/$comcall>`
    * :doc:`$comval </identifiers/$comval>`
    * :doc:`$dll </identifiers/$dll>`
    * :doc:`/comclose </commands/comclose>`
    * :doc:`/comopen </commands/comopen>`
    * :doc:`/dll </commands/dll>`
