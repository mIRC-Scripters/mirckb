$regerrstr
==========

$regerrstr returns the PCRE error string of the compile function for the last regex call made, if any.

A regular expression must be compiled first, and then it's executed against a string.

If an error occurs in the compile function, $regerrstr is filled with an error string, corresponding to a positive number (listed below), but only the string is returned.

$regex and similar regex functions reporting number of matches ($regsubex with output variable or $regsub) will report a value of -14.

This value actually comes from the exec function, this is for convenience. $regex etc always return a negative value when an error occurs.

-14 is supposed to mean an internal pcre error, but this is only the case if $regerrstr is not set, then. You can find more info about on the regex page

Synopsis
--------

.. code:: text

    $regerrstr

Parameters
----------

None

Properties
----------

None

List of error
-------------

* 1:  \ at end of pattern
* 2:  \c at end of pattern
* 3:  unrecognized character follows \
* 4:  numbers out of order in {} quantifier
* 5:  number too big in {} quantifier
* 6:  missing terminating ] for character class
* 7:  invalid escape sequence in character class
* 8:  range out of order in character class
* 9:  nothing to repeat
* 10:  [this code is not in use]
* 11:  internal error: unexpected repeat
* 12:  unrecognized character after (? or (?-
* 13:  POSIX named classes are supported only within a class
* 14:  missing )
* 15:  reference to non-existent subpattern
* 16:  erroffset passed as NULL
* 17:  unknown option bit(s) set
* 18:  missing ) after comment
* 19:  [this code is not in use]
* 20:  regular expression is too large
* 21:  failed to get memory
* 22:  unmatched parentheses
* 23:  internal error: code overflow
* 24:  unrecognized character after (?<
* 25:  lookbehind assertion is not fixed length
* 26:  malformed number or name after (?(
* 27:  conditional group contains more than two branches
* 28:  assertion expected after (?(
* 29:  (?R or (?[+-]digits must be followed by )
* 30:  unknown POSIX class name
* 31:  POSIX collating elements are not supported
* 32:  this version of PCRE is compiled without UTF support
* 33:  [this code is not in use]
* 34:  character value in \x{} or \o{} is too large
* 35:  invalid condition (?(0)
* 36:  \C not allowed in lookbehind assertion
* 37:  PCRE does not support \L, \l, \N{name}, \U, or \u
* 38:  number after (?C is > 255
* 39:  closing ) for (?C expected
* 40:  recursive call could loop indefinitely
* 41:  unrecognized character after (?P
* 42:  syntax error in subpattern name (missing terminator)
* 43:  two named subpatterns have the same name
* 44:  invalid UTF-8 string (specifically UTF-8)
* 45:  support for \P, \p, and \X has not been compiled
* 46:  malformed \P or \p sequence
* 47:  unknown property name after \P or \p
* 48:  subpattern name is too long (maximum 32 characters)
* 49:  too many named subpatterns (maximum 10000)
* 50:  [this code is not in use]
* 51:  octal value is greater than \377 in 8-bit non-UTF-8 mode
* 52:  internal error: overran compiling workspace
* 53:  internal error: previously-checked referenced subpattern not found
* 54:  DEFINE group contains more than one branch
* 55:  repeating a DEFINE group is not allowed
* 56:  inconsistent NEWLINE options
* 57:  \g is not followed by a braced, angle-bracketed, or quoted name/number or by a plain number
* 58:  a numbered reference must not be zero
* 59:  an argument is not allowed for (*ACCEPT), (*FAIL), or (*COMMIT)
* 60:  (*VERB) not recognized or malformed
* 61:  number is too big
* 62:  subpattern name expected
* 63:  digit expected after (?+
* 64:  ] is an invalid data character in JavaScript compatibility mode
* 65:  different names for subpatterns of the same number are not allowed
* 66: (*MARK) must have an argument
* 67: this version of PCRE is not compiled with Unicode property support
* 68:  \c must be followed by an ASCII character
* 69:  \k is not followed by a braced, angle-bracketed, or quoted name
* 70:  internal error: unknown opcode in find_fixedlength()
* 71:  \N is not supported in a class
* 72:  too many forward references
* 73:  disallowed Unicode code point (>= 0xd800 && <= 0xdfff)
* 74:  invalid UTF-16 string (specifically UTF-16)
* 75:  name is too long in (*MARK), (*PRUNE), (*SKIP), or (*THEN)
* 76:  character value in \u.... sequence is too large
* 77:  invalid UTF-32 string (specifically UTF-32)
* 78:  setting UTF is disabled by the application
* 79:  non-hex character in \x{} (closing brace missing?)
* 80:  non-octal character in \o{} (closing brace missing?)
* 81:  missing opening brace after \o
* 82:  parentheses are too deeply nested
* 83:  invalid range in character class
* 84:  group name must start with a non-digit
* 85:  parentheses are too deeply nested (stack check)

Example
-------

.. code:: text

    //echo -a $regex($str(a,2700),/(?<=a*)/) $regerrstr

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$regex </identifiers/regex>`

