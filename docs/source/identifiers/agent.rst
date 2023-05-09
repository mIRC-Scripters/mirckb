$agent
======

$agent returns the filename of the Nth available agent installed on your system, or informations about a loaded agent.

Synopsis
--------

.. code:: text

    $agent(N).property

.. code:: text

    $agent(name,[N2]).property

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth agent available on your system
    * - name
      - The name used in /gload to load the agent
    * - N2
      - The N2th queued line for a loaded agent.

Properties
----------

When N is passed as the first parameter, the following property is available:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - char
      - Returns the character name of the Nth agent instead of the filename.

When name is passed as the first parameter, the following properties are available:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Method
    * - name
      - Returns the name you gave to this agent
    * - fname
      - Returns the filename you gave to this agent, or the filename to the default agent
    * - visible
      - Returns :doc:`$true </identifiers/true>` if the agent is visible, :doc:`$false </identifiers/false>` otherwise
    * - x
      - Returns the x coordinate of the position of the agent (left)
    * - y
      - Returns the y coordinate of the position of the agent (top)
    * - w
      - Returns the current width of the agent
    * - h
      - Returns the current height of the agent
    * - ow
      - Returns the original width of the agent
    * - oh
      - Returns the original height of the agent
    * - speed
      - Returns the speaking speed of the agent
    * - pitch
      - Returns the speaking pitch of the agent
    * - idle
      - Returns :doc:`$true </identifiers/true>` if the idle behavior is on, :doc:`$false </identifiers/false>` otherwise
    * - effects
      - Returns :doc:`$true </identifiers/true>` if the effects are on, :doc:`$false </identifiers/false>` otherwise
    * - active
      - Returns :doc:`$true </identifiers/true>` if the agent is active, :doc:`$false </identifiers/false>` otherwise
    * - langid
      - Returns the language ID of the system
    * - balloons
      - Returns the balloons settings, can be on, off, size, pace, hide
    * - hide
      - Returns the auto hide setting
    * - anim
      - Returns the names of the animations available for this agent, you can use N2 to get the N2th animation.
    * - line
      - Returns the list of lines currently queued for talking for this agent, you can use N2 to get the N2th line.

Example
-------

.. code:: text

    //echo -a $agent(0)

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$agentname </identifiers/agentname>`
    * :doc:`$agentver </identifiers/agentver>`
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`$notags </identifiers/notags>`
    * :doc:`/gload </commands/gload>`
    * :doc:`/gunload </commands/gunload>`
    * :doc:`/gtalk </commands/gtalk>`
    * :doc:`/gshow </commands/gshow>`
    * :doc:`/ghide </commands/ghide>`
    * :doc:`/gmove </commands/gmove>`
    * :doc:`/gsize </commands/gsize>`
    * :doc:`/gplay </commands/gplay>`
    * :doc:`/gpoint </commands/gpoint>`
    * :doc:`/gstop </commands/gstop>`
    * :doc:`/gopts </commands/gopts>`
    * :doc:`/gqreq </commands/gqreq>`
    * :doc:`on agent </events/on_agent>`

