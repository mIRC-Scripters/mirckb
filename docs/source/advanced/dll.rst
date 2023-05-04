DLL
===

mIRC allows programs to make calls to various **dynamic-link libraries** (**DLL**'s) designed to work with mIRC. The main reason you would want to do this is that processing information in a DLL can be far faster than doing so in a mIRC script, so for intensive data processing a DLL would be more efficient.

.. note:: mIRC also supports calling :doc:`COM </advanced/com>` objects, for calling non-standard DLLs.

Using a Dll
-----------

Synopsis
^^^^^^^^

.. code:: text

	/dll <filename> <procname> [data]

	/dll -u <filename>

	$dll(<filename>, <procname>, [data])

	$dllcall(<filename>, <alias>, <procname>, [data])

Switches
^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switches
      - Description
    * - -u
      - Unloads the dll

Parameters
^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - The filename for the dll you wish to use.
    * - <procname>
      - The case-sensitive name of the function/procedure you wish to call.
    * - [data] 
      - The optional parameters for the function/procedure, used by the procname as input and as return =2 command or =3 return string.
    * - <alias>
      - If you use :doc:`$dllcall </identifiers/dllcall>`, it calls the function asynchronously, meaning that the code won't stop processing until the dll function finishes, $dllcall won't return a value. Instead, mIRC calls the specified <alias> when the function finishes.

Creating a Dll
--------------

.. note:: We won't deal with how to create a dll in details, the scripter here must be familiar with dll creation already.

Because mIRC wasn't unicode before, the exported functions used to be the following function prototype:

.. code:: c

	int __stdcall funcName(HWND mWnd, HWND aWnd, char *data, char *parms, BOOL show, BOOL nopause);</source>

With mIRC being unicode, the new prototype is:

.. code:: c

	int __stdcall funcName(HWND mWnd, HWND aWnd, TCHAR *data, TCHAR *parms, BOOL show, BOOL nopause);</source>

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - Parameter
      - Description
    * - mWnd 
      - The handle of the main mIRC window.
    * - aWnd
      - The handle of the window in which the command is being issued, this might not be the currently active window if the command is being called by a remote script.
    * - data 
      - This is a buffer you can write to if you want mIRC to perform a command or to return a value from a {{mIRC|$dll}} call (remember that {{mIRC|$dllcall}} do not return a value by design even if you fill this buffer)
    * - parms 
      - For a better handling of command execution, this is a buffer which can be filled if you are filling the 'data' buffer with a command. mIRC will fill the variable $1- with this value, which you can include in the command in 'data'. The examples shows how to use it.
    * - show 
      - This Bool value is FALSE if a dot '.' has been used to make the command (/.dll) quiet.
    * - nopause
      - This Bool value is TRUE if mIRC is in a critical routine, meaning that you must not stop the processing in mIRC (long while loop for example).


If you call a non unicode dll with mIRC being unicode, mIRC must call the prototype with a char * and will convert its utf16 to utf8, and whenever this happens in mIRC, the data is chopped at $maxlenl+100 bytes.

Both 'data' and 'params' are allocated with a number of bytes that is close to ($maxlenl+100)*2+N where N is 100 or a bit more, and this is true both unicode and non unicode mode. This effectively mean that you can write that many bytes into the buffer yourself in both mode.

These functions must use the stdcall calling convention. (This is also the standard calling convention for all other Microsoft Win32 API functions.)

Note on C++ Dll and stdcall
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are making a C++ dll, you need to use the extern "C" directive on all the function that you want to export (all the function called from mIRC including the LoadDll and UnloadDll routine), which indicates the function has "C" linkage as opposed to "C++".

The interesting difference is that C linkage does not use "mangling" when exporting your function, an operation which rename your functions with additional information to help the linking process.

.. code:: c

	extern "C" int __stdcall funcName(HWND mWnd, HWND aWnd, char *data, char *parms, BOOL show, BOOL nopause);</source>

However, the __stdcall standard convention implies a mangling operation which extern "C" does not override.

To solve this problem, most of the linker will allow you to provide a .def file, where you can define the real name of your exported functions

Creating a file for that can be annoying, on Visual Studio you can use a #pragma directive to do that on the fly, the examples illustrate this

.. note:: If you use GCC Gnu to compile, it has something similar to ``__stdcall``, ``__attribute__((stdcall))``.

Return value
^^^^^^^^^^^^

The function returns an integer, this value indicates what mIRC should do:

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - 0 
      - Means that mIRC should /halt processing.
    * - 1 
      - Means that mIRC should continue processing without returning the contents of the DATA buffer.
    * - 2 
      - Means that you have filled the 'data' variable with a command which mIRC should perform, you can also fill the "parms" variable with the parameters to use, if any.
    * - 3 
      - Means that the DLL has filled the data variable with the result that $dll() as an identifier should return.

.. note: This only applies when using $dll or /dll.

Keeping a Dll loaded
^^^^^^^^^^^^^^^^^^^^

In the past, by default, a DLL used to be unloaded immediately after you made the /dll or $dll()/$dllcall call.

You had to use the function below, called by mIRC when it loads your dll, and set mKeep to True to keep the dll loaded (mKeep defaulted to False)

Things changed since it's typically more useful to keep the dll loaded, now mIRC keeps the dll loaded by default with mKeep defaulting to True, and you can set it to False to unload the dll.

.. code:: c

	void __stdcall LoadDll(LOADINFO*);

	typedef struct {
	   DWORD  mVersion;
	   HWND   mHwnd;
	   BOOL   mKeep;
	   BOOL   mUnicode;
	   DWORD  mBeta;
	   DWORD  mBytes;
	 } LOADINFO;

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - mVersion
      - Contains the mIRC version number in the low and high words. i.e. version 7.55 fills this with 0x00370007
    * - mHwnd
      - Contains the window handle to the main mIRC window.
    * - mKeep
      - Is set to TRUE by default, indicating that mIRC will keep the DLL loaded after the call. You can set mKeep to FALSE to make mIRC unload the DLL after the call
    * - mUnicode
      - If set to true, indicates that the dll is using unicode as opposed to ansi (default). This means the data passed from/to the dll is in UTF16 (see above with TCHAR type instad of CHAR). If set to false, mIRC will convert utf16 to utf8 to comply with the CHAR type prototype of the function
    * - mBeta
      - contains the mIRC $beta version number, for public betas.
    * - mBytes
      - as of v7.64 contains the max safe byte length that can be placed into the 'data' and 'parms' buffers. This is always the double of the line length limit even when converting to utf8 with non unicode dll.

Unloading the Dll
^^^^^^^^^^^^^^^^^

mIRC will automatically unload a DLL if it is not used for ten minutes, or when mIRC exits.

You can define an UnloadDll() routine in your DLL which mIRC will call when unloading a DLL to allow it to clean up:

.. code:: c

	int __stdcall UnloadDll(int mTimeout);

The mTimeout value can be:

.. list-table::
    :widths: 15 85
    :header-rows: 0

    * - 0
      - UnloadDll() is being called due to a DLL being unloaded with /dll -u.
    * - 1 
      - UnloadDll() is being called due to a DLL not being used for ten minutes. You can return return 0 to keep the DLL loaded, or 1 to allow it to be unloaded.
    * - 2
      - UnloadDll() is being called due to a DLL being unloaded when mIRC exits.

Examples
--------

Example 1 : Using Visual studio (C++)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example use a non-unicode project. We don't use a .def file but a #pragma comment to export functions.

We use the LoadDll and UnloadDll routine to start/stop a communication with mIRC using SendMessage().

.. code:: c

	#include <cstdio>
	#include <windows.h>
	#define WM_MCOMMAND WM_USER + 200
	#define WM_MEVALUATE WM_USER + 201

	//__stdcall cause mangling of the form _yourfunctionname@N where N is the number of bytes for all the parameters
	//we use #pragma to redefine the name of the exported functions, if we don't do that, you can still call the dll using the name "_youfunctionname@24" ;)
	//the prototype of our function always takes 6 parameters, each taking 4 bytes 6*4=24
	//the prototype for LoadDll and UnloadDll takes one parameter, a structure which is 4 bytes
	#pragma comment(linker, "/EXPORT:usingSM=_usingSM@24")
	#pragma comment(linker, "/EXPORT:LoadDll=_LoadDll@4")
	#pragma comment(linker, "/EXPORT:UnloadDll=_UnloadDll@4")
	#pragma comment(linker, "/EXPORT:simple_example=_simple_example@24")
	#pragma comment(linker, "/EXPORT:average_example=_average_example@24")
	#pragma comment(linker, "/EXPORT:more_example=_more_example@24")
	#pragma comment(linker, "/EXPORT:from_event=_from_event@24")

	HANDLE file;
	LPSTR str;

	extern "C" int __stdcall simple_example(HWND mWnd, HWND aWnd, CHAR *data, char *parms, BOOL show, BOOL nopause)
	{
	        //we fill data with a simple string we want to return
		strcpy(data,"simple string");
		//we return 3 indicating $dll should return the value we copied in 'data'
		return 3;
	}

	extern "C" int __stdcall average_example(HWND mWnd, HWND aWnd, CHAR *data, char *parms, BOOL show, BOOL nopause)
	{
	        //we fill data with a command we want mirc to execute
		strcpy(data,"/echo -a Ã¨");
		//we return 2 indicating mIRC should execute the command in 'data'.
		return 2;
	}

	extern "C" int __stdcall more_example(HWND mWnd, HWND aWnd, CHAR *data, char *parms, BOOL show, BOOL nopause)
	{
	        //we fill data with a command we want mirc to execute
		strcpy(data,"/echo -a $1-");
	       	strcpy(parms,"test");
		//we return 2 indicating mIRC should execute the command in 'data', and set $1- to parms.
		return 2;
	}

	extern "C" int __stdcall from_event(HWND mWnd, HWND aWnd, CHAR *data, char *parms, BOOL show, BOOL nopause)
	{

	        strcpy(str,"$nick");
		SendMessage(mWnd, WM_MEVALUATE, MAKEWPARAM(0, atoi(data)), 0);
	        strcpy(data,str);
		return 3;
	}

	extern "C" int __stdcall usingSM(HWND mWnd, HWND aWnd, CHAR *data, char *parms, BOOL show, BOOL nopause)
	{
		//send //echo -s Hello world to mIRC
		strcpy(str,"//echo -a Hello world");
		SendMessage(mWnd, WM_MCOMMAND, 1 , 0);
		//Ask mIRC to evaluate and send back the result
		strcpy(str,"m $+ $upper(irc)");
		SendMessage(mWnd, WM_MEVALUATE, 0, 0);
		//Copy the result of "m $+ $upper(irc)" into data and we return 3 indicating $dll returns what 'data' contains
		strcpy(data,str);
		return 3;
	}

	 typedef struct {
	   DWORD  mVersion;
	   HWND   mHwnd;
	   BOOL   mKeep;
	   BOOL   mUnicode;
	   DWORD  mBeta;
	   DWORD  mBytes;
	 } LOADINFO;

	extern "C" void __stdcall LoadDll(LOADINFO *load) {
		file = CreateFileMapping(INVALID_HANDLE_VALUE,NULL,PAGE_READWRITE,0,4096, "mIRC");
		str = (LPSTR) MapViewOfFile(file, FILE_MAP_ALL_ACCESS, 0, 0, 0);
		//after MapViewOfFile(), 'str' is where you write to but also is the result of each call with WM_MEVALUATE:
	 }

	extern "C" int __stdcall  UnloadDll(int mTimeout) {
		//if dll is unloaded because mIRC exit or dll -u is used, we clean up, otherwise we prevent the unloading by returning 0.
		if (mTimeout != 1) 
	        {
	        UnmapViewOfFile(str);
	        CloseHandle(file);
	        }
		return 0;
	}

Use $dll(yourdll.dll,simple_example,) which will return "simple string".

Use $dll(yourdll.dll,average_example,) or '/dll yourdll.dll average_example', this will execute "/echo -a è" in mIRC 7.x, because the project is not unicode, the two bytes Ã¨ are sent as ascii, mIRC 7.x will correctly decode that as utf8. On mIRC 6.x (you would need to remove the mUnicode to mBytes variable in the LOADINFO structure), this would display the two bytes.

If you set the mUnicode variable to TRUE on mIRC 7.x in the LoadDll function and if you set your project to use unicode (in visual studio: project properties > configuration properties > general > character set), this would correctly show the two bytes as well.

Use $dll(yourdll.dll,more_example,) or '/dll yourdll.dll more_example' ;this will fill $1- from data with the value from parms and execute the final "//echo -a test".

Use $dll(yourdll.dll,from_event,$eventid) inside an event where $nick exists, this will use SendMessage() to evaluate $nick from the event context and fill data with that value, returned by $dll.

Use $dll(yourdll.dll,usingSM,) which will use SendMessage() to execute a command in mIRC, it will also evaluate a line of code and return the result in $dll().

Example 2 : Using GNU GCC on Windows (C)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

	//To compile, use:
	//gcc -c -O3 reverse.c ; gcc -shared --export-all-symbols -o reverse.dll -O3 reverse.o
	//reverse.c content:
	#include <windows.h>
	#include <string.h>
	  
	int __attribute__((stdcall))
	reverse(HWND mWnd, HWND aWnd, char *data, char *parms, BOOL show, BOOL nopause)
	{
	      char *l = *data ? data + strlen(data) - 1 : data;
	      char *p = parms;
	      while ((*p++ = *l--));
	      strcpy(data, "/echo -s ");
	      strcat(data+8, parms);
	      return 2;
	}

Use /dll reverse.dll reverse <text>.