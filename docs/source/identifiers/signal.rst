$signal
=======

$signal returns the name of the signal that caused the signal event to trigger.

Synopsis
--------

.. code:: text

    $signal

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:signal:test:{
      echo -a $signal
    }
//signal test

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on signal </events/on_signal>`
    * :doc:`/signal </commands/signal>`

