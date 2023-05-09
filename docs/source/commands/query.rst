/query
======

The /query command opens a query window to the specified nickname. If a message is provided, it is sent.

Synopsis
--------

.. code:: text

    /query -nxmd <nick> [message]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - n
      - Minimize the window (existing or while opening new)
    * - x
      - Maximize the window (existing or while opening new) (return to normal state with /window -r nick)
    * - m
      - Open new window as mdi (default)
    * - d
      - Open new window as desktop

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [msg]
      - If specified, sends the message.

Example
-------

None

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/msg </commands/msg>`
    * :doc:`/notice </commands/notice>`
    * :doc:`/queryrn </commands/queryrn>`
    * :doc:`$query </identifiers/query>`
