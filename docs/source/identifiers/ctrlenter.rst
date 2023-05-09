$ctrlenter
==========

The $ctrlenter identifier returns either :doc:`$true </identifiers/true>` or :doc:`$false </identifiers/false>` depending on whether or not an :doc:`on input </events/on_input>` event was triggered using the CTRL+ENTER combination.

Synopsis
--------

.. code:: text

    $ctrlenter

Parameters
----------

None

Example
-------

Echo to whether or not CTRL+ENTER was used in an input box:

.. code:: text

    ON *:INPUT:*: { echo -a $ctrlenter }

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on input </events/on_input>`
