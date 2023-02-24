/gunload
========

The **/gunload** command unloads any agent, by its agent name, that has been previously loaded via the **/gload**.

Synopsis
--------

.. code:: text

    /gunload <name>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name that you used to reference the agent in the initial **/gload** call

Example
-------

.. code:: text

    ; Unload a previously loaded agent named myagent
    /gunload myagent

Compatibility
-------------

Added: mIRC v5.7 (02 Feb 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ghide <ghide>`
    * :doc:`/gshow <gshow>`
    * :doc:`/gmove <gmove>`
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
