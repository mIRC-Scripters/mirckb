$fupdate
========

$fupdate returns the current integer 0-100 setting for the /fupdate command

Synopsis
--------

.. code:: text

    $fupdate

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    ; save current /fupdate setting, then display mirc.ini to status window, then restore previously existing setting:
    //var -s %a fupdate $fupdate | fupdate 99 | filter -fs mirc.ini * | fupdate %fupdate

.. note:: The /fupdate setting always reverts to default 0 each time mIRC restarts, so it must be reset each time using an ON START or perform-on-connect command

Error Messages
--------------

None
Compatibility
-------------

.. compatibility:: 7.65

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/fupdate </commands/fupdate>`
