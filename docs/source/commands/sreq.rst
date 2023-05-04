/sreq
=====

**/sreq** allows you to modify the mIRC DCC Send options on the fly, without having to open the mIRC options dialog.

Synopsis
--------

.. code:: text

    /sreq [+m|-m] [ask | auto | ignore]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - +m
      - Enable automatic minimizing of DCC Sends when they are initiated.
    * - -m
      - Disable automatic minimizing of DCC Sends when they are initiated.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - ask
      - Makes sure you get a notification on all incoming DCC Sends. You can either accept or decline each DCC Send.
    * - auto
      - Automatically accepts incoming DCC Sends.
    * - ignore
      - This parameter enables the ability to ignore all incoming DCC Sends.

Examples
--------

**Enable automatic minimizing of DCC Sends**

.. code:: text

    /sreq +m

**Set DCC Sends to automatically accept**

.. code:: text

    /sreq auto

Compatibility
-------------

Added: mIRC v3.8 (25 Nov 1995)

See Also
--------

.. hlist::
    :columns: 4

    * :doc:`/creq </commands/creq>`
    * :doc:`$creq </identifiers/$creq>`
    * :doc:`$sreq </identifiers/$sreq>`
