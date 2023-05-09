$sysdir
=======

$sysdir returns system folders for the current user.

Synopsis
--------

.. code:: text

    $sysdir(item)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - item
      - the item representing the folder, can be:
** profile - The profile folder, for example C:\Users\Wims\
** desktop - The desktop folder
** documents - The documents folder
** downloads - The downloads folder
** music -  The music folder
** pictures -  The pictures folder
** videos -  The videos folder

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $sysdir(music)

Compatibility
-------------

.. compatibility:: 7.43

See also
--------

.. hlist::
    :columns: 4

