$link
=====

$link returns the Nth item in the server Links window (called Links List), which can be retrieved with :doc:`/links </commands/links>`.

Synopsis
--------

.. code:: text

    $link(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth link in the Links list window, if N is 0, returns the total number of links.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .addr
      - returns the address of the server, same as $link(N) without property (default)
    * - .ip
      - returns the Ip associated with the server, if any
    * - .level
      - returns the level for that server
    * - .info
      - returns informations about that server.

Example
-------

.. code:: text

    //echo -a $link(0)

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/links </commands/links>`

