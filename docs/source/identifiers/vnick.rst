$vnick
======

$vnick returns the nickname of a person who was voiced/devoiced during an :doc:`on voice </events/on_voice>` or an :doc:`on devoice </events/on_devoice>` event.

Synopsis
--------

.. code:: text

    $vnick

Parameters
----------

None

Properties
----------

None

Example
-------

A scripted event that will echo the nickname of the person who was just voiced to the active window:

.. code:: text

    ON *:VOICE:#:echo -a $vnick

Compatibility
-------------

.. compatibility:: 4.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on voice </events/on_voice>`
    * :doc:`on devoice </events/on_devoice>`
    * :doc:`$hnick </identifiers/hnick>`
    * :doc:`$opnick </identifiers/opnick>`

