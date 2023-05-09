$date
=====

$date can be used to return the current date in day/month/year format.

Synopsis
--------

.. code:: text

    $date
    $date(time[,format])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
* time Optional ctime number. Default when not used is the current ctime
* format Optional format letters same as :doc:`$asctime </identifiers/asctime>`

.. note:: This identifier has identical syntax as $asctime. The only difference is the default displayed time when no format string is used.

Example
-------

.. code:: text

    Echo today's full date to the active window in dd/mm/yyyy format
    //echo -a $date
    Echo only the year-month for the specified ctime number
    //echo -a $date(1234567890,yyyy-mm)

Compatibility
-------------

.. compatibility:: 3.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`$fulldate </identifiers/fulldate>`
    * :doc:`$adate </identifiers/adate>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$day </identifiers/day>`
    * :doc:`$daylight </identifiers/daylight>`
    * :doc:`$timezone </identifiers/timezone>`
    * :doc:`$duration </identifiers/duration>`
    * :doc:`$uptime </identifiers/uptime>`
