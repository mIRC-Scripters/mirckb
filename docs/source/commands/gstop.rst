/gstop
======

The **/gstop** command stops an agent from doing what he is currently doing and removes all queued requests for the agent.

Synopsis
--------

.. code:: text

    /gstop -ch <name> [talk play]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Prevents the agent from poping up if mIRC is minimized and -h has been used in /gload to load that agent.
    * - -c
      - Only stops the current action.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name used in /gload to reference that agent.
    * - [talk]
      - Stops talk requests
    * - [play]
      - Stops play requests

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;Stop current action
    /gstop -c myagent

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
    * :doc:`/gsize <gsize>`
    * :doc:`/gtalk <gtalk>`
    * :doc:`/gplay <gplay>`
    * :doc:`/gpoint <gpoint>`
    * :doc:`/gmove <gmove>`
    * :doc:`/gopts <gopts>`
    * :doc:`/gqreq <gqreq>`
    * :doc:`$agentver </aliases/agentver>`
    * :doc:`$agentstat </aliases/agentstat>`
    * :doc:`$agentname </aliases/agentname>`
    * :doc:`$agent </aliases/agent>`
