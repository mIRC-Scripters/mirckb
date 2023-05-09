$chat
=====

The $chat identifier can be used to gather various details regarding open /dcc command - mIRC|DCC Chat windows.

Synopsis
--------

.. code:: text

    $chat(N/nick[,N])[.property]

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
      - Refers to either the Nth open DCC Chat connection, or the connection associated with a specific user's nickname
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
      - The connection id for the DCC Chat
    * - hwnd
      - The window handle for the DCC Chat
    * - idle
      - How long since the remote user sent data
    * - ip
      - The IP Address for the remote user
    * - status
      - The status of the DCC Chat; returns: active, inactive or waiting
    * - stamp
      - Returns either :doc:`$true </identifiers/true>`, or :doc:`$false </identifiers/false>` depending on if time-stamping is enabled or disabled.
    * - wid
      - The mIRC window id for the DCC Chat

Example
-------

Echo the IP Address of the 3rd open DCC Chat window, if any:

.. code:: text

    //echo -a $chat(3).ip

Echo if time-stamping is currently enabled on the 1st DCC Chat:

.. code:: text

    //echo -a $chat(1).stamp

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fserve </identifiers/fserve>`
    * :doc:`$get </identifiers/get>`
    * :doc:`$send </identifiers/send>`

