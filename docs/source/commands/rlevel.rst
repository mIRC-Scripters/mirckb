/rlevel
=======

The /rlevel command removes all users from the remote users list with the specified general access level

Synopsis
--------

.. code:: text

    /rlevel [-r] <levels>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Removes the specified levels for that users and not just the general access level, if the user has no level, the entry is removed from the users list.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <levels>
      - A comma seperated list of level to be removed.

Example
-------

None

Compatibility
-------------

.. compatibility:: 3.5

See also
--------