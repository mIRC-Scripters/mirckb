/gsize
======

The **gsize** command resizes an agent to the specified width and height.

Synopsis
--------

.. code:: text

    /gsize -h <name> <w> <h>

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
      - The name used in /gload to reference that agent
    * - <w>
      - The new width of the agent
    * - <h>
      - The new height of the agent

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;Resize the agent to a width of 42 and a height of 42
    /gsize myagent 42 42

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ghide </commands/ghide>`
    * :doc:`/gunload </commands/gunload>`
    * :doc:`/gshow </commands/gshow>`
    * :doc:`/gload </commands/gload>`
    * :doc:`/gmove </commands/gmove>`
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
