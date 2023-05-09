$halted
=======

$halted return $true if a previous event used :doc:`/halt </commands/halt>` or :doc:`/haltdef </commands/haltdef>` commands , $false otherwise.

Synopsis
--------

.. code:: text

    $halted

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:text:*:#:echo -a $haltdef

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/halt </commands/halt>`
    * :doc:`/haltdef </commands/haltdef>`
    * :ref:`ampersand-prefix`

