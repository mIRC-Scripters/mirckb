/updatenl
=========

The **/updatenl** command can be used with the on quit/kick/part events to update the IAL and the channel nicknames list right away, otherwise, these are updated when the scripts finish

Synopsis
--------

.. code:: text

    /updatenl

Switches
--------

None

Parameters
----------

None

Example
-------

Let's suppose only A, B and C are in the channel #example. Suddendly, B parts.
If we have this event, only triggering when $nick == $me (using the ! event prefix):

.. code:: text

    on !*:part:#example:{
    echo -a $nick($chan,0)
    } Can you guess the value of $nick($chan,0)? It will be 3, because the update are made after.

Now we change the event to:

.. code:: text

    on !*:part:#example:{
    echo -a $nick($chan,0)
    updatenl
    echo -a $nick($chan,0)
    } Which would echo 3 and 2.

Compatibility
-------------

Added: mIRC v5.4 (24 Jul 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on kick </events/on_events/on_kick>`
    * :doc:`on quit </events/on_events/on_quit>`
    * :doc:`on part </events/on_events/on_part>`
