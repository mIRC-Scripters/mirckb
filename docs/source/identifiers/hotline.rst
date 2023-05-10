$hotline
========

.. attention:: This feature has essentially been replaced by :doc:`$hotlink </identifiers/hotlink>`

The $hotline identifier returns the entire line of text that matched for an :doc:`on hotlink </events/on_hotlink>` event.

Synopsis
--------

.. code:: text

    $hotline

Parameters
----------

None

Example
-------

The below example will trigger when the mouse double-clicks on the word ``hoverme``, and echo the hotlink word and the entire line to the active window:

.. code:: text

    ON ^*:HOTLINK:\*hoverme\*:*:{
      if ($1 == hoverme) return
      halt
    }
    ON *:HOTLINK:\*hoverme\*:*:echo -a Hotlink: $1 - Hotlink line: $hotline

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on hotlink </events/on_hotlink>`
    * :doc:`$hotlinepos </identifiers/hotlinepos>`
    * :doc:`$hotlink </identifiers/hotlink>`

