$lock
=====

$lock returns $true or $false depending on the lock setting for the given item in the Lock dialog option.

Synopsis
--------

.. code:: text

    $lock(item|#chan|N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - item
      - See below for items
    * - N 
      - returns the Nth channel in the list of limited channels
    * - #chan 
      - returns the channel setting in the list of limited channels ($true if in the list)

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Item
      - Description
    * - startup
      - returns the setting for the 'ask for password: on startup' option
    * - sendmessage
      - returns the setting for the 'enable sendmessage server' option.
    * - dll
      - returns the setting for the 'disable: dll' option
    * - send
      - returns the setting for the 'disable: send' option
    * - get
      - returns the setting for the 'disable: get' option
    * - chat
      - returns the setting for the 'disable: chat' option
    * - query
      - returns the setting for the 'disable: query' option
    * - fserve
      - returns the setting for the 'disable: fserve' option 
    * - channels
      - returns the setting for the checkbox of the 'limits channels to' option, you can access the different channel using the Nth parameter.
    * - tray
      - returns the setting for the 'hide tray menu window list when locked' option
    * - tips
      - returns the setting for the 'hide tips when locked' option

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $lock(tray)

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

