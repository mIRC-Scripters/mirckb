$speak
======

$speak returns the Nth line currently queued via the :doc:`/speak </commands/speak>` command.

Synopsis
--------

.. code:: text

    $speak(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth line queued, if N is 0, returns the total number of queued line.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $speak(0)

Compatibility
-------------

.. compatibility:: 7.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/speak </commands/speak>`

