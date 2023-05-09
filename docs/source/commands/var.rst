/var
====

The /var command can be used to replace the value of existing variables or create a new variables and assign them values. By default /var creates local variable, this can be changed via the -g switch (:doc:`/set </commands/set>` command can be used to set global variables by default).

The Local Variables created by /var exist only within the :event: or ALIAS where they were created. If your event or alias calls another alias, that alias cannot see the local values unless passed to them in another way, such as a parameter used when calling the alias.

The var command can perform one math operation via one of the arithmetic operators: addition (+), subtraction (-), multiplication (*), division (/), modulo (%), bitwise-and (&), and exponent (^). They ''must'' be space delimited with both operands being a number. If any of the operands are not a number or if a space is missing, it will be treated as plain text.

.. note:: Unlike the :doc:`/set </commands/set>` command, var can assign a value to multiple variables at once.

Set Evaluation Routine:
Internally, the var command simply breaks down the line (by commas) and passes the arguments to /set. The set command has its own evaluation routine which lets you dynamically concatenate additional values onto the variable name before the assignment takes place.

.. code:: text

    //var -s % $+ $ctime ABC

Will create a variable like %1209425041 with the value of 'ABC'; Similarly this can be used with $nick and $chan in on events.

Synopsis
--------

.. code:: text

    /var [-sgnip] <%var> [[= ]value]
    /var [-sg] <%var> <number> <+ | - | * | / | %> <number>
    /var [-sg] <%var> [= ]<number> <+ | - | * | / | % | &> <number>
    /var [-sg] <%var> [[= ]value][, <%var> [[= ]value]][, ...]
    /var [-sg] <%var> [= ]<number> <+ | - | * | / | % | &> <number>[, ...]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Display variable assignment value
    * - -g
      - Creates a global variable instead
    * - -n
      - Prevents math operation
    * - -i
      - Creates the local variable only if that variable does not exist AS A LOCAL VARIABLE, even if $null
    * - -p
      - Permits value to be 2 literal doublequotes and permits value to end with a single $chr(32) space. Also performs -n switch behavior

.. note:: If you are placing an event's $1- into a variable, you should use -p to prevent 1 + 1 being evaluated to 2, or "" not being set

.. note:: The = in "var %a = value" is optional and is not placed into the value.

.. note:: See the :doc:`/set </commands/set>` page for more info about setting dynamic variable names using identifiers like $nick or $network

.. note:: much of the usage of /var is similar to that of /set except that switches like -uN or -e or -z or -k  have no meaning for local variables which cease to exist when the event or alias is finished.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <%var>
      - The name of the variable
    * - [value]
      - The value to assign to the variable. If not present or is $null the local var is unset
    * - <number>
      - Any arbitrary numerical value, can be a floating point number
    * - < + |
      - | * | / | % | ^ | & > - One of the seven possible arithmetic operations
    * - <number>
      - Any arbitrary numerical value, can be a floating point number

.. note:: if your [value] ends with a literal space seperated comma, mIRC will see it as a new variable assignement even if no '%' is found, you need to use two commas to produce one in this case: //var %a test ,,

Example
-------

.. code:: text

    ; Factorial
    ; 10! = $factorial(10) = 3628800
    alias factorial {
      var %result = 1, %x = $1
      while (%x) {
        var %result = %result * $v1
        dec %x
      }
      return %result
    }

.. code:: text

    -s can be used to debug scripts, showing variables being set to their values. The message displays to the active window if typed in editbox, or Status Window if in an alias/event:
    //var -s %a test
    returns: * Set %a to test

.. code:: text

    -g sets global as if you used /set instead of /var:
    //unset %a %a | var -g %a global | echo -a $var(%a,1).local $var(%a,1).value | .timer 1 0 echo 5 -a timer sees % $+ a
    returns:
    $false global
    timer sees global

.. code:: text

    var defaults to using math operations if there are 3 tokens separated by spaces, and the 1st and 3rd are numbers, and the 2nd token is any of the 6 operators listed above:
    //var %a 1 + 2 | echo -a %a
    returns: 3
    //var %a $pi - 1 | echo -a %a
    returns: 2.141593
    //tokenize 32 4 5 | var %a $1 * $2 | echo -a %a
    returns: 20
    //var %b 7 | var %a %b / 3 | echo -a %a
    returns: 2.333333
    //var %a $ctime % 3600 | echo -a %a seconds since the top of the hour
    returns: <number> seconds since the top of the hour
    //var %a 2^16 | var %b 2 ^ 16 | echo -a %a because not tokenized by spaces vs %b
    returns: 2^16 because not tokenized by spaces vs 65536
    //var %b 7 , %c 11 , %a %b & %c | echo -a a= %a b= $base(%b,10,2) c= $base(%c,10,2) b&c= $and(%b,%c)
    returns: 3 because bit-1 and bit-2 are the only common bits between 7 and 11
    //var %a 1 + 1 + 1 | echo -a %a because only 1 math operation allowed
    returns: 1 + 1 + 1 because only 1 math operation allowed
    Prevent math operation with -n switch
    //var %a 1 + 1 | var -n %b 1 + 1 | echo -a %a vs %b
    returns: 2 vs 1 + 1

.. code:: text

    -i causes /var to act only if local var does not exist, even if it is $null. "/var %a" does not unset the local var, it sets it to $null:
    //set %a Global | var -i %a Local1 | echo -a Value1: %a | var -i %a Local2 | echo -a Value2: %a | var %a | echo -a Value3: %a | var -i %a Local3 | echo -a Value4: %a | echo -a $var(%a,1).local / $var(%a,1).value vs $var(%a,2).local / $var(%a,2).value
    returns:
    Value1: Global
    Value2: Local2
    Value3:
    Value4:

.. code:: text

    By default, /var and /set do not allow value to be a pair of double quotes nor to end with a single space (multiple spaces can be set)
    The -p changes /var and /set to allow these values:
    //var -p %a "" | var -p %b test $+ $chr(32)  | echo -a %a vs $len(%b)
    returns: "" vs 5
    //var    %a "" | var    %b test $+ $chr(32)  | echo -a %a vs $len(%b)
    returns: vs 4
    -p also includes -n blocking of math operation:
    //var -p %a 1 + 1 | echo -a %a
    returns: 1 + 1

.. code:: text

    The = is no longer required, and is a difference in behavior between /set and /var, though it makes it easier to make a local var beginning with the = symbol:
    //set %a = testa | set %b = = testb | echo -a 1. %a vs %b
    //var %a = testa | var %b = = testb | echo -a 2. %a vs %b
    Return:
    1. = testa vs = = testb
    2. testa vs = testb

By default, /var and /set do not allow value to be a pair of double quotes nor to end with a single space (multiple spaces can be set)
The -p changes /var and /set to allow these values:
//var -p %a "" | var -p %b test $+ $chr(32)  | echo -a 1. %a vs $len(%b)
//var    %a "" | var    %b test $+ $chr(32)  | echo -a 2. %a vs $len(%b)
Return:
1. "" vs 5
2. vs 4</syntaxhighlight>

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$var </identifiers/var>`
    * :doc:`/set </commands/set>`
    * :doc:`/unset </commands/unset>`
    * :doc:`/unsetall </commands/unsetall>`
    * :doc:`$calc </identifiers/calc>`
