$modefirst
==========

$modefirst return :doc:`$true </identifiers/true>` if the channel event is the first to trigger, :doc:`$false </identifiers/false>` otherwise.

Synopsis
--------

.. code:: text

    $modefirst

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:op:#:{
      echo -a $modefirst
    }
and send /mode #channel +oo nick1 nick2

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$modelast </identifiers/modelast>`
    * :doc:`$modespl </identifiers/modespl>`

