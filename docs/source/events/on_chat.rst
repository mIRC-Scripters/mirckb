On Chat
=======

The ON Chat event, much like the On serv - mIRC|ON Serv event, is triggered when a message is sent via a :doc:`dcc chat </commands/dcc>` window.

Synopsis
--------

.. code:: text

    ON <level>:CHAT:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <matchtext>
      - The corresponding matchtext for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Local identifiers
-----------------

You can use :doc:`=$nick </identifiers/nick_identifier>` to refer to the dcc chat window, rather than a query window.

Examples
--------

.. code:: text

    ; This event waits for any user on a DCC Chat to use the
    ; command !time and then relays back to them the current time
    
    ON *:CHAT:!time:msg =$nick The current time is: $time(hh:nntt)

In the above example, the message is sent to the dcc chat window

Compatibility
-------------

.. compatibility:: 3.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on serv </events/on_serv>`
    * :doc:`on text </events/on_text>`

