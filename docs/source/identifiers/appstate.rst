$appstate
=========

The $appstate identifier returns the current state of the mIRC application window.

Synopsis
--------

.. code:: text

    $appstate

Properties
----------

None

Results
-------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Description
    * - full
      - The mIRC application window size is full.
    * - hidden
      - The mIRC application window size is hidden.
    * - maximized
      - The mIRC application window size is maximized.
    * - minimized
      - The mIRC application window size is minimized.
    * - tray
      - The mIRC application window has been minimized to the Windows tray.

Example
-------

Echo the mIRC application window state to the active window

.. code:: text

    //echo -a $appstate

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$locked </identifiers/locked>`
    * :doc:`$titlebar </identifiers/titlebar>`

