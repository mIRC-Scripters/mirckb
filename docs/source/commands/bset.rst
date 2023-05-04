/bset
=====

The **/bset** command lets you assign specific ASCII values (or text) at a specific position. If the variable does not exist, a new binary variable will be created and zero-padded until <pos>. If <pos> exceeds the length of the variable, the variable will extend (by zero-padding the gap) to accommodate the new values.

.. note:: Important fact to remember about binary variables is that they are not limited to the local scope of the alias but instead they remain set until processing is complete. Thus it's possible to use the same binary variable within multiple aliases if they call each other during the same script execution.

Synopsis
--------

.. code:: text

    /bset [-c] <&bvar> <pos> <asciivalue> [asciivalue ... asciivalue]
    /bset -t[ac] <&bvar> <pos> <string>
    /bset -z <&bvar>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -t
      - Indicates a string is to be written instead of 1 or more literal ASCII values
    * - -a
      - When used along with -t switch, don't apply UTF-8 encoding to characters in the range 0-255, as long as the string parameter contains no characters > 255.
    * - -c
      - Fills the binary variable with the string/ASCII values and truncates anything after it
    * - -z
      - Creates new or truncates existing &binvar at zero length

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <&bvar>
      - The binary variable name to use/create
    * - <pos>
      - The position to set the new ASCII values or the string, use -1 to append. The first byte of the string is pos 1. If <pos> is greater than the existing length of the binary variable, the string is zero-padded to fill undefined bytes between <pos> and the prior end of string.
    * - <asciivalue>
      - ASCII 0-255 value to write. If values are in range 256 - 2^31-1, writes $and(value,255). If value >= 2^31, writes 255.
    * - [asciivalue ... asciivalue]
      - Additional ASCII values to be written
    * - <string>
      - The string to be written. The length of string or number of values is limited only by the 4150 character line length for the entire command including 'bset'

Example
-------

.. code:: text

    Alias Example {
    ;Create a binary variable set it to "This is fun!"
    bset -t &Example 1 This is fun!

    ;Print out the content of the variable
    echo -a $bvar(&Example, 1-).text
    }

Binary variables have the advantage that they can be accessed from anywhere during the script execution.

.. code:: text

    Alias Example {
    ;Create a binary variable
    bset -t &Example 1 Hello There Bob.
    bb
    }
    Alias bb {
    ; Override that last part and truncate it
    bset -tc &Example 7 Stranger!
    cc
    }
    Alias cc {
    ; print the value
    echo -a $bvar(&Example, 1-).text
    }

This example shows how the variable gets zero-padded if <pos> is outside the size of the variable:

.. code:: text

    Alias Example {
    ; put 'd' as the 5th byte in &var
    bset &var 5 100
    ; same as
    ; bset &var 5 $asc(d)

    ; will print: 0 0 0 0 100
    echo -a $bvar(&var, 1-)

    ; zero-pad bytes 6-8
    bset &var 9 33
    ; will print: 0 0 0 0 100 0 0 0 33
    echo -a $bvar(&var, 1-)

    ; re-writing the 6th byte in order to chop the 7th and later bytes
    bset -c &var 6 $bvar(&var,6)
    ; will print: 0 0 0 0 100 0
    echo -a $bvar(&var, 1-)

    ; append the 4 bytes of the "test" string to the end of existing bytes
    bset -t &var -1 test
    ; will print: 0 0 0 0 100 0 116 101 115 116
    echo -a $bvar(&var, 1-)

    ; replace the 2nd through 4th bytes with "abc"
    bset &var 2 97 98 99
    ; will print: 0 97 98 99 100 0 116 101 115 116 / abcd
    echo -a $bvar(&var, 1-) / $bvar(&var, 2-).text
    ; the string "test" does not print because it starts at byte 2 and stops at position 6 when encountering the ASCII 0
    }

.. code:: text

    create variable with UTF-8 encoding:
    //bset -t &var 1 $chr(233) | echo -a $bvar(&var,1-)
    returns: 195 169
    //bset -ta &var 1 $chr(233) | echo -a $bvar(&var,1-)
    returns: 233
    -a works only when no characters are codepoint 256+
    //bset -ta &var 1 $chr(233) $+ $chr(10004) | echo -a $bvar(&var,1-)
    returns: 195 169 226 156 148
    //bset &var 1 10004 | echo -a $bvar(&var,1-)
    returns $and(10004,255) = '20' instead of the 3 encoded bytes of $chr(10004)

Binary variables are not limited to 4150 length. To fill a 7mb binary variable with all $chr(0)'s sets the last byte as 0, and allows zero-filling the prior bytes with 0x00's:

.. code:: text

    //bset &var 7654321 0 | echo -a Length of variable is $bvar(&var,0)

 To fill a 7mb variable with non-zeroes, it's more efficient to lengthen with /bcopy but bset can set long variables by repeatedly appending bytes. Max length of binary string can depend on your system resources:

.. code:: text

    /fill_with_ones 7654321

    alias fill_with_ones {
    if ($1 !isnum 1-) return | bset &var 1 1
    while ($1 > $bvar(&var,0)) {
    bset &var -1 $str(0 $chr(32),$iif($calc($1 - $bvar(&var,0)) > 999,$v2,$v1))
    echo -a current length: $bvar(&var,0)
    }
    echo -a variable length is $bvar(&var,0)
    }

Prior to 7.69, zero length &binvar had to be created with kludge workarounds like:<br>
noop $regsubex(foo,$null,,,&var)<br>
//bset -t &var 1 A | noop $decode(&var,bm)<br>

.. code:: text

    ;create zero length &binvar:
    //bset -z &var | echo -a $bvar(&var) : $bvar(&var,0)

Because bset is a /command instead of $identifier, it cannot directly write leading/trailing/multiple spaces within variable strings into a binary variable. To accomplish this, you must do it indirectly. This alias shows 3 ways of trying to set a variable containing spaces. The red line shows that using /bset to set a string removes leading/trailing/multiple spaces. The green line shows how to preserve the spaces by adding the bytes of the string 1 at a time. The maroon line shows a much faster way to place long text strings into the binary variable.

.. code:: text

    alias fake_bset-t {
    var -s %var $+($chr(32),$chr(233),$str($chr(32),2),x,$str($chr(32),2))
    bset -t &bin1 1 %var
    echo 4 -a $bvar(&bin1,1-)
    var %i 0
    while (%i < $len(%var)) {
    inc %i
    if ($mid(%var,%i,1) == $chr(32)) bset &bin2 -1 32 | else bset -t &bin2 -1 $mid(%var,%i,1)
    }
    echo 3 -a $bvar(&bin2,1-)
    noop $regsubex(,%var,,,&bin3)
    echo 5 -a $bvar(&bin3,1-)
    bset -t &bin4 1 $replace(%var,$chr(32),$chr(7)) | breplace &bin4 7 32
    echo 7 -a $bvar(&bin4,1-)
    }

If you change the "bset -t &bin2" into bset -ta &bin2" the green method mimics "bset -ta" by storing the $chr(233) as the 233 byte instead of UTF8-encoding it as the 2 bytes 195 169. The last brown method works only if you can identify a character in the 1-127 ASCII range which is guaranteed to not be present in the variable. To accomplish "bset -ta" with the $regsubex method, it'll need to call another alias to handle the different handling of codepoints above 255. (The above method can use either $regsub or $regsubex but below can't use $regsub) Because binary variables exist across all aliases for the duration that your alias or event is executing, you need to make sure to not destroy a binary variable in whichever script calls your alias. You can either pass the variable name as one of the parameters or have the alias create a unique binary variable name based on $ctime and/or $ticks. You can make a unique variable name like:

.. code:: text

    //var %a dummy $+ $ticks $+ $ctime | bset -t & $+ %a 1 test | echo -a $bvar(& $+ %a ,1-).text

Instead, this alias passes "&dummy" as a parameter, and the alias uses that variable name for its own use. The display from running /fake_bset-ta shows that - unlike /var - the binary variables exist outside an alias where they are set or changed. The last 3 of 6 bytes are from $chr(10004) which UTF8-encodes as a 3 byte string.

.. code:: text

    alias fake-bset-ta-sub {
    if ($asc($2) < 256) return $v1
    bset -ta $1 1 $2
    return $bvar($1,1-)
    }
    alias fake-bset-ta {
    var -s %var1 $+($chr(233),$str($chr(32),2),$chr(10004))
    noop $regsubex(,%var1,/(.)/gu,$fake-bset-ta-sub(&dummy,\t) $+ $chr(32) ,%var2)
    bset &bin 1 %var2
    echo -a $bvar(&bin,0) / $bvar(&bin,1-) / last character: $bvar(&dummy,1-)
    }

.. note:: these last 2 methods do not strictly conform to -ta because they add ASCII 128-255 as single bytes even when codepoint 256+ is present. Also, the last method is limited to the number of ASCII numbers which can fit on the command line, so for long strings you need to add them to the variable in shorter chunks at a time, with special handling to make sure you don't lose a space at the end of a chunk. Some codepoints like 10004 encode into 3 3-digit bytes, so if it's possible for a string to consist entirely of such codepoints, you couldn't safely add more than around 330 characters at a time.

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$bvar </identifiers/$bvar>`
    * :doc:`/bcopy </commands/bcopy>`
    * :doc:`/bread </commands/bread>`
    * :doc:`/bwrite </commands/bwrite>`
    * :doc:`/breplace </commands/breplace>`
    * :doc:`$replace </identifiers/$replace>`
    * :doc:`$bfind </identifiers/$bfind>`
    * :doc:`/bunset </commands/bunset>`
    * :doc:`/btrunc </commands/btrunc>`
    * :doc:`$regsubex </identifiers/$regsubex>`
