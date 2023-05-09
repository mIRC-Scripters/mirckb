$sqrt
=====

$sqrt returns the square root.

Synopsis
--------

.. code:: text

    $sqrt(<N>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Number for which the square root is returned

If N is negative, returns $null. You can use the letter 'e' or 'd' as ``*10^N, $sqrt(5e6) = $sqrt($calc(5*10^6))``

Square Root is limited to 6 decimal places. When squared, it often has a rounding error difference from the original N.

Example
-------

.. code:: text

    //echo -a $sqrt(3) is the same as $calc(3^.5)
    ; returns: 1.732051 is the same as 1.732051

.. code:: text

    //var %i 7 | echo -a $calc( $sqrt(%i) * $sqrt(%i) )
    ; slight rounding error due to decimal limited to 6 places: 6.999998

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$calc </identifiers/calc>`

