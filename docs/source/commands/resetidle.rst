/resetidle
==========

The /resetidle command  resets the :doc:`$idle </identifiers/idle>` identifier to zero or to the number of seconds you specify.

Synopsis
--------

.. code:: text

    /resetidle [seconds]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [seconds]
      - If specified, reset the $idle idenfifier to that number of seconds.

Example
-------

.. code:: text

    /resetidle 5

Compatibility
-------------

.. compatibility:: 5.31

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$idle </identifiers/idle>`

