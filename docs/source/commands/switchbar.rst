/switchbar
==========

When used without any arguments, the /switchbar command displays the current state of the switchbar. The state is also displayed even if an argument is specified. You can prefix the command with a period to silent that behavior. The "on" and "off" arguments can be used to show and hide the switchbar programmatically. The switchbar is a toolbar with all the networks and channels on it displayed as buttons.

Synopsis
--------

.. code:: text

    /switchbar [on|off]

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
      - Either an 'on' or 'off' visibility option.

Example
-------

.. code:: text

    /switchbar on

Will turn the switchbar on and display

.. code:: text

    * Switchbar is on

Compatibility
-------------

.. compatibility:: 6.32

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$switchbar </identifiers/switchbar>`
    * :doc:`$menubar </identifiers/menubar>`
    * :doc:`$toolbar </identifiers/toolbar>`
    * :doc:`$treebar </identifiers/treebar>`
    * :doc:`/menubar </commands/menubar>`
    * :doc:`/titlebar </commands/titlebar>`
    * :doc:`/toolbar </commands/toolbar>`
    * :doc:`/treebar </commands/treebar>`

