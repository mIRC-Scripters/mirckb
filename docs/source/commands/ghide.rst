/ghide
======

The **/ghide** command hides a previously loaded agent.

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

Added: mIRC v5.7 (02 Feb 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/gload <gload>`
    * :doc:`/gunload <gunload>`
    * :doc:`/gshow <gshow>`
    * :doc:`/gmove <gmove>`
    * :doc:`/gsize <gsize>`
    * :doc:`/gtalk <gtalk>`
    * :doc:`/gplay <gplay>`
    * :doc:`/gpoint <gpoint>`
    * :doc:`/gstop <gstop>`
    * :doc:`/gopts <gopts>`
    * :doc:`/gqreq <gqreq>`
    * :doc:`$agentver </aliases/agentver>`
    * :doc:`$agentstat </aliases/agentstat>`
    * :doc:`$agentname </aliases/agentname>`
    * :doc:`$agent </aliases/agent>`

