$round
======

$round returns a floating point number rounded to a number of decimal.

Synopsis
--------

.. code:: text

    $round(N,D)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The number you want to round, can be negative. 
    * - D
      - The number of decimal to round but if D is 0, it rounds up to the nearest whole number, if $null, number is not changed

.. note:: You can use the letter 'e' or 'd' as ``*10^N for N and D, $round(5e6,2) = $round($calc(5*10^6),2)``

.. note:: mIRC's floating point accuracy is currently at 6 places, so D has no effect outside the range 0-6. Rounding to D fractional digits can show fewer than D digits because it does not pad trailing zeroes.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $round(4.98472,3)
    
    Even though $pi has 20 decimal places, all results limited to 6 places. Note that $calc also rounds to 6 places:
    //echo -a $pi calc: $calc($pi) round: $round($pi,7)
    result: 3.14159265358979323846 calc: 3.141593 round: 3.141593
    
    Because of floating point translation to/from base 10, the result is not always the fraction expected:
    //var %i 1 , %list | while (%i isnum 1-100) { var %list %list $round(%i $+ .05 ,1) | inc %i } | echo -a round: %list
    result: round: 1.1 2 3 4 5 6 7 8.1 9.1 10.1 11.1 12.1 13.1 14.1 15.1 16.1 17.1 18.1 19.1 20.1 21.1 22.1 23.1 24.1 25.1 26.1 27.1 28.1 29.1 30.1 31.1 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$int </identifiers/int>`
    * :doc:`$ceil </identifiers/ceil>`
    * :doc:`$floor </identifiers/floor>`
    * :doc:`$abs </identifiers/abs>`
    * :doc:`$calc </identifiers/calc>`
