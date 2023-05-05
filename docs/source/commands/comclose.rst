/comclose
=========

The **/comclose** command closes an existing :doc:`cOM connection </advanced/com>` by a specific handle.

The supplied com handle must have been previously created via the :doc:`/comopen command </advanced/comopen>` or the :doc:`$com </identifiers/com>` / :doc:`$comcall </identifiers/comcall>` identifiers.

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

Added: mIRC v5.9 (15 Jun 2001)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$com </identifiers/com>`
    * :doc:`$comcall </identifiers/comcall>`
    * :doc:`$comval </identifiers/comval>`
    * :doc:`/comopen </commands/comopen>`
    * :doc:`/comreg </commands/comreg>`
