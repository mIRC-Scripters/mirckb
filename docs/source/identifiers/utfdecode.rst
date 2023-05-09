$utfdecode
==========

$utfdecode returns text decoded to utf8

Synopsis
--------

.. code:: text

    $utfdecode(text,gdi)

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

    //echo -a $utfdecode(Ã©)
    
    ; Unicode code point 915 is encoded via $utfencode() to form its UTF-8 analogue.
    ; The encoded sequence is implicitly decoded back to code point 915 but this is not returned immediately.
    ; First the abstract character GREEK CAPITAL LETTER GAMMA is resolved, then code page GREEK_CHARSET is traversed until the abstract character is found.
    ; GREEK CAPITAL LETTER GAMMA in GREEK_CHARSET is detected at position 195.
    //echo -a $asc($utfdecode($utfencode($chr(915)), 161))
    

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$utfdecode </identifiers/utfdecode>`

