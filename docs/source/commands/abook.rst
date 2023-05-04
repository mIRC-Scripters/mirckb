/abook
======

**/abook** is used to open the Address Book dialog window.

The nickname parameter can be used to open the address book to that specific user with the whois tab.

.. note:: The user must already exist in the address book for this option to work.

The various switches can be used to set the focus of specific tabs.

Synopsis
--------

.. code:: text

    /abook -w [nickname]
    /abook -chln

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -w
      - Open the whois tab
    * - -c
      - Open the control tab
    * - -h
      - Open the highlight tab
    * - -l
      - Open the colors tab
    * - -n
      - Open the notify tab

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nickname>
      - If -w is used to open the whois tab, this optional parameter can be used to specify which user from the address book to select. The user must already be in your address book.

Example
-------

.. code:: text

    ;Open the address book, highlight tab
    /abook -h
    ;Open the address book and show Ahnk's whois info
    /abook -w Ahnk

Compatibility
-------------

Added: mIRC v5.1 (11 Sep 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$abook </identifiers/$abook>`
    * :doc: `$cnick </identifiers/$cnick>`
    * :doc: `/cnick </commands/cnick>`
    * :doc: `/uwho </commands/uwho>`
