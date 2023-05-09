$level
======

$level finds a matching address in the remote users list and returns its corresponding levels list.

Synopsis
--------

.. code:: text

    $level(address)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - address
      - The address used you want the correspond levels list of

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $level(*!*@mirc.com)

.. code:: text

    would display something like =5,10,20,21,32

Compatibility
-------------

.. compatibility:: 7.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dlevel </identifiers/dlevel>`
    * :doc:`$ulevel </identifiers/ulevel>`
    * :doc:`$ulist </identifiers/ulist>`
    * :doc:`/dlevel </commands/dlevel>`

