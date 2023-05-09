$menutype
=========

$menutype return the type of menu inside a menu { }.

For status/channel/query/menubar, $menutype returns the same as :doc:`$menu </identifiers/menu>`, which is "status", "channel" etc..
But for custom windows, $menutype returns "custom".

Synopsis
--------

.. code:: text

    $menutype

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    menu nicklist,channel,@win,@other {
         $iif($menutype == nicklist,...):{}
         $iif($menutype == custom,$iif($menu == @other,stuff,otherstuff)):{}
    }

Compatibility
-------------

.. compatibility:: 6.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$menu </identifiers/menu>`
    * :doc:`$menucontext </identifiers/menucontext>`

