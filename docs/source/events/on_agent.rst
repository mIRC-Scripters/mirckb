On Agent
========

The ON AGENT triggers when an Agent has finished speaking.

Synopsis
--------

.. code:: text

    ON <level>:AGENT:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <commands>
      - This is the area in which you want to perform the commands to execute after an Agent has finished speaking.

Local identifiers
-----------------

The on agent event expose one local identifier:


.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$agentname </identifiers/agentname>`
      - Returns the name of the agent triggering the event

Example
-------

After an Agent finishes speaking, echoes that it finished''

.. code:: text

    ON *:AGENT:echo -s agent $agentname finished talking

Compatibility
-------------

.. compatibility:: 5.9

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
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`$agentver </identifiers/agentver>`
