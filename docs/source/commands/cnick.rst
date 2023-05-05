/cnick
======

The **/cnick** command allows you to modify items from the address book's nick color list.

Synopsis
--------

.. code:: text

    /cnick -rfaniovpylNmNsN [nick[!user@host]] [color] [modes] [levels]
    /cnick <on/off>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Removes the specified nick or address
    * - -f
      - Forces mIRC to add another item instead of replacing an existing one
    * - -a
      - Sets the Any Mode option
    * - -n
      - Sets the No Mode option
    * - -i
      - Sets the ignore option
    * - -o
      - Sets the op option
    * - -v
      - Sets the voice option
    * - -p
      - Sets the protect option
    * - -y
      - Sets the notify list option
    * - -lN
      - Sets the idle time
    * - -mN
      - Sets the highlight method (0-2)
    * - -sN
      - Sorts the item into the Nth position in the list

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [nick[!user@host]]
      - Nickname or the host mask to be added
    * - [color]
      - The color to assign the nick/host. 0-98 or autocolor=*
    * - [modes]
      - List of modes that is required for the nick/host (Ed. ~&@%+)
    * - [levels]
      - Access level form the user list
    * - <on/off>
      - turns nick colors on or off

Example
-------

.. code:: text

    ;Turn nick color on
    /cnick on
    ;Add color 5 for all Operators
    /cnick * 5 @
    ;Add color 3 for all half-op
    /cnick * 3 %

AutoColor
---------

Starting v7.58 you can now have nicks pseudo-randomly colored based on the nick. The rules appear to be:
1. colors chosen for the auto-color palette depend on the RGB value of $color(background) (even if that is a different color than the background for the nicklist)
2. If a color index has an RGB value matching one that's already been chosen, the 2nd color index is not chosen. This means that for the "mIRC Classic" scheme where index 4 and 52 have the same RGB, that it will not choose both 4 and 52 into the palette.
3. Colors are chosen if an algorithm determines that their RGB has sufficient contrast against the background RGB, with no attempt to avoid 2 colors in the palette not contrasting against each other.
4. If there is another Nick Colors rule already using a color index, that index is not chosen for auto-color even if it contrasts well. That means you can have a rule to make all @op nicks be color 4 red, and index 4 will not be added to the palette. However, since 4 is not chosen, 52 being identical RGB to color 4 can still be chosen if it contrasts against the background.
5. Each time a color rule is added/removed to/from Nick Colors and you click OK, the palette is recalculated to see the palette changes. Same goes for each time /color Background N is used, even if that does not change to a different index. But it does not automatically update the palette when using the /cnick command.
6. The nick's color is based on the case-sensitive value of the nick itself, so it does change if using 'Maroon' vs 'maroon' and does not change due to the nick being at a different network or if the address changes.
7. Because the auto color for the same nick depends on the number of colors in the autocolor palette, adding or removing another rule can change the number of colors in the palette, which changes the bucket of colors into which each nick is placed.

If you find that the autocolor is using too many colors which do not contrast against the background, there are some workarounds which may or may not work for you.

One is to change your black background from index 1 to one of the color indices like 89 or 90 which look like black but have slightly different RGB which causes a different batch of colors to be chosen for the palette. However, be aware that this can have an adverse effect on colored strings which normally change color 1 into color 0 if the background is also index 1 - and those will no longer do the same for background 88 even if that has an identical RGB to index 1

Another is to take advantage of the fact that colors used by other nick color rules are not chosen for the autocolor palette, so you can simply create a dummy rule that won't actually match any nicks, but the presence of this rule will prevent it being chosen for the autocolor palette. To do this, you can use the Alt+P editor to place this line into your nicklist popups menu. (If putting into a dropdown menu you probably need to prefix the label with a .period)

Dummy rule for autocolor $nick($chan,$1).color : var %color $nick($chan,$1).color | !.cnick -m2s $+ $calc(1+$cnick(0)) ;dummycolor $+ %color %color @ | !.color background $color(background)

.. note:: that it contains the command to reset the background to the existing background color, because that's necssary to force the autocolors to reset based on the new palette that has 1 fewer colors in it.

If you want to use that color again, you can simply go to the Nick Colors tab of the address book and delete it.

Compatibility
-------------

Added: mIRC v6.1 (17 Feb 2006)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$abook </identifiers/abook>`
    * :doc:`$cnick </identifiers/cnick>`
    * :doc:`$nick </identifiers/nick>`
    * :doc:`/abook </commands/abook>`
