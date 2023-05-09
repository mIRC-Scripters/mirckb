On Invite
=========

The ON INVITE event triggers when a user sends the mIRC client and invite to a specific channel.

Synopsis
--------

.. code:: text

    ON <level>:INVITE:<#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <#[,#]>
      - The channel or channels for which the event occurred.
    * - #
      - If no channel mentioned, targets all channels; otherwise, a specific channel.
    * - [,#]
      - Can be used to specify multiple, literal channel targets.</div>
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

Echo to the active window the user and channel of the invite details:

.. code:: text

    ON *:INVITE:#:echo -a $nick has extended an invite to $chan

Automatically join the channel from the invite:

.. code:: text

    ON *:INVITE:#:join $chan

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on notice </events/on_notice>`
    * :doc:`on text </events/on_text>`

