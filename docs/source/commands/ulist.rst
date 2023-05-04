/ulist
======

**/ulist** allows you to list the access levels of users based on a certain criteria.

Synopsis
--------

.. code:: text

    /ulist [<|>] <level>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - >
      - Display all users with access greater than or equal to the level parameter specified.
    * - <
      - Display all users with access less than or equal to the level parameter specified.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - This specifies the access level that you wish to list.

Examples
--------

**List all users with an access level lower than or equal to 10**

.. code:: text

    /ulist <10

This would result in something similar to the screenshot below:

[[File:User access list.png]]

**List users with access level greater than or equal to 5**

.. code:: text

    /ulist >5

**List users with access level equal to 3**

.. code:: text

    /ulist 3

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/auser </commands/auser>`
    * :doc: `/flush </commands/flush>`
    * :doc: `/guser </commands/guser>`
    * :doc: `/isuer </commands/iuser>`
    * :doc: `/ruser </commands/ruser>`
