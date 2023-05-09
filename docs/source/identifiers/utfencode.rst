$utfencode
==========

$utfencode returns text encoded to utf8

Synopsis
--------

.. code:: text

    $utfencode(text,gdi)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The text you want to encode to utf8
    * - gdi
      - the gdi charset number representing a codepage, possible value are documented in the next table.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - GDI Charset number
      - Description
    * - 000
      - ANSI_CHARSET
    * - 001
      - DEFAULT_CHARSET
    * - 002
      - SYMBOL_CHARSET
    * - 077
      - MAC_CHARSET
    * - 128
      - SHIFTJIS_CHARSET
    * - 129
      - HANGEUL_CHARSET
    * - 130
      - JOHAB_CHARSET
    * - 134
      - GB2312_CHARSET
    * - 136
      - CHINESEBIG5_CHARSET
    * - 161
      - GREEK_CHARSET
    * - 162
      - TURKISH_CHARSET
    * - 163
      - VIETNAMESE_CHARSET
    * - 177
      - HEBREW_CHARSET
    * - 178
      - ARABIC_CHARSET
    * - 186
      - BALTIC_CHARSET
    * - 204
      - RUSSIAN_CHARSET
    * - 222
      - THAI_CHARSET
    * - 238
      - EASTEUROPE_CHARSET
    * - 255
      - OEM_CHARSET

.. note:: GDI charsets 1 and 255 are system dependent and are therefore expected to return different results across different machines. Values not on the table are treated as a reference to DEFAULT_CHARSET, equivalent to using gdi = 1.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $utfencode(é)
    
    ; Code point 195 in GREEK_CHARSET is looked up and found to have been assigned the abstract character named GREEK CAPITAL LETTER GAMMA.
    ; Unicode's code page is referenced and GREEK CAPITAL LETTER GAMMA is located at code point 915 (U+0393 or $chr(915) in mIRC).
    ; Code point 915 is now encoded using the standard procedure for UTF-8 encoding, as though $utfencode($chr(915)) was originally used.
    //echo -a $utfencode($chr(195), 161)
    

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$utfdecode </identifiers/utfdecode>`

