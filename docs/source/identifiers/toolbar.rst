$toolbar
========

$toolbar returns :doc:`$true </identifiers/true>` if the toolbar is enabled in mIRC, :doc:`$false </identifiers/false>` otherwise. It also returns information about the items on the toolbar.

Synopsis
--------

.. code:: text

    $toolbar

.. code:: text

    $toolbar(name|N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
None
or
Name|N = Name or Nth item in toolbar about which to return information. 0 = total number of toolbar items.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
* .name
* .type
* .tip
* .alias
* .popup
* .width
* .height
* .wide
* .enabled
* .visible
* .checked
* .alpha

Example
-------

.. code:: text

    //echo -a the toolbar is $iif($toolbar,On,Off) and contains $toolbar(0) items
    //var %i 0 | while (%i < $toolbar(0)) { echo -a %i : $toolbar(%i).name : $toolbar(%i).tip | inc %i }

Compatibility
-------------

.. compatibility:: 6.32

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$menubar </identifiers/menubar>`
    * :doc:`$switchbar </identifiers/switchbar>`
    * :doc:`$treebar </identifiers/treebar>`
    * :doc:`/toolbar </commands/toolbar>`

