/dlevel
=======

The **/dlevel** command changes the default level to the number specified. You can change the default user level to allow unlisted (from the User list) users to access more events.

Synopsis
--------

.. code:: text

    /dlevel <level>

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
    * - <level>
      - the default level, a positive integer greater than 0

Example
-------

.. code:: text

    /dlevel 5

Now unlisted users can access events whose access level are in the range [1-5]

Compatibility
-------------

Added: mIRC v3.1 (23 Apr 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ulevel </identifiers/$ulevel>`
    * :doc:`$dlevel </identifiers/$dlevel>`
    * :doc:`$level </identifiers/$level>`
