SendMessage
===========

The SendMessage() function can be used to communicate with mIRC from your external process (e.g. another program or a dll). mIRC provides a number of private Window Messages to evaluate or execute commands and identifiers.

Initializing communication
--------------------------

The external programs that send these messages must create a mapped file with the `CreateFileMapping() <http://msdn.microsoft.com/en-us/library/windows/desktop/aa366537%28v=vs.85%29.aspx>`__ function:

.. code:: c

	 CreateFileMapping(
	   _In_      HANDLE hFile,
	   _In_opt_  LPSECURITY_ATTRIBUTES lpAttributes,
	   _In_      DWORD flProtect,
	   _In_      DWORD dwMaximumSizeHigh,
	   _In_      DWORD dwMaximumSizeLow,
	   _In_opt_  LPCTSTR lpName
	 );

* Use INVALID_HANDLE_VALUE for the hFile parameter, which basically allows the sytem to handle the file for us.
* Use NULL for lpAttributes, for a default security.
* Use PAGE_READWRITE for flProtect, to be able to read and write from/to the file.
* Use 0 for dwMaximumSizeHigh and 4096 for dwMaximumSizeLow to indicate a file of that size

.. note:: The mapped file must be at least 4096 bytes.

* lpName is the name of the file, in previous version of mIRC, this parameter had to be "mIRC", you certainly can see the limitation with this, so it was extended, you can now specify a name of the form "mIRCN" where N is a number. You can also still use mIRC of course.

.. note:: To prevent simultaneous access to the mapped file, your code must check whether the mapped file exists or not before using it. If it exists, you should assume that it is in use by another program, and should try again later.

Communicating
-------------

After creating the mapped file, you need to write to that file the line mIRC will receive, see the examples to get an idea about how to write to that file.

Performing Commands
^^^^^^^^^^^^^^^^^^^

The following call to SendMessage() makes mIRC perform the commands that you specify:

.. note:: the 'command' is placed into the editbox and enter is pressed is the exact behavior, this can be used to send IRC messages by not prefixing the command with slashes, but you must prefix it with at least one slash then, if you want to execute a command.

.. code:: c
 
	SendMessage(mHwnd, WM_MCOMMAND, cMethod, cIndex)

* mHwnd - The handle of the main mIRC window, or the handle of a Channel, Query, etc. window.
* WM_MCOMMAND - Which should be defined as WM_USER + 200 
* cMethod - How mIRC should process the message, where:
	* 1 = As if typed in editbox (default). 
	* 2 = As if typed in editbox, send as plain text
	* 4 = Use flood protection if turned on, can be or'd with 1 or 2, and 8
	* 8 = Use unicode text. For backward compatibility reason, mIRC takes the data in the mapped file as ANSI by default, if you are willing to use unicode, you must use this. This can be or'd with 1 or 2, and 4.
* cIndex - If you created a mapped filename of the form "mIRCN", this is where you specify the N parameter to use, if cIndex is 0, the filename must be "mIRC".

This call returns 1 on success, 0 if it fails.

Evaluating Identifiers and Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following call to SendMessage() makes mIRC evaluate the contents of any line that you specify:

.. code:: c

	SendMessage(mHwnd, WM_MEVALUATE, cMethod, cIndex)

* mHwnd - The handle of the main mIRC window, or the handle of a Channel, Query, etc. window.
* WM_MEVALUATE - Should be defined as WM_USER + 201
* cMethod - How mIRC should process the message, where:
	* 8 = Use unicode text. For backward compatibility reason, mIRC takes the data in the mapped file as ANSI by default, if you are willing to use unicode, you must use this.
* cIndex - If you created a mapped filename of the form "mIRCN", this is where you specify the N parameter to use, if cIndex is 0, the filename must be "mIRC".

This call returns 1 on success, 0 if it fails.

Remote Event Context
--------------------

If during a remote event, such as on TEXT, your script calls a DLL which then uses SendMessage() to execute a command or evaluate an identifier, you can tell SendMessage() to execute in the context of that remote event.

During a remote event, a :doc:`$eventid </identifiers/eventid>` identifier is set to a unique value to identify the event. This can be passed to a DLL which can then pass it back to mIRC using:

.. code:: c

    SendMessage(mHwnd, WM_MCOMMAND, MAKEWPARAM(cMethod, cEventId), cIndex)

This will cause the command/evaluation to execute in the context of the remote event identified by cEventId. If cEventId is 0, this indicates a non-remote event.

Extended Version Information
----------------------------

If cMethod is set to -1, you can set cIndex to:
* -1 - to receive the mIRC version number.
* -2 - to receive the cMethod options that are supported.

Extended Error Information
--------------------------

If cMethod is or'd with the value 16, this will make SendMessage() return more useful error values instead of just 0 for failure and 1 for success. The return values are:
* 0 - Success.
* 1 - Failure, You can OR that value to get more specific errors:
** 2 - Bad mapped filename.
** 4 - Bad mapped file size.
** 8 - Bad eventid.
** 16 - Bad server.
** 32 - Bad script - means that the script does not exist
** 64 - Disabled (if disabled in lock dialog).

1 alone means that a script error occured, 16 and 32 can only happen if you use $eventid in SendMessage() in the context of a remote event but the script from which it was called no longer exist.

Examples
--------

.. code:: c

	#include <stdio.h>
	#include <windows.h>
	#define WM_MCOMMAND WM_USER + 200
	#define WM_MEVALUATE WM_USER + 201
	HANDLE file;
	LPSTR str;

	int main(int argc, char * argv[])
	{
		char* command = "//echo -a Hello world";
		char* evaluation = "m $+ $upper(irc)";
		file = CreateFileMapping(INVALID_HANDLE_VALUE, NULL, PAGE_READWRITE, 0, 4096, L"mIRC");
		if (file == NULL)
			exit(0);
		str = (LPSTR)MapViewOfFile(file, FILE_MAP_ALL_ACCESS, 0, 0, 0);
		if (str == NULL)
			exit(0);
		HWND mhwnd = (HWND)atoi(argv[1]);
		//send //echo -s Hello world to mIRC
		strcpy_s(str, 4096, command);
		SendMessage(mhwnd, WM_MCOMMAND, 1, 0);
		//Ask mIRC to evaluate and send back the result
		strcpy_s(str, 4096, evaluation);
		SendMessage(mhwnd, WM_MEVALUATE, 0, 0);
		printf("%s", str);
	}

You must pass the handle of the main mIRC window or a valid channel, query etc window as the first parameter of the program in the command line for it to work.
