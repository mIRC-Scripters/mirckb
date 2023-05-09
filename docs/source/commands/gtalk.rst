/gtalk
======

The gtalk command makes an Agent speak the specified text.

Synopsis
--------

.. code:: text

    /gtalk -kwlu <name> <text | <wavefile> <text>>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Prevents the agent from popping up if mIRC is minimized ''and'' -h has been used in :doc:`/gload </commands/gload>` to load that agent.
    * - -k
      - Makes the agent think the text in a balloon without speaking it.
    * - -l
      - Applies the lexicon settings in the lexicon dialog to the text.
    * - -u
      - Applies the speech settings in the speech options dialog.
    * - -w
      - Allows you to play a wave sound filename along with Agent text to speak.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The name used in /gload to reference that agent
    * - text
      - The text to be spoken
    * - <wavefile> <text>
      - The sound filename, must be wave format, and the text to be spoken while playing the file

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;make the agent plays 'lol.wav' and speak "text"
    /gtalk -w myagent lol.wav text

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
    * :doc:`/gmove </commands/gmove>`
    * :doc:`/gplay </commands/gplay>`
    * :doc:`/gpoint </commands/gpoint>`
    * :doc:`/gstop </commands/gstop>`
    * :doc:`/gopts </commands/gopts>`
    * :doc:`/gqreq </commands/gqreq>`
    * :doc:`$agentver </identifiers/agentver>`
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`$agentname </identifiers/agentname>`
    * :doc:`$agent </identifiers/agent>`

