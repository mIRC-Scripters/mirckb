/gpoint
=======

The gpoint command makes an agent point towards the specified position

Synopsis
--------

.. code:: text

    /gpoint -h <name> <x> <y>

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
    * - <x>
      - The 'x' coordinate
    * - <y>
      - The 'y' coordinate

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;Make the agent point at coordinate 42,42
    /gpoint myagent 42 42

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ghide </commands/ghide>`
    * :doc:`/gunload </commands/gunload>`
    * :doc:`/gshow </commands/gshow>`
    * :doc:`/gload </commands/gload>`
    * :doc:`/gsize </commands/gsize>`
    * :doc:`/gtalk </commands/gtalk>`
    * :doc:`/gplay </commands/gplay>`
    * :doc:`/gmove </commands/gmove>`
    * :doc:`/gstop </commands/gstop>`
    * :doc:`/gopts </commands/gopts>`
    * :doc:`/gqreq </commands/gqreq>`
    * :doc:`$agentver </identifiers/agentver>`
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`$agentname </identifiers/agentname>`
    * :doc:`$agent </identifiers/agent>`

