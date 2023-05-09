$color
======

The $color identifier allows mIRC to return the color index number associated with the specified target/event, or return the RGB color for a color index number. $colour is an identical functioning identifier for those who find comfort using a 'u' to spell color.

Synopsis
--------

.. code:: text

    $color(name/N)[.dd]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - Returns the color index number for the specified name/action/event. Partial matches work as well: $color(action)
    * - N
      - Returns the 24-bit integer RGB color value for index N where N is 0-99, of which 0-15 are displayed in the CTRL+K list and the ALT+K window.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .dd
      - When used with name, allows the color index numbers 0-9 to be returned in double-digit format, eg: 02 instead of 2. Does not work on RGB-returned values.

Names
-----

Most of the names are shown in the Alt+K dialog, and some of them use spaces due to similar name for the background color in that area. The names accepted by $color are the same names used by echo's -c switch. The names for the background colors are not shown:

.. code:: text

    //echo -a $color(background)
    //echo -a $color(listbox)
    //echo -a $color(treebar)
    //echo -a $color(editbox)

The only names requiring 'text' are those where the absence of 'text' would be the same name as any of the above four:

.. code:: text

    //echo -a $color(listbox text)
    //echo -a $color(treebar text)
    //echo -a $color(editbox text)

These names do not require quotes when used as the $color parameter, but do require quotes when used with echo's -c switch:

.. code:: text

    /echo -ac "listbox text" test

Examples
--------

Echo the color index number for action events:

.. code:: text

    //echo -a $color(action)

If Index 0-9 are used for that event, displays a single number unless the .dd property is used:

.. code:: text

    //echo -a $color(action).dd

Echo the RGB code for index 4:

.. code:: text

    //echo -a $color(4)

.. code:: text

    //echo $color(ctcp) $chan this color changes when ctcp event color changes. it does not put color code into logfile
    //echo $chan $chr(3) $+ $color(ctcp) this color does not change when ctcp event color changes. it does put color code into logfile

Using .dd prevents numeric first character of string being considered part of the color code, in the event the event's color index is 0-9.

.. code:: text

    //var %string 123 | echo -a $chr(3) $+ $color(ctcp).dd $+ %string
    vs
    //var %string 123 | echo -a $chr(3) $+ $color(ctcp)   $+ %string

mIRC blocks the effect of $color if it matches the color used by the background for that text, except when used in the format ^Kn,n which sets the background along with the foreground. In attempting to avoid matching the background color, echo first tries $color(normal) to find a different color index then $color(gray). Invalid 'name' strings return 0.

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/color </commands/color>`
    * :doc:`$colour </identifiers/colour>`
    * :doc:`$rgb </identifiers/rgb>`
    * :doc:`/echo </commands/echo>`
