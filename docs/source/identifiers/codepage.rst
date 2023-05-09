$codepage
=========

The $codepage identifier allows you to list all the available codepages and/or get informations about a given codepage.

Synopsis
--------

.. code:: text

    $codepage(N/ID)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N/ID
      - The Nth codepage to be returned, or 0 for the total number of codepage in the list, you can also pass an ID.

.. note:: first ID starts at 437 and only increases from that, while there's a total of only 58 codepages currently, and there should be no overlap given no new codepage are added.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Method
    * - name
      - Returns the name of the codepage
    * - desc
      - Returns the description of the codepage.
    * - id
      - Returns the ID of the codepage (default).

Examples
--------

.. code:: text

    //var %a 1 | while ($codepage(%a)) { echo -sg $v1 -- $codepage(%a).name -- $codepage(%a).desc -- $codepage(%a).id  | inc %a }

* 437 -- ibm437 -- OEM United States -- 437
* 737 -- ibm737 -- OEM Greek -- 737
* 775 -- ibm775 -- OEM Baltic -- 775
* 850 -- ibm850 -- OEM Western European -- 850
* 852 -- ibm852 -- OEM Central European -- 852
* 855 -- ibm855 -- OEM Cyrillic -- 855
* 857 -- ibm857 -- OEM Turkish -- 857
* 858 -- ibm00858 -- OEM Multilingual -- 858
* 860 -- ibm860 -- OEM Portuguese -- 860
* 861 -- ibm861 -- OEM Icelandic -- 861
* 862 -- dos-862 -- OEM Hebrew -- 862
* 863 -- ibm863 -- OEM French Canadian -- 863
* 864 -- ibm864 -- OEM Arabic -- 864
* 865 -- ibm865 -- OEM Nordic -- 865
* 866 -- cp866 -- OEM Russian -- 866
* 869 -- ibm869 -- OEM Greek Modern -- 869
* 874 -- windows-874 -- ANSI Thai -- 874
* 932 -- shift_jis -- ANSI Japanese Shift-JIS -- 932
* 936 -- gb2312 -- ANSI Chinese Simplified GB2312 -- 936
* 949 -- ks_c_5601-1987 -- ANSI Korean Hangul -- 949
* 950 -- big5 -- ANSI Chinese Traditional Big5 -- 950
* 1250 -- windows-1250 -- ANSI Central European -- 1250
* 1251 -- windows-1251 -- ANSI Cyrillic -- 1251
* 1252 -- windows-1252 -- ANSI Western European -- 1252
* 1253 -- windows-1253 -- ANSI Greek -- 1253
* 1254 -- windows-1254 -- ANSI Turkish -- 1254
* 1255 -- windows-1255 -- ANSI Hebrew -- 1255
* 1256 -- windows-1256 -- ANSI Arabic -- 1256
* 1257 -- windows-1257 -- ANSI Baltic -- 1257
* 1258 -- windows-1258 -- ANSI Vietnamese -- 1258
* 1361 -- johab -- Korean Johab -- 1361
* 10000 -- macintosh -- MAC Roman -- 10000
* 20866 -- koi8-r -- Russian KOI8-R -- 20866
* 20932 -- euc-jp -- Japanese JIS X 0208/0212 -- 20932
* 20936 -- x-cp20936 -- Chinese Simplified GB2312 -- 20936
* 21866 -- koi8-u -- Ukrainian KOI8-U -- 21866
* 28591 -- iso-8859-1 -- ISO Western European -- 28591
* 28592 -- iso-8859-2 -- ISO Central European -- 28592
* 28593 -- iso-8859-3 -- ISO South European -- 28593
* 28594 -- iso-8859-4 -- ISO Baltic -- 28594
* 28595 -- iso-8859-5 -- ISO Cyrillic -- 28595
* 28596 -- iso-8859-6 -- ISO Arabic -- 28596
* 28597 -- iso-8859-7 -- ISO Greek -- 28597
* 28598 -- iso-8859-8 -- ISO Hebrew Visual -- 28598
* 28599 -- iso-8859-9 -- ISO Turkish -- 28599
* 28603 -- iso-8859-13 -- ISO Estonian -- 28603
* 28605 -- iso-8859-15 -- ISO Latin-9 -- 28605
* 38598 -- iso-8859-8-i -- ISO Hebrew Logical -- 38598
* 50220 -- iso-2022-jp -- ISO Japanese JIS -- 50220
* 50221 -- csiso2022jp -- ISO Japanese JIS Kana -- 50221
* 50222 -- iso-2022-jp-sio -- ISO Japanese JIS X 0201 -- 50222
* 50225 -- iso-2022-kr -- ISO Korean -- 50225
* 50227 -- x-cp50227 -- ISO Chinese Simplified -- 50227
* 50229 -- iso-2022-cn -- ISO Chinese Traditional -- 50229
* 51949 -- euc-kr -- EUC Korean -- 51949
* 52936 -- hz-gb-2312 -- Chinese Simplified HZ -- 52936
* 54936 -- gb18030 -- Chinese Simplified GB18030 -- 54936
* 65001 -- utf-8 -- Unicode UTF-8 -- 65001

Compatibility
-------------

.. compatibility:: 7.69

See also
--------

.. hlist::
    :columns: 4

