$starting
=========

$starting return 1 in the :doc:`on start </events/on_start>` event if mIRC is really starting, (on start could trigger after a /load command), 0 otherwise.

Synopsis
--------

.. code:: text

    $starting

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:start:{
      echo -s $starting
    }

Compatibility
-------------

.. compatibility:: 7.23

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$exiting </identifiers/exiting>`
    * :doc:`on start </events/on_start>`

