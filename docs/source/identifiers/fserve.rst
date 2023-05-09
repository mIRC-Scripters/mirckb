$fserve
=======

The $fserve identifier can be used to gather various details regarding open /fserve command - mIRC|Fserve windows.

Synopsis
--------

.. code:: text

    $fserve(N/nick[,N])[.property]

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
    * - cd
      - The current directory of the Fserve
    * - cid
      - The connection id for this window
    * - hwnd
      - The window handle for this window
    * - idle
      - How long since the remote user sent data
    * - ip
      - The IP Address for the remote user
    * - status
      - The status of the window; returns: active, inactive or waiting
    * - stamp
      - Returns either :doc:`$true </identifiers/true>`, or :doc:`$false </identifiers/false>` depending on if time-stamping is enabled or disabled.
    * - wid
      - The mIRC window id for this window

Example
-------

Echo all open Fserve connections:

.. code:: text

    //echo -a $fserve(0)

Echo the current directory of the 1st Fserve:

.. code:: text

    //echo -a $fserve(1).cd

Compatibility
-------------

.. compatibility:: 6.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chat </identifiers/chat>`
    * :doc:`$get </identifiers/get>`
    * :doc:`$send </identifiers/send>`

