$parms
======

The $parms identifier is a non tokenize version of the $1- identifier, effectively preserving spaces. It works everywhere where $1- can be used.

Synopsis
--------

.. code:: text

    $parms

Properties
----------

None

Examples
--------

.. code:: text

    ;Execute in mIRC's editbox with a single slash: /testingparms a   b
    alias testingparms echo -a $len($1-) -- $len($parms)

Compatibility
-------------

.. compatibility:: 7.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$1- </identifiers/dollar1dash>`

