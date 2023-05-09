$maxlenl
========

$maxlenl return the maximum number of characters that can safely be used in a statement in a script.

The current value is 10240

Line Length Limit
-----------------

The value of this identifier return a bit less that the real limit. The real limit is often referred to as the line length limit, it was previously 4150 (where $maxlenl would most likely have returned a safe value of 4096), it is currently 10340, 100 more than the safe limit of $maxlenl's 10240, and this is to account for the length of the command, switches etc, but note that if you come up with a total length of 100+ for your command + switches (think about /write -w"longstringhere"), you obviously won't have 8192 character left, but less.

Versions History of $maxlenl and Line Length Limit:
* 900-ish through v6.31
* 4096+54=4150 Version v6.32 through v7.52 (before $maxlenl identifier existed)
* 8192+100=8292 v7.53 through v7.61 with creation of $maxlenl in v7.53
* 10240+100=10340 v7.62 through current

The main reason this was increased from 8192 to 10240 bytes was to support IRCv3 tags whose length is currently capped at 8191 plus a trailing space, which does not count against the 510 limit for the IRC message itself, but the combined string needed to fit within $maxlenl.

Synopsis
--------

.. code:: text

    $maxlenl

Parameters
----------

None

Examples
--------

.. code:: text

    //echo -a $maxlenl

Note that many identifiers chop strings at $maxlenl+100 instead of chopping at $maxlenl, which makes it difficult to use the output in a script. This next command shows that the output from $utfencode is chopped at $maxlenl+100, which does not leave any remaining room for anything else on the command line. The method for creating %c is one way to prevent the error which happens when trying to create %d:

.. code:: text

    //var %a $str($chr(10004),$maxlenl) | var -s %b $len($utfencode(%a)) | var %c $left($utfencode(%a),$maxlenl) | var %d $utfencode(%a)

As the value of this identifier changes and/or the +100 extra length changes, this can change the result of scripts. The next command shows that /bset silently chops this command from writing more than $maxlenl+100 bytes into the &binvar even though the string is a UTF8 string much longer than 20k bytes in length. $sha1 also chops the input at $maxlenl+100, which is why hashing the %a variable in the next example returns the same result as hashing a variable of length 10240+100=10340 bytes in length, even though this chop is in the middle of the multi-byte UTF8 encoding of a character. So in effect, sometimes this is a CHARACTER limit, and other times it's a BYTE difference.

This identifier also affects strings sent to/from a DLL, where regardless whether the DLL has enabled Unicode mode or not, the byte limit is set to double that of $maxlenl, with the assumption that strings sent to/from the DLL will be UTF16 strings where each character is exactly 2 bytes.

.. code:: text

    //var %a $str($chr(10004),$maxlenl) | bset -tc &v 1 %a | echo -a $bvar(&v,0) -> $sha1(&v,1) same as $sha1(%a)

$cb(-1).len is supposed to return the total length of the string in the clipboard, but the following command shows that, even though the clipboard contains 10 lines each containing 5000 letters, for a total of 50k, the reply from $cb(-1).len is capped at 100+$maxlenl even though $cb(0) includes a total that includes text beyond the 10340th character, so there may be cases where you need to add the lines individually to get an accurate total, should the total state 100+$maxlenl

.. code:: text

    //var %i 1 | clipboard | while (%i isnum 1-10) { clipboard -an $str(a,5000) | inc %I } | var -s %i $cb(0) | while (%i) { echo -ag line %i is $cb(%i).len | dec %I } | echo -a $regsubex(foo,$cb(-1),,,&v) binvar now has $bvar(&v,0) bytes from $cb(0) lines of clipboard with reported total of $cb(-1).len 
    
    result: binvar now has 10340 bytes from 10 lines of clipboard with reported total of 10340

Compatibility
-------------

.. compatibility:: 7.53

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$maxlens </identifiers/maxlens>`
    * :doc:`$maxlenm </identifiers/maxlenm>`
