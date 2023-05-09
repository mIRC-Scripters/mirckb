$filtered
=========

$filtered returns the number of matching lines found by the latest filter in the current script thread, if any.

Synopsis
--------

.. code:: text

    $filtered

Parameters
----------

None

Properties
----------

None

Example
-------

$filtered holds the number only during the current script thread, and knows the result even if the filter was performed in another alias or identifier.
$filtered returns 0 if no filter command yet performed in that script thread.

.. code:: text

    //echo -a previous filter result shows zero $filtered | filter -fk versions.txt noop */* - mirc * | echo -a filter found $filtered matching lines in versions.txt

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/filter </commands/filter>`

