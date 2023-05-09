$mouse
======

$mouse returns informations about the mouse and its buttons

Synopsis
--------

.. code:: text

    $mouse

Parameters
----------

None

Properties
----------

This identifier almost uniquely takes no parameter but has properties (:doc:`$insong </identifiers/insong>` and the like also have this), it is not possible to use such syntax for custom identifier, $myalias.prop would just call the alias named "$myalias.prop"

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .x and .y
      - returns the position of the mouse relative to the active window
    * - .mx and .my
      - returns the position of the mouse relative to the main mIRC window
    * - .dx and .dy
      - returns the position of the mouse relative to the desktop window
    * - .cx and .cy
      - returns position relative to the primary monitor.
    * - .win
      - returns the name of the active window
    * - .lb
      - returns $true if a mouse event occured over a listbox, $false otherwise.
    * - .key
      - Returns a bitmask, you can use the bitwise & operator to check for button/shift/alt/control state. See next table.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Bitmask
      - Description
    * - if ($mouse.key & 1)
      - echo left mouse button is pressed.
    * - if ($mouse.key & 2)
      - echo control key is pressed.
    * - if ($mouse.key & 4)
      - echo either left-or-right shift key is pressed.
    * - if ($mouse.key & 8)
      - echo either alt key is pressed.
    * - if ($mouse.key & 16)
      - echo right mouse button is pressed.
    * - if ($mouse.key & 32)
      - echo middle mouse button is pressed.
    * - if ($mouse.key & 64)
      - echo right shift key is pressed.
    * - if ($mouse.key & 128)
      - echo right control key is pressed.
    * - if ($mouse.key & 256)
      - echo right alt key is pressed.
    * - if ($mouse.key & 512)
      - echo capslock is enabled.
    * - if ($mouse.key & 1024)
      - echo scroll lock is enabled.
    * - if ($mouse.key & 2048)
      - echo numlock lock is enabled.
    * - if ($mouse.key & 4096)
      - echo left shift key is pressed.
    * - if ($mouse.key & 8192)
      - echo left control key is pressed.
    * - if ($mouse.key & 16384)
      - echo left alt key is pressed.

Example
-------

.. code:: text

    //echo -a $mouse.x

Notes
-----

Pressing any of the Ctrl or Alt or Shift keys causes 2 of the above masks to be non-zero, so pressing the right-shift enables both the 4 and 64 bit masks. You can check if the right-shift IS pressed and the left-shift is NOT pressed, by checking whether $and($mouse.key,$calc(4096+64)) == 64

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$click </identifiers/click>`

