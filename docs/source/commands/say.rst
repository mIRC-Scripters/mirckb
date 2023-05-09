/say
====

The /say command sends a message to the active window which can be a channel or a query.  The say command can only be used within events that can be triggered directly by you (i.e. on input, on tabcomp, on hotlink, etc...). To send a message from any event, use the :doc:`/msg </commands/msg>` command.

Synopsis
--------

.. code:: text

    /say <message>

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <message>
      - The actual message to be sent

Example
-------

Compatibility
-------------

.. compatibility:: n/a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$active </identifiers/active>`
    * :doc:`/ame </commands/ame>`
    * :doc:`/amsg </commands/amsg>`
    * :doc:`/describe </commands/describe>`
    * :doc:`/me </commands/me>`
    * :doc:`/msg </commands/msg>`

