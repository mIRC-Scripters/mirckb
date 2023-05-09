$opnick
=======

$opnick returns the nickname of a person who was opped/deopped during an :doc:`on op </events/on_op>`, :doc:`on deop </events/on_deop>`, :doc:`on owner </events/on_owner>` and :doc:`on deowner </events/on_deowner>` event.

Synopsis
--------

.. code:: text

    $opnick

Switches
--------

None

Example
-------

A scripted event that will echo the nickname of the person who was just opped to the active window:

.. code:: text

    ON *:OP:#:echo -a $opnick

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on op </events/on_op>`
    * :doc:`on deop </events/on_deop>`
    * :doc:`$hnick </identifiers/hnick>`
    * :doc:`$vnick </identifiers/vnick>`

