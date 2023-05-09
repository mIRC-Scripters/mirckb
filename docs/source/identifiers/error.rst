$error
======

The $error identifier is used to catch errors in a script's execution. When an error occurs, mIRC looks for any goto point named :error and continues executing. $error is then filled with the current error, and can be used to determine what went wrong with the script.

Synopsis
--------

.. code:: text

    $error

Example
-------

See :doc:`/reseterror </commands/reseterror>`

Compatibility
-------------

.. compatibility:: 6.14

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/reseterror </commands/reseterror>`

