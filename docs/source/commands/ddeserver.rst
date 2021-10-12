/ddeserver
==========

The **/ddeserver** command turns mIRC's DDE Server on or off. You can also rename mIRC DDE server. The default mIRC DDE Server is enabled when mIRC first starts and assign itself the name 'mIRC' unless another application as already taken that name.

Synopsis
--------

.. code:: text

    /ddeserver [on [service name] | off]

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
    * - [on]
      - Turns the DDE Server on
    * - [service name]
      - Renames the DDE Servers
    * - [off]
      - Turns the DDE Server off

Example
-------

.. code:: text

    ;Turn on the DDE Server, name it \'mIRCServer\'
    /ddeserver on mIRCServer

will output:

.. code:: text

    * DDE Server is on (mIRCServer)

.. code:: text

    ;Turn off the DDE Server
    /ddeserver off

will output:

.. code:: text

    * DDE Server is off

Compatibility
-------------

Added: mIRC v3.9 (28 Dec 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dde </aliases/dde>`
    * :doc:`$isdde </aliases/isdde>`
    * :doc:`$ddename </aliases/ddename>`
    * :doc:`/dde <dde>`