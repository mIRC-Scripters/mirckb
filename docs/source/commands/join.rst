/join
=====

The /join command is used when you want to join a channel.

Synopsis
--------

.. code:: text

    /join [-inxmd] [#] [key]

 Note: All switches are optional.

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

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #channel
      - name of the channel
    * - [key]
      - channel key (password)

Examples
--------

Join channel

.. code:: text

    /join #mIRC

Join multiple channels

.. code:: text

    /join #mIRC,#help

Join channel minimized

.. code:: text

    /join -n #mIRC

Join channel with a key (password)

.. code:: text

    /join #mIRC password

Compatibility
-------------

.. compatibility:: 2.7a

See also
--------