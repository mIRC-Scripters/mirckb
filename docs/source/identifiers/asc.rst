$asc
====

$asc returns the Unicode code point number for the character (or first character of the string).

Synopsis
--------

.. code:: text

    $asc(<char|string>)

Switches
--------

None
Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - char
      - This would be any special character, letter, or number for which you wish to retrieve the Unicode code point. Only codepoints 1-65535 are valid. For codepoints above 65535, it instead returns the first UTF-8 surrogate. If the parameter is a string, the 1st character of the string is used as the 'char'. If parameter is a string, it uses only the 1st character of that string.

.. note:: mIRC v6.35 and earlier only support codepoints 1-255

Examples
--------

Echo the Unicode code point for the letters ''A'' and ''a'' to the active window

.. code:: text

    //echo -a A is $asc(A) and a is $asc(a)

Echo the Unicode code point for the number ''7'' to the active window

.. code:: text

    //echo -a $asc(7)

.. code:: text

    Echo the Unicode codepoint for the lower-case 'm' because that's the first character of the string.
    //echo -a $asc(mIRC)
    
    Retrieve the codepoint for any input:
    alias Get_Asc {
      //var %a $input(type or paste any character/string or alt-NNN or alt-0NNN value,e) | echo -a the codepoint for %a  is $asc(%a)
    }
    
    The C parameter for the token identifiers uses the same codepoint number output by $asc():
    //echo -a mIRC.exe is located in folder $gettok($mircexe,-2,$asc(\))

.. code:: text

    Unicode codepoint 128286 has UTF-8 Encoding of 0xF0 0x9F 0x94 0x9F and UTF-16 Encoding of 0xD83D 0xDD1F. Translated to decimal, these numbers are UTF-8 240 159 148 159 and UTF-16 55357 56607. If you change the font to "Segoe UI Symbol" which supports viewing this emoji, you'll see a number 10 inside a box. The numbers in the displayed message are the same even if your Font doesn't correctly display the emoji. This shows that $asc sees the only the UTF-8 surrogates of the string.
    
    //bset &v 1 240 159 148 159 | var %a $bvar(&v,1-).text | echo -a  %a is $asc($mid(%a,1)) $asc($mid(%a,2))

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chr </identifiers/chr>`
    * :doc:`$gettok </identifiers/gettok>`
