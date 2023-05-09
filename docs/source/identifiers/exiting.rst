$exiting
========

The $exiting identifier returns whether mIRC is exiting, not exiting, or if it is restarting. The identifier is filled with 1, 0, and 2, respectively.

Synopsis
--------

.. code:: text

    $exiting

Returns
-------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - 0
      - mIRC is not exiting
    * - 1
      - mIRC is exiting
    * - 2
      - mIRC is restarting

Example
-------

.. code:: text

    ; Check in an on exit event if mIRC is exiting
    ON *:EXIT:echo -a mIRC is $iif($exiting,$iif($exiting == 1,exiting,restarting),not exiting)

The above example will return the proper condition for whether or not mIRC is exiting. An example output is below:

.. code:: text

    mIRC is not exiting

Compatibility
-------------

.. compatibility:: 7.23

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$starting </identifiers/starting>`
    * :doc:`on exit </events/on_exit>`

