$submenu
========

$submenu can be used in popups definition to dynamically create a popup

Synopsis
--------

.. code:: text

    $submenu($id($1))

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - $id
      - The name of the identifier called by mIRC, the parameter passed to it is always $1, used by mIRC to pass information to your identifier.

It calls $id first with the parameter "begin" then will pass an incremented integer starting at 1 and will increase as long as you return a correct popups definition, then will send "end" 

.. note:: You cannot use this to create nested submenus, it will only build one single submenu.

Properties
----------

None

Example
-------

.. code:: text

    menu status {
      Animal
      .$submenu($animal($1))
    }
    alias animal {
      echo -s > $1
      if ($1 == begin) return -
      if ($1 == 1) return Cow:echo Cow
      if ($1 == 2) return Llama:echo Llama
      if ($1 == 3) return Emu:echo Emu
      if ($1 == end) return -
    }

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

