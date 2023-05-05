/gplay
======

The **gplay** command makes an agent play one of its animation.

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

Added: mIRC v5.7 (07 May 2000)

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
    * :doc:`/gmove </commands/gmove>`
    * :doc:`/gpoint </commands/gpoint>`
    * :doc:`/gstop </commands/gstop>`
    * :doc:`/gopts </commands/gopts>`
    * :doc:`/gqreq </commands/gqreq>`
    * :doc:`$agentver </identifiers/agentver>`
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`$agentname </identifiers/agentname>`
    * :doc:`$agent </identifiers/agent>`
