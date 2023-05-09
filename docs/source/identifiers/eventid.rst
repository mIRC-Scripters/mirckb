$eventid
========

The $eventid is a local identifier which is filled with a unique ID inside any event in mIRC. This identifier allows scripters to use ''SendMessage()'' in an event context, in order to evaluate local identifiers (such as :doc:`$nick </identifiers/nick>` inside an :doc:`on text </events/on_text>` event). Theoretically, this unique ID can be used for anything.

Synopsis
--------

.. code:: text

    $eventid

Example
-------

Compatibility
-------------

.. compatibility:: 7.33

