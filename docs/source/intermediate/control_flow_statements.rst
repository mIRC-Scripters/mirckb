Control Flow Statements
=======================

If-Then-Else
------------

A conditional statement is a control flow construct in mIRC that can execute a set of commands only after comparing or testing a condition. A condition in mIRC has a false truth value if it's $null, $false, or 0.

Intro
~~~~~

You almost never want a script to simply do the same exact thing over and over. In many occasions, you want it to compare two things and decide what to do upon the result of that comparison. For example:

-  Did the user select blue or red?
-  Is the number less than 10?
-  Am I on channel #mIRC?
-  Is the %counter variable assigned or not?

If Statements
~~~~~~~~~~~~~

In many occasions, you will find the need to do a different task based on a condition. The if statement allows you to control what part of your program gets executed or ignored based on conditional statement. Without a conditional statement like an if statement a script would run almost the exact same way each time.

An if statement executes a block of code only if the condition is true. So what does true mean? A true statement is one that evaluates to anything but a zero or a $null value. A false statement is one that evaluates to a zero or a $null value.

The basic syntax for an if statement is:

.. code:: text

   if (condition) {
     ;code to execute only if the condition was true
   }

A typical conditional statement consists of two operands and an operator. An operand is an entity on which an operation is performed. Take for example the following conditional statement:

.. code:: text

   2 > 3

In the example above, ">" is the symbol for the greater than operator. The example above has 2 operands: 2 and 3. In the case of the example above, the answer is false, 2 is not greater than 3.

Operators
~~~~~~~~~

mIRC provides the following types of operators:

-  Arithmetic Operators
-  Math Comparison Operators
-  String Comparison Operators
-  Logical Operators
-  Channel-related Operators
-  List-related Operators

Example
^^^^^^^

Take a look at the following example. In this alias we take a percentage in decimal format and return it in a human readable way. We also want a negative percent to be enclosed by a pair of parentheses.

.. code:: text

   Alias percent {
     ;is the percent negative?
     if ($1 < 0) {
       return ( $+ $calc($1 * 100) $+ % $+ )
     }
     return $calc($1 * -100) $+ %
   }

sample output:

.. code:: text

   //echo -a $percent(-.33)
   (33%)
   //echo -a $percent(.94)
   94%

In the example above, we used an if statement to check if the user input ($1) was less than zero so we could handle it differently than a positive decimal number. When the if statement evaluates to true, the code inside its body, enclosed by a pair of curly brackets, get executed, in our case it also made it return the value to the calling routine, effectively preventing the other statement from ever getting executed.

Else
~~~~

The else statement gives you the ability to execute a block of code when the conditional statement of the if part was false. Notice the else part does not have a conditional statement of its own, it simply acts upon the result of the if statement.

The basic syntax is:

.. code:: text

   if (condition) {
     ;code to execute only if the condition was true
   }
   else {
     ;code to execute only if the condition was false
   }

In the example below, we assign the appropriate time of day to the "%time" variable. We then displayed the result to the screen. We used an if statement to check if the time (just the hours) is less than 10. If true, set %time to day, else, set %time to morning. Depending on the time of day for you, the result will be "Good morning!" or "Good day!".

.. code:: text

   Alias greet {
     if ($time(H) > 10) {
       var %time = day
     }
     else {
       var %time = morning
     }
     echo -a Good %time $+ !
   }

ElseIf
~~~~~~

I am sure at this point you are already thinking what If you had more than one condition that needs to go to a different block of code. An elseif statement is when you have multiple conditional statement that each needs to do something different. If the initial if statement returned false, mIRC will then move on to the elseif and evaluate its condition just like if it was a normal if. If the condition was true, it will execute its body. If the condition of the elseif was false, it will move on to the next elseif or else.

The basic syntax is:

.. code:: text

   if (condition) {
     ;do something if the condition was true
   }
   elseif (condition) {
     ;do something if the /if was false, but the /elseif was true
   }
   else {
     ;do something if both the if and the elseif were false
   }

How would that look in a real scenario? Remember our time of day script? What if we wanted to check if its noon or night as well?. Lets write it down:

.. code:: text

   Alias greet {
     var %hours = $time(H)
     if (%hours < 10) {
       var %time = morning
     }
     elseif (%hours == 12) {
       ;it's 12 o'clock
       var %time = noon
     }
     elseif (%hours > 20) {
       ;it's passed 8:00PM
       var %time = night
     }
     else {
       ;if it's 11 or 1-7PM
       var %time = day
     }
     echo -a Good %time $+ !
   }

Reference Of Parameters
~~~~~~~~~~~~~~~~~~~~~~~

mIRC provides two identifiers to retrieve the first or second parameter of the conditional statement. Please note, the identifiers will return the first and second parameter of the last condition following short-circuit evaluation guidelines.

.. code:: text

   $v1 and $v2

For example:

.. code:: text

   Alias ifExample {
     if (4 < 5) {
       echo -a yes, $v1 is less than $v2
     }
   }

Will have the following output:

.. code:: text

   yes, 4 is less than 5

IIF Identifier
~~~~~~~~~~~~~~

IIF, inline if, is a built in identifier that evaluates a condition, similar to /if statement, and returns one of two values if the condition was true or false.

Syntax:

.. code:: text

   $iif(condition, <code for true>)
     
   ;or
     
   $iif(condition, <code for true>, <code for false>)

.. note:: Unlike a normal identifier, only the true or only the false part of the identifier gets evaluated depending on the condition.

.. _example-1:

Example
^^^^^^^

.. code:: text

   Alias Example {
     echo -a $iif($calc(1 + 1) == 2,1+1 Equals 2)
     echo -a $iif(2 == 5,I Guess 2 Does Equals 5 After All,Nope 2 != 5)
   }

The code above generates the following output:

.. code:: text

   1+1 Equals 2
   Nope 2 != 5

A common usage for an inline if is to decide where to send a reply of a command. For example on some networks ! means a channel message while . means a notice.

.. code:: text

   on $*:text:/^([!.])example$/Si:#:{
     var %send = $iif($regml(1) == ., notice $nick, msg $chan)
     %send This is an example
     %send This is another line!
   }

.. _operators-1:

Operators
---------

By now, you should have a pretty good idea of what variables are and how to use them. Now, all you need to be able to do is operate on them. That's exactly what mIRC Operators lets you do. Operators are special symbols or keywords that perform specific operations on two or three operands in mIRC.

.. _operators-2:

Types Of Operators
~~~~~~~~~~~~~~~~~~

mIRC provides the following types of operators:

-  Arithmetic Operators
-  Math Comparison Operators
-  String Comparison Operators
-  Lexicographical String Comparison Operators
-  Logical Operators
-  Channel-related Operators
-  List-related Operators

Arithmetic Operators
~~~~~~~~~~~~~~~~~~~~

mIRC supports the following arithmetic operators:

================================================= ======
Operator                                          Syntax
================================================= ======
Addition                                          a + b
Subtraction                                       a - b
Multiplication                                    a \* b
Division                                          a / b
Modulo                                            a % b
Power                                             a ^ b
Bitwise AND                                       a & b
Floor division (does not work with /set and /var) a // b
================================================= ======

They can be used in conjunction with the /var or /set commands as well as using the $calc Identifier. One special feature of the $calc identifier over the /var and /set commands is that it supports combination of operators as well as parenthesis to be able to change the order of operations.

.. code:: text

   alias example {
     var %x = 5
     ;5 * 5 = 25
     %x = %x * 5
     echo -a %x

     ;remainder of 25 / 9 = 7
     var %y = %x % 9
     echo -a %y

     ;25 + 7 - 2 = 30
     %x = $calc(%x + %y - 2)
     echo -a %x
   }

Math Comparison Operators
~~~~~~~~~~~~~~~~~~~~~~~~~

Math Comparison operators allow you to compare two values:

+------------+-------------------------------+------------------------------------------------------------+
| Syntax     | Name                          | Result                                                     |
+============+===============================+============================================================+
| %x == %y   | Equal                         | True, if %x is equal to %y.                                |
+------------+-------------------------------+------------------------------------------------------------+
| %x != %y   | Not equal                     | True, if %x is not equal to %y.                            |
+------------+-------------------------------+------------------------------------------------------------+
| %x < %y    | Less than                     | True, if %x is strictly less than %y.                      |
+------------+-------------------------------+------------------------------------------------------------+
| %x > %y    | Greater than                  | True, if %x is strictly greater than %y.                   |
+------------+-------------------------------+------------------------------------------------------------+
| %x <= %y   | Less than or equal to         | True, if %x is less than or equal to %y.                   |
+------------+-------------------------------+------------------------------------------------------------+
| %x >= %y   | Greater than or equal to      | True, if %x is greater than or equal to %y.                |
+------------+-------------------------------+------------------------------------------------------------+
| %x // %y   | Multiple Of (Divides)         | True, if %x divides %y.                                    |
+------------+-------------------------------+------------------------------------------------------------+
| %x \\\\ %y | Not Multiple Of (Not Divides) | True, if %x does not divides %y.                           |
+------------+-------------------------------+------------------------------------------------------------+
| %x & %y    | Bitwise And                   | True, if (bit representation of) %x AND %y is a none zero. |
+------------+-------------------------------+------------------------------------------------------------+

.. _example-2:

Example
^^^^^^^

.. code:: text

   alias example2 {
     ;true (3 a multiple of 9)
     if (3 // 9) echo yes!
     ;false
     if (4 < 4) echo no
     ;00001010 = 10
     ;00000100 = 4
     ;00000000 = 0
     ;true, we used the '!' to negate the operator
     if (10 !& 4) echo yes
   }

String Comparison Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~

mIRC provides a set of operators that can be used to compare two strings. The two iswm and iswmcs operators support two wildcard characters as well, the question mark (?) substitutes for any one character and the asterisk character ("\*") substitutes for any zero or more characters.

+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| Syntax                | Name                               | Result                                                                                         |
+=======================+====================================+================================================================================================+
| %x isin %y            | Is In                              | True, if %x is fully found inside %y.                                                          |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isincs %y          | Is In (case sensitive)             | True, if %x is fully found inside (case sensitive) %y.                                         |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x iswm %y            | Wildcard Matching                  | True, if wildcard string %x matches %y.                                                        |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x iswmcs %y          | Wildcard Matching (case sensitive) | True, if wildcard string %x matches (case sensitive) %y.                                       |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isnum              | Is Digit                           | True, if %x is a number                                                                        |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isnum N            | Is Digit, Equal to                 | True, if %x is number N                                                                        |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isnum N-           | Is Digit, Greater than or equal to | True, if %x is number N or greater                                                             |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isnum N-M          | Is Digit, in Range                 | True, if %x is a number between N and M (inclusively)                                          |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isletter           | Is a Letter                        | True, if %x is a letter                                                                        |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isletter N         | Is a Letter In A List              | True, if %x is a letter in a list of letters                                                   |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isalnum            | Alphanumeric Characters            | True, if %x contains only alphabetic or numeric characters.                                    |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isalpha            | Alphabetic Characters              | True, if %x contains only alphabetic characters.                                               |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x islower            | All lower case letters             | True, if %x does not contain any upper case letters. %x can contain non alphabetic characters. |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+
| %x isupper            | All upper case letters             | True, if %x does not contain any lower case letters. %x can contain non alphabetic characters. |
+-----------------------+------------------------------------+------------------------------------------------------------------------------------------------+

.. _example-3:

Example
^^^^^^^

.. code:: text

   alias example3 {
     var %x = Hello!
     if (?ell?? iswm %x) echo true
     ;false, because of '!'
     if (%x isalpha) echo no
     %x = 5
     if (%x isnum 1-10) echo true
     if (%x isnum)  echo true
   }

Lexicographical String Comparison Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lexicographical comparison is a comparison generally used to sort words alphabetically in dictionaries and indexes. If both strings are equal but one is shorter than the other, the shorter string is lexicographically less than the longer one.

+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| Syntax                | Name                                  | Result                                                              |
+=======================+=======================================+=====================================================================+
| a == b                | Case insensitive character comparison | True, if character a is equal to character b, case insensitive.     |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| a === b               | Case sensitive character comparison   | True, if character a is equal to character b, case sensitive.       |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| a != b                | Case insensitive character comparison | True, if character a is not equal to character b, case insensitive. |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| a !== b               | Case insensitive character comparison | True, if character a is not equal to character b, case insensitive. |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| a !=== b              | Case sensitive character comparison   | True, if character a is not equal to character b, case sensitive.   |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| str1 == str2          | Case insensitive String comparison    | True, if str1 equals str2 in a case insensitive manner.             |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| str1 === str2         | Case sensitive String comparison      | True, if str1 equals str2 in a case sensitive manner.               |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| str1 != str2          | Case insensitive String comparison    | True, if str1 does not equal str2 in a case insensitive manner.     |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| str1 !== str2         | Case insensitive String comparison    | True, if str1 does not equal str2 in a case insensitive manner.     |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| str1 !=== str2        | Case sensitive String comparison      | True, if str1 does not equal str2 in a case sensitive manner.       |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| a < b                 | Lexicographically Less Than           | True, if the $asc(a) comes before $asc(b)                           |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| a > b                 | Lexicographically Greater Than        | True, if the $asc(a) comes after $asc(b)                            |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| str1 < str2           | Lexicographically Less Than           | True, if str1 comes before str2                                     |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+
| str1 > str2           | Lexicographically Greater Than        | True, if str1 comes after str2                                      |
+-----------------------+---------------------------------------+---------------------------------------------------------------------+

Logical Operators
~~~~~~~~~~~~~~~~~

In an if statement, you are allowed to have more than one condition. Each condition has to be connected to the other using a logical operator. There are two logical operators: \|\| meaning OR and && meaning AND.

.. _example-4:

Example
^^^^^^^

.. code:: text

   if ((%x < 0) || (%x >  10)) {

In the if statement above, %x has to be less than 0 OR greater than 10 to make the if statement be true.

.. code:: text

   if ((%input isupper) && ($len(%input) < 10)) {

The if statement above will only be true if %a contains only upper case letters and its total length is less than 10.

Short-circuit evaluation
^^^^^^^^^^^^^^^^^^^^^^^^

mIRC will only evaluate as much of the condition has it needs. Consider the AND example from above, if %input doesn't contain only upper case letters, the second condition will never even evaluate. This is important to keep in mind when using custom identifiers inside an if statement.

Channel-related Operators
~~~~~~~~~~~~~~~~~~~~~~~~~

mIRC also provides a set of commands to involve IRC channels:

+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Syntax                | Name                  | Result                                                                                                                               |
+=======================+=======================+======================================================================================================================================+
| %x ison %y            | Is On                 | True, if nick %x is on channel %y.                                                                                                   |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x isop %y            | Is an Operator        | True, if nick %x is an operators on channel %y.                                                                                      |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x isowner %y         | Is an Owner           | True, if nick %x is an owner on channel %y.                                                                                          |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x ishop %y           | Is a Halfop           | True, if nick %x is a halfop on channel %y.                                                                                          |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x isvoice %y         | Is a Voice            | True, if nick %x is a voice on channel %y (isvo operator also supported).                                                            |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x isreg %y           | Is a Regular          | True, if nick %x is a regular user on channel %y.                                                                                    |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x ischan             | Is a Channel          | True, if channel %x is a channel you are on and if the %x channel window is still open (doesn't matter if you are connected or not). |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x isban %y           | Is a ban              | True, if ban address %x is a ban on channel %y. (taken from IBL)                                                                     |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| %x isquiet %y         | Is a quiet ban        | True, if ban address %x is a quiet ban on channel %y. (taken from IQL)                                                               |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+

.. _example-5:

Example
^^^^^^^

.. code:: text

   alias example4 {
     ;am I on #mIRC
     if (#mIRC ischan) echo yes
     ;is that ban on #mSL's internal ban list?
     if (*!*@example.com isban #offTopic) echo yes
     ;am I an OP on #mIRC?
     if ($me isop #mIRC) echo yes
   }

List-related Operators
~~~~~~~~~~~~~~~~~~~~~~

mIRC has 5 additional operators to check mIRC internal lists:

+-----------------------+-----------------------------+------------------------------------------------------------+
| Syntax                | Name                        | Result                                                     |
+=======================+=============================+============================================================+
| %x isaop              | In Auto-Op List             | True, if host %x is in the auto-op list.                   |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isaop %y           | In Auto-Op List For Chan    | True, if host %x is in the auto-op list for channel %y.    |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isavoice           | In Auto-Voice List          | True, if host %x is in the auto-voice list.                |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isavoice %y        | In Auto-Voice List For Chan | True, if host %x is in the auto-voice list for channel %y. |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isignore           | In Ignore List              | True, if host %x is in the ignore list.                    |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isignore %y        | In Ignore List For Type     | True, if host %x is in the ignore list for type %y.        |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isprotect          | In Protect List             | True, if host %x is in the protect list.                   |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isprotect %y       | In Protect List For Chan    | True, if host %x is in the protect list for channel %y.    |
+-----------------------+-----------------------------+------------------------------------------------------------+
| %x isnotify           | In Notify List              | True, if host %x is in the notify list.                    |
+-----------------------+-----------------------------+------------------------------------------------------------+

.. _example-6:

Example
^^^^^^^

.. code:: text

   Alias example5 {
     ;is the host in the auto-op list
     if (dave101!*@* isaop) echo yes

     ;assume we have ignore all ctcps: /ignore -tw *!*@*
     ;check if *!*@* in the ignore list for CTCPs:
     if (*!*@* isignore ctcp) echo yes
   }

While Loops
-----------

In many occasions, you may end up doing a task over and over again in a single script (For example, counting from 0 to 10, or sending a message to multiple people or channels). A while loop is a control flow statement that allows code to be executed repeatedly based on a given condition. The code inside the while loop block will get executed as long as the condition is true.

Syntax
~~~~~~

The basic syntax of a while loop is:

.. code:: text

   while (<condition>) {
     ;Code here will be executed
   }

Here is how the while loop works:

1. The conditional statement is checked. If the statement is true, continue on to step 2. If the statement is false go to step 4.
2. The code inside the while loop (inside the brackets) is executed.
3. The entire process starts all over again. Going back to step 1.
4. If the statement was false. No code inside the while loop is executed and the script skips right down to any code below it.

True Conditions
^^^^^^^^^^^^^^^

So we said the while loop will continue to iterate as long as the condition is true. But what exactly does that mean? In mSL, a condition is true if the outcome of the condition is NOT 0, $null, or $false. For example let %x be 5, if the condition is ``while ($calc(%x - 5)) {``, since 5-5 is 0, the while loop's condition is false, thus it will not execute any code inside it.

.. note:: If you are using an operator, for example while (0 == 0) {, the operator is going to define if the condition is true or not, 0 being equal to 0, this condition is true.

.. _example-7:

Example
'''''''

Take a look at the following alias:

.. code:: text

   alias whileExample1 {
     echo -a Line number: 1
     echo -a Line number: 2
     echo -a Line number: 3
     echo -a Line number: 4
     echo -a Line number: 5
     echo -a Line number: 6
     echo -a Line number: 7
     echo -a Line number: 8
     echo -a Line number: 9
     echo -a Line number: 10
   }

This simple alias prints "line number:" follows by the line number, 1 to 10. This simple alias has lots of repeated code; The ideal place for a while loop.

We can rewrite that alias:

.. code:: text

   Alias whileExample1 {
     var %line = 1
     while (%line <= 10) {
       echo -a Line number: %line
       inc %line
     }
   }

Using the while loop, we can repeat the echo statement as many times as we want. Let's take a look at what's going on:

1. We create a local variable called "%line" and assign it the number 1
2. The while loop checks our conditional statement. As long as "%line" is less than or equal to 10, we can enter the while loop.
3. The first statement inside the while loop will cause mIRC to print to the active window "Line number:" follows by the value of "%line".
4. The second statement inside the while loop will cause the "%line" variable to increase by 1 (if no number is specified the default is one).
5. Go back to step 2.

Nested Loops
~~~~~~~~~~~~

A nested loop is a loop that is situated within the body of the other. In a nested loop, the first iteration of the outer loop causes the inner loop to execute. The inner loop will execute its body as long as its condition is true. Upon completion the outer loop executes again, causing the inner loop to execute again. This sequence of events will keep on executing until the outer loop is complete. There is no limit to how many loops can be nested inside each other.

Take a look at this example:

.. code:: text

   alias nestedLoopExample {
     var %x = 1
     ;outer loop
     while (%x <= 3) {
       var %y = 1
       ;inner loop
       while (%y <= 3) {
         echo -a %x - %y
         inc %y
       }
       inc %x
     }
   }

This code will generate the following output:

.. code:: text

   1 - 1
   1 - 2
   1 - 3
   2 - 1
   2 - 2
   2 - 3
   3 - 1
   3 - 2
   3 - 3

Jump Statements
^^^^^^^^^^^^^^^

Jump statements are used to perform an immediate transfer of control. Using jump statements, you can effectively break out of the current loop, jump to the beginning of the current, or transfer program control to another part of the program.

mIRC support the following types of statements:

-  The break statement
-  The continue statement
-  The return statement
-  The goto statement

.. note:: In this tutorial, we will not cover the /return or the /goto commands.

Break Statement
'''''''''''''''

The break statement lets you break out of the currently executing while loop at any point. The break statement will only break out of the while loop in which it is nested in.

break In the example below, we set variable "%x" to 10 and decrease it by one each time. When "%x" reaches 5, break out of the loop.

.. code:: text

   alias breakDemo {
     var %x = 10
     while (%x > 0) {
       if (%x == 5) break
       echo -a %x
       dec %x
     }
   }

The output is:

.. code:: text

   10
   9
   8
   7
   6

If multiple while loops are involved, the outer loops will not be effected.

.. code:: text

   alias multLoopDemo {
     var %x = 5
     while (%x) {
       echo -a %x
     
       while ($true) {
         break
         ; anything here will never be executed
         echo -a You will never see this.
       }
     
       dec %x
     }
   }

The output is:

.. code:: text

   5
   4
   3
   2
   1

Continue Statement
''''''''''''''''''

A continue statement in mIRC will cause the program control to jump to the end of the loop body. causing it to evaluate the conditional statement again skipping any subsequent code. A continue statement can only be used within a loop.

The continue statement has the form:

.. code:: text

   continue

Take a look at this example:

.. code:: text

   alias listEven {
     var %x = 1
     while (%x < 20) {
       inc %x
       if (%x & 1) continue
       echo -a %x
     }
   }

In the example above we created a loop to go from 0 to 20. The if statement checks if the number is odd. If true, we make it jump to the next iteration (Via the /continue command). The last statement of the loop's body is used to print the number.

The output is:

.. code:: text

   2
   4
   6
   8
   10
   12
   14
   16
   18
   20

.. note:: The result is all the even numbers between 2 to 20. If you are wondering how did it echo 20 even though our conditional statement tells mIRC anything less than 20. We have an answer: when %x gets to 19, the if statement will cause the /continue command to execute, as a result, the program control goes back to the conditional statement, 19 < 20, which is true. %x then gets increased by 1 to 20, which will then make it to the echo command.

.. _reference-of-parameters-1:

Reference Of Parameters
~~~~~~~~~~~~~~~~~~~~~~~

mIRC provides two identifiers to retrieve the first or second parameter of the while's conditional statement. Please note, the identifiers will return the first and second parameter of the $TRUE condition following short-circuit evaluation guidelines.

.. code:: text

   $v1 and $v2

In the example below we will count from 1 to 10 using a while loop. Variable "%a" will be set to 1, the loop will keep executing as long as %a is less than or equal to 10.

.. code:: text

   alias refExample {
     var %a 1
     while (%a <= 10) {
       echo -a Count: $v1
       inc %a
     }
   }

Infinite Loops
~~~~~~~~~~~~~~

An infinite loop happens when a condition always evaluates to true. Most times, its due to an error. If that's the case, you can force mIRC to break out of it using the :kbd:`Control-Break` key combination. Such a condition may be used on purpose, where you need to use the break statement to break out of the loop, but you can always rewrite the code otherwise to avoid this type of condition.

.. code:: text

   ;returns a random nickname on a channel while excluding yourself ($me) from the list
   while (1) {
     if ($nick($chan,$r(1,$nick($chan,0))) != $me) {
       echo -a $v1
       break
     }
   }

   ;Equivalent:

   while ($nick($chan,$r(1,$nick($chan,0))) == $me) /
   echo -a $v1

Keeping mIRC Responsive
~~~~~~~~~~~~~~~~~~~~~~~

Whilst your loops are looping, mIRC is not able to process any other activities such as messages sent from the server or your own keystrokes or mouse clicks. So while loops which loop a lot of times can result in mIRC appearing to lag or be unresponsive.

For these situations there are several techniques you can use to mitigate this:

1. Rather than iterating through a hash table item by item or a custom list window line by line to fidn what you want, use mIRC functionality to search for what you are seeking.
2. Split the loops into smaller chunks and use .timer 0 1 to queue the next chunk of iterations, letting mIRC process any server messages, keystrokes and mouse clicks before running the timer.

Goto Statements
---------------

Goto is a command that allows you to jump unconditionally to a specific location within a procedure. Gotos can 'jump' forward or backward within a script but they may not leave the alias or event itself (they cannot jump to any calling routine as well). The goto command tells mIRC to jump to another line which matches a label.

Although in many cases the use of gotos can often lead to spaghetti-code. and can usually be replaced with easier to read and follow while statements and if statements, it is still important to understand this command and have it in your toolbox.

.. _syntax-1:

Syntax
~~~~~~

The goto command has the following syntax:

.. code:: text

   goto label

A line is labeled using the following syntax:

.. code:: text

   :label

The label has to start with the colon symbol (:) and must be a single word.

Jumping
~~~~~~~

There is a neat difference in the way mIRC jumps backward and the way it jumps forward. To get mIRC to reach a goto label that is before the current position, mIRC must has seen that goto label, for example:

.. code:: text

   alias test {
   if (a == b) {
     :label
   }
   goto label
   }

displays

.. code:: text

   "* /goto: 'label' not found (line N, script.mrc)" 

.. note:: The condition does not get executed, the goto label is not seen by mIRC.

Change the code to:

.. code:: text

   alias test {
   if (a == a) {
     :label
     inc -us %test
   if (%test == 2) return
   }
   goto label
   }

Now the goto is seen by mIRC and you should see %test being increased to 1 and then to 2.

To get mIRC to jump to a goto label that is after the current position, this is less strict: mIRC parse the code without executing it, which means it is basically parsing the code according to major rules defining the language, the '{', '}', '\|' and newlines tokens. so considering the following:

.. code:: text

   alias test {
   goto label
   if (a == b) {
     :label
     inc -us %test
   if (%test == 2) return
   }
   goto label
   }

The first /goto label statement gets mIRC to parse the rest as token, probably just words, and :label is found despite the if statement being false, %test is increased to 1 and then to 2, proving that the label is found from the first time with the first goto label (forward jump) and then backward since the label was found the first time.

Conditional Transfer Of Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many times you only want a script to go to a specific location according to a certain condition. You can use an if statement to achieve this. A simple syntax looks like this:

.. code:: text

   if (<condition>) {
     goto label
   }

Goto Loops
~~~~~~~~~~

Goto statements can also be used to create a loop by jumping back to a previous location in the script. The example below is a simple loop counting from 1 to 10. If for any reason you mistakenly caused your script to execute endlessly, you manually break the loop using the Ctrl+Break keys.

.. code:: text

   Alias Count {
     :loop
     var %c $calc(%c + 1)
     echo -a %c
     if (%c <= 9) goto loop
   }

Random Name Example
~~~~~~~~~~~~~~~~~~~

Sometimes a goto can result in smaller code if we need a do-while style loop like other languages. A practical example of this is a random nickname generator which excludes us from the list. Such alias might look like this:

.. code:: text

   ; precondition: $nick($chan, 0) > 1
   alias rnd {
     :retry
     if ($nick($chan, $rand(1, $nick($chan, 0))) == $me) goto retry
     return $v1
   }

Error Handling
~~~~~~~~~~~~~~

Although it is rare to use this feature, the "error" label is a designated goto section for error checking. If there is an error in the script, mIRC try to find an :error label in the current routine. If no :error label is found in the current routine, mIRC will propagate the error backward to any calling routine and look for an :error label in those routines.

This gives you the ability to continue with the script at any point regardless of the error, if you want.

After catching an error with :error, you must check for an error by checking $error with a typical /if statement to make sure you reached the :error part because of an error and not because the script is just reaching that point.

If you want to keep going with the code, use /reseterror as soon as possible, this reset the error (and therefore $error's value), mIRC leaves the error state and you can safely execute anything you want.

If you don't use /reseterror, you can also use /return to tell mIRC to look for a different :error label in previous routines. If you don't use /reseterror or /return you must be careful: mIRC is in an error state, yet it must still process your code somehow to allow you to *at least* check for error and reset it, so the if statement feature probably always works, /echo itself also probably does always work but it's unclear what you can do and what you can't do. You would think that since mIRC is somehow forced to allow you to use the scripting engine to check for error and reset it, you could be able to do anything even without calling /reseterror first, this is not true (see examples), the exact list of features that are working in this situation are unknown, it's recommended not to do anything before using /reseterror in this situation.

.. code:: text

   /*  EXAMPLE 1
       This typical example shows that after reaching :error and without using /reseterror, /echo itself works, but see the next example, a lot of simple operation might be done there.
       Since we don't halt or reset the error, mIRC will display both our echo and its own error for $rand.
    */
   Alias Example {
     echo -a $rand(1,)
     return
     :error
     echo -a Error: $error
   }
   /* EXAMPLE 2
      In this case, we try to execute /echo again after a /if error, but on $regsubex, for some reasons, that $regsubex gets mIRC to silentely halts while inside a routine.
      You should get the first echo 'ok' and an echo '> $str(ab,2000)' is expected, but you shouldn't see it.
      Use /reseterror first and it works as expected.
   */
   alias testgoto {
     if
     :error
     echo -a ok | echo -a > $regsubex($str(ab,2000),/(a*)b*(a*)*b/,)
   }
   /* EXAMPLE 3
   Although this example might look a little confusing, bear with me:
   Calling alias /Foo will echo what alias FooBar returns.
   Alias foobar will return what alias bar returns.
   Because alias bar errors out (since $mid is missing a few parameters), mIRC will look for an :error label in alias Bar but won't find any.
   So it will look in the previous routine, the alias FooBar. an :error label is found in the alias FooBar.
   It is executed, echoing Error followed by the error message and returning 1000 to alias foo.
   The /reseterror command effectively prevents mIRC from halting the script and allows it to finish executing.
   */

   Alias Foo {
     echo -a $FooBar
   }
   Alias Bar { 
     return $mid($1)
   }
   Alias FooBar {
     return $Bar(Example)
     :error
     echo -a Error Using Value 1000 instead! ( $+ $error $+ )
     reseterror
     return 1000
   }

Groups
------

Inside the script editor, you can use group to disable/enable a whole piece of code, an alias, an on text event, a menu, a dialog etc.

.. code:: text

   #group_name off
   alias myalias {
     echo -a hey!
   }
   #group_name end

Effectively disables the **myalias** alias. The keyword that can appear after the #group_name on top are "on" to enable it or "off", to disable it. At the bottom the keyword is always "end".

You can use /enable #group and /disable #group to enable/disable a group, you can use $group to get the state of a group, its name, and the file in which the group can be found. You can use /groups to list the groups.

.. note:: You cannot nest groups. Using /disable or /enable implies mIRC writes to the file to change the keyword above, to either on or off.

Groups are useful for speeding mIRC overall with your scripts, if you use if statement as an on/off %variable to ignore code, mIRC still has to trigger you code:

.. code:: text

   on *:text:*:#:{
    if (%enabled) {
    ;some code
    }
   }

vs

.. code:: text

   #group on
    on *:text:*:#:{
    ;some code
   }
   #group end  

On a channel with a lot of activity and/or if you have a lot on text event, in the first code, mIRC will trigger the on text event for all messages, which means running the scripting engine, which means a lot of processing for no reason.

For the second code with the group, after you disable the group mIRC never execute the on text event. Groups also do not require a resource like a %variable.
