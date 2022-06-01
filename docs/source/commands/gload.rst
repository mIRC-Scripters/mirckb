/gload
======

The **/gload** command loads an agent.

Synopsis
--------

.. code:: text

    /gload -h <name> <filename | N | default>

Switches
---------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - Hides the agent whenever mIRC is minimized

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name that will be used to reference that agent
    * - <filename | N | default>
      - You can specify the filename to an agent if you know it, or, you can load the Nth agent installed on the system or even specify 'default' which will load the default agent on the system

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default

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
