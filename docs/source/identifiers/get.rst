$get
====

The $get identifier can be used to gather various details regarding open /dcc command - mIRC|DCC Get windows, even if the transfers completed.

Synopsis
--------

.. code:: text

    $get(N/nick[,N])[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N/nick
      - Refers to either the Nth open connection, or the connection associated with a specific user's nickname
    * - [N]
      - If a nickname is specified in the primary parameter, the secondary N targets the Nth connection associated with that nickname match

When N = 0, $get(N) returns the total number of all transfers, and $get($nick,N) returns total transfers from $nick.
$get($nick) used without the 2nd N parameter returns $nick if there is at least 1 $get or $null if no transfers.
When N >=1, $get(N) or $get($nick,N) returns the $nick associated with that transfer.
When sender changes nick, the $get is still associated with the old nick unless you use: :doc:`/dcc nick -sgcf \<oldnick\> \<newnick\> </commands/dcc>`

.. note:: $get(-1) can be used during the :doc:`on filercvd </events/on_filercvd>` and :doc:`on getfail </events/on_getfail>` events, it refers to the 'get' which triggered that event.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - cid
      - The connection id
    * - cps
      - The characters-per-second transfer rate, averages speed during recent time period until transfer finishes, when rate is averaged across entire connection time
    * - done
      - Returns :doc:`$true </identifiers/true>` if the transfer has completed, otherwise returns :doc:`$false </identifiers/false>`
    * - file
      - The file name of the current transfer
    * - hwnd
      - The window handle
    * - idle
      - the number of seconds that the file transfer has been idle
    * - ip
      - The IP Address for the remote user
    * - path
      - The path of the file name being transferred
    * - pc
      - The percentage complete for the transfer
    * - rcvd
      - The total amount of bytes received so far including the resume offset received during a previous get
    * - resume
      - If the transfer has been resumed, returns the location in the file from where the resume took place. Does not offer a way to discern between a transfer not resumed and a transfer resumed at offset zero
    * - secs
      - The total number of seconds the transfer has been connected
    * - size
      - The file size in bytes for the transfer
    * - status
      - The status of the window; returns: sent, active, failed, received or waiting
    * - wid
      - The mIRC window id for this window

Example
-------

Echo the total percent completed of the 3rd transfer:

.. code:: text

    //echo -a $get(3).pc

Echo the total number of transfers:

.. code:: text

    //echo -a $get(0)

Summary of open /dcc command - mIRC|DCC Get windows:

.. code:: text

    //var %i 1 | while ( %i isnum 1- $get(0) ) { echo -a %i nick: $get(%i) file: $get(%i).file size: $get(%i).size status: $get(%i).status | inc %i }

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chat </identifiers/chat>`
    * :doc:`$fserve </identifiers/fserve>`
    * :doc:`$send </identifiers/send>`

