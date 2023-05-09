$newnick
========

$newnick is filled when the :doc:`on nick </events/on_nick>` event is triggered on a channel when either a remote user changes their nickname on a channel, or the local mIRC client has changed its nickname.

Synopsis
--------

.. code:: text

    $newnick

Parameters
----------

None

Example
-------

Echo to the channel when the local nickname is changed, and halt mIRC's default message:

.. code:: text

    ON ME:^*:NICK: {
      echo $chan You are now ==> $newnick
    
      ; Halt the default mIRC message
      haltdef
    }

The example above should have an output resembling the following:

.. code:: text

    You are now ==> whoMe

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on join </events/on_join>`
    * :doc:`on mode </events/on_mode>`
    * :doc:`on part </events/on_part>`

