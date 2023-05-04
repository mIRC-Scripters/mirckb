/gunload
========

The **gunload** command unloads any agent, by its agent name, that has been previously loaded via the :doc:`/gload </commands/gload>` .

Synopsis
--------

.. code:: text

    /gunload <name>

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name that you used to reference the agent in the initial :doc:`/gload </commands/gload>` call

Example
-------

.. code:: text

    ; Unload a previously loaded agent named myagent
    /gunload myagent

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ghide </commands/ghide>`
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
