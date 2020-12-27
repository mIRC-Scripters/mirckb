Variables
=========

mIRC variables are items which can hold data temporarily, or permanently, for use at a later time.. You can create, edit, or delete them at any time. All mIRC variables must be prefixed with a % sigil (example %var or %cookies). Variables are untyped – therefore capable of storing letters, numbers, or strings at any given point.

Variable Scope: Global vs. Local
--------------------------------

There are two kinds of variables: local and global. Scope refers to the visibility of variables in your code. In other word, where these variables can be seen from.

Local Variables
~~~~~~~~~~~~~~~

Local Variables are given local scope. They are created for the duration of the routine that created them and they can only be accessed from within that routine Once the routine is finished, the variable is deleted. A routine represents an alias, an event, a menu, or when you execute code with two /slash from the editbox.

.. note:: Local variables can be seen from the execution of /scon or /scid: //var %a ok \| scon -r echo -a $ + %a ($1- can’t be seen the same way)

Syntax:

.. code:: text

   ;single variable
   var %temp = value
    
   ;multiple variables
   var %a = value, %b = second value, %c = and so on and so forth

.. note:: Since mIRC 6.21, you can avoid using the = sign when using the /var command.

Local variables are good for temporary things like string manipulations and math expressions. Most of your code will use local variables.

.. code:: text

   Below is a simple addition alias that uses two local variables:

   alias add {
     var %number1 = $1, %number2 = $2
     echo -a %number1 + %number2 = $calc(%number1 + %number2)
   }

An example usage of the script above is: /add 1 3 which will output: 1 + 3 = 4. Once the add alias has finished executing, both “%number1” and “%number2” are destroyed. Remember, these local variables cannot be called upon outside of their code blocks.

Incorrect use of local variables:

.. code:: text

   alias wrong {
     var %myvar = 3
     wronger
   }
   alias wronger {
     echo -a %myvar
   }

If you were to execute the above by typing /wrong, you would get the following error: \* /echo: insufficient parameters. This is because the local variable, in this case %myvar, has been stored within the wrong alias code block, and is, therefore, unavailable to the /wronger alias that has been called.

Global Variables
~~~~~~~~~~~~~~~~

A global variable is a variable that is accessible from every alias or event. They can be created and edited from every script. They are not deleted unless they are purposely destroyed using the unset command (we will talk about that later on).

Syntax:

.. code:: text

   ;create variable
   set %var value

.. note:: The /set command does not use the = operator.

Because the /set command can only set a single variable at a time, you can use the /var command in conjunction with -g switch to set multiple global variables.

;multiple variables var -g %var = foo, %var2 = bar, %var3 = foobar Practical use: a global variable is good for storing variables that you will need to use in the future from another script or at different time. (Login System, Away System, Sockets, Etc…)

Semi Global
-----------

You can use set -u0 to create a variable that can be seen by any routine (global) but is destroyed when the scripting engine exits (when all routines are done), like binary variables.

The Equal Sign ‘=’
------------------

Although it’s not required in /var since 6.21, the equal sign can be used to assign a value to a variable without actually using a command:

.. code:: text

   %var = value

If %var is local, this will change the local variable. If %var is global, it will naturally change the global variable. If %var doesn’t exist, it will create a global variable.

Unsetting Variables
-------------------

If you have already set a variable you can unset it at any time during using the /unset command. The unset command supports a single variable or multiple variables. Generally, there is no reason to unset local variables as they will get destroyed anyway at the conclusion of the script execution.

Syntax
~~~~~~

.. code:: text

   ;unset a single variable
   unset %variable
    
   ;unset multiple variables
   unset %var1 %var2 %var3

The /unset command supports wildcard characters for each of the variable, to be able to unset multiple variables. For example:

.. code:: text

   alias unsetWildExample {
     set %exampleHello hello there
     set %exampleHey another var
     set %exampleVar yet another var
    
     /*
      Illustrating that each variable can be a wildcard
      unset -s %exampleH* %exampleVar

     */ 

     ;unset all of them
     unset %example*
   }

You can also unset all of the variables using the /unsetall command.

!!! caution This will permanently delete all of your variables! You cannot recover them once you have performed this command, so be careful.

$null values
------------

If a variable is referred to but does not exist, it returns the value $null. Likewise, a variable without any data stored in it returns $null as well.

.. code:: text

   alias nullExample {
     ; make sure our variable doesn't exist
     unset %example1
     if (%example1 == $null) {
       echo -a % $+ example1 is null!
     }
     ; set a variable with no data
     set %example2
     if (%example2 == $null) {
       echo -a % $+ example2 is also null!
     }
   }

Upon executing /nullExample, you will notice that mIRC will echo the following to the active window:

.. code:: text

   %example1 is null!
   %example2 is also null!

Math Operations
---------------

You can do one math operation with variable when setting a value.

The operators supported are: ‘+’ ‘-’ ‘/’ ‘\*’ ‘%’ ‘^’ where % id the modulus and ^ is power.

You must use a space around all parameters and you must provide correct values, numbers can be float.

If you don’t respect the format, it will set the value as plain text, use -n to override this behavior when dynamic content.

For Example:

.. code:: text

   alias mathExample {
     ;10
     var %a = 5 + 5
     ;9
     var %b = %a - 1
     ;90
     var %c = %b * %a
     ;print it to the screen
     echo -a %c
   }

Other Commands
--------------

mIRC has two additional commands that can be used to easily increase and decrease the value of a numerical variable.

The dec command allows you to decrease the value of a variable by 1 or by a given value if specified:

.. code:: text

   dec %var [value]

For Example:

.. code:: text

   alias example {
     var %g = 10
     dec %g
     ;9
     echo -a %g
   }

The inc command allows you to increase the value of a variable by 1 or by a given value if specified:

.. code:: text

   inc %var [value]

For Example:

.. code:: text

   on *:action:$(slaps $me $+ *):#mSL:{
     ;increase the variable by 1
     inc %slaps
     msg $chan I have seen %slaps slaps!
   }

Dynamic Variable Names
----------------------

In many occasions you may need to save individualized data (data for a particular user or channel for example). Dynamic variables allow you to do just that. A dynamic variable’s name usually consists of a static part (a part that doesn’t change) and a dynamic part (the part that changes).

Setting Values
~~~~~~~~~~~~~~

The basic syntax to set a dynamic variable is:

.. code:: text

   set %<static_part> $+ <dynamic_part>
   ; or (use var -g to make them global variables)
   var %<static_part> $+ <dynamic_part>

Although you can omit the static part out, its strongly discouraged because variables should have a meaningful name that explains their purpose.

.. note:: You may have seen script using evaluation brackets to set a value to a dynamic variable, they are not required.

Let’s take a look at an example:

.. code:: text

   on *:text:!setColor *:#:{
     ;save their favorite color
     set %color. $+ $nick $2
     notice $nick Your favorite color $qt($2) was saved!
   }

Let’s take a closer look at the variable assignment statement:

.. code:: text

   set %color. $+ $nick $2

The static part is color., which is never going to change, and the dynamic part is $nick. Let’s assume someone by the name John types !setColor blue; this is what happens:

-  mIRC evaluates the identifier $nick to “John” and $2 to blue

.. code:: text

   set %color. $+ John blue

-  mIRC will then append “John” to “%color.” Before executing the /set command, thus the final variable looks like this:

.. code:: text

   %color.John blue

Retrieving Values
~~~~~~~~~~~~~~~~~

Static Variables
^^^^^^^^^^^^^^^^

Retrieving values from static variables is pretty straightforward. Let’s assume you have a variable called %myvar and it’s value is abc, you can get this value simply by referring to the variable outright:

.. code:: text

   alias showVar {
     echo -a Here is the value of % $+ myvar: %myvar
   }

Simply put, this will echo the following to the active window where you typed the /showVar command:

Here is the value of %myvar: abc

Dynamic Variables
^^^^^^^^^^^^^^^^^

Retrieving a value from a dynamic variable is a little bit more complicated. There are two ways.

Using Bracket Evaluation [ ]
''''''''''''''''''''''''''''

.. code:: text

   %<static> [ $+ [ <dynamic> ] ]

This is the evaluation brackets method. They allow us to force mIRC to evaluate part of a statement before anything else. Take a look at the rest of the myColor script:

.. code:: text

   on *:text:!favColor *:#:{
     var %color = %color. [ $+ [ $2 ] ]
     if (%color != $null) {
       notice $nick $2's favorite color is %color $+ .
     }
     else {
       notice $nick $2 doesn't have a favorite color set yet.
     }
   }

In the example above, we retrieved the color from the dynamic variable and set it to a local variable called %color for use in the rest of the script. Let’s take a closer look at the retrieval statement:

.. code:: text

   var %color = %color. [ $+ [ $2 ] ]

When you first glance at this statement, it might look a bit confusing, but in fact it is pretty straightforward. Let us continue with John’s example and assume someone else typed !favColor John:

1. The first thing mIRC will evaluate is the innermost evaluation brackets [ ], in this case its $2, which will evaluate to John.

.. code:: text

   %color. [ $+ John ]

2. mIRC will then evaluate the outer evaluation bracket “$+ John”.

.. code:: text

   %color.John

Here is another example:

.. code:: text

   alias varExample {
     var %array.1 = Item A
     var %array.2 = Item B
     var %array.3 = Item C
     var %array.4 = Item D
     var %array.5 = Item E
     var %x = 1
     while (%x <= 5) {
       echo -a %x = %array. [ $+ [ %x ] ]
       inc %x
     }
   }

The above code will echo the following:

.. code:: text

   1 = Item A
   2 = Item B
   3 = Item C
   4 = Item D
   5 = Item E

What this does is create a bunch of static variables, each with ascending-ordered numerical digits. You will notice we used the evaluation brackets around the variable counter, %x. This allows mIRC to evaluate the variable, and attach it to the static portion of %array.. Basically, during run-time, whatever the %x variable’s value is will be automatically appended to %array..

.. note:: If you have multiple dynamic variable to add together, you need to add another pair of $+ [ … ] for each element:

.. code:: text

    %static [ $+ [ %dynamic1 $+ [ %dynamic2 ] ] ]
    %static [ $+ [ %dynamic1 $+ [ %dynamic2 $+ [ %dynamic3 ] ] ]
    etc..

Using $eval
'''''''''''

You can also get the value of a dynamic variable by using $eval.

$eval allows you to force an expression to evaluate more than once, a bit like the brackets [ ], but brackets are meant to alter the order of evaluation of a line, which itself can have its own drawbacks.

.. code:: text

   $eval($+(%,<static>,<dynamic>),2)

From our earlier example:

.. code:: text

   var %color = %color. [ $+ [ $2 ] ]

is the same as

.. code:: text

   var %color = $eval($+(%,color.,$2),2)

$+(%,color.,$2) will produce the plain text “%color.John”, and that is then evaluated a second time (the 2 in $eval(,2)) to produce the value of the variable just like usual. Note that with the brackets method, you also get a double evaluation, but they happen at a different levels.

This method is easier to read/handle than the bracket, you can simply get the plain text variable you want with $+(), and then you evaluate that twice to get the content of the variable, this method is recommended, but note that it’s a bit slower than the bracket.

.. note:: $eval is often used in the simple form $()

Special Behaviors & Quirks
--------------------------

Variables routines are a bit special because usually, the first argument given to a variables related command is a variable name, yet mIRC doesn’t evaluate it.

Indeed if //echo %var would display its content, it’s because %var is evaluated and then passed as the parameter to the /echo command. //var %var is obviously not doing that otherwise the content of the variable or $null would be passed to it. So mIRC, on purpose doesn’t evaluate the variable name, but it will fail to do so in some case, when the arguments are dynamically passed for example:

.. code:: text

   //set -u $+ %var %setting

which should set %setting but won’t, because it gets evaluated, you need to use % $+ setting here, /inc & /dec are most likely affected the same way.

/unset also suffers from an evaluation problem, due to its ability to unset more than one variable on the same line, there is an issue when trying to unset a variable dynamically from a variable:

.. code:: text

   //var -s %a a,%b b,%ab,%a%b | unset -s %a $+ %b

You might expect this to evaluate %b and stick its content to plain text “%a”, just like in //var -s %a $+ %b, but it won’t, mIRC won’t evaluate %b at all, thinking it’s a seperate variable name you want to unset as well, unsetting the wrong %a%b instead of %ab.

To workaround this problem, you must use evaluation brackets to force the evaluation:

.. code:: text

   //var -s %a a,%b b,%ab,%a%b | unset -s %a $+ [ %b ]

If most commands cannot preserve spaces, /var can preserve spaces in all situations except if you provide a single trailing space:

.. code:: text

   //var -s %a $+($chr(32),a,$chr(32),$chr(32),b,$chr(32),$chr(32)),%b $+($chr(32),a,$chr(32),$chr(32),b,$chr(32)) | echo -a $len(%a) $len(%b)

which is displaying 7 5 instead of 7 6 (there is one less space at the end, which is lost because it’s a single trailing space)

Variables are a great resource to have at your fingertips within mIRC! As you’ve seen, they are very powerful, and yet don’t require too much of a headache to understand :)
