$gettok
=======

$gettok returns the Nth $asc(C)-delimited token from a list.

Synopsis
--------

.. code:: text

    $gettok(<LIST>,<N>,<C>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - LIST:
      - Text list delimited by a character into tokens
    * - N:
      - The token(s) to be returned. N can also be negative or a range
    * - C:
      - The :doc:`$asc </identifiers/asc>` value which splits TEXT into tokens

If N=0, returns total number of tokens, same as :doc:`$numtok </identifiers/numtok>` 
If N is greater than the total number of tokens, returns :doc:`$null </identifiers/null>` 
If N is negative, returns tokens relative to the last token. -1 is the last token, -2 is next-to-last token, etc.
N- returns all tokens beginning with the Nth token.
N1-N2 returns all tokens in the range of those 2 numbers, including the between delimiters.

.. note:: You can reverse the order of the number: $gettok(a b c,3-2,32) is the same as $gettok(a b c,2-3,32)

.. note:: N2 can also be negative: $gettok(a b c d e f,-2-3,32) return the token from the 3rd token to the -2th but $gettok(a b c d e f,-2--3,32) return e f, from -3 to -2

.. note:: For readability you can also code this as $gettok(a-b-c-d-e,2,$asc(-)).

Properties
----------

None

Examples
--------

Echo to the active window, the 2nd token as delimited by the $chr(45) hyphen:

.. code:: text

    //echo -a $gettok(a-b-c-d-e,2,45)
    ; returns b

$chr(32) is the space character. Echo the current month to the active window:

.. code:: text

    //echo -a The current month is $gettok($asctime,2,32)

This returns ``Mon Tue`` because the space between %x %y becomes the 2nd delimiter:

.. code:: text

    //var %x Sun Mon | var %y Tue Wed Thu Fri Sat | echo -a $gettok(%x %y,2-3,32)

$chr(58) is the colon, $chr(92) is the backslash:

.. code:: text

    //echo -a This $gettok($mircexe,-1,92) is installed on the $gettok($mircexe,1,58) drive letter in a program folder named $gettok($mircexe,-2,92)
    //var %i $gettok($mircexe,0,92) | echo -a $gettok($mircexe,1- $+ $calc(%i -1) ,92) is mIRC's path without the ending backslash

.. code:: text

    //echo -a $gettok(Sun.Mon.Tue.Wed.Thu.Fri.Sat,2-4,46)
    ; returns Mon.Tue.Wed (including the delimiter period between the returned tokens
    //echo -a $gettok(Sun.Mon.Tue.Wed.Thu.Fri.Sat,3-,46)
    ; returns all tokens beginning with the 3rd: Tue.Wed.Thu.Fri.Sat

.. code:: text

    //echo -a $gettok(11x22x33x44,3,120)
    ; returns 33 because $chr(120) is lower-case x
    //echo -a $gettok(x11xxxx22x33x44x,3,120)
    ; also returns 33 because duplicate, leading, and trailing delimiters are stripped before $gettok processes the TEXT
    //echo -a $gettok(11x22X33x44,3,120)
    ; returns 44 because the C token is case-sensitive, so capital X isn't a delimiter

$gettok allows the range numbers to be negative

.. code:: text

    //echo -a $gettok(Sun.Mon.Tue.Wed.Thu.Fri.Sat,-4- $+ -2,46)
    ; returns the 4th-from-last through 2nd-from-last tokens
    //echo -a $gettok(Sun.Mon.Tue.Wed.Thu.Fri.Sat,-2-,46)
    ; returns the last 2 tokens
    //echo -a $gettok(Sun.Mon.Tue.Wed.Thu.Fri.Sat,2- $+ -2,46)
    ; returns 2nd token through 2nd-from-last token

$gettok puts range numbers in the correct order before evaluating them.

.. code:: text

    //echo -a $gettok(Sun.Mon.Tue.Wed.Thu.Fri.Sat,4-3,46)
    ; returns same results as if range 3-4 were used
    //echo -a $gettok(Sun.Mon.Tue.Wed.Thu.Fri.Sat,-4-3,46)
    ; returns 4th-from-last token thru the 3rd token regardless whether the 3rd token is the earlier or later token in the list.

.. note:: $gettok differs from CSV format in that it does not use double-quotes to allow a delimiter to be part of another token. If you want $filename to be a token in a comma-delimited list of tokens, you should use :doc:`$replace </identifiers/replace>` to change the comma in the filename into another character that cannot appear in the filename before adding as a token, then use :doc:`$replace </identifiers/replace>` on the extracted token to restore any comma(s). Alternatively use a character other than a comma (like '|') as a delimiter instead.

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$wildtok </identifiers/wildtok>`

