/ghide
======

The **ghide** command hides a previously loaded agent.

Synopsis
--------

.. code:: text

    /ghide -h <name>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Prevents the agent from poping up if mIRC is minimized and -h has been used in /gload to load that agent

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name under which you loaded the agent

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;Hide the agent
    /ghide myagent

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/gload </commands/gload>`
    * :doc:`/gunload </commands/gunload>`
    * :doc:`/gshow </commands/gshow>`
    * :doc:`/gmove </commands/gmove>`
    * :doc:`/gsize </commands/gsize>`
    * :doc:`/gtalk </commands/gtalk>`
    * :doc:`/gplay </commands/gplay>`
    * :doc:`/gpoint </commands/gpoint>`
    * :doc:`/gstop </commands/gstop>`
    * :doc:`/gopts </commands/gopts>`
    * :doc:`/gqreq </commands/gqreq>`
    * :doc:`$agentver </identifiers/$agentver>`
    * :doc:`$agentstat </identifiers/$agentstat>`
    * :doc:`$agentname </identifiers/$agentname>`
    * :doc:`$agent </identifiers/$agent>`
