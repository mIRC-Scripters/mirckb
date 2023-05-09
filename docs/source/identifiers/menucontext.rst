$menucontext
============

$menucontext return the context in which the popups is created.

The value can be 'window' or 'treebar'.

Synopsis
--------

.. code:: text

    $menucontext

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    menu nicklist,channel, {
         $iif($menu == nicklist,...):{}
         $iif($menu == channel && $menucontext == treebar,...):{}
    }

Compatibility
-------------

.. compatibility:: 6.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$menutype </identifiers/menutype>`
    * :doc:`$menu </identifiers/menu>`

