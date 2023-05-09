On Unban
========

The ON UNBAN event is triggered much like the :doc:`on ban </events/on_ban>` event, however it triggers when a ban is removed from a channel's ban list.

Synopsis
--------

.. code:: text

    ON <level>:UNBAN:<#[,#]>:<commands>

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
      - The channel name(s) where the ban was removed.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

.. code:: text

    ; Unban event that listens on all channels
    ; and responds by messaging the channel.
    
    ON *:UNBAN:#:msg # Hey, look, the address $banmask was just removed from the channel's ban list!

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$banmask </identifiers/banmask>`
    * :doc:`$bnick </identifiers/bnick>`
    * :doc:`$ibl </identifiers/ibl>`
    * :doc:`/ban </commands/ban>`
    * :doc:`on ban </events/on_ban>`

