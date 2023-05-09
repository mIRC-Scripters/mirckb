$cmdbox
=======

The $cmdbox identifier will return :doc:`$true </identifiers/true>` if a command or script was initiated via the ''command editbox''. Otherwise, it will return :doc:`$false </identifiers/false>`.

Synopsis
--------

.. code:: text

    $cmdbox

Parameters
----------

None

Command editbox
---------------

The command editbox is actived by typing the following command in any mIRC window:

.. code:: text

    /editbox -q1

This will enable the secondary command-line, which is the command editbox, in the current window for which this identifier is useful for.

Example
-------

Create a command editbox in the active window:

.. code:: text

    /editbox -q1

Next, type the following in both editboxes, and hit the Enter key:

.. code:: text

    //echo -a $cmdbox

Depending on which window you performed this on first, the echo will show either :doc:`$true </identifiers/true>`, or :doc:`$false </identifiers/false>`.

Compatibility
-------------

.. compatibility:: 6.01

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/editbox </commands/editbox>`

