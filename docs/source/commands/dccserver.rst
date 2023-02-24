/dccserver
==========

The **/dccserver** commands lets you turn DCC server on or off. The dccserver can also be used to change the default mIRC DCC Server port. Using + or - you can add/remove listening for send, chat, and/or fserver.

.. note:: By default mIRC DCC Server operates on port 59.

Synopsis
--------

.. code:: text

    /dccserver [[+-]scf] [on|off] [port]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - +s
      - Listen for send
    * - +c
      - Listen for chat
    * - +f
      - Listen for fserver
    * - -s
      - Don't listen for send
    * - -c
      - Don't listen for chat
    * - -f
      - Don't listen for fserver

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [on|off]
      - turn dcc server on/on
    * - [port]
      - change port number

Example
-------

.. code:: text

    /dccserver off

.. code:: text

    * DCC Server is off

.. code:: text

    ;send/chat no fserver
    /dccserver +sc-f on

.. code:: text

    * DCC Server is on (59,Send,Chat)

.. code:: text

    ;fserver only, port 500
    /dccserver +f-sc on 500

.. code:: text

    * DCC Server is on (500,Fserve)

Compatibility
-------------

Added: mIRC v5.1 (28 Aug 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dccport </identifiers/dccport>`
    * :doc:`$dccignore </identifiers/dccignore>`
    * :doc:`/dcc <dcc>`