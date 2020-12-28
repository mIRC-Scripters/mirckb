Matching Tools
==============

Wildcard
--------

Wildcard characters are special characters that are interpreted when comparing text.

There are three meaningful wildcard characters:

-  ? - Matches a single character
-  \* - Matches verything (including nothing)
-  & - Matches a whole word if used alone

Examples
~~~~~~~~

The expression "t*s a \*?t" matches the string "this is a text".

.. note:: If **&** is not used alone it matches the plain text '&' character. It also doesn't match $chr(32) if used to match a whole word, see below.

-  "test &" matches "test this" or "test that"
-  "test &his" matches only "test &his"
-  "test thi&" matches only "test thi&"
-  "test th&s" matches only "test th&s"
-  "test &" doesn't match "test $chr(32)" (consider $chr(32) to be evaluated here)

Bitwise operator?
^^^^^^^^^^^^^^^^^

Be careful when using the **&** wildcard character inside /if (and the like: $iif, /while, /elseif) it could be interpreted as the & bitwise operator:

.. code:: text

   if (test & iswm test this)

This is not true because & is used as the bitwise operator, you can use $eval() to force mIRC to read the parameter the way you want:

.. code:: text

   if ($(test &) iswm test this)

.. note:: If you need to use any of these special characters as plain text in an expression where they are taken as wildcard character (that is, not always the case for &), you can try to use a regular expression instead.

The number of function/feature of the language supporting wildcard matching is simply too high to make a list, but here are the main usage:

The iswm operator can be used with /if (and the like) to make a wildcard comparison:

.. code:: text

   if (test* iswm $1-) { }

Wildcard-matches can also be used in token manipulation, hash tables, custom windows, on events, variables, etc. etc.

Regex
-----

Regular expressions, from here on referred to as regex, can be used to perform complicated pattern matching operations. Users should already be familiar with, and comfortable using, Regular Expressions at this point.

.. note:: A back reference is the same as a capturing group.

General information
~~~~~~~~~~~~~~~~~~~

mIRC uses the 8bits version of PCRE library to implement regex with the following options enabled:

.. code:: text

   --enable-utf8
   --enable-unicode-properties
   --with-match-limit - around 1,000,000
   --with-match-limit-recursion - 999

The newline sequence by default is $lf.

mIRC has four custom modifiers for regex:

.. code:: text

   S - Strips control codes from the input before matching (not supported by $hfind).
   g - Performs global matches: after one match has been found, mIRC tries to match again from the current position.
   F - Enable the correct regex behavior: before mIRC 7.44, non participating capturing group were ignored in $regml, see http://forums.mirc.com/ubbthreads.php/topics/260397/Bug_$regmlex#Post260397
   u - Enable the (*UCP) option (makes \b and \w works for unicode letters) and the (*UTF8) option (forces the string and pattern to be interpreted as utf8).

mIRC does not allow you to retrieve the full match. You can access simple captures but you cannot access named capture. Here is an alias which allow you to get the full match (made by jaytea):

.. code:: text

   ; $regexm(<string>, <regex> [, N])[.pos] or its position

   ; Get the Nth value of match[0] (defaults to N = 1)
   ; Return its position with .pos

   alias regexm {
     noop $regex(full, $2, /^(?|m(.)?|(/)|^)(.*?)(?:\1(?!.*\1)(.*)$)?$/usD)
     noop $regex(pcre, $regmlex(full, 1, 2), /^((?:(?!\((?:(?:MARK|PRUNE|SKIP|THEN|\*(?=:))(?::[^()]*)?|ACCEPT|COMMIT)\))\(\*.*?\))*)(.*)/us)
     if (!$regex( , $+(/, $regmlex(pcre, 1, 1), |, $regmlex(pcre, 1, 2), /))) {
       echo -eagc i * $!regexm: Invalid expression ( $+ $regerrstr $+ )
       return
     }
     var %char, %exp
     while ($chr($r(2048, 55295)) isin $1) /
     %char = $v1
     var %exp = $+(m, $regmlex(full, 1, 1), $regmlex(pcre, 1, 1), (?: $+ $regmlex(pcre, 1, 2) $+ \E)(?(R)|\K), $regmlex(full, 1, 1), $regmlex(full, 1, 3))
     var %str = $regsubex($1, %exp, %char) .
     if (!$pos(%str, %char, $regex($1, $2))) {
       noop $regex(check, $regsubex($1, $2, %char), / %char ( %char ?)/gxu)
       %str = $regsubex(fix, $left(%str, -2), / %char \K/gxu, $regml(check, \n)) .
     }
     noop $regex(final, $left(%str, -2), $+(/\Q, $replacecs($regsubex($1, $2, %char), \E, \E\\E\Q, %char, \E(.*?)\Q $+ %char), \E/u))
     if ($prop == pos) && ($3. isnum 1- $regml(final, 0)) return $calc(1 + $regml(final, $3).pos - $3)
     returnex $regml(final, $3 1)
   }

mIRC remembers up to 50 regex matches. After 50 matches, the first match is overwritten and the backreferences for that match are lost.

Example:

.. code:: text

   /(This is) (a ) pattern/

This represent one regular expression (or one pattern) with 2 captured backreferences.

Sanitizing the input
^^^^^^^^^^^^^^^^^^^^

If you pass value dynamically in a regex pattern, you have to escape any characters in such value that could otherwise be interpreted by the PCRE regex engine.

Instead of escaping a bunch of characters with , which is supported, PCRE allows for the \Q \E construct to not interpret anything between that construct:

Looking for a match on a nickname such as nick[name], you could use ``/\b $+ \Q $+ $nick $+ \E\b/``

This is good but still has one flaw, if $nick contains \E, it will terminate the escaping sequence and subsequent character would be interpreted by PCRE.

To solve the issue, you have to "escape" all the \E inside the value you're using:

.. code:: text

   /b\Q $+ $replacecs($nick,\E,\E\\E\Q) $+ \E\b/

There's no way to escape a character inside the escaping sequence \Q\E, you have to first terminate the sequence yourself with \E, then you have to match the actual \Emfrom the input with \\E, and then start a new escape sequence with \Q.

Regex Identifiers
~~~~~~~~~~~~~~~~~

The four main identifiers, $regex, $regsub, $regml, and $regsubex, can take an optional Name as a parameter. This name can be used to get the backreference captured by the regex match. If a name is not specified, mIRC uses a default one.

$regex
^^^^^^

.. code:: text

   $regex([name],<input>,<regex>)

The sample above performs a regular expression match and returns the number of matches found.

If the /g modifier is used, that number can be greater than 1. You may see a negative value being returned if an error occured.The list below is not exhaustive, but the error ommited are the one that can only happen because of a bug in mIRC in the way it uses pcre, which should never happen in practice.

.. code:: text

   -5 - rare, the compiled pattern has an error in it, could be due to a bug in pcre or because the pattern has been overwritten.
   -6 - memory could not be allocated.
   -7 - memory could not be allocated (specific to retrieving capturing groups)
   -8 - you reached the maximum number of backtracks allowed, for example: $regex($str(a,4000),(a+a+)\*b)
   -14 - mIRC uses this value when compiling the pattern fails but it's a valid value meaning an internal error occured as well. If this error is returned because compiling the pattern failed, {{mIRC|$regerrstr}} is set with an error string, otherwise -14 it's the pcre meaning, which is more or less the same as -5 but happens elsewhere in the code.
   -21 - you reached an internal recursion limit, for example: $regex($str(a, 1000), (a)+)
   -26 - this error is returned when pcre detects a recursion loop within the pattern. Specifically, it means that either the whole pattern or a subpattern has been called recursively for the second time at the same position in the input string. Some simple patterns that might do this are detected and faulted at compile time, but more  complicated cases, in particular mutual recursions between two different subpatterns, cannot be detected until run time.

$regml
^^^^^^

.. code:: text

   $regml([name],N)

$regml can be used to return the Nth back-reference. It takes the optional [name] used in $regex/$regsub/$regsubex. As with all other aspects of mIRC identifier, if 0 is specified as the Nth reference, then the total number of backreferences is returned.

$regml also has a .pos property, which returns the position within the input where the capture occurred.

Below is an example of a regular expression, using name as the optional [Name] property, and then using $regml to reference the match(es):

.. code:: text

   //noop $regex(name, test, /([es])/g) | echo -a $regml(name, 0) : $regml(name, 1) -- $regml(name, 2)

would display "2 : e – s"

.. note:: $regml is a list of all captures accross all the matches made (/g modifier), which is often enough, but can be a problem in some cases.

.. code:: text

   //noop $regex(name, teasat, /([es])(a)/g) | echo -a $regml(name, 0) : $regml(name, 1) -- $regml(name, 2) -- $regml(name,3) -- $regml(name,4)

would display "4 : e – a – s – a"

You can now access the Nth captured group for a given match number with $regmlex.

$regmlex
^^^^^^^^

.. code:: text

   $regmlex([name],M,N)

As stated above for $regml, when /g is used, $regml can be inconvenient: you cannot get all the captured group for a given match number for sure when you don't know about the pattern or input string in advance, this identifier allows you to retrieve these captured groups (backreferences). M is the Mth match and N is the Nth capturing group, N default to 1 if not specified. It supports the same properties as $regml.

$regsub
^^^^^^^

.. code:: text

   $regsub([name], <input>, <regex>, <subtext>, <%varname>)

Performs a regular expression match, like $regex, and then performs a substitution using ``<subtext>``. Returns the number of substitution made and fills ``<%varname>`` with the resulting text.

.. code:: text

   //var %res | noop $regsub(name,test,/([es])/g,t,%res) | echo -a $regml(name,0) : $regml(name,1) -- $regml(name,2) : %res

$regsubex
^^^^^^^^^

.. code:: text

   $regsubex([name],<input>,<regex>,<subtext>)

$regsubex is a more modern version of $regsub, in that it performs the match, then the substitution, and finally returns the result of the substitution.

This time, ``<subtext>`` is evaluated during substitution so you can use %variables and $identifiers there, they will be evaluated.

.. note:: You can now use $regsubex the same way as $regsub to get it to return the number of match and filling a %variable with the result, the name is required, both also supports output to a binvar: ``$regsubex([name],<input>,<regex>,<subtext>,%var|&binvar)``

Markers, $1- and Nested $regsubex calls
'''''''''''''''''''''''''''''''''''''''

Special markers can be used inside the parameter of $regsubex:

.. code:: text

   \0 - Returns the number of matches.
   \n - Returns the current match number.
   \t - Returns the current match text (same as $regml(\n)).
   \a - Returns all matching items.
   \A - Returns a non-spaced version of \a.
   \1 \2 \N ... - Returns the Nth back-reference made for a given match

.. code:: text

   $regsubex(a@bc@ef,/([a-z])([a-z])/g,<\1><\n><\t><\a><\A><\2>)

Here you have two matches with two backreferences made per match:

First match is on 'bc':

.. code:: text

   \1 is 'b'
   \2 is 'c'
   \n is 1 because it's the first match.
   \t is the current matchtext (same as $regml(\n)), which is 'b'
   \a is "b c" while \A is "bc"

Second match is on 'ef':

.. code:: text

   \1 is 'e'
   \2 is 'f'
   \n is 2 because it's the second match.
   \t is the current matchtext (same as $regml(\n)), which is 'c' and not 'e' (\n is 2), it is important to note that when you have more than one backreference and more than one match (because of the /g modifier), \t is a bit meaningless.
   \a is "e f" while \A is "ef"

The way mIRC evaluates those markers is special, it is important at this point to talk about the main steps happening when evaluating $identifiers:

-  Process [ ], which evaluates any variables/identifiers inside of the brackets once, and [[ ]], which turns into [ ].
-  Separates the identifier's parameters and evaluates each parameter once. These evaluations take place in order from left to right.
-  Passes the parameters to the identifier

$regsubex is a bit different, it has its own parsing routine. By design, $regsubex must not evaluate the subtext parameter before doing the regex match. The steps for $regsubex are shown below:

-  Process [ ] and [[ ]].
-  Seperate parameters, evaluate the 'input' and the 'regex' parameters.
-  Perform the regex match.
-  Tokenize $1- according to the number of markers used in the 'subtext' parameters.
-  Replaces any markers used in the subtext with their corresponding $N identifiers's values.
-  Evaluate the subtext parameter (one or more times, if /g is used).
-  Performs the substitutions and returns the result.

mIRC internally uses $1- to store the values of the markers, it means the previous tokenization of $1- cannot be used in the subtext parameter (it is restored after).

The way mIRC does this is quite special, it checks how many markers you have and creates a list of tokens (so, with $1-). Each token is assigned a value and mIRC then replaces the markers with the corresponding $N value before evaluating that result.

Let's have a look at an example, consider the following subtext:

.. code:: text

   \t \t \1 \n

mIRC assigns the value of \t to $1 & $2, \\1 is assigned to $3 and finally, \n is assigned to $4.

Then each marker is replaced with their corresponding values, the subtext becomes:

.. code:: text

   $1 $2 $3 $4

And now mIRC evaluates that for each match and use it as a replacement.

.. note:: If the form \N is used in the subtext, where N is a positive number greater-than or equal to 1 (such as \\1), and there is no such back-reference number in the pattern, mIRC will use the value of $regml(\n + N - 1).

An example of this is shown below:

.. code:: text

   $regsubex(abcdefgij,/([a-z])/g,<\6>)

Here we have a break-down of the results of this regex:

-  The \\6 doesn't mean anything, as there are not 6 back-references made in the pattern (only one backreference, the pattern will, however, be applied 6 times and more because of the /g modifier)
-  When a is matched, \n is 1, and only one marker is used. Therefore, $1 (used to represent \\6) is filled with $regml(1 + 6 -1) = $regml(6), which is f
-  When b is matched, \n is 2, $1 is then filled with $regml(2 + 6 - 1) = $regml(7), which is g
-  And so on until \n + N - 1 is greater than the total number of back-references, which at this point, $null is used.

Nested calls
''''''''''''

Nested $regsubex calls are possible, but caution must be taken with markers.

First of all, if you use the /g modifier in either the outer or the inner $regsubex call and you need to use the different backreferences made in either of them, you must give a name to either one or both of them, otherwise, the call of the inner $regsubex will overwrite the backreferences of the outer $regsubex (if you don't use a name, mIRC use a default name, which would be the same here).

When mIRC replaces the markers, it will do so on the whole subtext parameter, consider:

.. code:: text

   $regsubex(name,abcdefcdab,/(cd)/g,$regsubex(\t,/(.)/g,$upper(\t)))

In the above example, the outer $regsubex will make the regex match, then it will loop on the result and replace \t accordingly everywhere in the subtext. Notice the subtext of the outer $regsubex is:

.. code:: text

   $regsubex(\t,/(.)/g,$upper(\t))

All occurences of \t (can appear anywhere and it can be touching others characters) are changed with their corresponding $N value, even the one inside $upper; this means that the code won't work as expected. Typically we want this \t inside $upper() to be the corresponding value from the inner $regsubex, not the outer one.

The idea is to get mIRC to see something other than \t (inside that $upper()) when looking for markers from the outer $regsubex context.

A simple $+ cannot be used:

.. code:: text

   $regsubex(\t,/(.)/g,$upper( \ $+ t ))

Having this as the subtext of the $regsubex would end up calling $upper(\t) with plain text "\t", because the $+ is going to be evaluated after the inner $regsubex made his own regex match & loop over its results, which is after both $regsubex looked for markers. Something need to be done before the markers of the inner $regsubex are replaced but after the outer $regsubex made his match: when the outer $regsubex is ready to loop over its result.

The solution is to use the **[[  $+ t ]]** construct:

.. code:: text

   $regsubex(name,abcdefcdab,/(cd)/g,$regsubex(\t,/(.)/g,$upper( [[ \ $+ t ]] )))

Indeed, the processing of **[ ] and [[ ]]** is done for the whole line. mIRC first changes this line into:

.. code:: text

   $regsubex(name,abcdefcdab,/(cd)/g,$regsubex(\t,/(.)/g,$upper( [ \ $+ t ] )))

The example above conveys how only the [[ ]] has changed. Remember $+ was not evaluated because the subtext parameter of $regsubex is not evaluated until the regex match is performed.

Now, the outer $regsubex is evaluated, it gets its parameters (without evaluating the subtext), makes the regex match, and calls the subtext for each match, the subtext is:

.. code:: text

   $regsubex(<value of \t from the outer $regsubex>,/(.)/g,$upper( [ \ $+ t ] ))

And when this $regsubex evaluates (for each replacement of the outer regsubex) [ \ $+ t ] will first produce \t and everything works as we wanted.

The more nested $regsubex you have, the more you have to make sure each subtext has the correct number of [[ ]].

Obviously, you can make this cleaner by calling a custom alias as the subtext with the markers passed as parameters and doing the nested $regsubex call here, but this is possible.

No Marker
'''''''''

You cannot use a marker inside the subtext of the inner $regsubex to get the value of the marker of the outer $regsubex context, that's why our previous example fails:

.. code:: text

   $regsubex(name,abcdefcdab,/(cd)/g,$regsubex(\t,/(.)/g,$upper(\t)))

You are tempted to think that \t inside $upper should always be "cd", because that's the only value that \t can have from the outer $regsubex and we just saw how the marker are replaced for the whole subtext, no matter where it appears. However, we also saw that mIRC does not blindly replace the markers with their real value, it uses the intermediate tokens identifiers ($1 etc), this is required otherwise element such as ) would be taken as closing parenthesis for identifier for example, or comma as argument seperator inside an identifier:

Two markers are used in the subtext of the outer $regsubex, so mIRC make the match, cd is found twice so a two iterations loop is made, each time replacing the match with the evaluation of the subtext parameter. Right before that loop, because two markers are used, mIRC fills $1 with \t as well as $2 with \t and then evaluate the subtext, which gives before evaluation:

.. code:: text

   $regsubex($1,/(.)/g,$upper( $+ $2 $+ )))

However remember that the subtext is not evaluated before the regex match is done, so only $1 gets evaluated here:

.. code:: text

   $regsubex(cd,/(.)/g,$upper( $+ $2 $+ )))

As you can see, mIRC adds the $+ if the markers have text surrounding them, that's why you don't need to space them out like identifiers. You might understand why it's failing at this point: $2 has no value in this example because no marker are used in this inner $regsubex's subtext parameter, so $2 is $null.

So how do you use the value of the marker of the outer $regsubex inside the subtext of the inner $regsubex?

The solution is to use **[[ \t ]]**:

.. code:: text

   $regsubex(name,abcdefcdab,/(cd)/g,$regsubex(\t,/(.)/g,$upper( [[ \t ]] )))

As we saw, mIRC will first turn this line into

.. code:: text

   $regsubex(name,abcdefcdab,/(cd)/g,$regsubex(\t,/(.)/g,$upper( [ \t ] )))

Then the outer $regsubex will make the regex match and replaces markers so the subtext of the outer regsubex becomes:

.. code:: text

   $regsubex($1,/(.)/g,$upper( [ $+ $2 $+ ] )))

The difference is that you now have a pair of bracket, which are processed first, forcing the evaluation of $2, which has the correct value at this point.

.. note:: The more you are nesting, the more you need to get mIRC to see the correct things, which easily gets ugly, calling an alias in the subtext to do the replacement is recommended.

/filter
~~~~~~~

/filter supports the -g switch, which uses a regular expression. It is important to note that the back-reference value cannot be obtained using $regml if a custom alias is used as the output (-k). In order to be able to use $regml, $regex would need to be called.

$hfind
~~~~~~

$hfind can be used along with regex. However, $hfind does not support the custom S modifier.

/write, $read, $fline, etc
~~~~~~~~~~~~~~~~~~~~~~~~~~

These, and many more, are various places where Regular Expressions can be used.

Syntax
~~~~~~

This part is meant to document all the different features of PCRE that work with mIRC, and to explain a bit of regular expression works.

A regular expression is a pattern that is matched against a subject string from left to right. Most characters stand for themselves in a pattern, and match the corresponding characters in the subject.

As a trivial example, the pattern "The quick brown fox" matches a portion of a subject string that is identical to itself.

The power of regular expressions comes from the ability to include alternatives and repetitions in the pattern.

These are encoded in the pattern by the use of metacharacters, which do not stand for themselves but instead are interpreted in some special way.

There are two different sets of metacharacters: those that are recognized anywhere in the pattern except within square brackets, and those that are recognized within square brackets.

Outside square brackets
^^^^^^^^^^^^^^^^^^^^^^^

The metacharacters are as follows:

.. code:: text

   \   general escape character with several uses
   ^   assert start of string (or line, in multiline mode)
   $   assert end of string (or line, in multiline mode)
   .   match any character except newline (by default)
   [   start character class definition
   |   start of alternative branch
   (   start subpattern
   )   end subpattern
   ?   extends the meaning of '(', also 0 or 1 quantifier, also "quantifier minimizer"
   *   0 or more quantifier
   +   1 or more quantifier, also "possessive quantifier"
   {   start min/max quantifier

Inside a character class
^^^^^^^^^^^^^^^^^^^^^^^^

Part of a pattern that is in square brackets is called a "character class".

In a character class the only metacharacters are:

.. code:: text

   \   general escape character
   ^   negate the class, but only if the first character
   -   indicates character range
   [   POSIX character class (only if followed by POSIX syntax)
   ]   terminates the character class

The Backslash \\
^^^^^^^^^^^^^^^^

The backslash character has several uses. Firstly, if it is followed by a character that is not a number or a letter, it takes away any special meaning that character may have.

This use of backslash as an escape character applies both inside and outside character classes.

Another usage of the backslash is to represent non printable character, they can all be used inside a character class:

.. code:: text

   \a         Bel character, ascii 07
   \cx        where x is any ascii character. The  precise effect of \cx on ASCII characters is as follows: if x is a lower case letter, it is converted to upper case. Then bit 6  of  the character (hex 40) is inverted. Thus \cA to \cZ become hex 01 to hex 1A (A is 41, Z is 5A), but \c{ becomes hex 3B ({ is 7B), and  \c;  becomes hex  7B (; is 3B). If the data item (byte or 16-bit value) following \c has a value greater than 127, a compile-time error occurs.  This locks out non-ASCII characters.
   \e escape character, ascii 27
   \f        form feed character, ascii 12
   \n        linefeed character, ascii 10
   \r        carriage return character, ascii 13
   \t        tab character, ascii 09
   \0dd      character with octal code 0dd. After \0, up to two further octal digits are read. If there are fewer than two digits, just those that are present are used. Thus the sequence \0\x\015 specifies two binary zeros followed by a CR character. Make sure you supply two digits after the initial zero if the pattern character that follows is itself an octal digit.
   \ddd      character with octal code ddd, or back reference
   \o{ddd..} character with octal code ddd..  The escape \o must be followed by a sequence of octal digits, enclosed in braces. An error occurs if this is not the case. This escape is an addition to Perl; it provides way of specifying character code points as octal numbers greater than 0777, and it also allows octal numbers and back references to be unambiguously specified.
   \xhh      character with hex code hh
   \x{hhh..} character with hex code hhh..

For greater clarity and unambiguity, it is best to avoid following by a digit greater than zero. Instead, use \o{} or \x{} to specify character numbers, and \g{} to specify back references. The following paragraphs describe the old, ambiguous syntax.

The handling of a backslash followed by a digit other than 0 is complicated, and Perl has changed in recent releases, causing PCRE also to change.

Outside a character class, PCRE reads the digit and any following digits as a decimal number. If the number is less than 8, or if there have been at least that many previous capturing left parentheses in the expression, the entire sequence is taken as a back reference.

Inside a character class, or if the decimal number following  is greater than 7 and there have not been that many capturing subpatterns, PCRE handles \\8 and \\9 as the literal characters "8" and "9", and otherwise re-reads up to three octal digits following the backslash, using them to generate a data character. Any subsequent digits stand for themselves.

For example:

.. code:: text

   \040   is another way of writing an ASCII space
   \40    is the same, provided there are fewer than 40 previous capturing subpatterns
   \7     is always a back reference
   \11    might be a back reference, or another way of writing a tab
   \011   is always a tab
   \0113  is a tab followed by the character "3"
   \113   might be a back reference, otherwise the character with octal code 113
   \377   might be a back reference, otherwise the value 255 (decimal)
   \81    is either a back reference, or the two characters "8" and "1"

.. note:: Octal values of 100 or greater that are specified using this syntax must not be introduced by a leading zero, because no more than three octal digits are ever read.

By default, after \x that is not followed by {, from zero to two hexadecimal digits are read (letters can be in upper or lower case). Any number of hexadecimal digits may appear between \x{ and }. If a character other than a hexadecimal digit appears between \x{ and }, or if there is no terminating }, an error occurs.

Characters that are specified using octal or hexadecimal numbers are limited to certain values, less than 0x10ffff and a valid codepoint.

Invalid Unicode codepoints are the range 0xd800 to 0xdfff (the so called "surrogate" codepoints), and 0xffef.

All the sequences that define a single character value can be used both inside and outside character classes. In addition, inside a character class, \b is interpreted as the backspace character (ascii 08).

\N matches a non newline character, (same as the dot '.' without single line mode (/s modifier), it is not allowed inside a character class.

\g+N or \g-N is a relative back reference, it matches the value of the capturing group that can be found by counting as many opening parentheses of named or numbered capturing groups as specified by the number from right to left starting at the backreference. (a)(b)(c)(d)\g<-3> matches abcdb.

Another use of backslash is for specifying generic character types:

.. code:: text

   \d     any decimal digit
   \D     any character that is not a decimal digit
   \h     any horizontal white space character
   \H     any character that is not a horizontal white space character
   \s     any white space character
   \S     any character that is not a white space character
   \v     any vertical white space character
   \V     any character that is not a vertical white space character
   \w     any "word" character
   \W     any "non-word" character
