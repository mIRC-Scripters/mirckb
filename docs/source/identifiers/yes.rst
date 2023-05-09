$yes
====

The $yes identifier is returned when an :doc:`$input </identifiers/input>` box has been invoked with the v switch and the Yes button was pressed.

Synopsis
--------

.. code:: text

    $yes

Parameters
----------

None

Properties
----------

None

Example
-------

Create an input with a yes button that will echo results to the active window:

.. code:: text

    //echo -a $input(Click yes to see the result.,yv)

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cancel </identifiers/cancel>`
    * :doc:`$false </identifiers/false>`
    * :doc:`$no </identifiers/no>`
    * :doc:`$ok </identifiers/ok>`
    * :doc:`$input </identifiers/input>`
    * :doc:`$true </identifiers/true>`

