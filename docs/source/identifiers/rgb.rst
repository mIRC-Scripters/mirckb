$rgb
====

$rgb converts between R,G,B vs color-number, or returns system colors.

Synopsis
--------

.. code:: text

    $rgb( <R,G,B> | <N> | <SystemColorName> )

Parameters
----------

Method #1 - Converting R,G,B to single RGB Color Number

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - R
      - Red Color intensity from 0-255
    * - G
      - Green Color intensity from 0-255
    * - B
      - Blue Color intensity from 0-255

Method#2 - Converting Color Number to R,G,B

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - N
      - Decimal RGB Color Number from 0 through 2^24-1

Method#3 - Return RGB Color Number for System Color Settings

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - SystemColorName
      - Must be a name from the following list: face, shadow, hilight, 3dlight, frame, and text, and returns an RGB color value.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a The RGB color number for #7 (olive) is $color(7) with R,G,B values $rgb($color(7))
    ; The RGB color number for #7 (olive) is 32764 with R,G,B values 252,127,0
    //echo -a $color(7) converted to hex is $base($color(7),10,16,6) which shows mIRC's RGB color number is actually combined as B,G,R
    ; 32764 converted to hex is 007FFC which shows mIRC's RGB color number is actually combined as B,G,R

If you want to get the RGB number for color Goldenrod, which is RGB color #DAA520, you can use $rgb to convert the 3 RGB 0-255 numbers into the single 24-bit decimal number

.. code:: text

    //var %c DAA520 | echo -a       $base($left(%c,2),16,10,2)   $base($mid(%c,3,2),16,10,2)   $base($right(%c,2),16,10,2)
    //var %c DAA520 | echo -a $rgb( $base($left(%c,2),16,10,2) , $base($mid(%c,3,2),16,10,2) , $base($right(%c,2),16,10,2) )
    ; converts 218,165,32 into 2139610 by using $calc(32*65536 + 165*256 + 218*1 )

RGB can also return the 24-bit RGB decimal number for system color names:

.. code:: text

    //var %i 1 | var %list face shadow hilight 3dlight frame text | while (%i isnum 1-6) { var %n $gettok(%list,%i,32) | echo -a system color for %n is $rgb(%n) or $rgb( $rgb(%n) ) | inc %i }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$color </identifiers/color>`
    * :doc:`/color </commands/color>`

