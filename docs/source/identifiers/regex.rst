$regex
======

$regex returns the number of string which matched the regular expression, more information about regex in mIRC :ref:`matching_tools-regex`

Synopsis
--------

.. code:: text

    $regex([name],input,regex)

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

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $regex(abcd,/[a-z]/g)

If the result is 0 then there were no matches. However it's possible that a syntax error in your pattern causes a negative result, so before using the $regex() result in an if() statement, either be sure to check that you didn't create a pattern subject to a negative result, such as $regex(string,[), or change...

.. code:: text

    from
    if ($regex(string,pattern))
    to
    if ($regex(string,pattern) != 0)

In addition to the normal regex escape sequences mentioned :ref:`matching_tools-regex` you need to make sure that your regex pattern does not contain characters which confuse the mIRC scripting engine, such as the above example returning -14 due to having an unmatched bracket. You may still use these, but must place them in a %variable then use that variable as the regex pattern. The mIRC scripting engine seeks to prioritize seeing characters in way they would evaluate these characters in the non-regex context before accepting them in your regex pattern. This includes unpaired parenthesis and brackets, literal commas, pipe symbols percents and dollars which could be evaluated with special meaning by the scripting engine due to their placement next to spaces and commas, etc.

For example, if you need to validate that a string is a valid mime string, you cannot simply check if the string contains characters of the mime alphabet, because you need to make sure there is a minimum of 2-or-more mime characters. The regex construct to ensure something appears 2-or-more times is {2,} but this literal comma confuses the scripting engine into thinking you're trying to use an extra parameter. While you can replace the comma with " $+ $chr(44) $+ " that can make the pattern harder to understand later, so you can instead simply the normal scripting syntax which accomplishes the task of putting your pattern into a variable:

.. code:: text

    //var %string deadbeef , %pattern ^[a-zA-Z0-9/+]{2,}=*$ | echo -a $regex(%string,%pattern)

When there are simple things which can be accomplished using the == or iswm or iswmcs operators, it's usually much faster to use those due to the overhead associated with making a $regex call. However, there can be situations where the equivalent to a regex pattern is a long series of if() statements, you can boil it down to a single regex. This example ensures that %switch is an optional hyphen followed by 1 character from a list of valid switch letters:

.. code:: text

    //echo -a $regex(name,%switch,/^-?[rstlne]$/g)

The 'name' is an optional parameter which allows you to later retrieve the capture groups from a search without having it be overwritten by the next $regex call. Note that you cannot retrieve the *result* of the $regex identifier, you can only retrieve capture groups created by the named regex call. Since the above pattern does not create any capture groups, the results retrieved by $regml() will be empty regardless of the result. If you do not use the 'name' parameter, mIRC internally uses the name 'default', as you can see by:

.. code:: text

    //echo -a $regex( $rand(1111,9999) ,/(.+)/g) always matches with $regml(1) same as $regml(default,1)

mIRC remembers the most recent 50 named searches, and the names are shared between $regex $regsub $regsubex. There is no function to obtain the list of named searches, or to identify how far away from deletion your name is. This next confirms that there can only be 50 named searches existing at any time, and shows that named searches go into the list-of-50 and are accessed or removed from the list in a case-insensitive manner:

.. code:: text

    //echo -a $regex(foo,foo,/^(.*)$/g) . $regex(Foo,Foo,/^(.*)$/g) $regml(foo,1) $regml(Foo,1) $regex(name1,name1string,/^(.*)$/g) | var %i 2 | while (%i isnum 1-100) { noop $regex(name $+ %i,z,/^(.)$/) | echo -ag %i $regml(foo,1) $regml(Foo,1) $regml(name1,1) | if ($regml(name1,0)) inc %i | else break } | if (!$regml(name1,0)) echo -ag name1 overwritten on $ord(%i) regex call

If you have a custom alias using a regex search, and the alias is intended to be called from scripts written by you and by others, it's good practice to use a name pattern which is unlikely to be used by other scripts who need to use the result later without worry that it can be overwritten by something else. One methodology is to always use 'foo' with a regex call for which you don't care for the result after your custom alias returns its result. This avoids trampling over results which another script needs to remember later, and avoids creating multiple names which can push the caller script's name off the list.

One efficiency with regex identifiers is to avoid using /g or creating capture groups when you don't need them. If you want to know whether or not a string contains at least 1 'a', don't use /g to count them all. If you want to count how many 'a' or 'b' are within the string, there's 2 ways to do it, note how the 2nd method does not create the 8 capture groups:

.. code:: text

    //echo -a $regex(foo,abbadabba,  /(a|b)/g) captures: $regml(foo,0)
    //echo -a $regex(foo,abbadabba,/(?:a|b)/g) captures: $regml(foo,0)

Spaces are treated differently inside regex patterns than outside them. In normal identifiers, leading or trailing spaces are ignored, like how the spaces aren't counted in $len( abc ). However part of the regex syntax requires it to treat all spaces as literal, but only if it's within the pattern. Note how the space within the pattern causes the 1st result to be zero, but the /x modifier causes literal spaces in the pattern to be stripped.

.. code:: text

    //echo -a $regex(foo,abbadabba,/ (?:a|b)/g)  captures: $regml(foo,0)
    //echo -a $regex(foo,abbadabba,/ (?:a|b)/gx) captures: $regml(foo,0)

See the :ref:`matching_tools-regex` page for more details on using regex in general. Note how $regml and $regmlex differ in how they handle capture groups in coordination with the /F modifier.

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$regml </identifiers/regml>`
    * :doc:`$regmlex </identifiers/regmlex>`
    * :doc:`$regsubex </identifiers/regsubex>`
    * :doc:`$regsub </identifiers/regsub>`
    * :doc:`$regerrstr </identifiers/regerrstr>`

