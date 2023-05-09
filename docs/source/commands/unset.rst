/unset
======

The /unset command removes any variables by their specified names. If a :ref:`matching_tools-wildcard` pattern was specified, all variables matching that pattern will be removed. The /unset command can be used to remove both local and global variables, however it can only remove one of them per name. Local variables take precedence over a global variable with the same name.

.. note:: /unset has an evaluation issue with dynamic variables, you can read more Variables - mIRC#Special_behaviors_&_quirks|here

Synopsis
--------

.. code:: text

    /unset [-slg] <%var> [%var2 [%var3...]]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Display an output showing the variables that are unset*
    * - -g
      - Make sure the global variable is unset if you have both a global and local variable of the same name
    * - -l
      - Make sure the local variable is unset if you have both a global and local variable of the same name

Parameters
----------

None

Example
-------

The most basic usage is to unset a specific variable:

.. code:: text

    /unset %foobar

Local variables take precedence over a global variable with the same name.

.. code:: text

    alias global_local {
      set %foo 1
      var %foo 2
      echo -a %foo
      unset %foo
      echo -a %foo
      unset %foo
    }

Which will produce the following result:

.. code:: text

    2
    1

/unset can only remove a local or global variable per each name specified, however it’s possible to remove both by specifying the variable name twice, for example:

.. code:: text

    alias global_local2 {
      set %foo 1
      var %foo 2
        
      ; unset both at once
      unset %foo %foo
      
      ; will print empty quotes
      echo -a $qt(%foo)
    }

Which will print empty quotes:

.. code:: text

    ""

No evaluation brackets are needed when unsetting dynamic variables:

.. code:: text

    alias dynamic_vars {
      var -s %foo. $+ $calc(1+2) Test
      var -s %bar. $+ $calc(1+3) Test
    
      unset -s %foo. $+ $calc(1+2) %bar. $+ $calc(1+3)
    }

Which will produce the following results:

.. code:: text

    * Set %foo.3 to Test
    -
    * Set %bar.4 to Test
    -
    * Unset %foo.3
    -
    * Unset %bar.4

if multiple cleaning 

.. code:: text

    /unset %semple,%foo,%cocorico,%mirc,%ms
    
     

.. code:: text

    alias unset {
      tokenize 44 $1-
      !.unset $*
    }
     

Compatibility
-------------

.. compatibility:: 4.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$var </identifiers/var>`
    * :doc:`/dec </commands/dec>`
    * :doc:`/inc </commands/inc>`
    * :doc:`/set </commands/set>`
    * :doc:`/unsetall </commands/unsetall>`
    * :doc:`/var </commands/var>`

