$numeric
========

$numeric returns the numeric value for a raw event. If the raw event is not a number (like a CAP message), then $numeric returns 0,

Synopsis
--------

.. code:: text

    $numeric

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    raw *:*:echo -a $numeric

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

