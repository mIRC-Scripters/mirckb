String And Token Manipulation
=============================

String Manipulation
-------------------

String manipulation is the building block of many of today's utilities and algorithms. Everything from formatting and validation to analysis and manipulation requires heavy use of string manipulation. Fortunately for you, the language provides powerful string manipulation facilities.

Basic String Operations
~~~~~~~~~~~~~~~~~~~~~~~

Since everything is a string in mSL, just assigning it to a variable is enough.

.. code:: text

   var %x = This is an example string.

We often want to get the length of such string. The $len identifier can be used to get that.

.. code:: text

   //echo -a $len(apples and oranges)
   18

It is often desired to join two strings together. Such operation is called a string concatenation. The $+ operator can be used to concatenate two string together. For example:

.. code:: text

   //echo -a A $+ B
   AB

It's important to note that both identifiers and variables can be substituted instead of A and B. For example:

.. code:: text

   alias hello {
     var %x = Hello World
     var %x = %x $+ !
     echo -a %x
   }

The output after executing the above code (/hello) is "Hello World!"

Substrings
~~~~~~~~~~

A substring is a string that is part of a longer string. There are a number of built-in identifiers that can be used to retrieve a smaller portion of the original string.

$left() and $right()
^^^^^^^^^^^^^^^^^^^^

The first two identifiers you should be familiar with are the $left and $right identifiers which can be used to return the left or right most part of the original string respectably. Their syntax is:

.. code:: text

   $left(<string>, <length>)
   $right(<string>, <length>)

$left always return text starting from the very left side while $right always return text starting from the right side.

If the length specified is a positive number, $left and $right will return up to that many characters from their respective sides. For example:

.. code:: text

   //echo -a $left(abcdefg, 4) $right(abcdefg, 4)
   ;Left: |abcd|efg
   ;Right: abc|defg|

If the length specified is a negative number, $left and $right return the entire text minus that many characters from their respective sides. For example:

.. code:: text

   //echo -a $left(abcdefg, -4) $right(abcdefg, -4)
   ;Left: |abc|defg
   ;Right: abcd|efg|

Here is one last example before we move on:

.. code:: text

   echo -a $left(Hello There!, 5) $right(Hi World!, 6)

This gets the five left-most characters ("Hello") and the five right-most characters ("World!"). The final output is:

.. code:: text

   Hello World!

$mid()
^^^^^^

$left() and $right() are great but they can get a little complicated if you want to get a substring from the middle of the string. For such cases, the $mid() identifier is a more powerful alternative. $mid() has the following syntax:

.. code:: text

   $mid(<string>, <start>)
   $mid(<string>, <start>, <length>)

Start is the start of the substring from the left. A negative value indicates a start from the right. In both case, an optional length can be specified. A negative length can be used to remove that many characters from the end.

.. code:: text

   alias example {
     var %str = I have not failed. I've just found 10,000 ways that won't work.
     echo -a $mid(%str, 53, 10)
   }

Will output "won't work".

Case Transformation
~~~~~~~~~~~~~~~~~~~

The $islower and $isupper identifiers can be used to determine if a string is entirely made up of uppercase or lowercase letters ($true), or else they return $false. The same functionality is also built into an if statement using the isupper and islower operators. The $upper and $lower identifiers perform case conversion on an entire string or a string character.

.. code:: text

   alias case_example {
     var %x = Some random line!
     echo -a %x = $isupper(%x) $islower(%x)
     var %x = $upper(%x)
     echo -a %x = $isupper(%x) $islower(%x)
     var %x = $lower(%x)
     echo -a %x = $isupper(%x) $islower(%x)
   }

Will generate the following output:

.. code:: text

   Some random line! = $false $false
   SOME RANDOM LINE! = $true $false
   some random line! = $false $true

$lower() and $upper()
^^^^^^^^^^^^^^^^^^^^^

The $lower() and $upper() identifiers can be used to transform the entire string into uppercase or lowercase letters. For example:

.. code:: text

   //echo -a $upper(HeLlO tHeRe)
   //echo -a $lower(HeLlO tHeRe)

Will produce:

.. code:: text

   HELLO THERE
   hello there

Searching
~~~~~~~~~

There are a number of identifiers that can be used to search for a substring within a string. The first one is the $pos identifier which has the following syntax:

.. code:: text

   $pos(<string>, <substring>)
   $pos(<string>, <substring>, <occurrence>)

The first variation returns the position of the first instance of the substring. If the substring is found multiple times within the string, you can specify the Nth occurrence you want. If you specify 0 for the occurrence, $pos will return the total number of substring found within the string.

.. note:: $poscs is a case-sensitive version of $pos; it has the same syntax.

If you simply want to count the number of occurrences a list of substring is found in the string, you can use the $count identifier instead. It's syntax is as follows:

.. code:: text

   $count(<string>, <substring>[, <substring2>, ...])

Multiple substrings can be counted at once. Here is a simple example:

.. code:: text

   $count(Apples and Oranges, apple, orange)

Which will print "2".

.. note:: $countcs is a case-sensitive version of $count; it has the same syntax.

Substring Replacement And Removal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Replacement
^^^^^^^^^^^

There are two built-in string replacement identifiers, $replace and $replacex. The major difference between the two is that the later one will not apply replacement to any of the replaced strings.

It should be noted that both will replace ALL ocurrences of a substring within a string, not just the 1st encountered.

The syntax for both of them is:

.. code:: text

   $replace(<string>, <substring>, <replacement>[, <substring2>, <replacement2>, ...])
   $replacex(<string>, <substring>, <replacement>[, <substring2>, <replacement2>, ...])

Let's start off with a small example:

.. code:: text

   echo -a $replace(Hello World!, world, there)

Which will print "Hello there!". Below is a simple example. Note the difference between $replace and $replacex.

.. code:: text

   alias rep {
     var %str = 1 2 3 4
     ; Each replacement will replace the previous one
     echo -a $replace(%str, 1, 2, 2, 3, 3, 4, 4 , 5)
     ; Exclusive replacements
     echo -a $replacex(%str, 1, 2, 2, 3, 3, 4, 4, 5)
   }

Executing /rep will produce the following results:

.. code:: text

   5 5 5 5
   2 3 4 5

An example of replacing ALL occurances can be seen in:

.. code:: text

   //echo -s $replace(This is a test of the replace function, $chr(32), .)

which will output (in this case to the status window [-s]):

.. code:: text

   This.is.a.test.of.the.replace.function

$replacex will provide the same in this case.

.. note:: $replacecs/$replacexcs are case-sensitive versions of $replace/$replacex; it has the same syntax.

Substring Removal
^^^^^^^^^^^^^^^^^

$remove is an identifier that can remove all occurrences of the substrings from the string. The syntax is:

.. code:: text

   $remove(<string>, <substring>[, <substring2>, <substring3>, ...])

A small example is:

.. code:: text

   //echo -a $remove(aa bb cc dd ee aa bb cc dd ee, bb, dd)

Produces:

.. code:: text

   aa cc ee aa cc ee

Miscellaneous Identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~

Two more identifiers you should be aware of are $str() and $strip().

$str()
^^^^^^

$str returns the same exact string repeated N amount of times. The syntax is:

.. code:: text

   $str(<string>, <N>)

For example:

.. code:: text

   //echo -a $str(Example, 10)

Produces:

.. code:: text

   ExampleExampleExampleExampleExampleExampleExampleExampleExampleExample

$strip()
^^^^^^^^

The $strip identifier can remove control codes from a string. The syntax for it is:

.. code:: text

   ;Removes all control codes (bold/underline/italics/color/reverse)
   $strip(<string>)
   ;Removes any combination of control codes
   $strip(<string>, buricmo)

.. code:: text

   b = bold
   u = underline
   r = reverse
   i = italics
   c = color
   m = use messages option settings

Using Token Manipulation
~~~~~~~~~~~~~~~~~~~~~~~~

Whilst the token manipulation functionality is designed to be used for maintaining lists of delimited tokens, they can also be used for string manipulation. For example, extracting a channel from a string can be done with:

.. code:: text

   //echo -a # $+ $gettok($gettok(Why not join #superheros now?,2,35),1,32)
   #superheros

.. _token_manipulation:

Token Manipulation
------------------

If you are like many people who are coming from another programming language it might come as a surprise to you that there are no true arrays in mSL. This is because the paradigm is a little different: an array in mSL can be thought of as simply a list or vector of tokens. In mSL, a token is simply a string of characters that is separated by a single, unique character. mIRC provides an extensive set of identifiers and commands to help you manipulate this list of tokens.

Lists
~~~~~

To better understand this concept; let's consider a simple alias that returns the day of the week from a given Nth day. In this case, our list of tokens will look something like this:

.. code:: text

   Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday

The first thing you can see is that we have the tokens (in this case, the days of the week) separated by a comma. In this example, the comma is called a delimiter. In mSL, a delimiter is a single character used to specify the boundary between two separate tokens in a list. The example above also has a special name: comma-separated values (CSV).

One of the most commonly used identifiers is the $gettok identifier. The $gettok identifier can be used to retrieve a single token from a list separated by a specific character according to its position. For example, Sunday is the first token and thus position 1. Monday is position 2.

Lets take a look at a working $getday alias. We will talk about the exact syntax of $gettok later on.

.. code:: text

   /* $getday(<1-7>) - returns the day of the week
    */
   alias getday {
     if ($1 !isnum 1-7) {
       echo -sce info * Invalid parameters: $!getday
       halt
     }
     var %days = Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
     return $gettok(%days, $1, 44)
   }

The example above will return the day of the week given its Nth position, for example $getday(1) will return Sunday. Notice how $gettok took the list of days, the position (first argument), and the delimiter. 44 is the code point for the comma character (U+002C). We will talk about how the $gettok identifier works in more detail later on.

Delimiter
~~~~~~~~~

As we said before, a delimiter is a single character used to specify the boundary between two separate tokens in a list. For all the built-in token manipulation commands and identifiers, the delimiter is the code point value of the character. For more information, check out Unicode.

It is important to note that you cannot represent a $null or empty token. Additionally, multiple consecutive delimiters are treated as a single delimiter. Leading and trailing delimiters are ignored.

$N Identifiers
~~~~~~~~~~~~~~

You may have noticed the use of the $1 identifier in the getday alias above. $1 returns the first argument that was passed to the alias. For example, if we use $getday(3), $1 will be 3. The exact rules on how the $N identifiers work can be found in the aliases tutorial. The number of tokens in $N is stored in $0.

It is important to note that you can also populate the $N identifiers via the /tokenize command.

Adding/Inserting/Replace Tokens To A List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two built-in ways to add or insert a token into a list: the $addtok and $instok identifiers.

.. code:: text

   var %newList = $addtok(<list>, <token>, <code_point>)
   var %newList = $instok(<list>, <token>, <Nth_pos>, <code_point>)

The major difference between $instok and $addtok is that $addtok will not append a token that is already found in the string while $instok will. \<Nth_pos\> is the position of where the token should be placed. For example 5 will be the 5th element. A negative number can be used as well to indicate the Nth token from the end instead of the begin. For example -1 is the 2nd to last element, or the 1 element before the last element.

.. code:: text

   //echo -a $addtok(A B C D, E, 32)
   A B C D E
   ;remember $addtok will not add duplicates
   //echo -a $addtok(A B C D, A, 32)
   A B C D
   //echo -a $instok(a b c, @, 1, 32)
   @ a b c
   ;instok will add duplicates
   //echo -a $instok(a b c, a, 2, 32)
   a a b c

A nice application is an auto-joiner script. Using the /ajoin_add command we can add more channels to our auto-join script.

.. code:: text

   ; add channel to auto-join list
   ; /ajoin_add #foo
   alias ajoin_add {
     set %auto_join $addtok(%auto_join, $1, 44)
   }
   on *:connect:{
     timer 1 1 join %auto_join
   }

Replacing Tokens
^^^^^^^^^^^^^^^^

To replace a token you can use $puttok and the $reptok. $puttok replaces by the Nth token while $reptok replaces by the token's value.

.. code:: text

   var %str = $puttok(<list>, <token>, <Nth_pos>, <code_point>)
   var %str = $reptok(<list>, <token>, <newToken>, <Nth_pos>, <code_point>)

for example:

.. code:: text

   ; mask an ip address
   alias maskIP return $puttok($1, xxx, 3-, 46)
   ; //echo -a $maskIP(192.168.1.1)
   ; 192.168.xxx.xxx

Removing Tokens
^^^^^^^^^^^^^^^

There are two identifiers that lets you remove tokens from the list: $deltok allows the deletion of tokens by their position while $remtok can be used to delete tokens by their value.

.. code:: text

   var %str = $deltok(<list>, <Nth_pos>, <code_point>)
   ;$deltok also supports a range of tokens
   var %str = $deltok(<list>, <Nth_pos-N2th_pos>, <code_point>)
   var %str = $remtok(<list>, <token>, <Nth_pos>, <code_point>)

$deltok can delete a single token or multiple depending on the specified range. $remtok's parameter is used to specify the Nth matching token to be removed. If is 0, all matching tokens are removed.

.. code:: text

   //echo -a $deltok(this is not really cool!, 3-4, 32)
   this is cool!
   //echo -a $deltok(A B C D, -1, 32)
   A B C
   //echo -a $remtok(A:B:C:A:B:C:A:B:C, A, 0, 58)
   B:C:B:C:B:C

Practical Applications
~~~~~~~~~~~~~~~~~~~~~~

By now, you should be seeing why arrays in other languages can be visualized as a list of tokens in mSL. Below is a practical example of a simple queue (a FIFO, first-in-first-out, data structure). You can run the driver by calling /queue_example.

.. code:: text

   /* A very simple queue example
   */
   alias queue_push {
     set %queue $instok(%queue, $1, 0, 7)
   }
   alias queue_pop {
     var %tok = $gettok(%queue, 1, 7)
     set %queue $deltok(%queue, 1, 7)
     if (!%queue) unset %queue
     return %tok
   }
   alias queue_example {
     queue_push item1
     queue_push item2
     queue_push item3
     while ($queue_pop) echo -a $v1
   }

The script above uses character with the code point of 7 as its delimiter. The script works pretty well for small values (can store as much as 200 items with an average value length of 20 characters or 20 lines with an average of 200 characters per line). Clearly one of the preconditions is that the value cannot contain any characters with a code point value of 7. This example is clearly not suitable for large queues or queues that must execute really fast. (The reason we've used code point 7 is because it's a control character that means bell signal. This makes it one of the least likely characters to be used as a value).

Token Searching/Retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes we do not know the position or the entire value of a token. There are a number of built-in identifiers to help search a list for a specific token. To search for a token in a string there are three useful identifiers for that: $findtok, $matchtok, and $wildtok. To retrieve the Nth token from a string there is $gettok.

.. code:: text

   ;will return the position of the Nth matching token
   var %pos = $findtok(<list>, <token>, <Nth_pos>, <code_point>)
   var %result = $matchtok(<list>, <substring>, <Nth_pos>, <code_point>)
   var %result = $wildtok(<list>, <wildstring>, <Nth_pos>, <code_point>)
   ;to get the Nth token
   var %tok = $gettok(<list>, <N>, <code_point>)

$findtok looks for an exact match while $matchtok looks for a partial match. $wildtok supports wildcard characters (? & \*) in the substring parameter. They also support 0 for to get the total number of matches.

.. code:: text

   //echo -a $findtok(a a b c d, a, 0, 32)
   2
   //echo -a $matchtok(this is an example, e, 1, 32)
   example
   //echo -a $wildtok(this is a test, ?e?t, 1, 32)
   test
   //echo -a $gettok(192.168.1.0, 1, 46)
   192

.. _miscellaneous-identifiers-1:

Miscellaneous Identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the identifiers we've introduced above, there are a few identifiers that have a more general purpose.

Size Of List
^^^^^^^^^^^^

To get the size or number of tokens in a list, you can use the $numtok identifier:

.. code:: text

   var %count = $numtok(<list>, <code_point>)

Existence And Sorting
^^^^^^^^^^^^^^^^^^^^^

The $istok identifier is perhaps the most commonly used identifier in the entire language. It simply returns true or false if the token exists in a list or not.

.. code:: text

   var %result = $istok(<list>, <token>, <code_point>)

Another useful feature is the $sorttok identifier which lets you sort the list of tokens numerically, alphabetically, or according to the channel mode prefix. Using r with any of the options will reverse the order.

.. code:: text

   var %result = $sorttok(<list>, <code_point>, <sortingOption>)

A common application is to validate that a value is one of a few possible options.

.. code:: text

   if ($istok(red green blue yellow, $1, 32)) {
     echo -sce info * Invalid color: $!foobar
     halt
   }

The sorting options are n for numeric, c for channel prefix, and a for alphabetical. r can be used with any of the options to reverse the order.

.. code:: text

   ;reverse numeric sort
   //echo -a $sorttok(456 3 7 2345 78 23 9943 123 54 1 34 -45 -22, 32, nr)
   9943 2345 456 123 78 54 34 23 7 3 1 -22 -45
   ;channel prefix
   //echo -a $sorttok(+aa @bb +cc dd @ee, 32, c)
   @bb @ee +aa +cc dd

Tokenizing A String
^^^^^^^^^^^^^^^^^^^

Recall from an earlier tutorial that when you call an alias as a command, all the parameters you pass to it are stored in $N. It's possible to programmatically create this same result using the /tokenize command. That command lets you break down a string into tokens that will be stored in $N.

.. code:: text

   tokenize <code_point> <string>

For example

.. code:: text

   //tokenize 32 A B C | echo -a $0 - $3, $2, $1
   3 - C, B, A

Case Sensitivity
~~~~~~~~~~~~~~~~

None of the identifiers explained above are case sensitive. If you wish to work with a case sensitive list or tokens, it's still possible. All the identifiers have their counterpart case sensitive version. They follow the same syntax and they names are identifier with the addition of the "cs" at the end.

For example:

-  $istok -> $istokcs
-  $matchtok -> $matchtokcs
-  $findtok -> $findtokcs
