$eval
=====

$eval allows you to dynamically evaluate a line of code N times.

Synopsis
--------

.. code:: text

    $eval(text,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The text you want to double evaluate.
    * - N
      - The number of time you want to evaluate something, if N = 0, the text is not evaluated,

Properties
----------

None

Example
-------

.. code:: text

    //var %prefix_ $+ $me value | echo -a $eval($+(%,prefix_,$me),2)

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$evalnext </identifiers/evalnext>`

