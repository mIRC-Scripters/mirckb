mIRC Installation
=================

There are multiple type of installations of mIRC that can be done.

There are two main installation types, the 'old', which is how mIRC used to install in the past, and the 'new', which is how mIRC is now installing.

Old type
--------

Before, and because windows itself wasn't really pushing mutli-user installation of program, mIRC used to place all the files in the same folder you selected. So mirc.ini mirc.exe, the help file, the scripts etc, everything was inside one main folder.

New type
--------

Then, multi-users was added in Windows and quickly, it was designed so that programs would be typically installed to 'Program files', which cannot be written to unless you have admin rights, while the different settings files would be placed in a different folder, which doesn't require admin rights. Not only this is more organized, from the OS's point of view, but it ensures program can run correctly without having to take care of write permissions.

Some people still prefer the old install type with all the files in the same folder, it is possible to get mIRC to do such an installation: if you place a mirc.ini file inside the folder you are installing to, the mIRC installer will do an old type installation.

.. note:: The same applies for mirc.exe once installed, if you run mirc.exe inside a folder with a mirc.ini file, it will use that file as mirc.ini and won't store settings in the appropriate location (%appdata%)

Portable
--------

A portable installation will make an old type installation and will prevent mIRC from storing information on the machine, to use mIRC from an usb stick for example. mIRC won't use the registry to store your license or information about the 30day trial as well as registering mIRC as the application to use for ``irc://`` url

Installing/Upgrading
--------------------

If you're starting with mIRC or don't want to do anything, just do a normal install, the new type, so just run the installer once you have downloaded it.

The default folder for installation should be something like C:\Program Files (x86)\, if you installed mIRC previously on the machine, it's possible for this value to be different.

If mIRC recognizes the folder as a mIRC folder, it will warn you and select the 'upgrade' option, which only update the .exe and the help file, basically.

Others options are "full", which is the default for a first installation, or "custom" where you can select which components to install.

Command line
------------

When executing mirc.exe to run mIRC, you can pass argument to the executable. This can be used to instruct mIRC to do something on start.

Switches
^^^^^^^^

The arguments have switches format:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s<server:port>
      - makes mIRC connect to the specified server and port on start, you can also specify a group name from the server list.
    * - -j<#chan,#chans> 
      - makes mIRC join the specified channel on connect
    * - -p<password> 
      - makes mIRC use that for the password parameter of JOIN message, to join channel protected by password
    * - -n<main,alternate> 
      - sets your main and alternate nickname
    * - -i<filename.ini> 
      - makes mIRC uses the specified file as the mirc.ini file, the remaining settings files are still stored to the same folder as before
    * - -r<path> 
      - sets the path where mIRC saves mirc.ini as well as others settings files, if no path is specified, the path used is the path where the mIRC executable is stored.
    * - -noreg 
      - makes mIRC avoid use of the registry, (no ``irc://`` link support among others things).
    * - -noconnect 
      - prevents mIRC from connecting on startup if that option is enabled in mIRC.
    * - -nowine 
      - disables Wine support in mIRC
    * - -portable 
      - this is a combination of -r with no path and -noreg

Parameters
^^^^^^^^^^

The installer also supports command line parameters:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - /S 
      - Silent install
    * - /FULL 
      - Force a full install
    * - /DESKTOP 
      - enables creation of shortcut on the desktop
    * - /NODESKTOP 
      - disables creation of shortcut on the desktop
    * - /STARTMENU 
      - enables creation of shortcut on the start menu
    * - /NOSTARTMENU 
      - disables creation of shortcut on the desktop

The installer had others commmand line options which are no longer applicable:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - -nouninst 
      - prevents mIRC from adding an uninstall item to the control panel add/remove dialog (mIRC now has an uninstall.exe in the folder)
    * - -services 
      - made mIRC run as a service on win 95/98 (mIRC no longer supports these OS)
