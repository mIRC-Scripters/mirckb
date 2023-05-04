/gload
======

The **gload** command loads an agent.

Synopsis
--------

.. code:: text

    /gload -h <name> <filename | N | default>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Hides the agent whenever mIRC is minimized

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name that will be used to reference that agent
    * - <filename | N | default>
      - You can specify the filename to an agent if you know it, or, you can load the Nth agent installed on the system or even specify 'default' which will load the default agent on the system

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/ghide </commands/ghide>`
    * :doc: `/gunload </commands/gunload>`
    * :doc: `/gshow </commands/gshow>`
    * :doc: `/gmove </commands/gmove>`
    * :doc: `/gsize </commands/gsize>`
    * :doc: `/gtalk </commands/gtalk>`
    * :doc: `/gplay </commands/gplay>`
    * :doc: `/gpoint </commands/gpoint>`
    * :doc: `/gstop </commands/gstop>`
    * :doc: `/gopts </commands/gopts>`
    * :doc: `/gqreq </commands/gqreq>`
    * :doc: `$agentver </identifiers/$agentver>`
    * :doc: `$agentstat </identifiers/$agentstat>`
    * :doc: `$agentname </identifiers/$agentname>`
    * :doc: `$agent </identifiers/$agent>`
