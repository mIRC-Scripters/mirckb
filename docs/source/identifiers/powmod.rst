$powmod
=======

$powmod performs integer exponentiation over a modulus.

Details
-------

For integers (B,E,M) the remainder of B^E modulo M is a result that is a non-negative integer less than M, and can obtain the result even when the E exponent is large. Should be compatible with the Powermod function in Wolfram Alpha

Synopsis
--------

.. code:: text

    $powmod(B,E,M)

.. note:: Unlike the % percent operator in $calc the result cannot be negative. If 'B' is negative, the result is calculated after casting 'B' to positive by adding 1-or-more multiple of the M modulus, so (-1,2,11) is the same as (10,2,11).

* If the exponent E is negative, the result of (B,-E,M) is obtained from ($modinv(B,M),+E,M), so $powmod(B,-1,M) is the same as $modinv(B,M) 
* Inputs should be integer, so fractions in any parameter are ignored.
* While most math identifiers support numbers as large as 2^53, care should be used for this function if using a modulus greater than $sqrt($calc(2^53)), because this algorithm uses an intermediate result which can potentially be as large as (M-1)^2. When in doubt, either use this function where a %var.bf name is involved or if /bigfloat ON mode is enabled.
* In spite of using a shortcut which allows obtaining results involving large E exponents without calculating the full result of B^E, the result can be very slow for very large numbers. The main factors affecting the time for non-trivial (B,E,M) are:
    # Bit length of M
    # Bit length of E
    # Number of '1' bits returned from $base(E,10,2)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - B
      - Integer Base of the exponentiation
    * - E
      - Integer Exponent
    * - M
      - Integer Modulus over which the exponentiation is found

Properties
----------

None

Example
-------

.. code:: text

    //var -s %x $rand(3,2026) , %A $powmod(2,%x,2027) , %y $rand(3,2026) , %B $powmod(2,%y,2027) | echo -a $powmod(%A,%y,2027) = $powmod(%B,%x,2027)

Compatibility
-------------

.. compatibility:: 7.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$modinv </identifiers/modinv>`
    * :doc:`$gcd </identifiers/gcd>`
    * :doc:`$lcm </identifiers/lcm>`
