/gopts
======

The **gopts** command is used to sets various option of a loaded agent

Synopsis
--------

.. code:: text

    /gopts -b <name> <on | off | size | pace | hide | nosize | nopace | nohide>
    /gopts -i <name> <on | off>
    /gopts -e <name> <on | off>
    /gopts -q <name> (undocumented)
    /gopts -n <name> <langid>
    /gopts -h <name> <on | off>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -b
      - Turns balloons on or off, but you can instead specify <size>/<nosize> to enable/disable the balloons to fit the text being spoken, <pace>/<nopace> to enable/disable the display of text word by word as it is being spoken, and <hide>/<nohide> to hide/show the balloons when no text is being spoken.
    * - -i
      - Turns idle effects on or off.
    * - -e
      - Turns sound effects on or off.
    * - -n
      - Allows you to set a language id
    * - -h
      - Turns the auto-hide feature on or off (see /gload for more info).

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The name used in /gload to reference that agent
    * - <on | off>
      - The state for that option
    * - <size | pace | hide | nosize | nopace | nohide>
      - Can be used with -b instead of <on | off> to change the way the balloon is displayed
    * - <langid>
      - Used with -n, the hex id value for the language

Example
-------

.. code:: text

    ;Load the default agent on your system
    /gload myagent default
    ;Turns off sound effect
    /gopts -e myagent off

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/ghide </commands/ghide>`
    * :doc: `/gunload </commands/gunload>`
    * :doc: `/gshow </commands/gshow>`
    * :doc: `/gload </commands/gload>`
    * :doc: `/gsize </commands/gsize>`
    * :doc: `/gtalk </commands/gtalk>`
    * :doc: `/gplay </commands/gplay>`
    * :doc: `/gpoint </commands/gpoint>`
    * :doc: `/gstop </commands/gstop>`
    * :doc: `/gmove </commands/gmove>`
    * :doc: `/gqreq </commands/gqreq>`
    * :doc: `$agentver </identifiers/$agentver>`
    * :doc: `$agentstat </identifiers/$agentstat>`
    * :doc: `$agentname </identifiers/$agentname>`
    * :doc: `$agent </identifiers/$agent>`
