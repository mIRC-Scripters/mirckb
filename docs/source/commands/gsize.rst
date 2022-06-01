/gsize
======

The **/gsize** command resizes an agent to the specified width and height.

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

Added: mIRC v5.7 (02 Feb 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
---------

.. hlist::
    :columns: 4

    * :doc:`/ghide <ghide>`
    * :doc:`/gunload <gunload>`
    * :doc:`/gshow <gshow>`
    * :doc:`/gload <gload>`
    * :doc:`/gmove <gmove>`
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
