$vc
===

The $vc identifier is used to retrieve commands in the voice command list, same as :doc:`$vcmd </identifiers/vcmd>`.

Synopsis
--------

.. code:: text

    $vc(N)

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

Nonr

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

