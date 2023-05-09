$isutf
======

$isutf returns the status of the text where 0 = not utf8 (contains invalid utf8 sequence), 1 = seems to be plain text, 2 = seems to contain valid utf8. In older 6.x versions, the result can change depending on which UTF8 setting is active in the /font dialog.

Synopsis
--------

.. code:: text

    $isutf(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The text you want the status of

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $isutf(é) $isutf($utfencode(é)) $isutf(plain)

Note how this indicates whether the text contains the UTF8 codepoints of a UTF8 sequence, not whether the input is a UTF8 string, which all %strings in a unicode-aware client should be, which is why the next command returns "0 2".

.. code:: text

    //echo -a $isutf($chr(233)) vs $isutf($chr(195) $+ $chr(169))

If you need to test if a &binvar contains a UTF8 string, you can take advantage of the $regsubex feature where it can output a string into a binvar. If the input is $bvar(&var1,1-).text, you can test whether &var2 is created as an exact replica. Note how $isutf returns 0 for both binvars. On the other hand, the isbinvarutf alias returns 2 for &v1 which contains a UTF8 byte sequence, but returns 0 for &v2 because the cloned UTF8 output from $regsubex was not the same bytes as the original. Note that there's a limit to how long of a binvar can be tested using this method, because $regsubex only permits the $2 string to contain more than approximately $maxlenl *bytes* even when that string has fewer than 4000 UTF8 *characters*.

.. code:: text

    //bset &v1 1 195 169 | bset &v2 1 233 | var -s %a1 $bvar(&v1,1-).text , %a2 $bvar(&v2,1-).text | echo -a $isutf(%a1) $isutf(%a2) vs $isbinvarutf(&v1) $isbinvarutf(&v2)
    
    alias isbinvarutf {
      if ($bvar($1,0) == 0) return 0 | var %len1 $v1
      noop $regsubex(foo,$bvar($1,1-).text,,,&tempvar2)
      var %len2 $bvar(&tempvar2,0) | if (%len1 != %len2) return 0
      if ($calc(%len1 + %len2) < 2000) { if ($bvar($1,1-) == $bvar(&tempvar2,1-)) return 2 | else return 0 }
      else { if ($sha256($1,1) == $sha256(&tempvar2,1)) return 2 | else return 0 }
    }

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$utfencode </identifiers/utfencode>`
    * :doc:`$utfdecode </identifiers/utfdecode>`
