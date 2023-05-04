/tnick
======

The **/tnick** command can be used to change own IRC nickname without changing the main or alternative nick ( :doc:`/anick </commands/anick>` ) options.

Synopsis
--------

.. code:: text

    /tnick <newName>

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
    * - <newName>
      - The temporary nickname.

Example
-------

.. code:: text

    alias away {
    ; change nick
    tnick $me $+ |away
    !away
    }

Compatibility
-------------

Added: mIRC vmIRC 6.0 ()

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/$nick>`
    * :doc:`$anick </identifiers/$anick>`
    * :doc:`/anick </commands/anick>`
