$wrap
=====

$wrap returns the Nth line in text wrapped to the specified width in the specified font.

This function is typically useful for picture window if you have to display text inside a specific rectangle and you have to wrap text.

Note that the pN option is enabled by default and that control codes are preserved accross wrapped lines

Synopsis
--------

.. code:: text

    $wrap(text,font,size,width [,b[N]i[N]p[N]t[N]w[N] ],N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The text you want to know wrapping information about
    * - font
      - The name of the font
    * - size
      - The size of the font, you can specify a negative value to match the size of fonts in the font dialog
    * - width
      - The width at which the text should wrap

Previously, the 5th parameter was an optional 'word' parameter accepting either 0 (disabled) or 1 (enabled) to indicate handling of word wrapping. Though the old syntax is still enabled, it's now a set of options to go with $width and $height:

* bNiNpNtN - Optional parameter, defines some options for the measurement, N can be 1 or 0 to enable or disable the option, with '1' assumed when 'N' not present:
** bN enables/disables the width used when the bold 'style' is enabled for that font
** iN enables/disables the width used when the italic 'style' is enabled for that font
** pN enables/disables control codes always handled as if zero-width characters 
** tN enables/disables tab character 0=zero_width 1=tab-expansion
** wN enables word wrapping 0=chop 1=entire word on next line
* N - The Nth line wrapped, use 0 to get the total number of wrapped line.

* Because the switches parameter is optional, it must not be present if no switches are used.

* The bN and iN settings refer to the 'style' dropdown in the 'select font' dialog, for the fonts who have different for some characters when the 'bold' or 'italic' style is enabled. They do NOT refer to the 'b' and 'i' control codes as used by $strip.

* Because /echo no longer expands the 'tab' character, the t[N] setting is no longer relevant there, but continues to be used by the /drawtext command.

Properties
----------

None

Example
-------

Suppose you want to implement a chat inside a picture windows, your chat area starts a X,Y = 50,50 and your width and height is W,H=300,300
You width is then 300 and you'd start displaying text at 50 + some margin:

.. code:: text

    alias picwinchat {
      var %x 50,%y 50,%w 300,%h 300
      window -BfdpC @chat -1 -1 400 400
      ;make the window full white
      drawrect -fr @chat 16777215 0 0 0 400 400
      drawrect -r @chat 0 0 %x %y %w %h
      ;we substract 10 to the real width because we will use a 5 pixel margin on both left/right
      var %n $wrap($1-,verdana,10,$calc(%w - 10),1,0)
      ;the margin
      var %xstart %x + 5 ,%ystart %y + 5,%a 1
      while (%a <= %n) {
        drawtext -r @chat 0 verdana 10 %xstart %ystart $wrap($1-,verdana,10,$calc(%w - 10),1,%a)
        inc %a
        ;increase a constant value for y, this example isn't about $height after all!, but eventually you would be using $height with a margin too
        inc %ystart 20
      }
    }

Now execute "/picwinchat test this is a very long text ok some more word please ok this is enough to illustrate the example i think maybe not"

.. note:: The widths used by the various switch settings are the same ones used by $width, where some characters in some fonts can have different widths depending on whether the font has the 'bold' or 'italic' setting enabled. This example shows the width of the Verdana 'M' differs depending on whether the font is bold or not, or whether the font is italic or not, or whether both bold+italic styles are used.

.. code:: text

    //var %c $asc(M) , %font Verdana | echo -a b1 $width($chr(%c),%font,21,b1) vs b0 $width($chr(%c),%font,21,b0) vs p1 $width($chr(%c),%font,21,p1) vs i1 $width($chr(%c),%font,21,i1) vs i0 $width($chr(%c),%font,21,i0) vs b1i1 $width($chr(%c),%font,21,b1i1)

* result: b1 20 vs b0 18 vs p1 18 vs i1 19 vs i0 18 vs b1i1 21

When changing %c to be the number 2 instead of $asc(M), the result for p1 changes to 0 because codepoint 2 is the control-code for 'bold', and the 'p1' processing of control-codes gives them all a zero width.

* result: b1 11 vs b0 10 vs p1 0 vs i1 10 vs i0 10 vs b1i1 11

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$width </identifiers/width>`
    * :doc:`$height </identifiers/height>`
    * :doc:`$strip </identifiers/strip>`
