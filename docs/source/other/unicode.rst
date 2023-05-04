Unicode
=======

This page does not attempt to describe what Unicode is but rather how mIRC handles it (or in some cases doesn't handle it). The technical terms are omitted on purpose.

mIRC and Unicode
----------------

Before Unicode (mIRC 7.x), mIRC supported Windows' code pages, handling various character sets used in different parts of the world. Code pages encode characters in 8 bits (1 byte): 8 bits can be used to represent 256 values. Code pages all use the first 128 values for ASCII, and then each code page adds the required characters for the language e.g. é for French, although before unicode, for japanese or chinese language, they already needed more than 256 values and where already using special encoding, using more than one byte.

Unicode provides a single character encoding which supports all languages using 1,114,112 distinct characters. Since IRC users are from all over the world, often using their own language and character set, using a single common character set is a major advantage.

Applications can implement Unicode internally in a variety of different ways. mIRC v7+ uses UTF16 encoding internally using 16 bits or 2 bytes to hold each character. Earlier versions used US-ASCII, using 8 bits or 1 byte per character. There are two mains reasons for this:

* The most frequently used characters are encoded from 0 to 65535, and with UTF16 these can be stored with only 16 bits. As a result, the mIRC code dealing with Unicode is going to be faster than UTF32.
* It uses less memory than UTF32.

Drawback: Characters over 65535 are encoded in utf16 as two 16 bits unit called surrogates but mIRC does not *support* this. :doc:`$asc </identifiers/asc>` and :doc:`$chr </identifiers/chr>` cannot be used with characters over 65535.

.. code:: text

    //var -s %a = $chr(55384), %b = $chr(56320) | echo -a %a $+ %b -- $len(%a $+ %b)
    ; 𦀀 -- 2

What happens here is that mIRC pass the two surrogates to /echo, /echos call a Windows' function to display the text, and it is this Windows' function that will 'decode' the surrogates and display the character correctly. As you can see from the example above, although a single character is displayed, $len() is 2, showing that mirc sees two characters.

$regsubex
---------

Whilst rendering functions will normally display characters over 65536 correctly when programmed in this way, some usages of some functions in mIRC, such as $regsubex, won't handle the surrogate as expected. 

.. code:: text

    //echo -ag $regsubex(aa,/(a)/gu,$chr($gettok(55357 56607,\n,32))) vs $replace(ab,a,$chr(55357),b,$chr(56607))

For $regsubex this is because mIRC is using the 8 bits pcre api: when replacing it has to convert your 16 bits unit ($chr(55357) in the first iteration) to UTF8.

.. note:: In fact mIRC does convert the two surrogates to their utf8 representation, except that this is not really correct because surrogates are not really characters; they are just code points used to form others characters, therefore it's improper to decode those bytes to that character because the general algorithm for UTF8 can still be used, and is used by mIRC here, to encode the lone surrogate. So, when mIRC decodes what $regsubex generated, to UTF8, it recognises the illegal sequence and simply return the characters corresponding to the byte, so you get 3 characters per surrogate.

$utfencode / $utfdecode
-----------------------
You can also express those characters with their UTF8 representation using :doc:`$utfdecode </identifiers/utfdecode>`, which decodes UTF8:

.. code:: text

    ;you can use utf8 to form the character 65536 for example, which is four bytes in utf8 (f0 90 80 80):
    //var -s %a $utfdecode($chr($base(f0,16,10)) $+ $chr($base(90,16,10)) $+ $chr($base(80,16,10)) $+ $chr($base(80,16,10)))

    ;𐀀


$utfencode can be used to encode text to utf8:

.. code:: text

    //var -s %a $utfencode(è)

    ;Ã¨

Code Pages
----------
The scripting language still somewhat support code pages, you can decode text to utf8 while the bytes in the text are interpreted in the given code page.

Each code page has a number (Gdi charset):

* 000 - ANSI_CHARSET
* 001 - DEFAULT_CHARSET
* 002 - SYMBOL_CHARSET
* 077 - MAC_CHARSET
* 128 - SHIFTJIS_CHARSET
* 129 - HANGEUL_CHARSET
* 130 - JOHAB_CHARSET
* 134 - GB2312_CHARSET
* 136 - CHINESEBIG5_CHARSET
* 161 - GREEK_CHARSET
* 162 - TURKISH_CHARSET
* 163 - VIETNAMESE_CHARSET
* 177 - HEBREW_CHARSET
* 178 - ARABIC_CHARSET
* 186 - BALTIC_CHARSET
* 204 - RUSSIAN_CHARSET
* 222 - THAI_CHARSET
* 238 - EASTEUROPE_CHARSET
* 255 - OEM_CHARSET

.. note:: GDI charsets 1 and 255 are system dependent and are therefore expected to return different results across different machines. Values not on the table are treated as a reference to DEFAULT_CHARSET, equivalent to using C = 1.

For example, if you want to get the text (FROM GREEK TO UTF8), which used the ISO-8859-7 (GREEK) encoding for greek letters, in utf8, you need to encode that to utf8, interpreting the bytes as per in the GREEK code page, and then to decode that to utf8: $utfdecode($utfencode(text,161))

If you want to send the text in GREEK over IRC, mIRC will encode the bytes internally so you must encode the text in utf8, and then decode to utf8, interpreting the bytes as per in the GREEK code page: /raw -n privmsg #chan $utfdecode($utfencode(text),161)

It must be noted that some commands and identifiers will encode your text to utf8, changing the integrity of your input.
Each character is represented as 16 bits internally, the array of character is not an array of byte, it's an array of 16 bit (two bytes).
But let's take a look at "/msg #chan é".
é is the code point 233, which fits in one byte, but mIRC will encode your byte 233 to utf8, giving the two bytes 165 169.
Now in this case there is little value not encoding in utf8, on IRC you usually don't really care about the integrity of your bytes.
However there are others features where it's not so simple.
$sha1(é) for example can be tricky, this is going to give the hash of the two bytes.
The reason this is happening is because of the conversion, the hashing algorithm works on an array of byte, so mIRC has to take your character (represented in an array of two bytes) and convert them to single bytes, that's why the utf8 conversion happens.
And this is happening pretty much everywhere.

:doc:`/raw -n </commands/raw>` can be used for IRC, it sends the data to the server without encoding the characters in the range 0-255 to utf8.

:doc:`/sockwrite -u </commands/sockwrite>` can be used to the same effect, won't encode characters in the range 0-255 to utf8.

Normalisation
-------------

It is beyond the scope of this wiki page to explain Unicode normalisation in detail, but you should note when e.g. comparing unicode strings that some unicode characters with accents can be encoded as a single integrated character or equally validly as an unaccented character with a modifying accent. 

For example Ô can be sent from another IRC client either as $chr(212) or decomposed into a capital O $chr(79) followed by a combining circumflex $chr(770).

Normalisation is a means of ensuring that all such characters are encoded either as the single integrated character or using modifiers in order that strings which might have a mixture of these techniques can be compared.

mIRC does not support normalisation of Unicode strings either explicitly OR implicitly when comparing strings. 

Experimentation suggests that mIRC does not normally recognise combining characters and will not display the combining character at all, which can lead to communication confusion. So a Ô sent decomposed into capital O $chr(79) followed by a combining circumflex $chr(770) will be displayed as O.

To complicate things still further, some unicode characters look the same as or very similar to other completely different characters - and some of these characters are always considered unequal in strict Unicode whilst others can be converted during normalisation. mIRC treats such characters as different under all circumstances.

Case insensitive comparisons
----------------------------

Without normalization, mIRC therefore fails to correctly compare unicode characters. This is not only true for the scripting language but anywhere in mIRC.

For example if you set a highlight entry with unicode letter, it won't work for a lower/uppercase version of that letter, same with :doc:`/if </commands/if>`'s "==" comparison operator with unicode letter:

.. code:: text

    //echo o === O $iif(o === O,$true,$false) , o == O $iif(o == O,$true,$false)
    ;o === O $false , o == O $true
    ;correct

    //echo ô === Ô $iif(ô === Ô,$true,$false) , ô == Ô $iif(ô == Ô,$true,$false)
    ;ô === Ô $false , ô == Ô $false
    ;incorrect

However, mIRC's :doc:`$upper </identifiers/upper>` :doc:`$lower </identifiers/lower>` identifiers correctly convert upper and lower case unicode:

.. code:: text

    //echo $ $+ lower(Ô) = $lower(Ô) , $ $+ upper(ô) = $upper(ô)
    ;$lower(Ô) = ô , $upper(ô) = Ô

So case insensitive comparisons can be made by explicitly converting both sides to upper or lower case e.g. "if ($upper(%a) === $upper(%b))":

.. code:: text

    //echo ô === $ $+ lower(Ô) $iif(ô === $lower(Ô),$true,$false) , ô == $ $+ lower(Ô) $iif(ô == $lower(Ô),$true,$false)
    ;ô === $lower(Ô) $true , ô == $lower(Ô) $true
    //echo Ô === $ $+ upper(ô) $iif(Ô === $upper(ô),$true,$false) , Ô == $ $+ upper(ô) $iif(Ô == $upper(ô),$true,$false)
    ;Ô === $upper(ô) $true , Ô == $upper(ô) $true

Special Unicode characters
--------------------------

There are also some special unicode characters that e.g. determine RTL / LTR display and these can cause unexpected results when displayed. However unless someone is deliberately trying to create mischief (e.g. a file name which looks innocuous but is in fact a virus laden executable file), these are not normally a problem.