$stripped
=========

$stripped returns the number of control codes that were stripped from an incoming message, if any, due to the settings in mIRC-options/IRC/Messages/"Strip codes from incoming messages". This can be used in any script event that triggers when a message is received from a user, including :doc:`on text </events/on_text>`, :doc:`on action </events/on_action>`, and ctcp events.

.. note:: It does NOT count control codes stripped by the :doc:`$strip </identifiers/strip>` identifier.

Synopsis
--------

.. code:: text

    $stripped

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:text:*:#:echo -a $stripped

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$strip </identifiers/strip>`

