$len
====

$len(text) returns the number of characters in the text

Synopsis
--------

.. code:: text

    $len(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
text - The input string you want to know the length of

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $len(ONE)

will return 3

.. code:: text

    //echo -a $len(ONE TWO)

will return 7

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$count </identifiers/count>`

