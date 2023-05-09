$vcmd
=====

The $vcmd identifier is used to retrieve commands in the voice command list.

Synopsis
--------

.. code:: text

    $vcmd(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Used to specify the Nth command in the list, or can be 0 to retrieve the total amount of commands in the voice command list.

Properties
----------

None

Examples
--------

Echo the total amount of voice commands to the active window:

.. code:: text

    //echo -a $vcmd(0)

Echo the 3rd command in the voice command list to the active window:

.. code:: text

    //echo -a $vcmd(3)

Echo the entire list of voice commands to the active window:

.. code:: text

    //var %i = 1 | while (%i <= $vcmd(0)) { echo -a $vcmd(%i) | inc %i }

Compatibility
-------------

.. compatibility:: 6.0

see also
--------

.. hlist::
    :columns: 4

    * :doc:`/vcadd </commands/vcadd>`
    * :doc:`/vcmd </commands/vcmd>`
    * :doc:`/vcrem </commands/vcrem>`
    * :doc:`$vcmdver </identifiers/vcmdver>`
    * :doc:`$vcmdstat </identifiers/vcmdstat>`
    * :doc:`on vcmd </events/on_vcmd>`

