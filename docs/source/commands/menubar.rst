/menubar
========

The **/menubar** command display the current status and optionally turns the menubar on/off.

Synopsis
--------

.. code:: text

    /menubar [on|off]

Switches
--------

none

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [on|off]
      - if specified, turns the menubar on/off

Example
-------

.. code:: text

    ; ensures the menubar is enabled
    /menubar on

.. note:: While the menubar is off, the menubar's options are now accessed from left-clicking the mIRC icon in the upper left corner of the main window, or right-clicking anywhere in the main window's titlebar.

Compatibility
-------------

Added: mIRC v6.32 (21 May 2008)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/toolbar </commands/toolbar>`
    * :doc:`/treebar </commands/treebar>`
    * :doc:`/switchbar </commands/switchbar>`
    * :doc:`$menubar </identifiers/$menubar>`
