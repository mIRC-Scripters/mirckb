$numbits
========

$numbits returns the bit length of N, the number of bits in the base-2 representation of N.

Not to be confused with * :doc:`$bits </identifiers/bits>`

Details
-------

Numbits is the number of bits needed to represent the input number. In effect, for non-negative numbers it's the equivalent of $len($base(N,10,2)), and $numbits($calc(2^N)) is N+1. Thought, the return string from $base is limited by $maxlenl.

Results are inaccurate in non-bigfloat mode for N >= 2^32, as well as for negative numbers.
<p>In non-bigfloat mode, N >= 2^32 returns '32', and negative numbers return unexpected results based on the length where the leftmost '1' are excluded, and everything <= -2^32 is '1'.

Synopsis
--------

.. code:: text

    $numbits(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Integer 
Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
None
Example
-------

.. code:: text

    //bigfloat on | var %n $rand(0,$calc(2^2048-1)) | echo -a the bit length of N is $numbits(%n)
    //var %n $rand(0,255) | echo -a the bit length of N is $numbits(%n) same as $len($base(%n,10,2))

Compatibility
-------------

.. compatibility:: 7.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$base </identifiers/base>`
