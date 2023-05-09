$factorial
==========

$fibonacci is a math identifier which returns the Nth term in the Fibonacci Sequence

In bigfloat mode, the maximum returned term in the series is $fibonacci(49325)
In doubles mode, the maximum number within the 2^53 limit is $fibonacci(78), and numbers above that lose precision.

More info at https://en.wikipedia.org/wiki/Fibonacci_number

With an implied 0 and 1 preceding it, the Nth number of the Fibonacci Sequence is the sum of the preceding 2 numbers, so the series begins at N=1 like [0 1] 1,2,3,5,8,13,21 ... and the limit as N approaches infinity for the Nth term divided by the N+1th term is the Golden Ratio $calc( ($sqrt(5) +1)/2)

Synopsis
--------

.. code:: text

    $fibonacci(<integer>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <integer>
      - The position in the Fibonacci Sequence for which the value is returned

Example
--------

.. code:: text

    //var -s %i 1 | while (%i isnum 1-20) { echo -a $ord(%i) : $fibonacci(%i) %null.bf  $calc( $fibonacci(%i) / $fibonacci($calc(1+%i)) )  | inc %i }

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$calc </identifiers/calc>`
    * :doc:`$factorial </identifiers/factorial>`
