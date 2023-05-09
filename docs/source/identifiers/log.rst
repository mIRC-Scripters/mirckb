$log
====

$log returns the natural logarithm (base e) of a number.

'e' is an irrational number whose digits begins with 2.718281828
'e' is the value where graphing the curve y=e^x has slope of X at every location along the curve.
The natural logarithm of the value N is the exponent X where e^X is the value N. $log(e) is 1, $log(1) is 0, $log of values between 0 and 1 are negative. Returns error for N=0 or N=negative.

There may be a rounding error due to mIRC preserving fractional digits to only 6 places.

Synopsis
--------

.. code:: text

    $log(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The number you want the natural logarithm of

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $log(50)
    result: 3.912023
    //echo -a $calc(2.718281^3.912023)
    result: 49.99994

.. code:: text

    //var %e = 2.718281828 , %begin_balance = 10 , %interest_rate = .07 , %years = 20 | echo -a As compounding interval becomes shorter, ending balance approaches $ $+ $calc(%begin_balance * (%e ^(%interest_rate * %years)))
    
    You can use $log to find the base-X logarithm for any value N with $calc( $log(N) / $log(X) )
    //echo -a base-3 logrithm of 50 is $calc( $log(50) / $log(3) )
    result: base-3 logrithm of 50 is 3.560878
    //echo -a $calc( 3 ^ 3.560878 )
    result: 50.000066
    
    It's due to the rounding error that this does not return 8:
    //echo -a $calc( $log(256) / $log(2) )

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$log10 </identifiers/log10>`

