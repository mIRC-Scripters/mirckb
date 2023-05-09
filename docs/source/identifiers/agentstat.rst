$agentstat
==========

The $agentstat identifier is used to retrieve the current status of your user-agent.

Synopsis
--------

.. code:: text

    $agentstat

Switches
--------

None

Results
-------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Description
    * - 0
      - User-agent is currently busy speaking.
    * - 1
      - User-agent is ready for commands.

Example
-------

Echo the current user-agent status to the active window:

.. code:: text

    //echo -a $agentstat

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/gload </commands/gload>`
    * :doc:`/gunload </commands/gunload>`
    * :doc:`/gshow </commands/gshow>`
    * :doc:`/ghide </commands/ghide>`
    * :doc:`/gmove </commands/gmove>`
    * :doc:`/gsize </commands/gsize>`
    * :doc:`/gtalk </commands/gtalk>`
    * :doc:`/gplay </commands/gplay>`
    * :doc:`/gpoint </commands/gpoint>`
    * :doc:`/gstop </commands/gstop>`
    * :doc:`/gopts </commands/gopts>`
    * :doc:`/gqreq </commands/gqreq>`
    * :doc:`$agent </identifiers/agent>`
    * :doc:`$agentname </identifiers/agentname>`
    * :doc:`$agentver </identifiers/agentver>`
    * :doc:`on agent </events/on_agent>`

