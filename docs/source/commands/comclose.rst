/comclose
=========

The **/comclose** command closes an existing COM connection by a specific handle.

The supplied com handle must have been previously created via the **/comopen** command or the **$com** / **$comcall** identifiers.

Synopsis
--------

.. code:: text

    /comclose <hname>

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
    * - <name>
      - The name of the connection to close

Example
-------

.. code:: text

    Alias Example {
      ;Create a WshShell object 
      comopen Example wscript.shell

      ;Destroy object
      comclose Example
    }

Compatibility
-------------

Added: mIRC v5.9 (26 Apr 2001)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.


See also
--------

.. hlist::
    :columns: 4

    * :doc:`$com </aliases/com>`
    * :doc:`$comcall </aliases/comcall>`
    * :doc:`$comval </aliases/comval>`
    * :doc:`/comopen <comopen>`
    * :doc:`/comreg <comreg>`