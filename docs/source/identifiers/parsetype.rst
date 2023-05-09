$parsetype
==========

$parsetype return either "in" or "out" in the :doc:`on parseline </events/on_parseline>` event depending on the nature of the line.

Synopsis
--------

.. code:: text

    $parsetype

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:parseline:*:*:echo -a $parsetype

Compatibility
-------------

.. compatibility:: 7.42

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/parseline </commands/parseline>`
    * :doc:`on parseline </events/on_parseline>`
    * :doc:`$parseline </identifiers/parseline>`

