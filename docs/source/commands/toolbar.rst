/toolbar
========

The **/toolbar** command allows you to modify the toolbar.

.. note:: Modifying some of the default mIRC buttons, such as Connect, Notify, etc. may not always work since they are managed by mIRC. They can however be deleted.

Synopsis
--------

.. code:: text

    /toolbar -aidmsxkNnNzNebwhyNurctplorf[sld] [N] <name/N> <tooltip> <picfile|@> [x y w h] [/alias] [popfile|@]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Adds a button
    * - -i
      - Inserts a button a position [N]
    * - -d
      - Deletes a button at position [N] or with name <name>
    * - -m
      - Moves a button <name/N> to position [N]
    * - -s
      - Adds a separator
    * - -x
      - Specifies a wide button
    * - -kN
      - Specifies a check button, check with N = 1, uncheck with N = 2
    * - -nN
      - Specifies the Nth icon index in the picture file
    * - -zN
      - Specifies the icon size, 1 = small, 2 = large, 3 = actual
    * - -e
      - Enables the button at position [N] or with name <name>
    * - -b
      - Disables the button at position [N] or with name <name>
    * - -w
      - Shows the button at position [N] or with name <name>
    * - -h
      - Hides the button at position [N] or with name <name>
    * - -yN
      - Sets the transparency for button [N] or <name>, N range 0 to 255
    * - -v
      - Allows support for alpha channel transparency with PNG files
    * - -u
      - Updates the display immediately
    * - -r
      - Reset buttons
    * - -c
      - Clears all buttons
    * - -f<sld>
      - <<nowiki />s>aves/<l>oads/<d>eletes settings in toolbar.ini, that file is automatically load on startup

Use empty quotes with the following switches to clear their entry:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -t
      - Updates the tooltip text
    * - -p
      - Updates the picture file
    * - -o
      - Updates the popups definition
    * - -l
      - Updates the [/alias] parameter

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [N]
      - Used with the switches -idmebwhy, the position of a button in the toolbar.
    * - <name/N>
      - The name or the Nth button in the toolbar.
    * - <tooltip>
      - The tooltip text for the button.
    * - <picfile|@>
      - The picture filename to be used for the icon or a @picture window name, minimum size is 16x16, maximum is 256x256.
    * - [w y w h]
      - The position in the bitmap and size of bitmap to use if you used a @picture window for the icon.
    * - [/alias]
      - The command to be performed when the button is clicked, $!1 is the button name.
    * - [popfile|@]
      - The popups filename or the menu for the @picture window name.

Example
-------

.. code:: text

    /toolbar -a Cow "Moo moo!" cow.bmp "/echo I am cow, hear my moo" @cow
    ;The above command creates a button called "Cow" with the tooltip "Moo moo!" using the button picture cow.bmp.
    ;If the button is clicked, it will run the command "/echo I am cow, hear my moo", and if right-clicked, it will popup the menu @cow.

    /toolbar -m 1 Cow
    ;The above command will move the button named "Cow" to position 1 in the toolbar.

    /toolbar -p Cow goat.bmp
    ;The above command will change the picture on the button named "Cow" to "goat.bmp"

    /toolbar -is 2 cowsep
    ;The above command will insert a separator named "cowsep" (every button and separator you add to the toolbar must have a name) at position 2.

Compatibility
-------------

Added: mIRC v6.2 (23 Nov 2006)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$toolbar </identifiers/$toolbar>`
