/showmirc
=========

The /showmirc command can be used to manipulate the main  mIRC window. Full screen mode (-f) switch can also be activated via the F11 shortcut key.

Synopsis
--------

.. code:: text

    /showmirc -xrsfop
    /showmirc -ltnm

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -x
      - maximize window
    * - -r
      - restore window
    * - -s
      - show window
    * - -f
      - go into full-screen mode

Minimize Options

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - minimize window
    * - -t
      - minimize to tray
    * - -m
      - minimize to tray according to tray settings.
    * - -l
      - lock when minimizing

On Top Settings

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -o
      - set on top settings
    * - -p
      - remove on top settings

Parameters
----------

None

Example
-------

.. code:: text

    alias example {
      ; restore mIRC after 2 seconds
      .timer 1 2 showmirc -r
      ; hide it for now
      showmirc -t
    }

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fullscreen </identifiers/fullscreen>`
    * :doc:`$appstate </identifiers/appstate>`
    * :doc:`$appactive </identifiers/appactive>`
    * :doc:`/exit </commands/exit>`
    * :doc:`/window </commands/window>`

