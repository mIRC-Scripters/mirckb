$1-
===

The $1- identifier returns a list of argument passed to an alias or returns the text message associated with an {{mIRC|on events|mSL Events}}. $1- is also filled by the :doc:`$tokenize </commands/tokenize>` command, and is also given different values within the command string for $findfile and $finddir. It also is used in popups menus to reference the 1-or-more nicks highlighted in that channel.

.. note:: $1- is built by tokenizing the parameters/text, which means that leading/trailing/consecutive spaces are lost, see :doc:`$parms </identifiers/parms>`, which is the same as $1-, but preserves spaces. However the /tokenize command destroys the existing $parms string as $null without replacing it with the tokenizing of the new $1- string.

If $1- represents the full line/parameters, you can use $1 to only reference the first parameter/word, you can use $2 to reference the second parameter/word and so on.

You can use $0 to return the total number of words or the total number of parameters.

You can append text to $1, $2 etc without using {{mIRC|$+}}, as long as your text does not contain a digit, for example:

.. code:: text

    //tokenize 32 Khaled | echo -a $1's skills are impressive!
    
If your attached text contains a number, mIRC skips every character in your text up to the last number and use the remaining text.
.. note:: if the value of $1 is $null, then $null is returned, instead of the text itself

.. code:: text

    //tokenize 32 Khaled xyz parm3 | echo -a $1foo2bar vs $1 $+ foo123bar and $1$2 vs $1 $+ $2 and $3test and $1-x2 but $5test is null
    result: Khaledbar vs Khaledfoo123bar and Khaled vs Khaledxyz and parm3test and Khaled xyz parm3 but is null

Range
-----

$1- returns the full line/parameters because '-' is actually used to set a range.

By adding a number after the '-' character, you can get multiple consecutive word/parameter, $1-2 returns from the first word/parameter to the second word/parameter.

So $1- means from the first word/parameter to the last/parameter, aka from the first word onward and $3- is from the third word/parameter onward.

Synopsis
--------

.. code:: text

    $1-

Properties
----------

None

Range in Token functions
------------------------

When using certain token functions (see :ref:`token_manipulation`) such as :doc:`$gettok </identifiers/gettok>`, you can sometimes use a range for the N parameter, in this case you can specify a range too, but with an extra feature, both number can be negative.

Negative numbers means that mIRC looks from the end instead of the start:

.. code:: text

     $gettok(A B C D E F,-1,32) returns B, the first word starting from the end
     $gettok(A B C D E F,-2-,32) returns E F, from the second word starting from the end, and then the last '-' means 'onward' as usual
     $gettok(A B C D E F,-2--5,32) returns B C D E, from the second word starting from the end, to the 5th word, starting from the end

Examples
--------

.. code:: text

    on *:text:*:#:echo -s $nick said $1-

Creating the space-delimited $1- by tokenizing with commas:

.. code:: text

    //var %a $readini($mircini,options,n4) | tokenize 44 %a | echo 4 -a %a tokenizes as $1- | echo 3 -a your dcc send port range is $13 through $26

Tokenizing by capital X creates tokens containing internal, trailing, leading spaces, and is not a case-insensitive tokenizing.

.. code:: text

    //tokenize 88 Xtest x test XXX testX | echo -a $qt($1) vs $qt($2)
    ;result: "test x test " vs " test"
    
The result is the same when the leading, trailing, consecutive capital X's are removed

Echo removes leading/trailing/consecutive spaces from the display. Replacing spaces with codepoint 160 shows that $1- also removes those same spaces, but they're preserved in $parms. This example does not hide the original text, so you can compare the original against these values when the original contains consecutive spaces:

.. code:: text

    on *:TEXT:*:#:{
    echo $chan 1- with .32 = $1-
    echo $chan 1- with 160 = $replace($1-,$chr(32),$chr(160))
    echo $chan parms with .32 = $parms
    echo $chan parms with 160 = $replace($parms,$chr(32),$chr(160))
    }

$1- and $parms are different values within the command parameter for $findfile and $finddir

.. code:: text
    
    //tokenize 32 foo bar | echo 4 -a $ $+ 1 is $qt($1) and $ $+ parms is $qt($parms) - $findfile($mircdir,$nopath($mircini),0,1,echo 3 -a $ $+ 1 is a different string $1 and parms is $parms ) $chr(22) and $ $+ 1 & $ $+ parms are back to being $qt($1) & $qt($parms)
    ;result:

.. code:: text
    
    $1 is a different string C:\path\mirc.ini and parms is C:\path\mirc.ini
    $1 is "foo" and $parms is "" - 1  and $1 & $parms are back to being "foo" & "" 

.. note:: even though $parms preserves consecutive spaces, a /command like /dcc send or /copy or /write loses the extra space, and either does not work, or in some cases finds the similarly named single-spaced filename.

In a popups menu, $1 $2 etc reference the 1st, 2nd, etc nicks highlighted in a window (top to bottom), with $0 being the total number of highlighted nicks. Because this example uses $$2- it does nothing unless there are at least 2 nicks highlighted. (Using double dollar with an identifier halts the script execution if the identifier returns null

.. code:: text
    
    TroutSlap2!:me slaps $$1- around a bit with a GMO trout. And don't rest easy $$2- I'm coming for you too!

In Options/mouse/drop, there are default entries for drag/drop of filenames from Windows Explorer or another file manager onto a nick in the nicklist. "*.wav:/sound $1 $2-" means that files matching that wildcard execute the SOUND command, where $1 is the nick receiving the drop and $1- is the filename enclosed in doublequotes. This $parms also includes the nick, so if you need a space-preserved filename, you must do something similar to:

.. code:: text
    
    //var %a nick "test $chr(32) filename.wav" | var -s %a2 $remove($mid(%a,$calc(1+$pos(%a,$chr(32)))),"),$chr(32),$chr(160)

Because $ has special meaning in regex, $1 in the replacement term must be evaluated with [ ] or placed in a variable, as even $eval($1,2) won't work:

.. code:: text

    //tokenize 32 foo bar | var %a $1 | echo -a $regsubex(foo bar,( $+ $1 $+ ),new $qt( [ $1 ] ) )
    //tokenize 32 foo bar | var %a $1 | echo -a $regsubex(foo bar,( $+ $1 $+ ),new $qt(%a) )

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------