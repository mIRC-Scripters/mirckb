$replace
========

$replace Performs search/replace on text strings. $replacecs is the case sensitive version.

$replace can replace an already replaced string, it searches all substrings at every position in the text and start from the beginning of the string whenever there is a replacement made, :doc:`$replacex </identifiers/replacex>` can be used to prevent what has already been replaced from being checked again

Synopsis
--------

.. code:: text

    $replace(text, substring, replace, stringN, replaceN)
    $replacecs(text , substring, replace, stringN, replaceN)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The string you want to replace from
    * - substring
      - The 1st string you want to search for
    * - replace
      - the replacement for the 1st string
    * - substringN
      - The Nth string you want to search for
    * - replaceN
      - the replacement for the Nth string

.. note:: Excluding the first parameter (input string), there must be an even number of substring/replace parameters

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $replace(Abcdabcd, a,b, a,c )
    The 2nd pair does nothing because the first pair replaced all the a's with b's. Search is case-insensitive so both 'A' and 'a' match against 'a'.
    result: bbcdbbcd
    
    //var %string $chr(233) , %search $upper(%string) | echo -a $replace( %string , %search ,x)
    result: é
    case-sensitive applies only to a-z A-Z ranges, and does not apply the same rules as $upper and $lower.
    
    //echo -a $replace(abcdabcd, a,b ,b,c )
    The 1st pair changes the string to bbcdbbcd
    The 2nd pair changes the modified string, changing all the b's into c's
    result: cccdcccd
    
    //echo -a $replace(abcdabcd, a,aa, a,x)
    The 1st pair changes each 'a' into 'aa', modifying string to aabcdaabcd
    The 2nd pair changes the modified string, changing the 4 'a' strings into 'x' strings.
    result: xxbcdxxbcd
    
    //echo -a $replace(abcdabcd, a,x, a,aa)
    With the search pairs in the opposite order, the first pair changes string to xbcdxbcd
    The 2nd pair does nothing because there are no 'a' strings in the modified string.
    
    //echo -a $replace( 1234, 1,2, 2,3, 3,4 )
    result: 4444
    The 1st search pair changes all '1' into '2', modifying string to 2234
    The 2nd search pair changes all '2' into '3', modifying again  to 3334
    The 2nd search pair changes all '3' into '4', modifying again  to 4444
    
    //echo -a $replacex(1234, 1,2, 2,3, 3,4 )
    result: 2344
    The 1st match against the 1st character replaces the '1' with '2', moving the pointer to the '2' following the match.
    The 1st match against that new position replaces that '2' with 3, moving the pointer to the '3' following the match.
    The 1st match against that new position replaces that '3' with '4', moving the pointer to the '4' following the match.
    There are no more replacements, leaving the string as 2344.
    
    //echo -a $replace(aaaaaa,aa,a)
    result: aaa
    The replacement strings do not become part of the match string for that same search/replace pair.
    
    //echo -a $replace( aaaaaa,aa,a,aa,a)
    result: aa
    The 2nd pair sees the modified 'aaa' string and finds only 1 match.
    
    //echo -a $replacex(aaaaaa,aa,a,aa,a)
    result: aaa
    The identical 2nd pair never has a chance to match anything because the first pair always matches anything the 2nd could match before the pointer moves forward.
    
    //echo -a $replace(aaabbb,ab,)
    result: aabb
    Removes the 'ab' at position 3 (replaces 'ab' with $null), to make the string be 'aabb' and set the cursor at the character following the match. It makes no more replacements because there are no more 'ab' strings beginning at the new position.
    
    //echo -a $replace(aaabbb,,ab)
    result: aaabbb
    Unlike $regsub, if searchstring is $null, no change is made.
    
    //echo -a $replace(red fred red,red,x)
    replaces all 'red' strings with 'x'
    result: x fx x
    
    //echo -a $replace(red fred red,red $+ $chr(32) ,x)
    replaces only when 'red' is followed by a space
    result: xfxred
    
    //echo -a $replace(red fred red,$chr(32) $+ red,x)
    replaces only when 'red' is preceded by a space
    result: red fredx
    
    $replace is faster than $regsub for simple search/replace, but for many pairs it can become slower. Removing punctuation by replacing them with spaces:
    
    //var %sp $chr(32) | tokenize 32 $me $+ !?,*() | var %string $replace($1-,$chr(44),%sp,.,%sp,',%sp,',%sp,?,%sp,*,%sp,$chr(40),%sp,$chr(41),%sp ,!,%sp,;,%sp,:,%sp) | echo -a $1- / $istok(%string,$me,32)

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$replacex </identifiers/replacex>`
    * :doc:`$regsub </identifiers/regsub>`
    * :doc:`$regsubex </identifiers/regsubex>`
