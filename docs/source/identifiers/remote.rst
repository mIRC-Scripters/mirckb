$remote
=======

$remote returns a bitwise integer indicating if ctcps/events/raws are enabled.

Synopsis
--------

.. code:: text

    $remote

The value are OR'ed together 1 | 2 | 4

0 is returned when remote are off, 7 when everything is enabled, see the example to check one of them manually.

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    if ($remote & 1) echo -a ctcps are enabled
    if ($remote & 2) echo -a events are enabled
    if ($remote & 4) echo -a raws are enabled

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/remote </commands/remote>`

