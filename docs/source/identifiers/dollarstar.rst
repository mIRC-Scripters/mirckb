$*
==

$* is a construct, not an identifier, it allows you to iterate over all of the tokens contained within $1-. The way this works is much like a while loop. $\* has been omitted from the help file since while loops were introduced, especially because the behavior of $\* is quirky in some places.

$\* is extremely powerful, because it is much faster than using a while loop on a list of tokens. Understanding how this works is pretty simple, so consider the following:

.. code:: text

    var %list a b c d,%a 1
    while ($gettok(%list,%a,32)) {
        echo -a $v1
        inc %a
    }

This can be written as:

.. code:: text

    tokenize 32 a b c d | echo -a $*

The above is much smaller, and a lot faster. Pretty cool, isn't it?

Notes & Quirks
--------------

Why was the $\* identifier removed from the help file in the first place? Well, $\* was removed because it does not really work the same way that the other identifiers do, and because it is quirky.

Quirky? Quirky, how?

Well, mIRC takes the command $\* appears in, and replaces all of the occurrences in the line by a special marker: `~$\*: An example of how this is accomplished is shown below:

.. code:: text

    //tokenize 32 abcd | echo -a $left($*,1) $+ $chr(3) $+ $mid($*,2)

Further examining the code, it is easy to understand why the above returns such a value:

.. code:: text

    //tokenize 32 abcd | echo -a $mid($*,2)

Why isn't this returning bcd? Because of the usage of the special marker \`~$\*, mIRC has stored the command as actually echo -a $mid(\`~$\*,2).

Then, for each token (here only $1 == abcd), mIRC evaluates the line. $mid(\`~$\*,2) becomes ~$\*, and then mIRC replaces the marker by the token and executes the echo command. However, after an operation like $mid in this example, that marker cannot be found. Basically, it cannot be guaranteed that the correct value of the marker inside an identifier can be found later for replacement of that marker.

There is a workaround for the above issue, and that is by using scid and scon:

.. code:: text

    //tokenize 32 abcd | scon -r echo -a $!mid( $* ,2)

.. note:: This workaround will double evaluate the content of the token, replace "abcd" above with $!time and it will evaluate.

mIRC replaces $\* by the marker, but scon has an extra evaluation system which fits perfectly. The $* mechanism is enabled on scon, and mIRC stores the command of the $\* as scon -r echo -a $!mid( \`~$\* ,2) mIRC then evaluates the line for each token, which then becomes: "scon -r echo -a $mid( abcd ,2)" Finally, the scon command is executed, resulting in the expected value being echoed.

Another issue is that you cannot call $* more than once in the same scope; the command will simply be skipped. However, this can also be circumvented/worked-around :)

Simply retokenize after using $\*.
However, note that $\* will remember the number of token it already went through, $\* will only start from the previous number of tokens + 1, look at this example:

.. code:: text

    //tokenize 32 1 2 3 | echo -a $* | tokenize 32 4 5 6 7 8 | echo -a $* | echo -a here

The first three tokens of the second tokenize, "4 5 6", are dummy tokens which are passed to fill in the gap. $\* is actually starting from the 4th token.
If you are dealing with dynamic parameter and want to use $* again in the same scope, you can use $str(AT,$0) $+ as the dummy tokens, where A is a non token character, and where T is a token character, that indeed makes sure the correct number of dummy tokens is used:

.. code:: text

    //tokenize 32 1 2 3 | echo -a $* | tokenize 32 $str(A $chr(32),$0) $+ 7 8 | echo -a $* | echo -a here

.. note:: This sexy workaround works even inside a loop, but a better workaround is to call an alias and to execute the new $* in there, the previous tokens will be cleared.

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

