On Ctcpreply
============

The ON CTCPREPLY event triggers when a user responds to a standard :doc:`$ctcp </commands/ctcp>` command.

Synopsis
--------

.. code:: text

    ON <level>:CTCPREPLY:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <matchtext>
      - The corresponding matchtextfor the event to trigger.
    * - <commands>
      - The commands to be performed when the event triggers

Example
-------

Echo, to the active window, the reply a user gives to a ctcp version request.

.. code:: text

    ON *:CTCPREPLY:VERSION*:echo -a $nick $+ 's IRC client is: $1-

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ctcp </commands/ctcp>`
    * :doc:`/ctcpreply </commands/ctcpreply>`

