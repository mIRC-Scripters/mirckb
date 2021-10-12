/creq
=====

**/creq** allows you to modify the mIRC DCC Chat options in the command-line, without having to open the mIRC options dialog.

Synopsis
--------

.. code:: text 

    /creq [+m|-m] [ask | auto | ignore]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - +m
      - Enable automatic minimizing of DCC Chat requests when they are initiated.
    * - -m
      - Disable automatic minimizing of DCC Chat requests when they are initiated.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - ask
      - Makes sure you get a notification on all incoming DCC Chat requests. You can either accept or decline each DCC Send.
    * - auto
      - Automatically accepts incoming DCC Chat Requests.
    * - ignore
      - This parameter enables the ability to ignore all incoming DCC Chat requests.

Examples
--------

Enable automatic minimizing of DCC Chats:

.. code:: text

    /creq +m

Set DCC Chats to automatically accept:

.. code:: text

    /creq auto

Compatibility
-------------

Added: mIRC v3.8 (25 Nov 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/sreq <sreq>`
    * :doc:`$creq </aliases/creq>`
    * :doc:`$sreq </aliases/sreq>`