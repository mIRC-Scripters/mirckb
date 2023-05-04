/commands
=========

.. attention:: This feature has essentially been replaced by :doc:`/ctcps </commands/ctcps>`.

The **/commands** command turns CTCP event processing on or off.

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

Added: mIRC v4.0 (20 Mar 1996)

Removed: mIRC v5.0 (21 Apr 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$nick </identifiers/$nick>`
    * :doc: `$remote </identifiers/$remote>`
    * :doc: `$rawmsg </identifiers/$rawmsg>`
    * :doc: `/ctcp </commands/tcp-socket>`
    * :doc: `/ctcpreply </commands/tcp-socket>`
    * :doc: `/events </commands/events>`
    * :doc: `/raw </commands/raw>`
    * :doc: `/remote </commands/remote>`
    * :doc: `/commands </commands/commands>`
