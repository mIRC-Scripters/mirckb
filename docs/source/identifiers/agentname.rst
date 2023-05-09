$agentname
==========

$agentname can be used in conjunction with the :doc:`on agent </events/on_agent>` in order to return the name of the Agent associated with the event.

Synopsis
--------

.. code:: text

    $agentname

Parameters
----------

None

Example
-------

After the ON AGENT Event triggers, return the name of the Agent that just finished speaking:

.. code:: text

    ON *:AGENT:echo -a $agentname has just finished speaking.

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on agent </events/on_agent>`
    * :doc:`/gload </commands/gload>`
    * :doc:`/gunload </commands/gunload>`
    * :doc:`/gshow </commands/gshow>`
    * :doc:`/ghide </commands/ghide>`
    * :doc:`/gmove </commands/gmove>`
    * :doc:`/gsize </commands/gsize>`
    * :doc:`/gtalk </commands/gtalk>`
    * :doc:`/gplay </commands/gplay>`
    * :doc:`/gpoint </commands/gpoint>`
    * :doc:`/gstop </commands/gstop>`
    * :doc:`/gopts </commands/gopts>`
    * :doc:`/gqreq </commands/gqreq>`
    * :doc:`$agent </identifiers/agent>`
    * :doc:`$agentstat </identifiers/agentstat>`
    * :doc:`$agentver </identifiers/agentver>`

