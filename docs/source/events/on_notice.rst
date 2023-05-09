On Notice
=========

The on notice event is triggered when mIRC receives a notice from a client on the server.

Synopsis
--------

.. code:: text

    ON <level>:NOTICE:<matchtext>:<target>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <matchtext>
      - The text that to be matched. Much like the :doc:`on text </events/on_text>` event, this can be any combination of text letters, numbers, and wildcards.
    * - <target>
      - The target(s) of the notice that the event listens on. This can either be a \*, or any combination of named channels, channel prefixes, ?, or a nickname that you are currently using - all separated by commas.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

Give a person "500 points" for sending a secret command:

.. code:: text

    on *:NOTICE:thesecretcommand:?:{
      .notice $nick Congratulations! You have entered the secret command!
      .notice $nick Please accept these free 500 points...
      hinc -m $+(points.,$network) $wildsite 500
    }

Op or deop a user with an Mirc access level|access level of 5 on the channel they specify:

.. code:: text

    on 5:NOTICE:*op #*:?:{
      if ($istok(op dop,$1,32)) {
        if ($me !ison $2) { .notice $nick I am not on that channel. }
        elseif ($me !isop $2) { .notice $nick I am not opped in that channel. } 
        else mode $2 $iif($1 == op,+o,-o) $nick
      }
    }

Automatically identify to most NickServ services if your current nickname is TheUsualNick:

.. code:: text

    on *:NOTICE:This nickname is registered*:TheUsualNick:{
      if ($nick == NickServ) { ns identify M`/p@SsW0r|) }
    }

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

