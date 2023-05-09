$bfind
======

$bfind searches &binvar for a matching value. Returns the Nth byte position in the binvar unless .regex prop is used, in which case it returns the number of matches.

Synopsis
--------

.. code:: text

    $bfind(&binvar, N , M , [name])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - &binvar
      - A binary variable name which begins with the & symbol.
    * - N
      - The position within the binary variable where it starts searching.
    * - M
      - Value being searched for, either ASCII decimals 0-255 or text.
    * - name
      - an optional name to go with .regex, to be able to reference captured group later on.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .text
      - - Treats a numeric N as text instead of bytes value, also decode bytes from utf8 before searching.
    * - .textcs
      - - When M is recognized as text, search is performed as case-sensitive
    * - .ansi
      - The bytes of the binvar are not decoded from utf8 before searching.
    * - .regex
      - performs a regex search, you can use the optional 4th name parameter to reference captured group later on. The N parameter is the Nth position in the binvar at which the input string for the regex engine starts,  so that $bfind(&var,3,/^pattern/).regex are possible where ^ matches because the input string starts at byte 3 in the binvar.

.. note:: Searches for text are case-insensitive by default.

Example
-------

.. code:: text

    //bset -t &var 1 test wavmIRC32WAV test | echo -a space beginning pos1: $bfind(&var,1,32) / space beginning pos11: $bfind(&var,11,32) / finds string '32' instead of chr(32) $bfind(&var,1,32).text / case-sensitive: $bfind(&var, 1, $asc(W) $asc(A) $asc(V) ) / case-insensitive: $bfind(&var,1,WAV).text / case-sensitive: $bfind(&var,1,WAV).textcs / not found: $bfind(&var,1,abc).text
    
    result: space beginning pos1: 5 / space beginning pos11: 18 / finds string '32' instead of chr(32) 13 / case-sensitive: 15 / case-insensitive: 6 / case-sensitive: 15 / not found: 0
    
    Note that 32 searches for ASCII 32 (space) except when .text is used. Searching for "WAV" is case-insensitive and finds the lowercase letters, but the search for the 3 ASCII values finds the matching case. Using .textcs is available as of 7.58 to search for a case-sensitive text string without translating it to byte values.
    
    ;Note: starting position in the binvar is either N = 0 or 1
    //bset -t &var 1 testing | echo -ag $bfind(&var,0,/./g).regex -- $bfind(&var,2,/^e/).regex
    ;7 -- 1

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/bread </commands/bread>`
    * :doc:`/bwrite </commands/bwrite>`
    * :doc:`/bcopy </commands/bcopy>`
    * :doc:`/bunset </commands/bunset>`
    * :doc:`/breplace </commands/breplace>`
    * :doc:`/btrunc </commands/btrunc>`
    * :doc:`/bset </commands/bset>`
    * :doc:`$bvar </identifiers/bvar>`
