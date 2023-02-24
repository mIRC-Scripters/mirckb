/list
=====

The **/list** command lists currently available channels.

.. note:: This sends a command to the irc network and returns the reply. It does not report info about hidden channels such as those with mode -s or -p set, unless your network privileges allow you to see that info.

Synopsis
--------

 /list -n [#channel] [-MIN N] [-MAX N]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - Minimize the channel list window

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #channel
      - If specified, mIRC will only list information for that channel. If you specify a wildcard, mIRC will list all channels that contain the wildcard expression.
    * - -MIN N
      - If specified, can be used to only display channels that has mimnimum N users
    * - -MAX N
      - If specified, can be used to only display channels that has maximum N users

.. note:: Default when no parameters or switches used is reporting all publicly visible channels.

Example
-------

.. code:: text

    /list -min 5 -max 20
    /list *mirc*


Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------
