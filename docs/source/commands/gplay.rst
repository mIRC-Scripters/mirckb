/gplay
======

The **/gplay** command makes an agent play one of its animation.

Synopsis
--------

.. code:: text

    /gplay -h <name> <anim | N> [timeout]

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
    * - <anim | N>
      - Either the name of the animation or the Nth animation
    * - [timeout]
      - Some animations are looping animations, which repeat continuously, and prevent an agent from doing anything else until you /gstop the agent. The [timeout] value allows you to specify a timeout for an animation after which it is automatically stopped, and the agent will then perform any remaining queued requests. If you do not specify a timeout value, the default is 5 seconds. If no play or talk requests are pending, the looping animation continues beyond the timeout until there are.

Example
-------


.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;Plays the 2nd animationi
    /gplay myagent 2


Compatibility
-------------

Added: mIRC v5.7 (02 Feb 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ghide <ghide>`
    * :doc:`/gunload <gunload>`
    * :doc:`/gshow <gshow>`
    * :doc:`/gload <gload>`
    * :doc:`/gsize <gsize>`
    * :doc:`/gtalk <gtalk>`
    * :doc:`/gmove <gmove>`
    * :doc:`/gpoint <gpoint>`
    * :doc:`/gstop <gstop>`
    * :doc:`/gopts <gopts>`
    * :doc:`/gqreq <gqreq>`
    * :doc:`$agentver </aliases/agentver>`
    * :doc:`$agentstat </aliases/agentstat>`
    * :doc:`$agentname </aliases/agentname>`
    * :doc:`$agent </aliases/agent>`
