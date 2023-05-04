/hotlink
========

The **/hotlink** command can be used to override the default popups menu when right clicking a word and triggering the :doc: `on hotlink </events/on_hotlink>` event.

Synopsis
--------

.. code:: text

    /hotlink -md [@menu]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -m
      - Creates a custom popup menu using a custom @menu
    * - -d
      - If you are rightclicking a type recognized by mIRC (such as an url, a nickname, or a channel), it adds the default popups for that type to the final popups menu

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - @menu
      - a custom menu to be used for the popup menu (only needed if you use -m)

Example
-------

1) Add a right click menu item to look up commands and identifiers in the help file on mouse hover of /command and $identifier.

.. code:: text

    menu @helppop {
    Lookup Help $1:!help $remove($1, $chr(40), $chr(41))
    }
    on $*:hotlink:/^[/$]\S+/:*:{
    if ($hotlink(event) == rclick) {
    hotlink -m @helppop
    }
    }

2) Override mIRC's default popups for nickname and replace them with... mIRC's default popups! (useless but that's to show /hotlink -d, this isn't handling /return or halt to show the hand)

.. code:: text

    on *:hotlink:*:*:{
    if ($hotlink(event) $hotlink(match).type == rclick nick) {
    ;no @menu with -d
    hotlink -d
    }
    }

Compatibility
-------------

Added: mIRC v7.23 (19 Mar 2012)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$hotline </identifiers/$hotline>`
    * :doc: `$hotlinepos </identifiers/$hotlinepos>`
    * :doc: `$hotlink </identifiers/$hotlink>`
    * :doc: `on hotlink </events/on_hotlink>`
