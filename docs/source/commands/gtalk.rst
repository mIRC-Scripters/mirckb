/gtalk
======

The **/gtalk** command makes an Agent speak the specified text.

Synopsis
--------

.. code:: text

    /gtalk -kwlu <name> <text | wavefile text>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Prevents the agent from popping up if mIRC is minimized **and** -h has been used in **/gload** to load that agent.
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
    * - wavefile text
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
    * :doc:`/gmove <gmove>`
    * :doc:`/gplay <gplay>`
    * :doc:`/gpoint <gpoint>`
    * :doc:`/gstop <gstop>`
    * :doc:`/gopts <gopts>`
    * :doc:`/gqreq <gqreq>`
    * :doc:`$agentver </aliases/agentver>`
    * :doc:`$agentstat </aliases/agentstat>`
    * :doc:`$agentname </aliases/agentname>`
    * :doc:`$agent </aliases/agent>`
