$uptime
=======

$uptime returns the number of milliseconds since the indicated event.

Synopsis
--------

.. code:: text

    $uptime(<mirc> | <server> | <system>[,N])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - mIRC
      - The time period counts since mIRC started
    * - server
      - The time period counts since connected to that server.
    * - system
      - The time period counts since windows booted up.

Optional Parameter N is an integer 0-3:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - 0
      - Default. Returns time as an integer number of milliseconds
    * - 1
      - Instead of returning time as an integer number of milliseconds, is Ndays Nhrs Nmins Nsecs
    * - 2
      - Same as N 1 except omits the Nsecs
    * - 3
      - Same as N 0, except returns number of seconds, dropping the last 3 digits.

Example
-------

.. code:: text

    //echo -a $uptime(system,0) is the same as $ticks
    //echo -a $uptime(system,3) is the same as $left($ticks,-3)
    //echo -a mIRC has been running for $uptime(mirc,2)
    //echo -a mIRC has been connected to $network server $server for $uptime(server,2)
    //echo -a Windows has been running for $uptime(system,2) since booting up $asctime( $calc($ctime - $uptime(system,3) ) )

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$ctime </identifiers/ctime>`

