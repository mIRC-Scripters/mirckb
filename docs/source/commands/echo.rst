/echo
=====

The **/echo** command prints text to the specified window. This command does not send anything to the server; text is only shown in the window.

Synopsis
--------

.. code:: text

    /echo [colour-number] [-deghi[N]tsaqlbfnmr] [window] <text>
    /echo -c[deghi[N]tsaqlbfnmr] <colour-name> [window] <text>

Switches
--------

Target window switches 
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - prints to the status window
    * - -a
      - prints to the active window
    * - -d
      - prints to the single message window

Settings Related: 
^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - Applies the strip settings to the text (as defined in mIRC Options / IRC / Messages).
    * - -l
      - Applies the highlight settings to the text (as defined in mIRC Address Book / Highlight).
    * - -b
      - Applies the windows beep settings (to beep if mIRC is not the active application) as defined in mIRC Options / Sounds and any individual window override.
    * - -f
      - Applies the flash settings to the window (to flash the mIRC System Tray icon) as defined in mIRC Options / IRC / Options and any individual window override.

Other switches 
^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Indicates that the <colour-name> parameter is provided as the 1st parameter following the switch(es).
    * - -e

.. note:: does not add a leading line if it already consists entirely of the line separator.

    * - -g
      - Prevents the text from being logged if the window has logging on.
    * - -h
      - Applies a hard-wrap on the text so that the wrap point does not change when the window is resized. Text is not wrapped if it is echoed to a custom listbox window.
    * - -i[N]

.. note:: When using a proportional font, the indented width is a constant width regardless of the width of the characters echoed.

    * - -t

.. note:: -t shows timestamp in Custom Windows even though they do not have a timestamp setting, but only if timestamping has been enabled in mirc-options/irc/messages/"timestamp events".

    * - -q
      - Honors the $show flag. (Displays nothing if the alias was called with the . prefix)
    * - -n
      - Prevents switchbar button/treebar colour change
    * - -m
      - Treats the line as an user message, colours the window button in the switchbar/treebar with the "Message" colour defined in the option alt+o>Display.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [colour-number]

.. note:: 99 is $colour(listbox text) instead of $colour(normal) even in #channel and Status window where background is $colour(background). If $colour(listbox text) is the same index as $colour(background), 99 tries $colour(normal) then $colour(gray) searching for a colour that doesn't match the background colour.

    * - <colour-name>

.. note:: If you later change the colour index for a colour name, the echoed lines change to that colour.

    * - [window]

.. note:: If target is a listbox @window created using the -l switch, the output echoes to the Status Window instead.

    * - <text>
      - The text to be printed

.. note:: regardless whether or not -e switch is used, echo will not create a 2nd consecutive line consisting of the line separator, unless the existing last line was created in a @window using /aline.

Examples
--------

Example 1: Hello world
^^^^^^^^^^^^^^^^^^^^^^

.. code:: text

    /echo -a Hello World!

Example 2: A loop prints a few lines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: text

    alias example {
    var %x = 5
    while (%x) {
    echo -a This is example line $v1 $+ .
    dec %x
    }
    }

The above will print:

.. code:: text

    This is example line 5.
    This is example line 4.
    This is example line 3.
    This is example line 2.
    This is example line 1.

Example 3: Timestamps
^^^^^^^^^^^^^^^^^^^^^

.. code:: text

    echo #test This line never has a timestamp
    echo -t #test This line has a timestamp only if timestamping is enabled within #test
    echo #test $timestamp This line always has a timestamp

Example 4: Colours
^^^^^^^^^^^^^^^^^^

.. code:: text

    //echo 4 -at abc $chr(22) def $chr(15) The timestamp and this text following the Ctrl-O revert to colour 4 (red)
    //echo -act ctcp abc $chr(22) def $chr(15) The timestamp and this text following the Ctrl-O revert to "ctcp" colour ( $+ $colour(ctcp) $+ )
    //echo -at $chr(3) $+ 04 $+ abc $chr(22) def $chr(15) The timestamp and this text appear as "normal" colour ( $+ $colour(normal) $+ )

Example 5: Switchbar/treebar colours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: text

    ; See mirc-options/display
    ; The 1st line causes the switchbar to change to the "event" colour.
    ; The 2nd line -m causes the switchbar to change to the "messages" colour, overriding the default EVENT colour.
    ; The 3rd line -n leaves the switchbar colour unchanged.

    .. note:: that Chanserv giving the joined nick OP level is a separate event, and mIRC will change the -m override, and that event will colour the switchbar as the EVENT colour.

    on ^*:JOIN:#:{
    echo $colour(join) -t # * $nick $+($chr(40),$gettok($fulladdress,2-,33),$chr(41)) has joined # $comchan($nick,0)
    echo $colour(join) -tm # * $nick $+($chr(40),$gettok($fulladdress,2-,33),$chr(41)) has joined # $comchan($nick,0)
    echo $colour(join) -tn # * $nick $+($chr(40),$gettok($fulladdress,2-,33),$chr(41)) has joined # $comchan($nick,0)
    haltdef
    }

.. code:: text

    /echo -m @window test
    /echo -m #channel test
    ;has the same effect as:
    /echo @window test
    /echo #channel test
    /window -g1 @window
    /window -g1 #channel

.. code:: text

    The echo command modifies <text> by hiding duplicate spaces and non-printable characters including $chr(9) tab.
    //var %a abc $+ $chr(32) $+ $chr(32) $+ def | echo -a $len(%a) %a
    returns: 8 abc def
    ... where the duplicate space is not displayed.
    //var %a abc $chr(9) def | echo -a $len(%a) %a
    returns: 9 abc def
    ... where there are 2 spaces appearing next to each other because they were not consecutive prior to the non-printable tab being hidden.
    All 6 letters are displayed on the same line because $crlf is non-printable:
    //var %a $+(abc,$crlf,def) | echo -a %a
    Echo a blank line because it contains only non-printable characters:
    //echo -a $crlf

Compatibility
-------------

Added: mIRC v3.7 (24 Oct 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$colour </identifiers/$colour>`
    * :doc:`$color </identifiers/$color>`
    * :doc:`$n </identifiers/$n>`
    * :doc:`/aline </commands/aline>`
    * :doc:`/dline </commands/dline>`
    * :doc:`/drawtext </commands/drawtext>`
    * :doc:`/editbox </commands/editbox>`
    * :doc:`/iline </commands/iline>`
    * :doc:`/rline </commands/rline>`
