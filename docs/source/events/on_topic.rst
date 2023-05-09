On Topic
========

The ON TOPIC event triggers in a channel when the topic is changed.

This event fills :doc:`$1- </identifiers/dollar1dash>` with the new channel topic text.

Synopsis
--------

.. code:: text

    ON <level>:TOPIC:<#[,#]>:<commands>

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
      - The channel, or channels to target. Leave as # to target all channels.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Send an action to a channel when the topic is changed:

.. code:: text

    ON *:TOPIC:#:action $chan approves of this new topic!

.. code:: text

    ON *:TOPIC:#:action $chan approves of this new topic!
    echo 4 $chan topic for # set by $nick to ' $+ $eventparms $+ '

.. note:: # and $chan are interchangeable. $parms or $eventparms preserve leading/trailing/consecutive spaces. Otherwise can use $1-

Compatibility
-------------

.. compatibility:: 5.7

See also
--------
