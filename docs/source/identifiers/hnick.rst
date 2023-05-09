$hnick
======

$hnick returns the nickname of a person who was being helped/dehelped during an [[On help - mIRC|ON HELP Event] or an On dehelp - mIRC|ON DEHELP Event].

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

* On help - mIRC|ON HELP Event
* On dehelp - mIRC|ON DEHELP Event
    * :doc:`$opnick </identifiers/opnick>`
    * :doc:`$vnick </identifiers/vnick>`

