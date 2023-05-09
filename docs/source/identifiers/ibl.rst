$ibl
====

$ibl returns the Nth address in the internal ban list

Synopsis
--------

.. code:: text

    $ibl(#chan,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #chan
      - the channel you want ban from
    * - N
      - the Nth banned address in the channel, use N = 0 for the total number of address

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .by
      - returns the nickname who set the ban
    * - .date
      - returns the date when the ban was set
    * - .ctime
      - returns the date when the ban was set, in :doc:`$ctime </identifiers/ctime>` format

Example
-------

.. code:: text

    //echo -a $ibl(#,0)

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ialchan </identifiers/ialchan>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$iil </identifiers/iil>`
    * :doc:`$iel </identifiers/iel>`
    * :doc:`$iql </identifiers/iql>`

