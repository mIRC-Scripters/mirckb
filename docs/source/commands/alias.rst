/alias
======

The /alias command can be used to add, replace and remove aliases. This command ONLY works for single line aliases. By default mIRC will add the alias to the first aliases script file.

.. note:: Trying to remove a multi-line alias will result in a "unable to remove" error message.

Synopsis
--------

.. code:: text

    /alias -s [filename] <aliasname> [command]

Switches
--------

https://forums.mirc.com/ubbthreads.php/topics/246550/alias-runs-silently

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - shows the alias command being performed.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [filename]
      - Optional parameter that can be used to specify which aliases file to use, the file must be already loaded.
    * - <aliasname>
      - The name of the alias to use.
    * - [command]
      - If specified, the commands that are associated with the alias (you can specify multiple commands on one line by seperating them properly with :ref:`beginner-piping`), if not specified the alias is removed.

Example
-------

.. code:: text

    ;Adds a new alias by the name "cookies"
    ;You can now do /cookies
    /Alias /Cookies /me hands out the cookie jar 
    
    ;We replaced the old cookies alias with this new one
    /Alias /Cookies /me Steals someone's cookies!
    
    ;Remove the alias
    /Alias /Cookies

Output:

.. code:: text

    * Added '/Cookies' alias
    * Replaced '/Cookies' alias
    * Removed '/Cookies' alias

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$isalias </identifiers/isalias>`
    * :doc:`$alias </identifiers/alias>`
    * :doc:`$exists </identifiers/exists>`
    * :doc:`$file </identifiers/file>`
    * :doc:`/load </commands/load>`
    * :doc:`/save </commands/save>`
    * :doc:`/unload </commands/unload>`
    * :doc:`/add </commands/add>`

