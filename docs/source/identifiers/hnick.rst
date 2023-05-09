$hnick
======

$hnick returns the nickname of a person who was being helped/dehelped during an :doc:`on help </events/on_help>` event or an :doc:`on dehelp </events/on_dehelp>` event.

Synopsis
--------

.. code:: text

    $hnick

Switches
--------

None

Example
-------

A scripted event that will echo the nickname of the person who was just helped to the active window

.. code:: text

    ON *:HELP:#:echo -a $hnick

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on help </events/on_help>`
    * :doc:`on dehelp </events/on_dehelp>`
    * :doc:`$opnick </identifiers/opnick>`
    * :doc:`$vnick </identifiers/vnick>`

