$style
======

$style can be used inside menu definition to create a checked or disabled (or both) menu item.

Synopsis
--------

.. code:: text

    $style(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - use N = 1 for checked, N = 2 for disabled and N = 3 for both

Properties
----------

None

.. note:: The $style(N) identifier must be the first word in the menu definition.

Example
-------

.. code:: text

    menu status {
      $iif($server == $null,$style(2)) Server Info
      .$style(1) This line is always checked:halt
      .Motd:/motd
      .Time:/time
    }

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

