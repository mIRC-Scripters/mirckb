$dname
======

The $dname identifier is used within an On dialog - mIRC|ON DIALOG event to get the name of the dialog that triggered the event.

Synopsis
--------

.. code:: text

    $dname

Parameters
----------

None

Example
-------

When any dialog opens, echo the name of the dialog to the active window:

.. code:: text

    ON *DIALOG:*:init:0:echo -a $dname

Compatbility
------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$devent </identifiers/devent>`
    * :doc:`$did </identifiers/did>`
    * :doc:`$didwm </identifiers/didwm>`
    * :doc:`$didreg </identifiers/didreg>`
    * :doc:`$didtok </identifiers/didtok>`
    * :doc:`/dialog </commands/dialog>`
    * :doc:`/did </commands/did>`
    * :doc:`/didtok </commands/didtok>`