On Ban
======

The ON BAN event is triggered whenever a user on a channel has been banned.

Synopsis
--------

.. code:: text

    ON <level>:BAN:<*,#[,#]>:<commands>

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
    * - <*><#[,#]>
      - The place, or places where the event listens, you can seperate them by comma.
        * \* - Any channel window
        * # - Any channel window
        * #channel[,#] - one or more specific channels, seperate them by comma
    * - <commands>
      - The commands to be performed when the event triggers

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$banmask </identifiers/banmask>`
      - Returns the banmask used to ban the user.
    * - :doc:`$bnick </identifiers/bnick>`
      - Returns the nickname of the user being banned. It is important to note that :doc:`$bnick </identifiers/bnick>` is not always filled, as some bans don't always contain the nickname.

Comparing levels
----------------

You can compare the levels of the banner and the banned by prefixing the line with <, >, <=, =>, <> (different than), or =, in the following way:

.. code:: text

    on >=2:BAN:#mIRC:/msg $chan $nick banned $banmask (legal)
    on 1:BAN:#mIRC:/msg $chan $nick banned $banmask (illegal)

In this situation, if the banners level is larger than or equal to the banned users level, then it is a legal ban.

Otherwise, it defaults to the second ON BAN line which indicates that it is an illegal ban. Remember, this is comparing the banners and banned users levels and has nothing to do with the level 2 in the definition.

Remember that $banmask is usually a :ref:`matching_tools-wildcard` string which means that it will match both wildcard and non-wildcard user strings in your remote users section.

Examples
--------

.. code:: text

    ; This ban event listens for a ban
    ; on all channels, and responds by messaging the channel.
    
    ON *:BAN:#:msg # Looks like the address $banmask has just been added to this channel's ban list.

.. code:: text

    ; This example will watch for a ban on two
    ; specific channels: #myChannel and #myOtherChannel. When a ban is
    ; noticed, the script will also attempt to find out if a $bnick was set.
    ; If it was not, it will use it, otherwise it will use $banmask.
    
    ON *:BAN:#myChannel,#myOtherChannel:msg # Wow, so $iif($bnick,$bnick just got in trouble,$banmask was just added to the channel's ban list) $+ .

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
    * :doc:`on unban </events/on_unban>`

