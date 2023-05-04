/exit
=====

The **exit** command can be used to safely close and exit mIRC.

.. note:: As of version 7.11 /exit -r will also pass the -i, -r, -noreg, and -portable command line parameters to the new mIRC.

Synopsis
--------

.. code:: text

    /exit -nr

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - switch disables the exit confirmation dialog.
    * - -r
      - switch restarts mIRC.

Parameters
----------

None

Example
-------

.. code:: text

    ;restart mIRC
    /exit -r

Compatibility
-------------

Added: mIRC v3.3 (21 Jun 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/load </commands/load>`
    * :doc: `/unload </commands/unload>`
