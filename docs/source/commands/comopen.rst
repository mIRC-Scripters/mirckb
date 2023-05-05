/comopen
========

The **/comopen** command opens a COM connection to specified programmatic identifier with the assigned name. Your script should check :doc:`$comerr </identifiers/comerr>` after opening the connection to make sure the connection was established successfully.

Synopsis
--------

.. code:: text

    /comopen <name> <progid>

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
    * - <name>
      - Connection name to be used
    * - <progid>
      - Programmatic Identifier

Example
-------

.. code:: text

    Alias Example {
    ;Create a WshShell object
    comopen Example wscript.shell

    ;Destroy object
    comclose Example
    }

.. code:: text

    ; see more documentation at: https://msdn.microsoft.com/en-us/library/system.windows.forms.sendkeys(v=vs.110).aspx
    ; and be careful about mIRC interpreting % & and other special characters
    //sendkeys {ESC}%o{END}{UP 2}%bText In mIRC Titlebar+{TAB}{ENTER}
    alias sendkeys {
    ; trying to create unique WshShell object
    var %name sendkeys $+ $ticks $+ $rand(111,9999)
    .comopen %name WScript.Shell
    if (!$comerr) {
    var %result $com(%name,SendKeys,3,bstr,$1-)
    ;Destroy object when finished with it
    .comclose %name
    return %result
    }
    return 0
    }

Compatibility
-------------

Added: mIRC v5.9 (15 Jun 2001)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$com </identifiers/com>`
    * :doc:`$comcall </identifiers/comcall>`
    * :doc:`$comval </identifiers/comval>`
    * :doc:`$comerr </identifiers/comerr>`
    * :doc:`/comclose </commands/comclose>`
    * :doc:`/comreg </commands/comreg>`
    * :doc:`/comlist </commands/comlist>`
