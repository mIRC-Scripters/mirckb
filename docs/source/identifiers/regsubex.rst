$regsubex
=========

$regsubex performs a regular expression match and then substitute/replace, just like $regsub, but it allows for markers in the replacement and return the substitutions immediatly by default, more information about regex in mIRC (and especially on $regsubex) :ref:`matching_tools-regex`

.. note:: All the matches are made before the replacements, the total number of matches as well as any capture of any match can be accessed in the replacement with :doc:`$regmlex </identifiers/regmlex>`

Note2: $regsubex returns the orignal input if there is no match found, if the /S modifier is used, the control code from the original input will not be returned.

Synopsis
--------

.. code:: text

    $regsubex([name],input,regex,subtext,%var|&binvar)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The optional name of the regex, to be used later to retrieve captured group with :doc:`$regml </identifiers/regml>` or :doc:`$regmlex </identifiers/regmlex>`
    * - input
      - The input text
    * - regex
      - The regular expression for :ref:`matching_tools-regex`
    * - subtext
      - the text to use to replace the match, it can contains the following markers (markers can touch text, they are automatically enclosed in $+ if they touch text). See next table.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Marker
      - Description
    * - \0
      - the total number of captures
    * - \n
      - the current match number
    * - \t
      - the 'matchtext', this is the same as $regml(\n), which is often misleading and not useful when you are using /g with multiple captures/backreferences, better to use \1
    * - \a
      - all match, spaces seperated
    * - \A
      - a non spaced version of \a
    * - \1 \N etc
      - returns the same as $regmlex(\n,N), returns the value of the Nth captured group for that match

Properties
----------

None

Example
-------

.. code:: text

    //var %a | echo -a $regsubex(abcd,/([a-z])/g,-\n \1-)

Note how the 1st example below returns the string in red because the input is not altered when there were no matches. However because the 2nd example found at least 1 match, the result excludes any control codes stripped by the /S modifier flag.

.. code:: text

    //echo -a $regsubex(foo,$chr(3) $+ 4test,/(z)/gS,x)
    //echo -a $regsubex(foo,$chr(3) $+ 4test,/(.)/gS,x)

$regsubex does not return a numeric indicator of whether or not there was a match, it simply returns the input string altered by 0 or more matches, though it also does fill the named capture groups seen by $regml and $regmlex.

Example of translating hex strings into the base10 format needed by /bset

.. code:: text

    //var -s %string $sha256(abc) , %pattern /([0-9a-fA-F]{2})\s*/g , %bytevals $regsubex(foo,%string,%pattern,$base(\t,16,10) $+ $chr(32)) | bset -c &binvar 1 %bytevals | echo -a $bvar(&binvar,1-)

Example of creating a list of the 94 text characters from codepoints 33-126. Note how this is only used for creating the \n token where it increments from the range 1-94, and since there were no capture groups the \t will always be null regardless if there were any matches, and the \t can be removed without changing the result:

.. code:: text

    //echo -a $regsubex(foo,$str(x,94),/x/g,\t $chr($calc(32+ \n)))

result: !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

Example of using $regsubex to create a series of 32 byte values. Then assuming there is 256 bits of entropy in the input, uses $regsubex to create a 256-bit key in hex format. Note that the 2nd method is probably preferrable since it allows each of the 32 random byte values to have an effect on each bit of the key, while the 1st method causes each byte value to affect only 8 bits of the key:

.. code:: text

    //var -s %bytevals $regsubex(foo,$str(x,32),/x/g,$rands(0,255) $+ $chr(32)) | echo -a method1: $lower($regsubex(foo,%bytevals,/(\d+)\s*/g,$base(\t,10,16,2))) | echo -a method2: $sha256(%bytevals)

Example of ROT13 which replaces the a-m range + 13 as n-z, and replaces n-z with a-m. Also the english version of Atbash which replaces each alpha letter with the letter as if the alphabet was flipped backwards. Wizard was possibly created as a word originally due to being itself spelled backwards in this encoding.

.. code:: text

    //echo -a $regsubex(maroon 123 FooBar,/([a-zA-Z])/g,$chr( $calc($asc(\t) $iif(\t isin abcdefghijklm,+13,-13) ))))
    //echo -a $regsubex(maroon 456 Wizard,/([a-zA-Z])/g,$chr( $calc(91+64 + $and(32,$asc(\t)) - $asc($upper(\t)))))

results:
znebba 123 SbbOne
nzillm 456 Draziw

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$regml </identifiers/regml>`
    * :doc:`$regmlex </identifiers/regmlex>`
    * :doc:`$regsub </identifiers/regsub>`
    * :doc:`$regex </identifiers/regex>`
    * :doc:`$regerrstr </identifiers/regerrstr>`
