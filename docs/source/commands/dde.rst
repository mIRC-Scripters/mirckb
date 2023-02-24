/dde
====

**Dynamic Data Exchange** (**DDE**) is a form of communication between two applications on a windows machine. The **/dde** command can be used to create a dde connection with a dde server. When the topic parameter is required, you can use empty quotes ("") to indicate a blank topic.

Transactions
------------
The dde command support three different types of transactions:


.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Transaction
      - Description
    * - XTYP_POKE
      - Used by default, sends unsolicited data to the server.
    * - XTYP_REQUEST
      - Used to request data from a server.
    * - XTYP_EXECUTE
      - Used to send a command string to the server.

The only time the [data] parameter is required is when the XTYP_POKE transaction type is used.

Synopsis
--------

.. code:: text

    /dde [-re] <service> <topic> <item> [data]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - uses XTYP_REQUEST transaction
    * - -e
      - uses XTYP_EXECUTE transaction

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <service>
      - DDE Server service name
    * - <topic>
      - DDE Topic
    * - <item>
      - DDE Item
    * - [data]
      - Data to be sent

Example
-------

.. code:: text

    ;Open a new tab in opera, navigate to www.zigwap.com/mirc/
    /dde -e Opera WWW_OpenURL "www.zigwap.com/mirc/"

Compatibility
-------------

Added: mIRC v3.9 (28 Dec 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dde </identifiers/dde>`
    * :doc:`$isdde </identifiers/isdde>`
    * :doc:`$ddename </identifiers/ddename>`
    * :doc:`/ddeserver <ddeserver>`