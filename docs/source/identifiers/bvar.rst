$bvar
=====

$bvar returns the contents of a binary variable. Default is returning the contents as decimal byte values in the range 0-255.

.. note:: $bvar(&var) used without N or M parameters returns the variable name if it exists, otherwise returns $null, this has to be used to check if a binary variable exists before checking $bvar(&bvar,0) to check if it has data.

Synopsis
--------

.. code:: text

    $bvar(&binvar, [ N [ ,M] ] )

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
      - The beginning position within the binary variable. N=0 returns the length of the binary variable. Can also be range, N- or N1-N2. (First byte is pos 1 not offset 0)
    * - M
      - Optional length of the number of values to return. If there are not M bytes beginning at the Nth position, returns all the remaining bytes beginning at the Nth position.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .text
      - - returns a string from the bytes, bytes are decoded from utf8
    * - .ansi
      - returns a string from the bytes, bytes are not decoded from utf8
    * - .word
      - Outputs decimal value of a 2-byte word, seeing bytes in little-endian byte order (low value first)
    * - .nword
      - Outputs decimal value of a 2-byte word, seeing bytes in big-endian byte order (high value first)
    * - .long
      - Outputs decimal value of a 4-byte dword (unsigned long), seeing bytes in little-endian byte order (low value first)
    * - .nlong
      - Outputs decimal value of a 4-byte dword (unsigned long), seeing bytes in big-endian byte order (high value first)

.. note:: word/nword/long/nlong return non-byte values ONLY when M is not used and N is a positive integer without a hyphen, and do not return a series of numbers from a lengthy variable. They return the value from the 2 or 4 bytes beginning at the Nth byte, and returns $null if there are not the needed 2 or 4 bytes to completely fill the word/long.

Example
-------

.. code:: text

    //bset &abc 1 12 34 56 78 | echo -a $iif($bvar(&abc),$v1 exists) $iif($bvar(&xyz),$v1 exists) / $bvar(&abc) / $bvar(&xyz)
      &abc exists / &abc /

.. code:: text

    //bset -ta &var 1 chlo $+ $chr(232) / $utfencode(chlo $+ $chr(232) )  | echo -a $bvar(&var,1-) // $bvar(&var,1-).text
      99 104 108 111 233 32 47 32 99 104 108 111 195 168 // chloè / chloè
    //bset -t  &var 1 chlo $+ $chr(232) / $utfencode(chlo $+ $chr(232) )  | echo -a $bvar(&var,1-) // $bvar(&var,1-).text
      99 104 108 111 195 169 32 47 32 99 104 108 111 195 131 194 168 // chloè / chloÃ¨
    //bset -t  &var 1 chlo $+ $chr(232) / $utfencode(chlo $+ $chr(233) )  | echo -a $bvar(&var,1-) // $bvar(&var,3-11).text
      99 104 108 111 195 169 32 47 32 99 104 108 111 195 131 194 168 // loè / ch
    //bset -t  &var 1 chlo $+ $chr(232) / $utfencode(chlo $+ $chr(232) )  | echo -a $bvar(&var,1-) // $bvar(&var,3-11,5).text
      99 104 108 111 195 169 32 47 32 99 104 108 111 195 131 194 168 // loè

.. code:: text

    Note: showing base-16 values to better visualize the little-endian/big-endian byte changes
    //bset &abc 1 231 32 33 34 35 36 37 38 | var %word = $bvar(&abc,1).word , %nword = $bvar(&abc,1).nword , %long = $bvar(&abc,1).long | var %nlong $bvar(&abc,1).nlong | echo -a in hex: word $base(%word,10,16) nword $base(%nword,10,16) long $base(%long,10,16) nlong $base(%nlong,10,16)
      in hex: word 20E7 nword E720 long 222120E7 nlong E7202122
    //bset &abc 1 16 32 48 64 | var %word = $bvar(&abc,1).word , %nword = $bvar(&abc,1).nword , %long = $bvar(&abc,1).long | var %nlong $bvar(&abc,1).nlong | echo -a in hex: word %word $base(%word,10,16) nword %nword $base(%nword,10,16) long %long $base(%long,10,16) nlong %nlong $base(%nlong,10,16)
     in hex: word 8208 2010 nword 4128 1020 long 1076895760 40302010 nlong 270544960 10203040
    //bset &abc 1 16 32 48 64 128 144 160 176 | echo -a in hex: $base($bvar(&abc,1).long,10,16)
      in hex: 40302010
    //bset &abc 1 16 32 48 64 128 144 160 176 | echo -a $base($bvar(&abc,2).long,10,16)
      80403020
    
    //bset -t &abc 1 abcdefghi | echo -a $bvar(&abc,3-) / $bvar(&abc,3).word $calc($bvar(&abc,4)*256+$bvar(&abc,3))  / $bvar(&abc,3).nword $calc($bvar(&abc,3)*256+$bvar(&abc,4))
      99 100 101 102 103 104 105 / 25699 25699 / 25444 25444
    
    The order swap is by byte not bit. If hex of .long is 0xdeadbeef then .nlong is 0xefbeadde
    //bset &abc 1 $base(ef,16,10) $base(be,16,10) $base(ad,16,10) $base(de,16,10) | echo -a $base($bvar(&abc,1).long,10,16) $base($bvar(&abc,1).nlong,10,16)

Compatibility
-------------

.. compatibility:: 5.3

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
    * :doc:`$bfind </identifiers/bfind>`

