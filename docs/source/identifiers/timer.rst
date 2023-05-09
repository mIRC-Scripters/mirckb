$timer
======

$timer returns informations about the specified timer.

Synopsis
--------

.. code:: text

    $timer(name/N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth timer, if N = 0 returns the total number of timer
    * - name
      - the name of a timer

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .com
      - returns the associated command of the timer
    * - .time
      - return the time parameter if used
    * - .reps
      - returns the number of repetition left
    * - .delay
      - returns the delay parameter
    * - .type
      - returns the online/offline status
    * - .secs
      - returns the number of second left before the timer is triggered
    * - .ms
      - returns the number of millisecond left before the timer is triggered (even for non millisecond timer)
    * - .mmt
      - returns $true if the timer is a multimedia timer (timer -h), $false otherwise
    * - .anysc
      - returns $true if the /timer -i switch was specified
    * - .wid
      - returns the window ID value associated with the timer
    * - .cid
      - returns the connection ID value associated with the timer
    * - .hwnd
      - returns the handle of the window associated with the timer
    * - .pause
      - returns $true if /timer -p has been used, $false otherwise
    * - .name
      - Forces the parameter to be seen as a name instead of the Nth timer if you pass a number.

Example
-------

.. code:: text

    //echo -a $timer(0)

Compatibility
-------------

.. compatibility:: 4.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/timer </commands/timer>`

