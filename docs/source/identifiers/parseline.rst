$parseline
==========

$parseline return the line involved in the :doc:`on parseline </events/on_parseline>` event.

Synopsis
--------

.. code:: text

    $parseline

.. note:: For ``out`` lines, $parseline is terminated with a $LF character that is not visible when viewed in mIRC. You may wish to remove this with:

.. code:: text

    var %pl $parseline
    if ($asc($right(%pl,1)) == 10) %pl = $right(%pl,-1)

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:parseline:*:*:echo -a $parseline

Compatibility
-------------

.. compatibility:: 7.42

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/parseline </commands/parseline>`
    * :doc:`on parseline </events/on_parseline>`
    * :doc:`$parsetype </identifiers/parsetype>`

