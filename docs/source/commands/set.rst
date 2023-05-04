/set
====

The **/set** command can be used to replace the value of an existing variable or create a new variable and assign it the given value. By default /set creates global variable, this can be changed via the -l switch. Unlike the :doc: `/var </commands/var>` command, set cannot assign a value to multiple variables at once. It support :doc: `one math operation </beginner/variables.html#math-operations>` .

Set evaluation routine
----------------------

The set command has its own evaluation routine which lets you dynamically concatenate additional values onto the variable name before the assignment takes place.

.. code:: text

    //set -ls % $+ $ctime ABC

Will create a variable like %1209425041 with the value of 'ABC'; Similarly this can be used with $nick and $chan in on events.

.. note:: /set will fail to evaluate your variable if you have dynamic parameters before the name, read more :doc: `here </beginner/variables.html#special-behaviors-quirks>`

Synopsis
--------

.. code:: text

    /set [-gisuNzneplk] <%var> [value]
    /set [-gisuNznelk] <%var> <number> <+ | - | * | / | % | ^ | &> <number>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Display variable assignment value
    * - -uN
      - Unsets the variable after N amount of seconds. A special case has been made for -u0 which will make the variable unset at the end of script processing, the same way binary variables do.
    * - -z
      - Decreases the value of the variable by 1/second until zero is reached. At zero the variable will be unset.
    * - -n
      - Treat the value as plain text, even if arithmetic operators are used.
    * - -e
      - Unsets the variable when mIRC exits
    * - -l
      - Creates a local variable instead
    * - -k
      - Keeps the unset time (-u) from a previous command
    * - -i
      - Only set the value to the variable if the variable does not already have a value, good for initialization
    * - -g
      - Since you can have a global variable and a local variable of the same name, this makes sure the global variable is set
    * - -p
      - Permits value to be 2 literal doublequotes and permits value to end with a single $chr(32) space. Also performs -n switch behavior

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
      - The value to assign to the variable
    * - <number>
      - Any arbitrary numerical value, can be a floating point number
    * - <+ |
      - | * | / | % | ^> - One of the six possible arithmetic operations
    * - <number>
      - Any arbitrary numerical value, can be a floating point number

Example
-------

.. code:: text

    ; /countDown
    Alias countDown {
    ; set some value
    set %var Countdown:
    ; print the value
    echo -a %var
    ; set the value to 3, decrease once per second
    set -zs %var 3
    }

Will output:

.. code:: text

    Countdown:
    -
    * Set %var to 3
    -
    * Set %var to 2
    -
    * Set %var to 1
    -
    * Unset %var
    -

The -u0 switch can be used to create a variable with global scope that will get unset at the end of the script processing. This can be very helpful at times.

.. code:: text

    Alias example {
    set -u0 %x A
    bb
    ; will print 'B'
    echo -a %x
    }
    alias bb {
    ; replace the value of %x with B, keep the unset setting
    set -k %x B
    }

A simple !seen script that uses /set special evaluation routine to create dynamic variables:

.. code:: text

    on *:text:!seen &:#mIRC:{
    ; check if the variable is set
    if ($var(seen. $+ $2)) {
    ; notice the user the value of '%seen.<nick>'
    notice $nick I have seen $2 $var(seen. $+ $2, 1).value
    }
    else notice $nick I have not seen $2 anywhere.
    }
    on *:text:*:#:{
    ; set the value to '%seen.<nick>'
    set %seen. $+ $nick Talking in $chan < $+ $nick $+ > $1-
    }

Compatibility
-------------

Added: mIRC v4.0 (20 Mar 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$var </identifiers/$var>`
    * :doc: `/dec </commands/dec>`
    * :doc: `/inc </commands/inc>`
    * :doc: `/unset </commands/unset>`
    * :doc: `/unsetall </commands/unsetall>`
    * :doc: `/var </commands/var>`
