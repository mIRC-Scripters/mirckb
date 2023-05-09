$disk
=====

$disk returns informations about hard disks.

Synopsis
--------

.. code:: text

    $disk(N/path)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth hard disks available, if N = 0, returns the total available drives
    * - path
      - a drive name

Without a property, returns $true if drive exists, otherwise $false

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - type
      - returns the type of drive; values are ''fixed'', ''removable'', ''cdrom'', ''ramdisk'', ''remote'', and ''unknown''.
    * - free
      - returns the number of free space on drive in bytes
    * - label
      - returns the name/label of the drive, if any
    * - size
      - returns the total size of the drive
    * - unc
      - returns the path for a network drive.
    * - path
      - returns the path of the drive

Example
-------

.. code:: text

    //echo -a $disk(0)

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

