/closemsg
=========

.. warning:: This feature has essentially been replaced by **/close** command.

The **/closemsg** command can be used to close all query windows. A name can be specified to close only that query window.

Synopsis
--------

.. code:: text

    /closemsg [nick]

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
    * - [nick]
      - a nickname for the window to close

Example
-------

.. code:: text

    ;Close Kol's query
    /closemsg kol

Compatibility
-------------

Added: mIRC v3.3 (21 Jun 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/clear <clear>`
    * :doc:`/clearall <clearall>`
    * :doc:`/close <close>`
    * :doc:`/debug <debug>`
    * :doc:`/window <window>`