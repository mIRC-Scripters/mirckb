$window
=======

$window returns information about the specified window for the current connection or returns the name of the @window that is left inside the 'leave' menu {} event.

Synopsis
--------

.. code:: text

    $window(N/name)
    
    $window

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth @custom window, if N is 0, returns the total number of windows.
    * - Name
      - The name of query/channel/@custom window, or "status window", "channel list", etc..

.. note:: you can use -1 or @desktop to refer to the screen, -2 or @mirc to refer to the main mIRC window, and -3 or @mdi to refer to the mdi window where all others windows inside mIRC are displayed, these @name are reserved. You can use the .x .y .w .h .dx .dy .dw .dh properties with these parameters to get the size of these windows (or your screen's size)

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - x,y,w,h
      - the left, top positions, and the width and height of the window respectively
    * - dx,dy
      - the left, top positions of the window relative to the desktop
    * - cx,cy
      - the left, top positions of the window relative to the primary monitor
    * - dw,dh
      - the width and height of the text display area
    * - bw,bh
      - the width and height of the bitmap for a graphic window
    * - mdi
      -  $true if the window is mdi, otherwise returns $false
    * - title
      - text in the titlebar of the window
    * - state
      - returns minimized/maximized/hidden/normal
    * - font
      -  the name of the window's font
    * - fontsize
      - the window's font size
    * - fontdialogsize
      - returns the size of the current font in font dialog size
    * - fontbold
      - $true if the font is bold, otherwise returns $false
    * - fontitalic
      - $true if the font is italic, otherwise returns $false
    * - fontcs
      - the character set of the current font
    * - fullscreen
      - $true if the window is in fullscreen, $false otherwise
    * - logfile
      - the path\filename of the window's logfile if one is open
    * - stamp
      - timestamp setting, $true or $false
    * - icon
      - returns on/off depending on whether icon is visible
    * - ontop
      - returns ontop status for a window, $true or $false
    * - type
      -  returns window type: status,channel,custom,query,etc...
    * - anysc
      -  returns $true or $false to indicate if the /window was created using the -i switch
    * - wid
      - returns the window id number
    * - cid
      - returns the connection id number associated with that window. Changes based on active network if @window created using the -i switch
    * - hwnd
      - returns the window handle number
    * - sbtext
      - sbtext returns the switchbar button text
* sbcolor the name of the switchbar highlight color, event/message/highlight, or $null if not colored
    * - sbstate
      - returns switchbar button state for a window, 0=hidden 1=not hidden
    * - tbtext
      - returns the treebar button text
    * - tbstate
      - returns treebar button state for a window, 0=hidden 1=not hidden
    * - idle
      - returns the number of second elapsed since someone different from you talked in a channel/query
    * - lb
      - returns 0 if the window has no listbox, 1 if it has a listbox, or 2 if it has a side listbox
    * - .utf
      - used to returns the utf mode of the window which could be changed via the /font setting in mIRC 6.17-6.35, 1 = default, 2 = utf8 is displayed (decoded) only, 3 = utf8 is displayed and encoded, nowadays it always seems to return 2, even if you disabled the encoding and decoding of utf8 in main mirc option

Example
-------

.. code:: text

    //echo -a There are $window(0) custom windows open $iif($window(1),The first custom window listed in 'window' menu is $v1)
    //echo -a Custom window @test $iif($window(@test),Does,Does Not) exist.
    //echo -a Channel named #test $iif($window(#test),is open on this .cid,is not open on this .cid but might be open on other .cid)

.. code:: text

    //var %i $window(0) , %list | while (%i) { var %list $window(%i).sbtext %list | dec %i } | echo -a These are the @custom windows as shown in the switchbar: %list (windows listed without @ were created using -k switch) 
    //echo -a The font of the active window is: $window($active).font $window($active).fontsize $iif($window($active).fontbold,Bold) $iif($window($active).fontitalic,Italic)
    //window -ea @test | titlebar @test This text appears in the titlebar | [ $iif($window(@test).type == listbox,aline,echo) ] @test The titlebar of this window shows $window(@test).title
    //window -c @test | window -ekaido @test | timertest 99 1 echo @test $!timer(test).reps $!asctime The Connection id $!window(@test).cid $!scid( $!window(@test).cid ).network changes as you click between windows attached to different connections

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/window </commands/window>`

