$agentver
=========

$agentver returns the current version of the installed Microsoft Agent.

Synopsis
--------

.. code:: text

    $agentver

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
      - No agent is installed.
    * - vN.NN
      - Essentially the vN.NN will be the installed version of your agent.

Example
-------

Echo the current user-agent version to the active window:

.. code:: text

    //echo -a $agentver

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
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`on agent </events/on_agent>`

