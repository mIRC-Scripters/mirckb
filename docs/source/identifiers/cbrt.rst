$cbrt
=====

$cbrt returns the cube root.

Details
-------

Synopsis
--------

.. code:: text

    $cbrt(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Number for which the cube root is returned

Properties
----------

None

Example
-------

//bigfloat on | var %n $rand(2,999) | echo -a the cube root of %n is approximately $cbrt(%n) same as $calc(%n ^ (1/3))  $calc($cbrt(%n) ^ 3)

.. code:: text

    //bigfloat on | var %n $rand(2,999) | echo -a the cube root of %n is approximately $cbrt(%n) same as $calc(%n ^ (1/3)) cubed is $calc($cbrt(%n) ^ 3)

Compatibility
-------------

.. compatibility:: 7.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sqrt </identifiers/sqrt>`
    * :doc:`$calc </identifiers/calc>`
