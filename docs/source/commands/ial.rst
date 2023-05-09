/ial
====

The ial command turns IAL (Internal Address List) on or off. If no on/off parameter is used, it will display the IAL status

.. note:: this setting is not persistent across sessions and resets to on every time mIRC is run.

Synopsis
--------

.. code:: text

    /ial [on|off]

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
    * - [on|off]
      - Turns the IAL on/off.

Example
-------

.. code:: text

    ;Turns IAL off
    /ial off

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ialclear </commands/ialclear>`
    * :doc:`/ialmark </commands/ialmark>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$address </identifiers/address>`
    * :doc:`$ialchan </identifiers/ialchan>`

