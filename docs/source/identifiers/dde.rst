$dde
====

$dde returns the value returned by the specified service name, topic, and item, by sending an XTYP_REQUEST.

Synopsis
--------

.. code:: text

    $dde(name, topic, item, delay)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The service name
    * - topic
      - The topic name
    * - item
      - The item name (optional)
    * - delay
      - if specified mIRC will wait <delay> seconds for a reply before giving up, default is 1 second (optional)

Properties
----------

None

.. note:: If the value returned by $dde() is too long for mIRC to handle, $dde returns a value of plain text "$error".

Note2: $dde supports one of the old syntax for some identifiers, evaluating '$dde name topic item' works (use 0 if no item, seems to be required sometimes), there's even a -dN switch for the delay: <script>//echo -a $dde mirc server 0"</script>should return the $server value you are connected to.

Example
-------

.. code:: text

    //echo My other mIRC is $dde(mirc, connected) to $dde(mirc, server)

Compatibility
-------------

.. compatibility:: 3.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/dde </commands/dde>`
    * :doc:`/ddeserver </commands/ddeserver>`
    * :doc:`$ddename </identifiers/ddename>`

