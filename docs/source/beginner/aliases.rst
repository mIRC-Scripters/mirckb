Aliases
=======

In many cases, it is easier to code a large program by working with a single, small, unit of logic at a time. Aliases, more commonly known in other languages as functions, are blocks of code which performs a specific task and can be relatively independent of the rest of the script. Most aliases are created to be used multiple times by different scripts. In addition to their normal usage, aliases can also be used to create custom shortcuts and function keys operations.

Syntax
------

Aliases have the following basic syntax:

.. code:: text

   ;single-line alias
   alias aliasName /commands

   ;multi-line alias
   alias aliasName {
     /commands
   }

A simple hello world alias would look like this:

.. code:: text

   Alias hello {
     echo -a Hello World!
   }

The keyword “alias” is required to tell mIRC the following code is an alias. “hello” is the name of the alias. Everything inside the pairs of brackets ({ and }) will get executed when this alias is called. To call that alias, we would simple call the name of it:

.. code:: text

   //hello

This will print:

.. code:: text

   Hello World!

Alias Arguments
---------------

Data can be passed to aliases via the argument list. The argument list is always evaluated from left to right. The arguments are passed to the alias via the $N identifiers, where N is a numeric value from starting at one.

If we called an alias called “example” like this:

.. code:: text

   /example A B C D
   ; or
   ... $example(A, B, C, D)

Alias example will have $1 returning ‘A’, $2 returning ‘B’, $3 returning ‘C’, and $4 returning ‘D’. The total number of tokens available can be retrieved via the $0 identifiers. In this case $0 will return 4.

The exact rules on how $N work is identical to the how they work with the /tokenize command.

Aliases Tab
-----------

The aliases tab is designed specifically for aliases only. Note that because it can only be used for aliases, the “alias” prefix must be left out:

.. code:: text

   aliasName {
     ; commands
   }

.. note:: Aliases from the aliases tab can freely call aliases from the remote tab and vice versa.

Commands vs. Identifiers
------------------------

in mSL, aliases can serve as both identifiers and commands. These two terms are used to describe the type of alias it is. In general, a command will usually not return anything but simply process some type of data. An Identifier on the other hand will generally return some kind of a value.

Aliases Prefixes
----------------

Command Prefixes
~~~~~~~~~~~~~~~~

. prefix (silencing)
^^^^^^^^^^^^^^^^^^^^

You can prefix your command call by a dot ‘.’ to prevent mIRC from displaying its typical message, such as: ``.timer``

! prefix (built-in call)
^^^^^^^^^^^^^^^^^^^^^^^^

By default, a command call will call any custom alias you may have defined, you can force a call to a mIRC built-in command by using the **!** prefix, /!join makes sure it calls the mIRC built-in join command instead of the custom join alias you may have defined.

Identifier Prefixes
~~~~~~~~~~~~~~~~~~~

$$ special construct (required value)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use $$identifier to halt a routine if the value returned by the identifier is $null, typically, this stops further processing if a parameter is missing.

/ and . prefix (custom call)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, an identifier call will call the built-in mIRC identifier, you can force a call to your own custom identifier by using the ‘/’ or ‘.’ prefix, $/me makes sure it calls your custom identifier. If you do not have the alias defined, mIRC consider it a call to an alias named with the ‘/’ or the ‘.’

~ prefix (built-in call)
^^^^^^^^^^^^^^^^^^^^^^^^

In essence, such a call to an identifier will only look at built-in identifiers, custom aliases won’t be searched for. This will bypass the Identifier Warning message but it’s a bit unclear why this is useful, it can allow you to check if an identifier exist in mIRC’s own language and has a value but you cannot use it to check built-in which would return $null then, and you have to execute the function, checking for "$findfile" or "$zip" would be problematic.

! prefix (delay evaluation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use $!identifier to return the plain text identifier instead of it getting evaluated, the rest of the line is evaluated normally, $!+( $me ) does not delay the evaluation of $me

Restriction On Alias Name
-------------------------

Given the alias prefixes above, you cannot start the name of an alias with a command prefix if you are going to call it as a command, same idea for identifier.

Commands
--------

A command usually does not return any value, but instead, it processes the arguments it’s given. In a command, every argument is separated by a space. $0 will contain the total number of arguments passed to that alias. $N (where N is a number 1 to $0) will contain the arguments. For example:

.. code:: text

   alias example {
     echo -a $0 arguments passed
     echo -a The first 3 arguments are:
     echo -a Arg1 = $1
     echo -a Arg2 = $2
     echo -a Arg3 = $3
   }

We can run the code using the follow statement:

.. code:: text

   /example A B C D

This will produce the following result:

.. code:: text

   4 arguments passed
   The first 3 arguments are:
   Arg1 = A
   Arg2 = B
   Arg3 = C

Identifiers
-----------

Generally, an identifier is a value-returning alias. This means we pass some arguments to that alias and we expect it to return something in return. Identifiers are prefixed with the dollar symbol ($). An identifier may or may not need arguments to be passed to it. If the identifier requires that some arguments be passed to it, the arguments must be in a parenthesis, comma delimited.

.. code:: text

   ;This identifier does not need any arguments
   echo -a $me
   ;This identifier requires that we pass it some arguments:
   echo -a $calc(1 + 1)

Unlike a command, arguments are now comma delimited. As a result, passing a single argument with spaces is possible. In addition, since identifiers require that some value be returned back, we use the /return keyword to return some value. The /return command allows the calling routine to continue on using the value returned. Below is an example:

.. code:: text

   alias example {
     return hello there!
   }

we can call that identifier using like this:

.. code:: text

   //echo -a $example

This will print:

.. code:: text

   hello there!

By default, ‘return’ strips leading/trailing/consecutive spaces from the result before returning it. Consider the following aliases:

.. code:: text

   alias example_result   return   $str($chr(32),2) $+ a $+ $str($chr(32),2) $+ a $+ $str($chr(32),2)
   alias example_resultex returnex $str($chr(32),2) $+ a $+ $str($chr(32),2) $+ a $+ $str($chr(32),2)

‘return’ removes the extra spaces, while returnex preserves them, as shown by:

.. code:: text

   //echo -a $replace($example_result  ,$chr(32),.)
   output: a.a
   //echo -a $replace($example_resultex,$chr(32),.)
   output: ..a..a..

Identifiers Properties
----------------------

Properties are a unique feature to identifiers with arguments. They allow you to pass one more additional remark to the alias. That remark can be retrieved from within the alias using the $prop identifier. Properties are usually a way to manipulate the arguments we pass to the alias.

Consider this basic alias that returns some quantity of degrees in radians:

.. code:: text

   ; converts degrees to radians
   alias convert {
     return $calc($1 * $pi / 180)
   }

For example:

.. code:: text

   //echo -a $convert(1)
   0.017453
   //echo -a $convert(15.5)
   0.270526

We can add two properties to make it convert from degrees to radians and and vice versa.

.. code:: text

   ; converts degrees to radians
   alias convert {
     if ($prop == deg2rad) return $calc($1 * $pi / 180)
     if ($prop == rad2deg) return $calc($1 * 180 / $pi)
     ; invalid property
     return 0
   }

For example:

.. code:: text

   //echo -a $convert(10).deg2rad
   0.174533
   //echo -a $convert(0.174533).rad2deg
   10.000004
   //echo -a $convert($convert(15.5).deg2rad).rad2deg
   15.499998

Aliases as Both an Ident and Cmd
--------------------------------

Although most aliases do only serve as identifiers or commands, it is possible to act as both.

Consider the following alias, logfind. Logfind finds the first matching line from the log for the active window. If it’s called as an identifier, we wil return the matching line. If it’s called as a command, we will print it instead:

.. code:: text

   ; Finds the first matching line from the log for the active window
   alias logfind {
     ; find the log file
     var %logfile $window($active).logfile
     var %match = $read(%logfile, nw, $1)
     ; if it was an identifier, return the match
     if ($isid) return %match
     ; print it if it was a command
     echo -agc info * Logfind Match: %match
   }

We can call that alias as an identifier, for example:

.. code:: text

   //echo -a $logfind(*kicked*)
   [12:33] * Foo was kicked by *.example.com (Flooding (Limit is 12 lines per 10 seconds))

We can also call it as a command:

.. code:: text

   /logfind *kicked*
   * Logfind Match: [12:33] * Foo was kicked by *.example.com (Flooding (Limit is 12 lines per 10 seconds))

.. note:: When an alias is called as a /my_alias command it inherits the $parms string as existing in the parent alias, but when called as $my_alias identifier the $parms string is set to $null.

Replacing Built-in Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can intercept any script’s use of a built-in command, as long as they have not used the ! prefix to force execution of the built-in command without searching all the aliases for a match. For example, here’s something to trap echo commands and remove colors, bold, etc from the displayed string:

.. code:: text

   alias echo {
     if ($1 isnum 0-) var %text $strip($2-)
     else             var %text $strip($1-)
     echo %text
   }

Because an alias is not re-entrant, using ‘echo’ inside an alias of the same name cannot be intercepted by that same alias, though it can be trapped by another alias named echo, unless this alias calls it like !echo. This does not completely trap all colors, because it does not remove the color from “/echo -c ctcp message”.

Especially if your alias is non-local, beware about trapping built-in commands without supporting ALL variations of syntax for them. For example, the /server command has different behaviors for different purposes. There are some sets of switches which join a server, and other syntax for modifying the servers.txt file.

Incorrect trapping of built-in commands is one source of bugs that can be easy to overlook, so you may need to use $isalias(built_in_command) to see if any of your scripts has trapped it, and even that doesn’t see local aliases unless $isalias is used from within that same script.

Something else which might need to be preserved is the state of $v1 and $v2. Consider the following while the above ‘alias echo’ is trapping the :

.. code:: text

   //if (var1 != var2) echo -a $ $+ v1 is $v1 and $ $+ v2 is $v2 | echo test | !echo and now $ $+ v1 is $v1 and $ $+ v2 is $v2
   output:
   $v1 is var1 and $v2 is var2
   test
   and now $v1 is test and $v2 is 0-

.. note:: The first echo interprets $v1 and $v2 before sending to the alias echo, so the values are not altered. But now see how the identical message has been altered by the if() statement within alias echo, due to $v1 and $v2 created in one alias being seen in the editbox or another alias. In case this can be an interference for the calling scripts, you can save the $v1 and $v2 values before altering them, then restore them afterwards:

.. code:: text

   alias echo {
     var -p %v1 $v1 , %v2 $v2
     if ($1 isnum 0-) var %text $strip($2-)
     else             var %text $strip($1-)
     echo %text
     if (%v1 == %v2) noop
   }

This saves the $v1 and $v2 as they exist when entering the alias. Then before exit, it creates a dummy if() statement which has the effect of restoring them.

Aliases For Other Users
-----------------------

A consideration in creating aliases which might be executed by other users is to take into account that other users will not use the same colors that you do. There are large user bases who use each of black or white backgrounds, and there are lots of colors which contrast well against one yet have poor contrast against the other. In the default ’mIRC Classic" color set, 8 “Yellow” and 11 “LightCyan” do poorly against a White background, but do well against Black. On the other hand, 2 “NavyBlue” does well against White but poorly against Black. And of course, the White and Black text colors obviously don’t contrast well against the same color background.

One choice for your script is to override the background while setting text color, but even that doesn’t guarantee the user has set that pair of index colors to be a good contrast against each other. To guarantee the actual color hues display as you intend, you can use color index 16-98 as long as the script will be used on v7.52 or higher, because on older versions interpret those color indexes as black. Only a few color hues of the default 0-15 “mIRC Classic” colors are duplicated exactly within the 16-98 range, so others might need to choose the closest approximation.

Another choice is to use echo’s -c switch to set the color which that user has assigned in their Alt+K dialog. For example, if your alias wishes to mimic a blue error message similar to those from built-in mIRC commands:

.. code:: text

   /echo -ac info this displays in the same color as mIRC error messages

Additional Alias Features
-------------------------

Regardless of whether or not an alias was called as a command or as an identifier, if it used the /return command to return back, you can get that value using the $result identifier.

.. code:: text

   alias example {
     foo
     echo -a $result
   }
   alias foo {
     return result!
   }

Output:

.. code:: text

   /example
   result!

In addition, aliases can be coded to work in verbose mode or not. If the command was prefixed with the dot (.) symbol, $show will return $false, otherwise it will $true. For example:

.. code:: text

   alias example {
     if ($show) {
       ;Indicate we are doing something
       echo -a we are doing something
       ;Show more debug info.
     }
     ;do something
   }

Output:

.. code:: text

   /example
   we are doing something
   /.example

.. note:: /echo -q is a built-in alternative to doing that, the echo will be displayed or not depending on the value of $show.

Shortcuts and Function Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aliases can be used to redefine function keys and shortcuts by simply renaming them the actual key or key combinations. For the F-keys all you need is to name the actual alias F1 through F12. S and C can be used for the Shift and Ctrl Key. For example SF1 is Shift+F1 keys.

For example:

.. code:: text

   alias SF1 {
     echo -a Shift+F1 was pressed!
   }

Local Aliases
-------------

By default, every alias is public. This means any script from any file is able to call that alias (even from the editbox). An alias can be made local by using the -l switch. A local alias is only visible to local scripts - scripts that are in the same file as the alias itself. This is especially useful when your aliases have common names and you don’t want to cause conflicts when distributing your script to other people.

.. code:: text

   Alias -l <name> {
     ;code
   }

Exposing Private And Public Functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It’s possible to allow more functionality for local aliases and hide that from outside scripts.

.. code:: text

   alias -l example {
     echo -a Local code called me!
   }
   alias example {
     echo -a Non-local script called me!
   }

If some code local to that script file calls example, the local alias will execute. If some other code outside of this script file calls it the second alias will execute instead. Note that the local alias must be on top, or else the other aliases inside that script will see only the non-local alias above it.

Alias Order
~~~~~~~~~~~

The order used by mIRC to locate your alias is as follows:

-  files are read from top to bottom and only the first found alias in file will be used
-  if the call is made from a script and there is an alias for that name in the script file, that alias is used (regardless if the alias is local or not)
-  if none of the above is true, then the order in which you loaded the script is used. mIRC looks for the first non local alias in the order 1-or-more aliases files in the Alt+D tab of the script editor, followed by the scripts of the Alt+R tab in the order they’re loaded. If you have the same alias name defined twice in the same file, the 2nd one cannot be executed.
-  if none is found, then mIRC check if this is a built-in command name
-  if still no match and if it was a command call, then it sends the command to the server, which sends back RAW numeric 421 if it’s an invalid server command

.. note:: The command line of a timer behaves as if it’s inside the script from where it was launched, it will execute aliases found in the file first.
