$strip
======

$strip removes colors and/or other control-code formatting from text.

Synopsis
--------

.. code:: text

    $strip(<text>[,burcimo])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Text
      - Text string from which to remove colors or control codes.
Optional types to strip from text. Default is $strip(text,burci)

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - b
      - Bold $chr(2)
    * - u
      - Underline $chr(31)
    * - r
      - Reverse Colors $chr(22)
    * - c
      - Colors $chr(3) followed by N[,N]
    * - i
      - Italics $chr(29)
    * - m
      - The Color/Other settings from mIRC-OptionsIRC//Messages
    * - o
      - The Only-If settings from mIRC-OptionsIRC//Messages/If-more-than
    * - e
      - StrikeThrough

Note from the above that the control-code entered at the keyboard is not always the same one sent. For example, you press Control-K to precede numbers in colors, which is also $chr(11), but it actually sends $chr(3) which is same as Ctrl-C. Same goes for entering Ctrl-I for Italics but the text actually contains $chr(29).

Example
-------

; Two consecutive ^B's used within a bad word does not alter the display, but prevents a match against the badword list unless $strip is first used on the text

.. code:: text

    on *:TEXT:*:#channelname:{
      var %i $CheckForBadWords($strip($1-))
      ; Using Strip to find 'bad words' that could have been disguised by colors and control-codes
    } 

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$stripped </identifiers/stripped>`

