$group
======

$group returns the name or status of a #group in a script.

Synopsis
--------

.. code:: text

    $group(N/name)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth group
    * - name
      - the name of a group, prefixed with a '#'

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .status
      - return the status of the group, 'on' or 'off'
    * - .name
      - return the name of the group
    * - .fname
      - return the filename in which the goup exists

Example
-------

.. code:: text

    //echo -a $group(0)

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/groups </commands/groups>`

