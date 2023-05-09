$beta
=====

$beta returns if running a beta version, returns the beta portion of the version number. Otherwise returns $null string.

Synopsis
--------

.. code:: text

    $beta

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //echo -a version is $version $+ $iif($beta,. $+ $beta)

When someone on forum is having trouble with their mIRC acting incorrectly, it's often part of the info string they're requested to paste in reply. The $beta identifier does exist even when it returns the $null string, because otherwise enabling "identifier warning" would generate an error message.

.. code:: text

    //echo -a $os $version $beta $md5($mircexe,2) $file($mircexe).sig $alias(0) $script(0) $dll(0) $com(0)

Compatibility
-------------

Only returns a value in beta versions

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$version </identifiers/version>`

