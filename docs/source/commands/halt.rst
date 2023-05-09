/halt
=====

The /halt command can be used to immediately stop any further processing in a script. If used from within an event (from within an alias that originated from an event), others events in others scripts files are still processed. You can use the & prefix event to prevent an event from being processed if /halt or /haltdef has been used in a previous event, you can also check the :doc:`$halted </identifiers/halted>` identifier from the event without using the & event prefix, which will be :doc:`$true </identifiers/true>`

.. note:: /halt inside an event stop the default processing if you are using the ^ event prefix 

Synopsis
--------

.. code:: text

    /halt

Switches
--------

None

Parameters
----------

None

Example
-------

.. code:: text

    ; /halt_example
    alias halt_example {
      echo -a Some echo!
      halt_example2
      echo -a This echo command will never execute
    }
    alias halt_example2 {
      echo -a Example 2!
      ; kill the script
      halt
    }

Will output:

.. code:: text

    Some echo!
    Example 2!

Compatibility
-------------

Added: 

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$halted </identifiers/halted>`
    * :doc:`/haltdef </commands/haltdef>`
    * :doc:`/return </commands/return>`

