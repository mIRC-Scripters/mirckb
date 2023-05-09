$ulist
======

$ulist returns the Nth address in the Users list that matches the specified address and level.

.. note:: $ulist also returns entries in the  Users list which are just nickname

Synopsis
--------

.. code:: text

    $ulist(nick!userid@address,L,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - nick!userid@address
      - the address used to match, you can specify a :ref:`matching_tools-wildcard` address. If you don't specify a full address, it completes with :ref:`matching_tools-wildcard`.
    * - L
      - if you provide this parameter, it must be a level number and only matching addresses that contain the specified level are returned
    * - N
      - The Nth matching address, default to 1. if N is 0, returns the total number of queued line.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .info
      - return the information string used in :doc:`/auser </commands/auser>` for example.

Example
-------

.. code:: text

    //echo -a $ulist(*,,0)

Compatibility
-------------

.. compatibility:: 5.41

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/auser </commands/auser>`
    * :doc:`/flush </commands/flush>`
    * :doc:`/guser </commands/guser>`
    * :doc:`/ruser </commands/ruser>`
    * :doc:`/rlevel </commands/rlevel>`
    * :doc:`/iuser </commands/iuser>`
    * :doc:`/ulist </commands/ulist>`
