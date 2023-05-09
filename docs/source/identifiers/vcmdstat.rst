$vcmdstat
=========

$vcmdstat can be used to get the current status of the voice command listener for mIRC.

Synopsis
--------

.. code:: text

    $vcmdstat

Parameters
----------

None

Properties
----------

None

Results
-------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Description
    * - 0
      - Service is not available.
    * - 1
      - Service is currently off.
    * - 2
      - Service is ignoring commands.
    * - 3
      - Service is on, and listening for commands.

Examples
--------

Echo the status of the voice command listener to the active window:

.. code:: text

    //echo -a $vcmdstat

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/vcadd </commands/vcadd>`
    * :doc:`/vcmd </commands/vcmd>`
    * :doc:`/vcrem </commands/vcrem>`
    * :doc:`$vcmd </identifiers/vcmd>`
    * :doc:`$vcmdver </identifiers/vcmdver>`
    * :doc:`on vcmd </events/on_vcmd>`

