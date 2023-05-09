$iql
====

$iql returns the Nth address in the internal quiet list

Synopsis
--------

.. code:: text

    $iql(#chan,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #chan
      - the channel you want quiet from
    * - N
      - the Nth quieted address in the channel, use N = 0 for the total number of address

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .by
      - returns the nickname who set the quiet
    * - .date
      - returns the date when the quiet was set
    * - .ctime
      - returns the date when the quiet was set, in :doc:`$ctime </identifiers/ctime>` format

Example
-------

.. code:: text

    //echo -a $iql(#,0)

Compatibility
-------------

.. compatibility:: 7.48

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ialchan </identifiers/ialchan>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$iil </identifiers/iil>`
    * :doc:`$ibl </identifiers/ibl>`
    * :doc:`$iel </identifiers/iel>`

