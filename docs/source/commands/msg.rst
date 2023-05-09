/msg
====

The /msg command sends a message to a specific channel or person. Many networks support multi-target messages - mIRC will not display the message in all the targets like it would with individual messages.

Synopsis
--------

.. code:: text

    /msg <nickname/channel> <message>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - activate/show the window
    * - -x
      - maximize the window
    * - -n
      - minimize the window
    * - -d
      - open new window as desktop

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nickname/channel>
      - The target channel or person for the message, use the form "=<nickname>" to reference a dcc window, =$nick is accepted.
    * - <message>
      - The message to be sent

Example
-------

Example 1
^^^^^^^^^

.. code:: text

    on *:text:!moo:#:{
      ; Message the channel moos back
      msg $chan moos back
    }

Example 2
^^^^^^^^^

.. code:: text

    /* Example 2
    */
    on ^*:open:?:{
      if ($away) {
        msg $nick I am currently away ( $+ $awaymsg $+ ), please leave me a memo: /ms send $me <memo>
      }
      halt
    }

Example 3
^^^^^^^^^

Using the equals sign to send ''SomeUser'' a message via DCC/FSERVE Chat

.. code:: text

    //msg =SomeUser Hey there, this is going to your open DCC/FSERVE Chat window, instead!

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ame </commands/ame>`
    * :doc:`/amsg </commands/amsg>`
    * :doc:`/describe </commands/describe>`
    * :doc:`/me </commands/me>`
    * :doc:`/qme </commands/qme>`
    * :doc:`/qmsg </commands/qmsg>`
    * :doc:`/say </commands/say>`

