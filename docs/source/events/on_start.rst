On Start
========

The on start event triggers either when mIRC is started, or a script file is loaded, either through the scripts editor, or via the :doc:`$load </commands/load>` command. Only one on start event is allowed per script file.

Synopsis
--------

.. code:: text

    on <level>:START:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

Add a pre-typed command to connect to certain networks upon pressing enter to the editbox:

.. code:: text

    on *:START:{
      var %c $chr(124) server -m
      editbox -a //server irc.swiftirc.net %c irc.dal.net %c irc.efnet.org
    }

Create a Hash Tables - mIRC|hash table named ''ircpoints'' and load data from a file named ''ircpoints.hsh'' into the table if the file exists:

.. code:: text

    on *:START:{
      if (!$hget(ircpoints)) { hmake ircpoints }
      if ($file(ircpoints.hsh).longfn) { hload ircpoints $v1 }
    }

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on load </events/on_load>`
    * :doc:`on unload </events/on_unload>`
    * :doc:`on exit </events/on_exit>`
    * :doc:`/load </commands/load>`
