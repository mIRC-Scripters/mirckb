/ctcps
======

The **/ctcps** command is used to turn processing of CTCP events on/off. With no parameters, this command will display whether or not CTCPs are on or off.

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

Added: mIRC v5.1 (28 Aug 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </aliases/nick>`
    * :doc:`$remote </aliases/remote>`
    * :doc:`/ctcp <ctcp>`
    * :doc:`/ctcpreply <ctcpreply>`
    * :doc:`/events <events>`
    * :doc:`/remote <remote>`
    * :doc:`/commands <commands>`