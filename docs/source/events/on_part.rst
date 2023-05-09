On Part
=======

The ON PART event triggers when the mIRC client, or a remote user, parts/leaves a channel.

Synopsis
--------

.. code:: text

    ON <level>:PART:<#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <#,[,#]>
      - The text that to be matched. Can also be a :ref:`matching_tools-wildcard`.
    * - [,#]
      - Specific channel names
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

Once the local mIRC client has left a channel, echo to the channel window the total users inside of the channel:

.. code:: text

    ON ME:*:PART:#:echo # You have left # $+ .

The above example makes use of the on me - mIRC|ON ME event, which triggers only when the local mIRC client triggers the event, not remote users.

When a user leaves, send them a notice:

.. code:: text

    ON *:PART:#:msg # So sorry to see you go, $nick $+ !

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on join </events/on_join>`

