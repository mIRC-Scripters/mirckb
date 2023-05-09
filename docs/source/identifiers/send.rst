$send
=====

$send can be used to gather various details regarding open DCC Send windows.

Synopsis
--------

.. code:: text

    $send(N/nick[,N])[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - N/nick
      - Refers to either the Nth open connection, or the connection associated with a specific user's nickname
    * - [N]
      - If a nickname is specified in the primary parameter, the secondary N targets the Nth connection associated with that nickname match

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - cid
      - The connection id
    * - cps
      - The characters-per-second transfer rate
    * - done
      - Returns :doc:`$true </identifiers/true>` if the transfer has completed, otherwise returns :doc:`$false </identifiers/false>`
    * - file
      - The file name of the current transfer
    * - hwnd
      - The window handle
    * - idle
      - How long since the file transfer has been idle
    * - ip
      - The IP Address for the remote user
    * - path
      - The path of the file name being transferred
    * - pc
      - The percentage complete for the transfer
    * - rcvd
      - The total amount of bytes received so far
    * - resume
      - If the transfer has been resumed, returns the location in the file from where the resume took place
    * - secs
      - The total number of seconds the transfer has been connected
    * - size
      - The file size in bytes for the transfer
    * - status
      - The status of the window; returns: active, failed, sent or waiting
    * - wid
      - The mIRC window id for this window

Example
-------

Echo the total percent completed of the 2nd transfer:

.. code:: text

    //echo -a $send(2).pc

Echo the total number of transfers:

.. code:: text

    //echo -a $send(0)

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chat </identifiers/chat>`
    * :doc:`$fserve </identifiers/fserve>`
    * :doc:`$get </identifiers/get>`

