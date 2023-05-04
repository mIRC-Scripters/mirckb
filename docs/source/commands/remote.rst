/remote
=======

The **/remote** command toggles the remote, CTCPS, and raw events processing. With no parameters, the /remote command displays the current state (either disabled or enabled).

Synopsis
--------

.. code:: text

    /remote [on|off]

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
      - Enables or disables events processing

Example
-------

To see the current state:

.. code:: text

    /remote

Which will print something like:

.. code:: text

    * Remote is on (Ctcps,Events,Raw)

Compatibility
-------------

Added: mIRC v4.0 (20 Mar 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$remote </identifiers/$remote>`
    * :doc: `$rawmsg </identifiers/$rawmsg>`
    * :doc: `/ctcps </commands/tcp-socket>`
    * :doc: `/raw </commands/raw>`
    * :doc: `/commands </commands/commands>`
