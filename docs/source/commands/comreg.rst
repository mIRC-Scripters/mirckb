/comreg
=======

The **/comreg** command can be used to registers and unregisters a COM with windows to make themselves accessible to applications. Regsvr32 command will not register .NET assemblies because of their very nature. However if you must, ` Regasm Might Help <http://msdn.microsoft.com/en-us/library/tzat5yw6(vs.71).aspx>`_.

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

Added: mIRC v5.1 (28 Aug 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$com </aliases/com>`
    * :doc:`$comcall </aliases/comcall>`
    * :doc:`$comval </aliases/comval>`
    * :doc:`$dll </aliases/dll>`
    * :doc:`/comclose </comclose>`
    * :doc:`/comopen </comopen>`
    * :doc:`/dll </dll>`