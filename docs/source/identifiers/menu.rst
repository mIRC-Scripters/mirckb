$menu
=====

$menu return the name of menu in use.

Synopsis
--------

.. code:: text

    $menu

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    menu nicklist,channel {
      $iif($menu == nicklist,...):{}
      $iif($menu == channel,...):{}
    }

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$menutype </identifiers/menutype>`
    * :doc:`$menucontext </identifiers/menucontext>`

