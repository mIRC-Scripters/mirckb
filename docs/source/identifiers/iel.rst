$iel
====

$iel returns the Nth address in the internal exception list

Synopsis
--------

.. code:: text

    $iel(#chan,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #chan
      - the channel you want exceptions from
    * - N
      - the Nth exception address in the channel, use N = 0 for the total number of address

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .by
      - returns the nickname who set the exception
    * - .date
      - returns the date when the exception was set
    * - .ctime
      - returns the date when the exception was set, in :doc:`$ctime </identifiers/ctime>` format

Example
-------

.. code:: text

    //echo -a $iel(#,0)

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
    * :doc:`$ibl </identifiers/ibl>`
    * :doc:`$iql </identifiers/iql>`

