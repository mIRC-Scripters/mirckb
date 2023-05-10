$hotlinepos
===========

.. attention:: This feature has essentially been replaced by :doc:`$hotlink </identifiers/hotlink>`

The $hotlinepos identifier returns the line number and the position of the word in that line that triggered an an :doc:`on hotlink </events/on_hotlink>` event.

Synopsis
--------

.. code:: text

    $hotlinepos

Parameters
----------

None

Example
-------

.. code:: text

    ON *:HOTLINK:\*hoverme\*:*:if ($1 == hoverme) echo -s $hotlinepos

Compatibility
-------------

.. compatibility:: 6.15

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on hotlink </events/on_hotlink>`
    * :doc:`$hotline </identifiers/hotline>`
    * :doc:`$hotlink </identifiers/hotlink>`

