$hotlink
========

$hotlink returns informations about what triggered the :doc:`on hotlink </events/on_hotlink>` event.

Synopsis
--------

.. code:: text

    $hotlink(item)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - item
      - the type of information you want, can be:
** word - returns the full word which matched the expression and triggered the event, same as $1, except that $hotlink(word) does not strip the word from control code
** match - returns the part of the word that was used for a comparison to gives the type of match. For example if you hover an operator on a channel with the word "<@nick>", $hotlink(match) is "nick" where $hotlink(word) is "<@nick>"
** event - returns the mouse event which triggered the :doc:`on hotlink </events/on_hotlink>` event, can be "mouse", "sclick", "uclick", "dclick", or "rclick"
** line - returns the full line which triggered the :doc:`on hotlink </events/on_hotlink>` event.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .pos
      - the .pos property can only be used with "line", "word" and "match" items:
** $hotlink(line).pos - returns the line's number in the window
** $hotlink(word).pos - returns the Nth token number of the word in the line (Nth word)
** $hotlink(match).pos - returns the position/index of the matching word in the line (Nth character), starting with an index count of 0.
*.type - used only with "match" item, returns the type of match, can be "nick", "channel", "url" and "other"

Example
-------

.. code:: text

    on *:hotlink:*:*:echo -a $hotlink(match)

Compatibility
-------------

.. compatibility:: 7.24

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hotlink </commands/hotlink>`
:doc:`on hotlink </events/on_hotlink>`

