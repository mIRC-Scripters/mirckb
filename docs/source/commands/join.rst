/join
=====

The **/join** command is used when you want to join a channel.

Synopsis
--------

.. code:: text

    /join [-inxmd] [#] [key]

.. note:: All switches are optional.*

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -i
      - join the last channel you were invited to.
    * - -n
      - joins the channel minimized
    * - -x
      - joins the channel maximized
    * - -m
      - joins the channel in mdi state
    * - -d
      - joins the channel in desktop state.

Parameters
----------

* *#channel'' - name of the channel

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [key]
      - channel key (password)

Examples
--------

**Join channel**

.. code:: text

    /join #mIRC

**Join multiple channels**

.. code:: text

    /join #mIRC,#help

**Join channel minimized**

.. code:: text

    /join -n #mIRC

**Join channel with a key (password)**

.. code:: text

    /join #mIRC password

Compatibility
-------------

Added: mIRC v2.7a (18 Mar 1995)

See also
--------
