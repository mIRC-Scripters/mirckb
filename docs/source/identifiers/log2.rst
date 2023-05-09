$log2
=====

$log2 returns the common logarithm (base 2) of a number

Details
-------

.. note:: for window logging please see :doc:`/log </commands/log>` :doc:`/logview </commands/logview>` :doc:`/loadbuf </commands/loadbuf>` :doc:`/savebuf </commands/savebuf>` :doc:`$logdir </identifiers/logdir>`  :doc:`$window().logfile </identifiers/window>`

Synopsis
--------

.. code:: text

    $log2(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Number for which to return its common logarithm

Properties
----------

None

Example
-------

.. code:: text

    //echo -a except for precision rounding 2^ $log2(7) is 7
    //echo -a $log2(7) is $log(7) / $log(2)

Compatibility
-------------

.. compatibility:: 7.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$log </identifiers/log>`
    * :doc:`$log10 </identifiers/log10>`
