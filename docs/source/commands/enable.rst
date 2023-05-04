/enable
=======

The **/enable** command enables the specified groups in all scripts. The command also accepts a :doc: `wildcard </intermediate/matching_tools.html#wildcard>` value which can be used to enable all matching groups.

Synopsis
--------

.. code:: text

    /enable <group1 group2 ... groupN>
    /enable <wildcard_expression>

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
    * - <group1 group2 ... groupN>
      - a list with the name of the groups to be enabled seperated by spaces
    * - <wildcard_expression
      - a :doc: `wildcard </intermediate/matching_tools.html#wildcard>` expression, all matching groups are disabled

Example
-------

.. code:: text

    /enable #one #two #three
    or
    /enable #*o*

.. code:: text

    * Group(s) enabled

First example enables the three groups specified while the second would only enables the first two (#one and #two, assuming that's the only matching groups)

Compatibility
-------------

Added: mIRC v3.5 (13 Aug 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$group </identifiers/$group>`
    * :doc: `/disable </commands/disable>`
    * :doc: `/groups </commands/groups>`
