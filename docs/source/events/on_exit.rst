On Exit
=======

The ON EXIT event triggers specifically when mIRC is exiting. This event can allow scripts to essentially clean themselves up, including removing unnecessary variables and other stored value types.

Synopsis
--------

.. code:: text

    ON <level>:EXIT:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Identifiers
-----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$exiting </identifiers/exiting>`
      - Returns 1 if mIRC is in the process of exiting, 2 if mIRC is exiting and restarting, 0 otherwise.

Example
-------

This example will popup an :doc:`$input </identifiers/input>` window before you exit mIRC:

.. code:: text

    ON *:EXIT:noop $input(Goodbye!,o,Bye Window)

Compatibility
-------------

.. compatibility:: 5.81

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on close </events/on_close>`
    * :doc:`on connect </events/on_connect>`
    * :doc:`on disconnect </events/on_disconnect>`
    * :doc:`on error </events/on_error>`

