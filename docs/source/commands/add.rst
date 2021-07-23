/add
====

.. attention:: This feature has essentially been replaced by /load.

The **/add** command is now obsoleted in favour of the **/load** command, but it could previously be used to replace the currently loaded aliases, popups, commands, remote users, and events sections from the specified ini file. The ini file must be formatted the same way /save formats them.

Synopsis
--------

.. code:: text

    /add [-apuce] <file.ini>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Load the aliases
    * - -p
      - Load the popups
    * - -u
      - Load the remote users
    * - -c
      - Load the commands
    * - -e
      - Load the events

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <file.ini>
      - The initializations file to load the appropriate section from.

Example
-------

.. code:: text

    /add -a helpfulCmds.ini

Will output:

.. code:: text

    *** Added: Commands from c:mirchelpfulCmds.ini

Compatibility
-------------

Added: mIRC v3.3 (21 Jun 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

Removed: mIRC v3.8 (25/11/1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$script </aliases/script>`
    * :doc:`$scriptdir </aliases/scriptdir>`
    * :doc:`/load <load>`
    * :doc:`/reload <reload>`
    * :doc:`/save <save>`
    * :doc:`/unload <unload>`
