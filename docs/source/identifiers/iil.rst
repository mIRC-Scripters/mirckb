$iil
====

$iil returns the Nth address in the internal invite list

Synopsis
--------

.. code:: text

    $iil(#chan,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #chan
      - the channel you want invite from
    * - N
      - the Nth invite address in the channel, use N = 0 for the total number of address

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .by
      - returns the nickname who set the invite
    * - .date
      - returns the date when the invite was set
    * - .ctime
      - returns the date when the invite was set, in :doc:`$ctime </identifiers/ctime>` format

Example
-------

.. code:: text

    //echo -a $iil(#,0)

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ialchan </identifiers/ialchan>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$ibl </identifiers/ibl>`
    * :doc:`$iel </identifiers/iel>`
    * :doc:`$iql </identifiers/iql>`

