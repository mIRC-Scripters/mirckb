$msgtags
========

$msgtags returns the full @ prefixed tags line (IRCv3 message tags) which are removed from incoming server messages. $msgtags() returns informations about specifics tags

Synopsis
--------

.. code:: text

    $msgtags
    $msgtags(tag|N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - tag
      - returns the tag if it exists, $null otherwise
    * - N
      - returns the Nth tag, if N = 0, returns the total number of tags

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
If a parameter is provided, you can use the following properties:
    * - .tag
      - returns the name of the Nth tag
    * - .key
      - returns the associated value of the Nth tag or of the given tag

Example
-------

.. code:: text

    ON *:TEXT:*:#: { echo $chan INFO: $nick -> $msgtags(account) -> $msgtags(msgid).tag -> $msgtags(msgid).key - Total: $msgtags(0) }

Compatibility
-------------

.. compatibility:: 7.42

See also
--------

.. hlist::
    :columns: 4

