/window
=======

The /window command can be used to create :doc:`custom windows </intermediate/gui_scripting>` and :ref:`picture_windows` (using the -p switch), or to manipulate an existing custom or channel window.

Synopsis
--------

.. code:: text

    /window [-abBcCdDe[N]fg[N]hHij[N]k[N]l[N]mMn[N]oprRsSuvw[N]xyz] [-tN,..,N] [+bdeflLnstx] <@name> [x y [w h]] [/command] [popup.txt/@popup] [font [size]] [iconfile [N]]

Switches
--------

Option Switches
^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Set as the active window 
    * - -b
      - Update horizontal scrollbar width for the listbox 
    * - -B
      - Prevent window from using an internal border 
    * - -c
      - Close window 
    * - -C
      - Center window 
    * - -d
      - Create a separate desktop window (separate button in Windows taskbar) instead of a mIRC mdi window 
    * - -D
      - Enables @window's upper-left system menu choice to toggle @window between mdi/desktop without closing the window
    * - -e[N]
      - Enable editbox; 0 = single, 1 = multi, 2 = auto, 3 = default 
    * - -f
      - Makes the w h the required width and height of the text display area (instead of the window size) 
    * - -g[N]
      - Set/Unset highlight for window button; 0 = none, 1 = message colour, 2 = highlight colour, 3 = event colour
    * - -h
      - hide window (from the switchbar / treebar - it is still visible in mIRC's Window menu)
    * - -H
      - Enables auto-hide for a side-listbox 
    * - -i
      - Associate window with the active connection 
    * - -j[N]
      - Change max lines. If N=0 or -j not used, max lines changes with current setting for mirc-Options/Other/WindowBuffer that defaults as 5000. Adding lines to full window causes lines at top of window to be deleted.
    * - -k[N]
      - Hides the @ prefix; 0 = hide, 1 = show 
    * - -l[N]
      - Listbox, n - width (character count) 
    * - -m
      - Enable line marker in the window 
    * - -M
      - Trims off the text at tab stops 
    * - -n[N]
      - Minimize window; 2 = Hide auto-expanding @Treebar item
    * - -o
      - (used with -d) keep the desktop window on top of other windows  
    * - -p
      - Creates a :ref:`picture_windows`
    * - -r
      - Restore window 
    * - -R
      - Reset window position to previously saved position 
    * - -s
      - Sorts the main window (can be text or listbox) 
    * - -S
      - Sort the side-listbox 
    * - -u
      - Removes on-top setting (-o) 
    * - -v
      - Close window when associated status window is closed 
    * - -w[N]
      - Show/hide window from treebar or switchbar; 0 = hide from both, 1 = show in switchbar, 2 = show in treebar, 3 = show in both 
    * - -x
      - Maximize window 
    * - -y
      - Disables logging menu for window.
    * - -z[N]
      - Place window button at end of switchbar; 0 = restore original position, 1 = place window at end. If [N] is not given it defaults to 1

Tab Switches
^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -tN,..,N 
      - Lets you set custom tab positions in a listbox. If a text contains tabs, it will be spaced out accordingly, if you don't specify at least one tab stop, the window is not created but no error will be displayed.

.. note:: By default a window contains a tab stop every 8 characters and it is possible to use /window -M without using /window -t.

.. note:: It is now possible to use N = 0 if you are using -M, to create an invisible column, which can be useful to hide meta-data for that line.

.. note:: You can update the tab stop position once the window has been created with /window -t @win N N N, which is different from the orignal syntax /window -tN,N,N @win

Appearance Switches
^^^^^^^^^^^^^^^^^^^

Mostly applicable to Desktop windows:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - +b
      - Border
    * - +d
      - No border 
    * - +e
      - 3d Edge 
    * - +f
      - Dialog frame 
    * - +l
      - Tool window <ref group="app." name="tool">Tools windows have no Titlebar or min/max/close buttons.</ref>
    * - +L
      - Tool window (hide from taskbar) <ref group="app." name="tool" />
    * - +n
      - Minimize window 
    * - +s
      - Sizeable
    * - +t
      - Titlebar
    * - +x
      - Maximize window

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <@name>
      - The window name, must be prefixed with a @ symbol
    * - x y [w h]
      - The coordinates for the position and the optional width and height, use -1 for any of the parameters to use default (or existing) value
    * - /command
      - default command which is used to prepopulate the window's editbox
    * - popup.txt/@popup
      - popup filename, must be plain text file, or can be the name of a window, representing the popups menu of that window in a remote file
    * - font [size]
      - font name [font size]
    * - iconfile [N]
      - sets a custom titlebar icon for the window [index]

.. note:: If you specify -1 for any of the x,y,w,h values, the current value is used for an existing window, or a default value used if you are creating a new window.

.. note:: mIRC does not allow window names @mirc (-2) or @mdi (-3) or @desktop (-1), that's because these names are used internally by mIRC to represent the different mIRC windows for $window(-1), $window(-2) and $window(-3). You can use these names in $window() though, to make things clearer if you want.

Examples
--------

Example 1
^^^^^^^^^

Picture window

.. code:: text

    Alias Example1 {
      ;Create a desktop + picture window, Coordinates: (250,250), size 300x300
      window -dep @Example 250 250 300 300
      ;color it color 3 (default green)
      drawfill @Example 3 3 1 1 100 100
      ;draw text \"Hello There!\"
      drawtext @Example 1 Arial 30 50 100 Hello There!
    }

Example 2
^^^^^^^^^

Custom window with side listbox

.. code:: text

    Alias Example2 {
      ;Create a desktop, Coordinates: (100,100), size 500x350
      ;Side listbox (width: 15 characters)
      window -del15 @Example 100 100 500 350
    
      ;Populate the side listbox with 5 items.
      var %a = 1
      while (%a < 5) {
        ;Add an item
        aline -l $v1 @Example Item $v1
        inc %a
      }
    
      ;Add 5 lines to the window buffer
      var %a = 1
      while (%a < 5) {
        ;Add a line of text
        aline $v1 @Example This is line $v1 $+ .
        inc %a
      }
    }

Example 3
^^^^^^^^^

Making unique window name from $nick while avoiding the 3 protected window names:

.. code:: text

    //window -ek @ $+ $nick $+ $iif($istok(mdi desktop mirc,$nick,32),$ctime)

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/window>`
    * :doc:`$line </identifiers/line>`
    * :doc:`$fline </identifiers/fline>`
    * :doc:`$sline </identifiers/sline>`
    * :doc:`/aline </commands/aline>`
    * :doc:`/cline </commands/cline>`
    * :doc:`/dline </commands/dline>`
    * :doc:`/iline </commands/iline>`
    * :doc:`/renwin </commands/renwin>`
    * :doc:`/rline </commands/rline>`
    * :doc:`/sline </commands/sline>`

