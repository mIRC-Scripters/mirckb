/ctcps
======

The /ctcps command is used to turn processing of CTCP events on/off. With no parameters, this command will display whether or not CTCPs are on or off.

Synopsis
--------

.. code:: text

    /ctcps [on|off]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [on|off]
      - Turns CTCP events on/off 

Example
-------

.. code:: text

    ;Turn CTCPs off 
    /ctcps off

The above example will output:

.. code:: text

    * Ctcps are off

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/nick>`
    * :doc:`$remote </identifiers/remote>`
    * :doc:`/ctcp </commands/ctcp>`
    * :doc:`/ctcpreply </commands/ctcpreply>`
    * :doc:`/events </commands/events>`
    * :doc:`/remote </commands/remote>`
    * :doc:`/commands </commands/commands>`

