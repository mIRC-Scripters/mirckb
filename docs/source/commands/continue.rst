/continue
=========

The **/continue** command lets you jump to the beginning of the current loop - not to any other loops enclosing it.

Synopsis
--------

.. code:: text

    /continue

Switches
--------

None

Parameters
----------

None

Example
-------

.. code:: text

    Alias Example {
    var %a = 1
    ;count form 1 to 10
    while (%a <= 10) {
    ;echo -a %a
    inc %a
    ;if its odd, skip it
    if ($v1 !& 1) continue
    ;echo even number
    echo -a %a
    }
    }

Will generate the following output

.. code:: text

    2
    4
    6
    8
    10

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/break </commands/break>`
    * :doc: `/halt </commands/halt>`
    * :doc: `/if </commands/if>`
    * :doc: `/return </commands/return>`
    * :doc: `/while </commands/while>`
    * :doc: `/returnex </commands/returnex>`
