/renwin
=======

The **/renwin** command renames an existing window and assigns an optional topic.

Synopsis
--------

.. code:: text

    /renwin <@currentName> <@newName> [topic]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <@currentName>
      - The current window name
    * - <@newName>
      - The new window name
    * - [topic]
      - Window's topic

Example
-------

.. code:: text

    ;rename @foo to @bar
    /renwin @foo @bar

Compatibility
-------------

Added: mIRC v5.4 (24 Jul 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/window>`
    * :doc:`/window </commands/window>`
