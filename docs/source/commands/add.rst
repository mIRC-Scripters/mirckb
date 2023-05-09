/add
====

.. attention:: This feature has essentially been replaced by :doc:`/load </commands/load>`

The /add command  could previously be used to replace the currently loaded aliases, popups, commands, remote users, and events sections from the specified ini file. The ini file must be formatted the same way /save formats them.

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

.. compatibility:: 3.3

Removed: mIRC v3.8

Removed On:25/11/1995

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$script </identifiers/script>`
    * :doc:`$scriptdir </identifiers/scriptdir>`
    * :doc:`/load </commands/load>`
    * :doc:`/reload </commands/reload>`
    * :doc:`/save </commands/save>`
    * :doc:`/unload </commands/unload>`

