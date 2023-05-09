On Nick
=======

The ON NICK event triggers when a user is on the same channel as you, and they change their nickname.

This event fills the :doc:`$newnick </identifiers/newnick>` and :doc:`$nick </identifiers/nick>` identifiers.


.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - $newnick
      - The new nickname of the user. You can use it with $comchan for example.
    * - $nick
      - The user's previous nickname.

Synopsis
--------

.. code:: text

    ON <level>:NICK:<commands>

Example
-------

Echo the nickname change, and disregard mIRC's default nick change message:

.. code:: text

    ON ^*:NICK: {
      echo $comchan($newnick,1) * $nick |==> $newnick
    
      ; Halt the default mIRC message
      haltdef
    }

The results of the above example resemble the following:

.. code:: text

    * Mr_SOCKS |==> noLaundry

Echo to the channel when the local nickname is changed, and halt mIRC's default message:

.. code:: text

    ON ME:^*:NICK: {
      echo $comchan($newnick,1) You are now ==> $newnick
    
      ; Halt the default mIRC message
      haltdef
    }

The example above should have an output resembling the following:

.. code:: text

    You are now ==> whoMe

.. code:: text

    Because ON NICK is not associated with # or $chan, to show a nick change message in all channels you share with that nick, you can use $comchan. You can simulate mIRC's default Nick Change message in channels with:
    
    ON ^*:NICK:{
      var %i $comchan($newnick,0)
      while (%i) {
        echo -ctg nick $chan(%i) * # $iif($nick == $me,Your nick # is now,$nick is now known as) $newnick
        dec %i
      }
     ; You can precede HALTDEF with a semi-colon to compare this messages with the default
     haltdef
    }

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
    * :doc:`$newnick </identifiers/newnick>`
    * :doc:`$nick </identifiers/nick>`

