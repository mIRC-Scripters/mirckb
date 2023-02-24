/inc
====

The **/inc** command increases the numeric value of a variable by a given value. If [value] is not specified, mIRC will increase the variable by one. The /inc command works with both positive and negative values alike.

.. note:: /inc always keeps the unset time if there is one for the current variable, as though there was a -k switch from :doc:`/set <set>`, there's no switch to prevent this behavior and unset the time while setting the value.

Synopsis
--------

.. code:: text

    /inc [-scrzeuN] <%var> [value]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Prints out the value of the variable

.. list-table:: Global variables only
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Increases the variable by 1 every second
    * - -r
      - Increases the variable by 1 every second (same as -c)
    * - -z
      - Decreases the variable by 1 every second until it reaches zero at which point the variable will get unset.
    * - -e
      - Unsets the variable when mIRC exits
    * - -uN
      - Increases the variable once and unsets the variable after N seconds

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - %var
      - The variable's name
    * - [value]
      - Optional numeric value to increase the variable by. Default is 1 if [value] not used

Example
--------

.. code:: text

    Alias Example {
      ;Create a local variable and set it to 5
      var %x 5
      ;Increase %x by 5
      inc %x 5
      ;Print out %x's content
      echo -a %x
    }

.. note::

    If script or timer execution lasts longer than 1 second, -c and -z can skip increments or decrements:

    .. code:: text

        //set %i 10 | inc -z %i | timertest 5 1 echo -a $!timer(test).reps $!asctime i= $eval(%i,0) $(|) var $eval(%j,0) 99999 $(|) while ( $eval(%j,0) ) $chr(123) var $eval(%k,0) $!rand(1,999) $(|) dec $eval(%j,0) $chr(125) | echo -a com: $timer(test).com | timer

        //var %i 1 | inc %i 0 | echo -a this did not change i= %i | var %j $null | inc %i | echo -a this changed by 1 because [value] is null i= %i

        this did not change i= 1
        this changed by 1 because [value] is null i= 2
        this incremented by 3 i= 5

        //var %i foo | inc %i | inc %i 5 | echo -a inc does not alter non-numeric values i= %i

Compatibility
-------------

Added: mIRC v4.0 (20 Mar 1996)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$var </identifiers/var>`
    * :doc:`/dec <dec>`
    * :doc:`/inc <inc>`
    * :doc:`/set <set>`
    * :doc:`/unset <unset>`
    * :doc:`/var <var>`
