/commands
=========

.. attention:: This feature has essentially been replaced by :doc:`/ctcps </commands/ctcps>`

The /commands command turns CTCP event processing on or off.

Synopsis
--------

.. code:: text

    /commands [on|off]

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
    * - <on|off>
      - turns CTCP event processing on or off

Example
-------

.. code:: text

    ; disable ctcps
    /commands off

Compatibility
-------------

.. compatibility:: 4.0

Removed: mIRC v5.0

Removed On:02/04/97

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/nick>`
    * :doc:`$remote </identifiers/remote>`
    * :doc:`$rawmsg </identifiers/rawmsg>`
    * :doc:`/ctcp </commands/ctcp>`
    * :doc:`/ctcpreply </commands/ctcpreply>`
    * :doc:`/events </commands/events>`
    * :doc:`/raw </commands/raw>`
    * :doc:`/remote </commands/remote>`
    * :doc:`/commands </commands/commands>`

