/gshow
======

The **/gshow** command shows an agent.

Synopsis
--------

.. code:: text

    /gshow -h <name> [x y]

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
    * - [x y]>
      - The coordinate of the agent, if not specified, its most recent position or a default will be used

Example
---------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;Show the agent at coordinate 42,42
    /gshow myagent 42 42

Compatibility
-------------

Added: mIRC v5.7 (02 Feb 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
---------

.. hlist::
    :columns: 4

    * :doc:`/ghide <ghide>`
    * :doc:`/gunload <gunload>`
    * :doc:`/gmove <gmove>`
    * :doc:`/gload <gload>`
    * :doc:`/gsize <gsize>`
    * :doc:`/gtalk <gtalk>`
    * :doc:`/gplay <gplay>`
    * :doc:`/gpoint <gpoint>`
    * :doc:`/gstop <gstop>`
    * :doc:`/gopts <gopts>`
    * :doc:`/gqreq <gqreq>`
    * :doc:`$agentver </identifiers/agentver>`
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`$agentname </identifiers/agentname>`
    * :doc:`$agent </identifiers/agent>`
