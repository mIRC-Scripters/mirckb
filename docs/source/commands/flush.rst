/flush
======

The /flush command clears the remote user list of nickname definitions that are no longer valid.

For each nick in the remote user list that matches the specified levels mIRC checks to see if that nick is on any of the channels that you are currently on. If not, the nick definition is removed from the remote user list. If you do not specify levels then mIRC clears all nicks from the remote user list that do not exist on channels you are on.

Synopsis
--------

.. code:: text

    /flush -l [levels]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -l
      - removes only the specified levels from entries in the user list, instead of removing the entries

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [levels]
      - A list of levels seperated by commas

Example
-------

.. code:: text

    /flush 1,2,3

Compatibility
-------------

.. compatibility:: 3.8

See also
--------