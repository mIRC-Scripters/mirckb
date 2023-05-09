$modelast
=========

$modelast return $true if the channel event is the last to trigger, $false otherwise.

Synopsis
--------

.. code:: text

    $modelast

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
      echo -a $modelast
    }

And send /mode #channel +oo nick1 nick2

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$modefirst </identifiers/modefirst>`
    * :doc:`$modespl </identifiers/modespl>`

