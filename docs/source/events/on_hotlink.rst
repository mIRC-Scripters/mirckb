On Hotlink
==========

The ON HOTLINK event triggers when you use your mouse over a specific word in a line of text in a window.

The ON HOTLINK event is very intensive, in that it monitors and tracks all mouse movements.
Therefore any commands executed in the event must be as quick, efficient, and small as possible. If the commands take too long to proceede, mIRC will begin to lag a great deal.

Synopsis
--------

.. code:: text

    ON <level>:HOTLINK:<matchtext>:<*#?=!@>:<commands>

You can use :doc:`$return </commands/return>` to enable hotlink over the current word and you can :doc:`$halt </commands/halt>` to disable hotlink and allows default processing.

$1 returns the word that matched, stripped from its control code.

.. note:: $hotlink() can be used to get the word that matched with control codes preserved.

The event triggers for various mouse events: sclick, dclick, rclick, mouse, uclick, you can use :doc:`$hotlink </identifiers/hotlink>` to get the mouse event as well as informations about the line number, the word position etc..

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
      - The text that to be matched. Can also be a :ref:`matching_tools-wildcard`.
    * - <*#?=!@>
      - The window type that this event should monitor.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.


.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Window type
      - Description
    * - *
      - Any window
    * - #
      - Any channel, or specific channel name(s)
    * - ?
      - Query windows
    * - =
      - DCC Chat windows
    * - !
      - Fserve windows
    * - @
      - Custom windows

Examples
--------

Monitor all windows for the a word matchting '*hoverme*' and echo to the active window the word that was hovered:

.. code:: text

    ON *:HOTLINK:*hoverme*:*:echo -a $1 was just hovered!

Old on hotlink handling
-----------------------

The event was revamped in mIRC 7.23, before, the event was working somewhat differently from others events:

.. code:: text

    on ^*:HOTLINK:\*help\*:#:{
     if ($1 == helpme) return
     halt
    }
    
    on *:HOTLINK:*:*:echo clicked word $1 in line $hotline $hotlinepos
    
The first ^ event is triggered when you move your mouse over a word that matches *help* in a channel window. You can then check $1 to see if you want the hotlink hand to appear over the word. If you halt the event, no hand will appear. The second non-^ event is triggered when you double-click on a word which has been filtered through the first hotlink event.

This implementation was very limited and is deprecated, :doc:`$hotline </identifiers/hotline>` and :doc:`$hotlinepos </identifiers/hotlinepos>` still work as they should with the new implementation but can be considered somewhat deprecated as the general :doc:`$hotlink </identifiers/hotlink>` now gathers all the precious informations.

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$hotline </identifiers/hotline>`
    * :doc:`$hotlinepos </identifiers/hotlinepos>`
    * :doc:`$hotlink </identifiers/hotlink>`
    * :doc:`/hotlink </commands/hotlink>`

