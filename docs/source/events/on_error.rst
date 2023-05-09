On Error
========

The ON ERROR event is triggered when an server sends an error message, most-likely a disconnect message.

Synopsis
--------

.. code:: text

    ON <level>:ERROR:<matchtext>:<commands>

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
      - The commands to be performed when the event triggers

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - $N
      - Returns the error message.

Example
-------

This example will trigger if the response ''full'' is in the server-returned error:

.. code:: text

    ON *:ERROR:\*full\*:echo -s This server is most-likely full. Server sent error: $1-

This example triggers if the word ''ban'' is within the server error:

.. code:: text

    ON *:ERROR:\*ban\*:echo -s You're most-likely banned from this server. Server sent error: $-

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on close </events/on_close>`
    * :doc:`on connect </events/on_connect>`
    * :doc:`on disconnect </events/on_disconnect>`
    * :doc:`on exit </events/on_exit>`

