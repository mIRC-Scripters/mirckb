/unload
=======

The /unload command is used to unload either an alias file or a script file.

.. note:: The command cannot unload the popups.ini file.

Synopsis
--------

.. code:: text

    /unload <-a|-nrs> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Allows you to unload a specific alias file.
    * - -rs
      - Unloads the specified script/remotes file.
    * - -n
      - Prohibits the script file you are unloading from triggering any ``ON *:UNLOAD:`` events.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - filename to load

Examples
--------

Unload a script file

.. code:: text

    /unload -rs myfile.mrc

Unload a script file and prevent it from triggering it's ``ON *:UNLOAD:`` event

.. code:: text

    /unload -rsn myfile.mrc

Unload an alias file

.. code:: text

    /unload -a myalias.mrc

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/load </commands/load>`

