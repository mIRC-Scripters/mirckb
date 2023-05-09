$vcmdver
========

$vcmdver is used to retrieve the version of your installed Speech Recognition software.

Synopsis
--------

.. code:: text

    $vcmdver

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
    * - vN.NN
      - The vN.NN would be replaced with the actual version number your Speech Recognition software returns to mIRC.
    * - $null
      - You do not have Speech Recognition software installed.

Examples
--------

Echo the current version of your Speech Recognition software to the active window:

.. code:: text

    //echo -a $vcmdver

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
    * :doc:`$vcmdstat </identifiers/vcmdstat>`
    * :doc:`on vcmd </events/on_vcmd>`

