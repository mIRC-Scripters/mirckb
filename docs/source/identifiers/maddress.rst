$maddress
=========

$maddress return the address that was matched for the event, or returns information about the user list.

Synopsis
--------

.. code:: text

    $maddress

.. code:: text

    $maddress(<address>,[L,<N>])
.. attention:: This feature has essentially been replaced by :doc:`$ulist </identifiers/ulist>`

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <address>
      - the address used to match, you can specify * for all address, non complete address are completed with wildcards
    * - L
      - if you specify L, only matching addresses that contain the specified level L are returned. Optional, but if you provide L, you must provide N below
    * - N
      - returns the Nth match, optional.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .info
      - returns information about that user in the user list

Example
-------

To get the address from the event:

.. code:: text

    on *:text:*:#:echo -a $maddress

And for the user list: 

.. code:: text
    
    //echo -a $maddress(*,1)

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fulladdress </identifiers/fulladdress>`
    * :doc:`$wildsite </identifiers/wildsite>`
    * :doc:`$site </identifiers/site>`
    * :doc:`$ulist </identifiers/ulist>`

