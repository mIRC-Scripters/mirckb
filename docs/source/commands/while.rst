/while
======

The /while command is a construct in the mIRC scripting language that can perform repetitive operations. The block of statement inside the while loop will get executed as long as the condition is true. You can manually break out of a loop by using the Cltr+Break key combinations.

Synopsis
--------

.. code:: text

    while (condition) {
      /statements
      /statements
      /statements
    }

Switches
--------

None

Parameters
----------

None

Example
-------

.. code:: text

    /* Example 1
    */
    Alias CountToTen {
      ;Create a counter variable, set it to one
      var %Counter = 1
    
      ;Loop while the counter variable is less than or equal to ten.
      while (%Counter <= 10) {
    
        ;Print out the value of the counter variable
        echo -a Count Number: %Counter
    
        ;Increase the counter variable by 1
        inc %Counter
      }
    }

The above example will output:

.. code:: text

    Count Number: 1
    Count Number: 2
    Count Number: 3
    Count Number: 4
    Count Number: 5
    Count Number: 6
    Count Number: 7
    Count Number: 8
    Count Number: 9
    Count Number: 10

Example 2:

.. code:: text

    
    /* Example 2
    */
    
    Alias ListVars {
      ;Check if there are any variables set
      if (!$var(*,0)) {
        echo -a There Are No Variables.
        halt
      } 
    
      ;Set a counter variable
      var %a 1
    
      ;Loop while the counter variable is less than or equal to the total number of variables
      while (%a <= $var(*,0)) { 
    
        ;Print out the variable and its value
        echo -a $v1 $+ ) $var(*,$v1) = $var(*,$v1).value 
    
        ;Increase the variable by one
        inc %a
      }
    }

The above example will output something like this:

.. code:: text

    1) %Foo = FooBar
    2) %Bar = BarFoo

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/break </commands/break>`
    * :doc:`/continue </commands/continue>`
    * :doc:`/if </commands/if>`
    * :doc:`/return </commands/return>`
    * :doc:`/returnex </commands/returnex>`

