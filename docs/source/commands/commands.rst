/commands
=========

.. warning:: This feature has essentially been replaced by **/ctcps** command.

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

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

Removed: mIRC v5.0 (02 Apr 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/nick>`
    * :doc:`$remote </identifiers/remote>`
    * :doc:`$rawmsg </identifiers/rawmsg>`
    * :doc:`/ctcp <ctcp>`
    * :doc:`/ctcpreply <ctcpreply>`
    * :doc:`/events <events>`
    * :doc:`/raw <raw>`
    * :doc:`/remote <remote>`
    * :doc:`/commands <commands>`