$query
======

$query returns the name of the Nth query window opened.

Synopsis
--------

.. code:: text

    $query(N/nick)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth query window, if N = 0, returns the total number of query window opened.
    * - nick
      - if a nickname is passed, returns the nickname if you have a query window with that nick, $null otherwise.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .addr
      - returns the user address, this value might not be correct, you have to get a message from the user to make sure the address is correct
    * - .logfile
      - returns the file name associated with this query window for logging
    * - .stamp
      - returns the timestamp setting for that query window
    * - .wid
      - returns the window ID of that query window
    * - .cid
      - returns the connection ID of that query window
    * - .hwnd
      - returns the handle of that query window
    * - .idle
      - returns the number of second since a message was sent or received for that query window

Example
-------

.. code:: text

    //echo -a $query(0)

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chan </identifiers/chan>`

