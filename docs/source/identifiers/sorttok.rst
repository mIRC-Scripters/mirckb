$sorttok
========

$sorttok case-insensitively sorts the list of tokens. $sorttokcs is the case sensitive version

Synopsis
--------

.. code:: text

    $sorttok(<list>,C[,nrca])
    $sorttokcs(<list>,C[,nrca])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <list>
      - The list of tokens (can be empty which causes output to also be $null)
    * - <C>
      - The ascii number (or code point) of the character separating the tokens
    * - ncra
      - default is alphabetical sort (ASCII order or codepoint order) if none of 'anc' are used, n = numeric sort; c = channel prefix sort; r = reverse; a = alpha-then-numerics sort

.. note:: Since there is no switch letter for the default sort order, if your script needs to have the sort order in a variable that could possibly be $null, you can put an invalid switch into the 3rd parm to prevent a $null 3rd parm returning the null string: $sorttok(%list,32,- %sort_method)

.. note:: 'n' sort makes no attempt to sort non-numerics, so using the 'n' sort in $sorttokcs is no different than the 'n' sort in $sorttok.

.. note:: DEFAULT sort without any switches is case-insensitive sort by codepoint order except the a-z and A-Z ranges are equivalent to each other, and codepoints 91-96 are inserted preceding 'a' and 'A'. However in $sorttokcs the DEFAULT sort order does not move 91-96 to the different location, and the sort order is entirely by codepoint.

.. note:: 'a' sort is 'alpha-then-numeric' sort, which is the same as DEFAULT except tokens are divided into numeric and non-numeric tokens, and the non-numeric tokens are sorted in 'DEFAULT' sort order followed by the numeric tokens sorted in 'n' order. This is also case-insensitive, treating a-z and A-Z as equivalents, unless using $sorttokcs.

.. note:: 'n' Numeric sort splits tokens into a numeric and non-numeric portion, where the absence of a numeric portion is the same as if '0' preceded non-numerics. When tokens are considered equivalent numerically, they are sorted in order of appearance regardless of the sort order of the non-numeric portion. Original order is also returned for the non-numeric sorts where strings are considered case-insensitive equivalents. The sort order appears to use the return value for $int() when strings are partly/entirely non-numeric. This includes stripping non-numerics from the tail end of numbers, except for considering a leading non-numeric among EeDe potentially being part of scientific notation

.. note:: 'c' sort is identical to DEFAULT sort except the characters of that connection's $prefix are inserted in front of the 'DEFAULT' sort for the 1st character only, while DEFAULT sort is applied to the remainder of the string

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $sorttok(C a c b A B,32)

Result is "a A b B C c" because the a-vs-A and c-vs-C letters are output in the same sequence in which they appear in the original input.

As shown by the following, the DEFAULT switch is mostly-codepoint order and the 'a' switch is alpha-then-numerics order. The DEFAULT sorts tokens in codepoint order except for handling A-Z and a-z as equivalents and inserting codepoints 91-96 immediately preceding the 'a' and 'A', though the DEFAULT sort order for $sorttokcs is pure codepoint order. However in 'a' sort order, tokens which are entirely valid numerics are sorted 'n' numerically following the 'DEFAULT' sort of the tokens which are not entirely numerics.
This next alias sorts the characters at codepoints 1-1223 using default sort order, and the reverse text shows the $asc() value of the sorted tokens, showing they are all sorted in codepoint order except for the 91-96 range and the case-insensitive alphabet.
However, if you modify the %b variable to use $sorttok(%a,32,a) this is using the 'a' sort order 'alpha then numerics', which is an identical sort except for sorting the numeric tokens numerically following the non-numerics:

.. code:: text

    //var %a $regsubex(foo,$str(x,1223),/x/g,$chr($calc(0+ \n)) $+ $chr(32)) , %b $sorttok(%a,32) | echo -a original: $strip(%a) | echo -a sort: $strip(%b) ==> $chr(15) $chr(22) $regsubex(foo,%b,/([^ ])/gu, $asc(\t) ) checksum: $crc(%b,0)
    
    You can change the 1223 to '127' to see a shorter list, making it easier to see the relocation of codepoints 91-96. This next example has the original string having the tokens in reverse order, showing that the case-insensitive equivalents now put the lower-case letters first, because in the unsorted string they now appear earlier than the uppercase letters:
    
    //var %a $regsubex(foo,$str(x,127),/x/g,$chr($calc(128- \n)) $+ $chr(32)) , %b $sorttok(%a,32) | echo -a original: $strip(%a) | echo -a sort: $strip(%b) ==> $chr(15) $chr(22) $regsubex(foo,%b,/([^ ])/gu, $asc(\t) ) checksum: $crc(%b,0)

.. code:: text

    alias NumericMax { return $gettok($sorttok($1- , 32 , rn),1,32) }
    alias NumericMin { return $gettok($sorttok($1- , 32 ,  n),1,32) }

.. note:: the above NumericMax assumes the input contains ONLY numbers, because in a numeric sort, non-numeric is treated as if zero, and is sorted between the positives vs the negative numbers.

.. code:: text

    //echo -a min: $NumericMin(1 2 11) max: $NumericMax(1 2 11)

It appears that $sorttok's numeric sort evaluates each token individually the same was as evaluated by $int(). This means that in 'n' sort, non-numerics are ignored at the end of the token if the token begins with a number, though it treats 'e' or 'E' as potentially being part of a number in scientific notation. 'n' sort treats tokens 2+2 or +2*2 or 2-2 the same as '2' because that's the number prior to encountering a non-numeric. All tokens which evaluate to the same number appear to always be kept in the order they appear in the input, so $sorttok(64 64.0,32,n) and $sorttok(64.0 64,32,n) both return an unchanged string.

.. code:: text

    Leading zero and non-numerics don't affect the numeric sort order:
    //echo -a $sorttok( 1:black 02:blue 14:grey 3:green 13:magenta 5:maroon 6:purple 04:red 7:tan 8:yellow 0:white ,32,n)
    result:
    0:white 1:black 02:blue 3:green 04:red 5:maroon 6:purple 7:tan 8:yellow 13:magenta 14:grey
    
    Content of the non-numeric portion has no effect on the 'n' sort order, so the tokens beginning with '2' are sorted in the order they appear regardless of the ASCII sort order for the non-numeric portion
    //echo -a $sorttok( 4 2:foo 2:bar 1:test,32,n)
    result: 1:test 2:foo 2:bar 4
    
    //var %a $regsubex($str(x,94),/x/g,$chr($calc(32+ \n)) $+ $chr(32)) | echo -a $sorttokcs(11 -11 -1 1 +1 -2 2 $true $false $true -x1xa 0 $false +2*2 0 0.0 %a 5-1 5-11 5-2 2+2 =4 101 99 1E2xx $false 0.1 1d2,32,n)
    
    Returns: -11 -2 -1 $true $false $true -x1xa 0 $false 0 0.0 ! " # $ % & ' ( ) * + , - . / 0 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ =4 $false 0.1 1 +1 1 2 +2*2 2 2+2 3 4 5 5-1 5-11 5-2 6 7 8 9 11 99 1E2xx 1d2 101

.. note:: The first $true through the last $false appear in the output as the same order as in the input because they all $int(token) evaluate as zero. The same happens to the several tokens which all evaluate as 2 or 5. 1E2xx sorts between 99 and 101 because $int(1E2) sees this as scientific notation for 100.

.. note:: The 'r' switch is a modifier which reverses the direction of the sort for the a/n/c sort orders. It does NOT always output the tokens in the reverse order as the sort excluding the 'r', because tokens considered numerical and/or case-insensitive equivalents remain sorted in the original unsorted order.

.. note:: Using the 'c' switch instead of the 'default' changes the sort order to a modified ASCII order matching the sort order of the nicklist for that network. For the 1st character of the string only, tokens beginning with any of the channel $prefix symbols are sorted to the front in the order they appear in $prefix, as if $prefix modes are codepoints below 1. The remaining characters are sorted in 'DEFAULT' order, so if all tokens begin with '@' there is no difference between 'c' and 'default' sort. The 'c' sort uses the $prefix identifier, so the result can be different in a blank status window created with "/server -n" which uses the default $prefix of @%+ than at a network which recognizes ~ and & as nick prefixes or who does not use the % prefix.

For example, the display of the following string depends on the value of $prefix in the window where that command executes:
//echo -a prefix: $prefix network: $network sort: $sorttok( ~owner &protectedop @op % $+ halfop +voice [nick] \nick\ ^nick^ anick znick |nick|,32,c)
Possible Results:<pre>
prefix: prefix: @+ network: freenode sort: @op +voice %halfop &protectedop [nick] \nick\ ^nick^ anick znick |nick| ~owner
prefix: ~&@%+ network: Rizon sort: ~owner &protectedop @op %halfop +voice [nick] \nick\ ^nick^ anick znick |nick|
</pre>

Another example of the default ASCII sort vs 'a' alpha-then-numeric. It includes the CRC32 of each sorted string, which allows you to edit the creation of %a to see how various sort orders may or may not change the original order:

.. code:: text

    //var %a test TEST 2:foo 2:bar 1 2 11 1:test 0 -0 +0 BAR bar FOO !test -1 @test @@x @!x @1 0 , %sort $sorttok(%a,32) , %sortn $sorttok(%a,32,n) , %sorta $sorttok(%a,32,a) , %sortc $sorttok(%a,32,c) | echo -a %a :original | .timer 1 1 echo -a $crc(%a,0) .%a:original order | echo 4 -a %sort :default | .timer 1 2 echo 4 -a $crc(%sort,0) .%sort:'default' = codepoint order then original order among case-insensitive matches | echo 3 -a %sortn :'n' | .timer 1 3 echo 3 -a $crc(%sortn,0) .%sortn :n=sort by $ $+ int(token), non-numerics among all '0' values in original order | echo 4 -a %sorta :'a' | .timer 1 4 echo 4 -a $crc(%sorta,0) .%sorta:a= non-numeric in 'default' sort, then numerics in 'n' sort | echo -a %sortc :'c' | .timer 1 5 echo -a $crc(%sortc,0) .%sortc:c='default' except only-1st-char has $prefix inserted at front
    
<pre>result:
test TEST 2:foo 2:bar 1 2 11 1:test 0 -0 +0 BAR bar FOO !test -1 @test @@x @!x @1 0 :original
!test +0 -0 -1 0 0 1 11 1:test 2 2:bar 2:foo @!x @1 @@x @test BAR bar FOO test TEST :default
-1 test TEST 0 -0 +0 BAR bar FOO !test @test @@x @!x @1 0 1 1:test 2:foo 2:bar 2 11 :'n'
!test 1:test 2:bar 2:foo @!x @1 @@x @test BAR bar FOO test TEST -1 0 -0 +0 0 1 2 11 :'a'
@!x @1 @@x @test +0 !test -0 -1 0 0 1 11 1:test 2 2:bar 2:foo BAR bar FOO test TEST :'c'
D42C1323 .%a:original order
7F1A34E4 .%sort:'default' = codepoint order then original order among case-insensitive matches
EE450764 .%sortn :n=sort by 0 non-numerics among all '0' values in original order
1A803382 .%sorta:a= non-numeric in 'default' sort, then numerics in 'n' sort
C75D4DEA .%sortc:c='default' except only-1st-char has @%+ inserted at front
</pre>

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sorttokcs </identifiers/sorttokcs>`
    * :doc:`$prefix </identifiers/prefix>`
    * :doc:`$max </identifiers/max>`
    * :doc:`$min </identifiers/min>`
    * :doc:`$addtok </identifiers/addtok>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$findtok </identifiers/findtok>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$instok </identifiers/instok>`
    * :doc:`$istok </identifiers/istok>`
    * :doc:`$matchtok </identifiers/matchtok>`
    * :doc:`$numtok </identifiers/numtok>`
    * :doc:`$puttok </identifiers/puttok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`
    * :doc:`$wildtok </identifiers/wildtok>`
