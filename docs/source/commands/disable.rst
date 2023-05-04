/disable
========

The **/disable** command disables the specified groups in all scripts. You can also specify a :doc:`wildcard </intermediate/matching_tools.html#wildcard>` to disable all matching groups.

Synopsis
--------

.. code:: text

    /disable <group1 group2 ... groupN>
    /disable <wilcard_expression>

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
      - a list with complete name of the groups to be disabled seperated by spaces
    * - <wildcard_expression>
      - a :doc:`wildcard </intermediate/matching_tools.html#wildcard>` expression, all matching groups are disabled

Example
-------

.. code:: text

    /disable #one #two #three
    or
    /disable #*o*

.. code:: text

    * Group(s) disabled

First example disables the three groups specified while the second would only disables the first two (#one and #two, assuming that's the only matching groups)

Compatibility
-------------

Added: mIRC v3.5 (13 Aug 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$group </identifiers/$group>`
    * :doc:`/enable </commands/enable>`
    * :doc:`/groups </commands/groups>`
