$mode
=====

$mode returns the Nth nick affected by a channel mode change, this identifier is meant to be used inside event such as :doc:`on op </events/on_op>`, :doc:`on rawmode </events/on_rawmode>`, :doc:`on mode </events/on_mode>` etc

Synopsis
--------

.. code:: text

    $mode(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth nick affected, you can use N = 0 to get the total number of nick affected

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
if you use properties, it returns the Nth nick for the specified mode change:

* .owner - returns the Nth nick which is given the owner status
* .deowner - returns the Nth nick which is demoted from the owner status
* .op - returns the Nth nick which is given the op status
* .deop - returns the Nth nick which is demoted from the op status
* .help - returns the Nth nick which is given the help status
* .dehelp - returns the Nth nick which is demoted from the help status
* .voice - returns the Nth nick which is given the voice status
* .devoice - returns the Nth nick which is demoted from the voice status
* .ban - returns the Nth nick which is banned
* .unban - returns the Nth nick which is unbanned

Example
-------

Although on op only triggers for op status, if you type /mode #chan +ob nick test, $mode(0) is still 2 and you can access all the modes lists

.. code:: text

    on *:op:#:echo -a $mode(0)

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$modefirst </identifiers/modefirst>`
    * :doc:`$modelast </identifiers/modelast>`

