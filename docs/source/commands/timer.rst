/timer
======

The **/timer** command can be used to create a general purpose timer. A timer is a way to execute code at some specific interval or time and delay. Timers can be named and unnamed. Unnamed timers will get the lowest numeric timer index available. Named timers are specifically useful if you need to recall that timer at a later period - to pause it, resume it, or simply reset it. Starting a timer with a name that already exists will override the old timer. Timers are not blocking command, they 
only get executed after the alias/event/etc is complete, losing the access to the local scope.

Synopsis
--------

.. code:: text

    /timers [off]
    /timer[n|name] [off]
    /timer[n|name] [-cdeomhipPrzN] [time] <repetitions> <interval> <nowiki><code></nowiki>

Switches
--------

Creation Manipulators

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -o
      - Creates a offline timer
    * - -c
      - Creates a catch-up timer
    * - -h
      - Creates a high-resolution timer (interval is in millisecond just like -m)

Attributes

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -m
      - Treats the interval parameter as milliseconds instead of seconds
    * - -d
      - Keeps the order of all -d timers
    * - -i
      - Dynamically associates itself with the active connection

Manipulator

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -e

.. note:: it decrease the number of repetition of the timer, probably resets the time counter as well)

    * - -p
      - Pauses a timer, but the countdown is not paused, this switch should serve no real purpose because of the countdown weirdness, -P was added to pause correctly the countdown.
    * - -P
      - Makes a real pause of the timer, countdown included.
    * - -r
      - Resumes a timer paused with -p or -P
    * - -z
      - Resets an online timer; N=2 resets total time, N=1, resets current time, and N=0 is the same as N=1 AND N=2

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [off]
      - A literal 'off' keyword, used to turn off a timer.
    * - [n|name]
      - The name or index of the timer
    * - [time]
      - Time to activate the timer, for example '15:30' for 3:30PM
    * - <repetitions>
      - The amount of times the timer should repeat itself. A repetition value of '0' will repeat forever.
    * - <interval>
      - The delay between two consecutive timer executions
    * - <nowiki><code></nowiki>
      - Code to be executed.

:doc:`$ctimer </identifiers/$ctimer>` & :doc:`$ltimer </identifiers/$ltimer>`
-------------------------------------------------------------------------------

:doc:`$ctimer </identifiers/$ctimer>` can be used to return the name of the timer which triggered the current script while :doc:`$ltimer </identifiers/$ltimer>` returns the name of the last timer which triggered.

Quirks
------

You can check the :doc:`msl injection </beginner/injection.html>` page to learn more about /timer's double evaluation issues.

/timer also has a special evaluation routine which checks for variable assignement (except /var), for example:

  //timer -ho 1 0 set -s %test 5 $(|) unset -s %test

Works correctly: /timer does not evaluate the variable %test both times as it recognize the assignement.

However this behavior is too intrusive, it is not possible to properly check for variable assigment:

  //var -s %a inc,%b somevalue | timer -ho 1 0 echo -s %a %b

here the variable %b's value disappear completely

Example
-------

Below is a simple count down timer that uses a call-back alias once per second:

.. code:: text

    alias example {
    ; start cou
    var %reps = 5

    ; call the timer %reps times after 1 second delay each
    .timer %reps 1 count-down

    ; print the first count
    count-down
    }
    alias -l count-down {
    echo -a Count: $timer($ltimer).reps
    }

The above code will generate the following output:

.. code:: text

    Count: 5
    Count: 4
    Count: 3
    Count: 2
    Count: 1
    Count: 0

A more basic example of a message being delayed for 3 seconds:

.. code:: text

    on *:text:!foo:#foo:{
    ; delay the message for 3 seconds
    timer 1 3 msg #foo Bar!
    }

A repetition of '0' can also be used to mean an repeat forever:

.. code:: text

    alias cur_time {
    timer 0 1 echo -s $!time(hh:nn:ss)
    }

Ending timers by using 'off' parameter, you can also end timers using wildcards.

.. code:: text

    alias test_timers {
    ; /test_timers

    ; creating 3 different names timers
    /timer[test_one] 1 3 echo -a Test one
    /timer[test_two] 1 6 echo -a Test two
    /timer[test_three] 1 10 echo -at Test three

    ; End only one of them
    /timer[test_one] off

    ; Ending all the timers created with 'test_' prefix
    /timer[test_*] off
    }

Compatibility
-------------

Added: mIRC vmIRC 3.3, 3.4 ()

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$timer </identifiers/$timer>`
    * :doc:`$ctimer </identifiers/$ctimer>`
    * :doc:`$ltimer </identifiers/$ltimer>`
    * :doc:`$time </identifiers/$time>`
    * :doc:`$date </identifiers/$date>`
    * :doc:`$gmt </identifiers/$gmt>`
    * :doc:`$asctime </identifiers/$asctime>`
    * :doc:`/scid </commands/scid>`
    * :doc:`/scon </commands/scon>`
