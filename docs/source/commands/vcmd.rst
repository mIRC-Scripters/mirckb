/vcmd
=====

The **/vcmd** allows you to enable your voice commands list, for your Speech Recognition Software, within mIRC.

Synopsis
--------

.. code:: text

    /vcmd -lcar <on | off | sleep>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -l
      - Lists all of the commands in the voice commands list.
    * - -c
      - Clears all of the commands from the voice commands list.
    * - -a
      - Does the same as :doc: `/vcadd </commands/vcadd>`
    * - -r
      - Does the same as :doc: `/vcrem </commands/vcrem>`

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - on
      - Turns voice command listening on.
    * - off
      - Turns voice command listening off.
    * - sleep
      - Temporarily disables voice command listening.

Example
-------

**Disable voice command listening**

.. code:: text

    /vcmd off

**Clear the voice commands list**

.. code:: text

    /vcmd -c

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/vcadd </commands/vcadd>`
    * :doc: `/vcrem </commands/vcrem>`
    * :doc: `$vcmd </identifiers/$vcmd>`
    * :doc: `$vcmdver </identifiers/$vcmdver>`
    * :doc: `$vcmdstat </identifiers/$vcmdstat>`
    * :doc: `ON VCMD Event </events/On_vcmd>`
