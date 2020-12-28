Data Storage
============

Binary Variables
----------------

Binary variables are a special storage offered by mIRC that can hold an array of bytes of arbitrary length.

Overview
~~~~~~~~

mIRC's binary &variables are distinguished from its text %variables by beginning with the & ampersand symbol, while text variables begin with the % percent symbol. They differ from text variables in content, scope, duration, and length.

-  They are composed of byte values, which can be any of the values 0-255. Among other differences, they can contain the $chr(0) value, which text variables cannot.
-  Their scope is similar to that of local identifiers such as $nick and $rawmsg. They exist as long as scripting engine is running, then are deleted.
-  Binary variables are not saved to the variables file (default name is vars.ini) the way global %variables are saved. To preserve them, you must either write them to a disk file, save to a hashtable item, or use $encode to save them to a %variable or hashtable.
-  While text variables are limited in length by the 4150 line length, binary variable length is limited by available memory.
-  mIRC does not interpret the content of your binary variable, while it does for simple %variable. By default a %variable cannot be set to the value "" (just two double quotes characters), this is because in core variable routines, it is interpreted as empty string, as though it supported quoted string. Note that since mIRC 7.52, /var and /set support a -p switch which preserves the data: "" are now allowed (except put directly in the variables section of the script editor for backward compat reason) but spaces are also completely preserved, without -p /var and /set will omit a single trailing space (but two or more are ok!). Of course $bvar(&binvar,,).text is decoding the content of your binary variable from utf8, which is reinterpreting the bytes, but that's good.

Some uses for Binary Variables include:

-  Holding content which can't be placed into text %variables
-  Holding content too long to be placed in text variables
-  Displaying duplicate spaces or non-printable characters like TAB which cannot be seen in echoed strings.

/Commands and $Identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few commands and identifiers created specifically to manipulate binary variables:

+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Name                                                                                | Description                                                                       |
+=====================================================================================+===================================================================================+
| /bset                                                                               | Create or modify binary variables.                                                |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| /bcopy                                                                              | Create or modify by copying byte values between/within binary variables.          |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| /breplace                                                                           | simple search/replace of all occurrences of a byte value with another.            |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| /btrunc                                                                             | Truncate a disk file at a specific filesize regardless of content or line ending. |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| /bunset                                                                             | Unset a binary variable prior to end of the script/event.                         |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| /bread                                                                              | Read file contents into a binary variable                                         |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| /bwrite                                                                             | Write binary variable to a disk file                                              |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| $bfind                                                                              | Search binary variable for pattern of 1-or-more byte values.                      |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| $bvar                                                                               | Display contents of binary variables as text or a series of decimal numbers       |
+-------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

+----------------------------------+----------------------------------+
| Name                             | Description                      |
+==================================+==================================+
|  /parseline                      | Can use a binary variable as     |
|                                  | input or output                  |
+----------------------------------+----------------------------------+
| $cb                              | can output a line or entire      |
|                                  | clipboard to a binary variable.  |
+----------------------------------+----------------------------------+
| $encode                          | Can use a binary variable as     |
|                                  | input+output                     |
+----------------------------------+----------------------------------+
| $decode                          | Can use a binary variable as     |
|                                  | input+output                     |
+----------------------------------+----------------------------------+
| $regsub                          | Can use a binary variable as     |
|                                  | output                           |
+----------------------------------+----------------------------------+
| $regsubex                        | Can use a binary variable as     |
|                                  | output                           |
+----------------------------------+----------------------------------+
| $compress                        | Can use a binary variable as     |
|                                  | input+output.                    |
+----------------------------------+----------------------------------+
| $decompress                      | Can use a binary variable as     |
|                                  | input+output.                    |
+----------------------------------+----------------------------------+
| /hadd                            | Can save a binary variable into  |
|                                  | a hash table item                |
+----------------------------------+----------------------------------+
| $hget                            | Can use a binary variable as     |
|                                  | output                           |
+----------------------------------+----------------------------------+
| /hsave                           | Can save a hash table to a       |
|                                  | binary file                      |
+----------------------------------+----------------------------------+
| /hload                           | Can load a binary file to a hash |
|                                  | table                            |
+----------------------------------+----------------------------------+
| $crc                             | Can use a binary variable as     |
|                                  | input                            |
+----------------------------------+----------------------------------+
| $md5                             | Can use a binary variable as     |
|                                  | input                            |
+----------------------------------+----------------------------------+
| $sha1                            | Can use a binary variable as     |
|                                  | input                            |
+----------------------------------+----------------------------------+
| $sha256                          | Can use a binary variable as     |
|                                  | input                            |
+----------------------------------+----------------------------------+
| $sha384                          | Can use a binary variable as     |
|                                  | input                            |
+----------------------------------+----------------------------------+
| $sha512                          | Can use a binary variable as     |
|                                  | input                            |
+----------------------------------+----------------------------------+
| $hmac                            | Can use a binary variable as     |
|                                  | input                            |
+----------------------------------+----------------------------------+
| $com                             | Can use a binary variable as     |
|                                  | input or output.                 |
+----------------------------------+----------------------------------+
| /sockudp                         | Can write a binary variable to a |
|                                  | socket                           |
+----------------------------------+----------------------------------+
| /sockwrite                       | Can write a binary variable to a |
|                                  | socket                           |
+----------------------------------+----------------------------------+
| /sockread                        | Can read from a socket into a    |
|                                  | binary variable                  |
+----------------------------------+----------------------------------+
| /fwri                            | Can write a binary variable to a |
|                                  | disk file                        |
+----------------------------------+----------------------------------+
| $fread                           | Can read disk file contents into |
|                                  | a binary variable                |
+----------------------------------+----------------------------------+

Position and Length
~~~~~~~~~~~~~~~~~~~

Position in binary variables is 1-based, where the first byte value in a binary variable is position 1. This is different than the position used by /bread and /bwrite to read/write binary variables to disk files, where file position 0 is the position for reading/writing the first byte of the file.

If a binary variable has length N, position N is the last byte of the variable. Because appending to a binary variable requires calculating and writing to position N+1, several of the binary commands allow using position -1 to append to a variable. Also, instead of using $bvar to find the length of a variable, some of them also allow -1 in the length parameter for writing the entire variable.

Unicode
~~~~~~~

Writing unicode characters to binary variables using the -t switch causes the length of the binary variable to be longer than the length of the text string written to them. Unicode characters 128-2047 add 2 bytes to a binary variable and 2048-65535 add 3 each. When adding text to a variable you can use -ta instead of -t to avoid encoding Unicode characters 128-255 as 2 bytes, but only if the text value being added contains no Unicode characters greater than 255.

.. code:: text

   //bset -t &var1 1 $chr(  233) | echo -a shows length is 2 -> $bvar(&var1,0)
   //bset -t &var2 1 $chr(10004) | echo -a shows length is 3 -> $bvar(&var2,0)
   //bset -ta &var3 1 $chr(  233) | echo -a shows length is 1 -> $bvar(&var3,0)
   //bset -ta &var4 1 $chr(10004) | echo -a shows length is 3 -> $bvar(&var4,0)
   //bset -ta &var5 1 $chr(233) $+ $chr(10004) | echo -a shows length is 2+3=5 -> $bvar(&var5,0)

.. note:: If you add $chr(233) and $chr(10004) as 2 separate -ta commands, you can add character 233 as 1 byte and add 10004 as 3 bytes. In that case the 10004 does not cause the 233 to be encoded as 2 bytes because the strings were added separately:

.. code:: text

   //bset -ta &var5 1 $chr(233) | bset -ta &var5 -1 $chr(10004) | echo -a shows length is 4 -> $bvar(&var5,1-)

Creating Binary Variables Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Binary variables can be created using one of the /commands or $identifiers which accept a binary variable as an output parameter, or by the /bset, /bcopy, and /bwrite commands created for that purpose.

.. code:: text

   Set &binvar to 99 byte value 0 followed by byte value 255 at position 100:
   //bset -c &binvar 100 255 | echo -a &bvar(&binvar,1-)
   Set &binvar to text contents of %variable
   //bset -tc &binvar 1 %variable | echo -a &bvar(&binvar,1-).text
   Create or append entire contents of &binvar to &var2
   //bcopy -1 &var2 1 &binvar -1
   Read entire contents of versions.txt into &versions
   //bread versions.txt 0 $file(versions.txt).size &versions  | echo -a &bvar(&binvar,0)
   Set &binvar to contents of channel message
   ON *:Text:*:#: { noop $regsubex(,$parms,,,&binvar) }
   Set &binvar to contents of clipboard
   //clipboard $+(abc,$crlf,def) | noop $cb(-1,,&binvar) | echo -a $bvar(&binvar,1-)
   Read from socket to &binvar
   on *:SOCKREAD:socket: { sockread 4096 &binsockread }

Modifying Binary Variables Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: text

   Replace all TAB characters with spaces:
   /breplace &binvar 9 32
   Compress contents of &versions
   //bread versions.txt 0 $file(versions.txt).size &versions | noop $compress(&versions,b) | echo -a $bvar(&versions,0)
   encrypt and encode contents of &versions
   //noop $encode(&versions,bcm,password)

Modifying Existing Binary Variables
'''''''''''''''''''''''''''''''''''

Binary variables are different than text variables in how you add values to them, and what happens when you add shorter content to an existing variable with longer content. If you add 3 bytes to position 1 of a binary variable with length of 5, the 3 added bytes replace the 3 bytes in those positions, and the values in positions 4-5 remain unless you use the -c switch:

.. code:: text

   //bset -t &var 1 1234567890 | bset -t &var 1 test | echo -a shows content is test567890 -> $bvar(&var,1-)

The above example could be a string even longer than 10 if &var previously contained a strong longer than 10. If the 1st command used -tc instead of -t, the variable content is chopped beyond the 10 bytes being added. If the 2nd command used -tc instead of -t, the content beyond the 4 bytes being added is chopped.

If you bset values into a variable at position 10, the first 9 positions are undefined, depending whether the variable already existed. If the variable already existed with length 4, the bytes at positions 5-9 are filled with value 0 (not text 0 which is byte value 48). If the variable did not yet exist, bytes at positions 1-9 are filled with value 0.

Binary Variables as Input Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: text

   display $sha1 hash of contents of &versions
   //echo -a $sha1(&versions,1)
   write &versions to disk
   //bwrite -c test.dat 0 -1 &versions

'local' Binary Variables
~~~~~~~~~~~~~~~~~~~~~~~~

When using %variables within an alias, you can take advantage of their 'local' scope to safely re-use variable names without worrying about destroying variables used by other scripts or aliases. You can use "/var %a value" in an alias to set that local variable without worrying that you will destroy that same variable name being used by the alias which called your alias, and don't need to worry if your script calls another alias which also uses that same name as a local variable.

However the scope of binary variables means they exist in all aliases called by each other or in the event which triggered their usage. To avoid aliases damaging the contents of each other's binary variables, if an alias needs to create binary variables, and is designed to be called by other aliases which might also be using binary variables, you must defend against destroying the binary variables used by the caller. Two ways to do this are:

-  Require the caller send the name of the variable as a parameter when calling your alias
-  Create a unique variable name to make it unlikely that another alias would use the same name for a binary variable. Pass binary variable name to alias, display $bvar output in hex instead of decimal:

.. code:: text

   //echo -a $BvarAsHex(&binvar)
   alias BvarAsHex { return $regsubex($bvar($1,1-1000),/(\d*)/g,$base(\1,10,16,2)) }

Create unique name to avoid destroying existing variable:

.. code:: text

   //var %a $(myalias,$ticks,$ctime) | bset -t & $+ %a 1 test | echo -a $bvar(& $+ %a ,1-).text

See Variables in the Guide for more details on creating dynamic variable names.

.. note:: If your temporary variable is no longer needed and is lengthy, you may wish to use /bunset to reduce memory usage if you are also creating other lengthy binary variables during that script execution. Otherwise, it will be deleted when the script execution ends.

Saving Binary Variables
~~~~~~~~~~~~~~~~~~~~~~~

Because binary variables disappear as soon as your script execution ends, if you need to use your binary variable later, you will need to find a way to save it:

write to a disk file:

.. code:: text

   //bwrite -c save.dat 0 1 &binvar

store in hash table:

.. code:: text

   /hadd -smb binvar_save binvar &binvar

.. note:: Hash tables aren't saved to disk, so you need to save that table to disk: ``/hsave -sb binvar_save savebins.dat`` … and then reload the binary variable the next time you re-start mIRC: ``/hload -sb binvar_save savebins.dat``

Use $encode to translate binary data to text, which can be saved to variables or written to disk.

.. code:: text

   //noop $encode(&binvar,bm) | set %binvar_save $bvar(&binvar,1-).text

.. note:: $encode translates 3 input bytes (binary or text) into 4 text characters, so you shouldn't try to use this method on binary variables longer than approximately 3000 bytes. Retrieve binary content from text %variable: ``//bset -t &binvar 1 %binvar_save | noop $decode(&binvar,bm)``

INI Files
---------

An initialization file (also known as INI file) is a plain text file with a distinct structure that allows for more convenient and organized data storage. An initialization file is convenient and permanent storage space, however it relatively slow compared to window buffers and Hash Tables. If speed is needed, a hash table is a much superior choice.

File Structure
~~~~~~~~~~~~~~

An ini file is composed of names, values, sections, and comments.

Property
~~~~~~~~

A property is the basic item that makes up the ini file. An equal sign delimiter separates the name from the value (name being on the left of the equal sign). Every name has a value associated with it.

.. code:: text

   item   = value
   item2  = value 2

Section
^^^^^^^

Sections Parameters are grouped together into a section. The name of the section is placed on a line of its own (enclosed by a pair of square brackets). All parameters after the section are automatically associated with that section.

.. code:: ini

   [section]
   item = value

Storing Information
~~~~~~~~~~~~~~~~~~~

mIRC offers a number of convenient commands and identifiers to read/write from/to an ini file.

Writing To An Ini File
^^^^^^^^^^^^^^^^^^^^^^

The writeini command can be used to write an item (and its value) in a specific section of the ini file.

.. code:: text

   /writeini [-n] <inifile> <section> <item> <value>

The -n switch no longer exists on mIRC 7.x and newer. On older mIRCs: The -n switch is used when the file exceeds 65,536 bytes (64 KB). It's a good idea to place it there if you think the file will get pretty big in the future.

For example:

.. code:: text

   writeini reminder.ini birthday jenna 2/28/1983
   writeini reminder.ini birthday Mike 10/10/1990

Will create the following file:

.. code:: ini

   [birthday]
   jenna  = 2/28/1983
   Mike   = 10/10/1990

You can easily see the actual ini file using the following command:

.. code:: text

   //run notepad.exe reminder.ini

Reading From An Ini File
^^^^^^^^^^^^^^^^^^^^^^^^

Reading a property from an INI file is pretty simple:

.. code:: text

   $readini(filename[, np], section, item)

The n switch is used when you do not want to evaluate the line. (This is especially helpful when you let the users save setting on your bot, you need to always think the worse of the users and how they might exploit your scripts)

The p switch is used to make mIRC evaluate pipes \| as is instead of plain text.

For example (using the file we created in the previous example):

.. code:: text

   echo -a Mike: $readini(reminder.ini, n, birthday, mike)
   echo -a Jenna: $readini(reminder.ini, n, birthday, jenna)

Will output:

.. code:: text

   Mike: 10/10/1990
   Jenna: 2/28/1983

Security Consideration
^^^^^^^^^^^^^^^^^^^^^^

ALWAYS use the 'n' switch unless you have a very good reason to not use it!

Deleting Items And Sections
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The remini can be used to delete an item or an entire section from an ini file:

.. code:: text

   ;remove an item
   /remini <inifile> <section> <item>
   ;remove an entire section
   /remini <inifile> <section>

For example:

.. code:: text

   /remini reminder.ini birthday mike

will remove mike's entry from the ini file.

Text Files
----------

Plain text files are files you can edit via a basic editor like notepad and has no special structure. Below are a few handy commands and identifiers to work with plain text files.

File Info
~~~~~~~~~

To determine if a file exists we can use the $isfile() identifier.

.. code:: text

   $isfile(file.txt)

In many cases you'd want to check the number of lines in the file. $lines() will help you there.

.. code:: text

   $lines(file.txt)

Reading From A Text File
~~~~~~~~~~~~~~~~~~~~~~~~

The $read() identifier is a very powerful command that can be used to read from a text file in a variety of ways.

n Switch
^^^^^^^^

By default, $read will evaluate the text it reads as if it was mSL code. To prevent this behavior you must use the n switch. Throughout this article we will ALWAYS use that switch. Improper use of the $read() identifier without the 'n' switch could leave your script highly vulnerable.

Reading A Random Line
^^^^^^^^^^^^^^^^^^^^^

The most basic functionality $read() offers is the ability to read a random line from a particular file. The syntax is:

.. code:: text

   ; read a random line from file.txt
   $read(file.txt, n)

Reading A Specific Line
^^^^^^^^^^^^^^^^^^^^^^^

To read a specific line from a file you can specify the line number as the third argument.

.. code:: text

   $read(file.txt, n, line)

Searching The File
^^^^^^^^^^^^^^^^^^

$read() offers three methods for searching a file:

-  Scanner
-  Wildcard Pattern
-  Regular Expression Pattern

Scanner
'''''''

The scanner is the most primitive search of the three. It will go through each line comparing the pattern provided to the first part of the line. If a match is found, mIRC will return the text that followed the pattern.

Consider the following abbr.txt:

.. code:: text

   lol laughing out loud
   lmao Laughing my ass off
   btw by the way
   brb be right back

We can use the following alias to get the abbreviation we are looking for.

.. code:: text

   alias abbr return $read(abbr.txt, ns, $1)

Executing the following code:

.. code:: text

   //echo -a $abbr(lol)
   //echo -a $abbr(brb)

Will produce the following output:

.. code:: text

   laughing out loud
   be right back

Wildcard And RegEx Patterns
'''''''''''''''''''''''''''

Both the wildcard pattern matching and the regex pattern matching works by searching for the first matching line and returning the entire line. It follows the same syntax as the scanner:

.. code:: text

   ; A wildcard pattern match:
   $read(file.txt, nw, *wildmatch*)

.. code:: text

   ; A regex pattern match:
   $read(file.txt, nr, /pattern/)

Starting Line
'''''''''''''

If you specify a line number after the pattern, that line will be used as the first line to start searching from.

For Example:

.. code:: text

   ; Start searching from line 400:
   $read(file.txt, nw, *hello*, 400)

Iterating Over Matches
~~~~~~~~~~~~~~~~~~~~~~

$readn is an identifier that returns the line that $read() matched. We can use that to start searching for our pattern on the next line.

For example, to search all the line containing the word 'test' in a file, we can construct a loop like this:

.. code:: text

   //while ($read(file.txt, nw, *test*, $calc($readn + 1))) echo -a $v1

In the code above, $readn starts at 0. We use $calc() to start at line 1. Every match $read() will start searching on the next line. When no more matches are after the line specified $read will return $null - terminating the loop.

Writing To A Plain Text File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The /write command can be used to manipulate a text file in a variety of ways.

Appending A Line
^^^^^^^^^^^^^^^^

/write's simplest operation is the append operation. By default, /write will write a text line to the end of the file.

.. code:: text

   /write text.txt <string>

Inserting A Line
^^^^^^^^^^^^^^^^

To insert text at specific line we have the following syntax:

.. code:: text

   /write -il<line> file.txt <text>

For example, the following line will write "Hello There!" at line 2.

.. code:: text

   /write -il2 file.txt Hello There!

Deleting A Line
^^^^^^^^^^^^^^^

The /write command provides the ability to delete a specific line from a file.

.. code:: text

   ; Delete line <line> from a file:
   /write -dl<line> file.txt

Clearing A File
~~~~~~~~~~~~~~~

The -c switch on /write can be combined to clear the file before writing to it.

.. code:: text

   ; clear the file
   /write -c file.txt

Deleting A File
~~~~~~~~~~~~~~~

The delete a file, you can use the /remove command:

.. code:: text

   /remove file.txt
   ; send to the recycle bin
   /remove -b file.txt

File Handling
-------------

File Handling allows you to manipulate files on disk using seperate, simple operations. This allows for efficiency.

To understand how it works, you must be familiar with text file operations such as /write and $read.

/fopen
~~~~~~

.. code:: text

   /fopen [-nox] <name> <filename>

/fopen opens the filename and use the specified name to reference it.

The command fail by default if the file does not exist, the -n switch creates the file if it does not exist, but fails if it exists. The -o switch creates a new file if it does not exist but overwrites the file if it exists. The -x switch opens the file for exclusive access, others processus cannot access that file

.. note:: If /fopen fails, it does not halt processing, you must check $ferr to see if an error occured, see below.

After you opened a file with /fopen, you have a pointer of the content of the file, it starts at 0. This pointer is the starting position to read/write from.

/fseek
~~~~~~

.. code:: text

   /fseek -lnwr <name> <position>

/fseek sets the read/write pointer to the specified <position> in the file, unless you use a switch:

-  -l - sets the pointer to the beginning of the Nth line, use <position> to specify the Nth line
-  -n - sets the pointer to the beginning of the next line (from the current position of the read/write pointer), this does not take a parameter
-  -w - sets the pointer to the beginning of the line matching the wildcard expression, use <position> to specify the wildcard expression
-  -r - sets the pointer to the beginning of the line matching the regular expression, use <position> to specify the regular expression

If /fseek fails, it sets the pointer to the end of the file, you must check $fopen().eof or $feof to know if /fseek failed.

/fwrite
~~~~~~~

.. code:: text

   /fwrite [-bn] <name> <text | &binvar>

/fwrite allows you to write to the file at the current pointer position, -b specify a binary variable, -n adds a $crlf at the end of the line.

/fclose
~~~~~~~

.. code:: text

   /fclose <name | wildcard>

/fclose closes all the matching name (wildcard expression allowed)

/flist
~~~~~~

/flist just lists all the current handles.

$fopen(name \| N)
~~~~~~~~~~~~~~~~~

$fopen Returns the name of that handle if it exists, or the Nth handle.

Properties:

-  .fname - returns the complete filename opened for that handle
-  .pos - returns the current position of the read/write pointer
-  .eof - returns $true if the end of the file has been reached
-  .err - returns $true if an error occured on the file In a script, $ferr = $fopen(handle).err and $feof = $fopen(handle).eof, always returns the state of last involved handle in a file handing command.

.. note:: Since file access errors will not halt a script, the eof and err properties or identifiers must be checked after each file access command.

$fread(name \| N)
~~~~~~~~~~~~~~~~~

This form of $fread returns the next $crlf delimited line, useful to read line by line

$fread(name \| N, M, &binvar)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This form of $fread returns the number of bytes read (from the file pointed by name or the Nth handle) into the specified binary variable, where M is the number of bytes to read.

$fgetc(name \| N)
~~~~~~~~~~~~~~~~~

$fgetc returns the next character.

When To Use File Handling
~~~~~~~~~~~~~~~~~~~~~~~~~

It important to know when to use explicit file handling, and when you can use /write and $read.

Let's take a look at /write, /write is a powerful tool which allows you to write to a file according to severals predefined options.

A simple "/write filename.txt line" involves the following file handling operations:

-  /fopen - opens the file
-  /fseek - goes to the end of the file
-  /fwrite - writes to the file
-  /fclose - closes the file So, executing /write twice involves 8 file handling operations; the more you have to write, the more operations you create. If you do /write three times, the 12 operations can be reduced to 5:

.. code:: text

   ; assuming text.txt is empty
   write test.txt line 1
   write test.txt line 2
   write test.txt line 3

   ; is better written as
   fopen test test.txt
   fwrite -n line 1
   fwrite -n line 2
   fwrite -n line 3
   fclose test

The same thing applies to reading, $read opens the file, try to match and close the file, so any consecutive call to $read means the file is opened/closed each time. If you are looking for a particular line, you can avoid multiple $read calls by searching with /fseek.

Whenever you are going to use /write or $read in a loop to write/read a lot of things, if the loop isn't small and if the file isn't small, it might get slow very quickly, and you should consider using file handling.

Hash Tables
-----------

A hash table is an associative array with item-data pairing. That is, data stored in the table is associated with a specific item. Logically speaking, a basic table would like something like this:

===== =====
Item  Data
===== =====
Item1 Data1
Item2 Data2
Item3 Data3
===== =====

mIRC provides facilities for manipulating the table and the values in a variety of ways.

General Details
~~~~~~~~~~~~~~~

Hash tables, unlike INI files, are stored completely in memory and are never written to disk (unless the /hsave command is used), making them much faster when it comes to storing and retrieving information. The performance gain is much more obvious with a large amount of item/data pairs.

.. note:: Because hash tables are only in memory, it must be saved to a disk file using /hsave if mIRC needs to have the hashtable in memory after an exit then restart. You can reload the table from a file after mIRC restarts.

Creating A Table
~~~~~~~~~~~~~~~~

A hash table must be created before you can work with it. This also applies to loading a hash table from a file. To create a table you need to use the /hmake command. The syntax is:

.. code:: text

   hmake <table_name>
   hmake <table_name> <buckets>
   ;hmake also have an -s switch which prints debug info

If you don't specify the number of buckets (or "slots"), the default is used, which is 101. If you do specify the number of buckets from 1-10000, for any number greater than 1 which is not prime, mIRC increases the number of buckets to be the next greater prime from 3-10007. Which is why the default 100 uses 101 bucket. Assuming that you are going to look up a specific item by name using $hget, then generally speaking the number of buckets should be decided based on the following equation:

.. code:: text

   buckets = number of items that will be used / 0.78

For example: a table with 101 buckets is optimal for 79 items. For 1000 items, 1282 buckets is best (which mIRC increases to the prime 1283).

.. note:: The maximum valid number for the buckets parameter is 10000, which mIRC increases to the next available prime number, 10007.

Or to put this another way, the optimum number of buckets is 1.282x the number of items you are going to store in the hash table.

.. note:: See the notes at the bottom of the page for explanation why it can be helpful for buckets to be greater than the number of items in the table.

Adding Items
~~~~~~~~~~~~

The /hadd command is used to add an item/data pair to the table. The syntax is:

.. code:: text

   hadd <table_name> <item> <data>
   or
   hadd -b <table_name> <item> <&bvar>
   An item can be added to the table with null data:
   hadd <table_name> <item>
   If it's possible the table is not yet created, use the -m switch, which creates the table if it doesn't exist
   hadd -m <table_name> <item>

Let's consider a table of favorite colors:

.. code:: text

   /hadd -sm100 colors Mary Green
   /hadd -s colors John Blue
   /hadd -s colors Lisa Red
   /hadd -s colors Gary Orange

The -s switch is needed to "show" the action, otherwise these commands are silent. The code above will produce the following result:

.. code:: text

   * Made hash table 'colors' (101)
   * Added item 'Mary' to hash table 'colors'
   * Added item 'John' to hash table 'colors'
   * Added item 'Lisa' to hash table 'colors'
   * Added item 'Gary' to hash table 'colors'

**"Colors" Hash Table**

==== ======
Item Data
==== ======
Mary Green
John Blue
Lisa Red
Gary Orange
==== ======

If you add an item name which already exists in the table, the new data replaces the existing item's data.

.. code:: text

   /hadd Colors Gary Yellow

This updates the Colors table, changing the item 'Gary' to contain the data 'Yellow' instead of 'Orange'.

Value Retrieval
~~~~~~~~~~~~~~~

To get a data value associated with a given item we will use the $hget identifier which has the following syntax:

.. code:: text

   $hget(<table_name>, <item>)

For example, if we were to check what is Mary's favorite color from our table; we will use the following piece of code:

.. code:: text

   //echo -a Mary's favorite color is $hget(colors, Mary)
   ;Mary's favorite color is Green

The $hget identifier can also be used to check if a table exists using the following syntax:

.. code:: text

   $hget(<table_name>)
   ; returns $null if the table does not exist

.. attention:: If the table does exist, returns N for the Nth existing table

.. note:: If $hget(colors) returns 2 indicating colors is the 2nd table, deleting the 1st table causes this command to return 1.

Iterating Over a Hash Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The $hget identifier can be used to iterate over the hash table. The syntax is:

.. code:: text

   ; Total Number of items in the table:
   $hget(<table_name>, 0).item
   ; Get the Nth Item
   $hget(<table_name>, <Nth>).item
   ; Get the value associated with the Nth Item
   $hget(<table_name>, <Nth>).data

.. note:: Iterating over a hash table like this is an inefficient way to retrieve values and items. See the explanation below for why mIRC will iterate over the hash table for every $hget - so the time required per lookup will increase linearly with the table size and the time for the script to iterate over the entire hash table will be proportional to the square of the table size. If it is possible to do so, then it's best to get a value using its item name.

An example of looping over every value in our Colors table will look like this:

.. code:: text

   Alias print_fav_colors {
     var %i = 1
     echo Colors Table:
     ; iterate over each item
     while ($hget(Colors, %i).item) {
       ; print the item/value pair
       echo -a %i $+ ) $v1 => $hget(Colors, $v1)
       inc %i
     }
   }

The execution of the alias (/print_fav_colors) will produce the following result:

.. code:: text

   Colors Table:
   1) Lisa => Red
   2) Mary => Green
   3) Gary => Yellow
   4) John => Blue
   (Gary shows Yellow instead of Orange because it was changed above)

This listing is almost always not in the same order they're added, because items are first listed according to the bucket they are placed into, before items within the bucket are listed. This is the listing order for v7.53, while the order in v7.52 is 1)Gary 2)Mary 3) Lisa 4) John. The listing order can also change if you change the number of 'buckets' within the same mIRC version, and the order of any items assigned to the same bucket can also be affected by the order in which those items are added or whether items in that bucket were deleted or added. Therefore, you should not depend on Mary being listed before Gary. More details in a later Technical section.

Deleting Items
~~~~~~~~~~~~~~

To delete pairs from the table, you need to use the /hdel command. Its syntax is:

.. code:: text

   hdel <table_name> <item>
   hdel -w <table_name> <wild_item>
   ;hdel has a -s switch which is the same as /hadd's

If the -w switch is used, a wildcard pattern for the item can be specified to delete multiple items at once. If we go back to our example:

.. code:: text

   /hdel -s colors Lisa

Will leave our table looking like this:

**"Colors" Hash Table**

==== ======
Item Data
==== ======
Mary Green
John Blue
Gary Orange
==== ======

But we can add Lisa again:

.. code:: text

   /hadd -s colors Lisa Red

If you repeat the /print_fav_colors list of items again, Lisa returns to her original position in the iterating list because her item name was assigned to a lower bucket number than the other names.

Saving/Loading Hash Table To/From File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because a hash table is stored exclusively in memory, it is important to save it to a file if one wishes to keep its content after a reboot or shut down. If a hash table is not stored in a file before mIRC closes, it will be gone for good.

mIRC offers the /hsave and /hload commands to handle the saving and loading of hash tables from your hard disk.

The syntax for the /hsave command is:

.. code:: text

   /hsave <table_name> <filename>
   ; The -s switch shows debug information
   ; The -a switch will append to an existing file, instead of the default overwriting
   ; The -i switch will create an ini file
   ; The -n switch saves the file containing only the data and not the item names.
   ; The -u switch avoids skipping temporary items created with /hadd's -uN switch.
   ; The -b switch will treat the file as a binary file, making it possible to save things like carriage returns and line feeds. It can save tables which do not contain any items containing binary data longer than 65535 bytes.
   ; The -B switch is the same as the -b switch, except it stores item/data pairs in a binary format which supports items having data length up to 4294967295 bytes.

If we wanted to save our little colors table to an INI file, we could use the following piece of code.:

.. code:: text

   /hsave -i Colors colors.ini
   ;colors.ini will have:
   ;  [hashtable]
   ;  Lisa=Red
   ;  Mary=Green
   ;  Gary=Orange
   ;  John=Blue

The /hsave command always overwrites any existing file unless you use the -a append switch.

To load a hash table we use the following syntax:

.. code:: text

   ; NOTE: The table must exists. I.e. you must have called /hmake first, or use the -m switch.
   /hload <table_name> <filename>
   ; The -s switch shows debug information
   ; The -i switch will read from an ini file containing lines of item=data
   ; The -n switch interprets the file as if it were /hsave'ed with the -n switch to contain only data, assigning item names as sequential integers beginning with 1.
   ; The -m[N] switch creates the hashtable if it does not already exist, optionally giving it N buckets different than the default 100 buckets.
   ; The -b switch will treat the file as a binary file in the format created by the /hsave -b switch.
   ; The -B switch will treat the file as a binary file in the format created by the /hsave -B switch.

To load the table we've just saved we would use the following code:

.. code:: text

   /hload -i Colors colors.ini

If you /hload a saved file into a hashtable, it behaves the same way that /hadd does. It creates item names that do not yet exist, and updates the data values of any item names which already exist.

Deleting A Table
~~~~~~~~~~~~~~~~

To complete destroy a table and all its values, you can use the hfree command:

.. code:: text

   /hfree <table_name>
   /hfree -w <*wild*table*>
   ;hfree has a -s switch which shows the action taken, as the other hashtable commands have

With the -w switch you can specify a wildcard pattern. All matching tables will be freed. If you already deleted a table and try to delete it again, "hfree tablename" halts your script. You must either use $hget(tablename) to verify the table's existence, or use -w without a wildcard. "hfree -w tablename_without_wildcards"

Searching For A Item And Value Pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The $hfind identifier can be used to search the table for a particular pair.

.. code:: text

   ; The Nth Item name that matches the wildcard pattern
   $hfind(<table_name>, <pattern>, <Nth>, w)
   ; The Nth Item that matches the RegExp pattern
   $hfind(<table_name>, <pattern>, <Nth>, r)
   ; The Nth Item that wildcard matches the text
   $hfind(<table_name>, <text>, <Nth>, W)
   ; The Nth Item that RegExp matches the text
   $hfind(<table_name>, <text>, <Nth>, R)
   ; $hfind(...).data will search the data instead of the item name.

If you specify 0 for Nth Item, the total number of matches will be returned instead. An example from our Colors table would be:

.. code:: text

   //echo -a $hfind(Colors, *ary*, 1, w)

Which will return "Mary". because Mary appeared before Gary in the iteration list of items. Prior to v7.53 it returned "Gary" because that name appeared first in the iteration list.

.. note:: Using a non-hashed method for finding an item or data using $hfind is an inefficient way to retrieve values and items. See the explanation below for why mIRC will iterate over the hash table for every $hfind - so time required per lookup will increase linearly with the table size. If it is possible to do so, then it's best to get a value using $hget using its item name.

.. note:: Use of $hfind to find the specific records that you want is, however, still likely to result in much better performance than iterating over the hash table using $hget(table,n) because mIRC can execute the single $hfind using compiled code rather than executing the large number of mSL statements needed to loop over the hash table using $hget.

Technical Explanation
~~~~~~~~~~~~~~~~~~~~~

mIRC's hash tables are implemented as follows.

1. When you create a hash table, it is created with a defined number of "slots" (or "buckets").
2. When you add an item to the table using /hadd, a hash algorithm calculates a bucket number based on the item name. Each bucket holds a linked-list of items whose names map to that bucket number, with each new item being added to the list of items in that bucket.
3. When you look up an item by name using $hget, then the same hash algorithm is used to locate the bucket it will be stored under and then the linked-list in that bucket is searched sequentially for the item. The purpose of hashing is to perform this kind of lookup on potentially large tables with faster performance. If a table has 101 buckets each containing 10 items, it is much faster to search within the 10 items than to search within all 1010 items.
4. When you get an item by position using $hget(table,position), or use $hfind to search data or search using wildcards or regular expressions, then the hash algorithm cannot be used to identify the correct bucket, and instead mIRC has to iterate across part or all of the hash table to count or to find the record you want.

If your hash table has a small number of buckets compared to the number of item records, then each bucket will have a large number of item records:

-  For a lookup of an existing item, on average mIRC will have to iterate over 50% of the bucket entries before locating the one you want
-  If you try to find a non-existent item, mIRC will need to iterate over the whole bucket list before determining that the item doesn't exist.

As you might imagine, mIRC iterating over a large number of hash table entries to find the item needed is CPU intensive and mIRC might start to feel unresponsive.

So for look-ups by item name, the best performance will be achieved when mIRC's hashing algorithm points to a bucket with a single table entry (or failing that - a small number of entries). Worst case scenario is if your hash table has only a single bucket, then all entries are stored in a single linked-list and every look-up needs to be iterated. On the other hand, if you have a large number of bucket (much greater than the number of items in the hash table), then the likelihood is that every item will be stored in its own bucket, so the hash function will take you to a bucket with a single entry, and no iteration will be needed to find the item. 101 buckets was recommended for 79 items because it's unlikely that picking 79 random numbers in the range 1-79 would have each number chosen only 1 time, but choosing 79 random numbers in the range 1-101 is much less likely that any number would be chosen more than 1 time.

All that said, even with a large number of buckets, you cannot guarantee that every item in the table will have a unique hash / bucket number. As an analogy, consider a class of 30 students. What is the probability that all students have birthdays on different days of the year? This is equivalent to asking whether a hash table with 365 buckets and 30 entries will have every entry using a different bucket. It turns out that in a class of 30 students there is significantly more than 50% probability that at least two students will share a birthday - indeed it only takes 23 students for the probability to be more than 50%. This seems weird - but for the mathematically inclined, the probability can be calculated by determining what the probability is that M students have all different birthdays:

The first student can have any birthday. The second student can have 364 of 365 days and still be different. The third student can have 363 of 365 days and still be different.

So the probability that M students all have different birthdays is therefore:

:math:`\frac{364}{365}*\frac{363}{365}*\frac{362}{365} ... \frac{\text{365-M+1}}{365}=\frac{(365-1)(365-2)...(365-M+1)}{365^{(M-1)}}=\frac{365!}{(365-M)! * 365^M}`

Returning to hash tables and buckets, the equivalent formula for a table with M entries and N buckets is:

:math:`\frac{(N-1)(N-2)...(N-M+1)}{N^{(M-1)}}=\frac{N!}{(N-M)! * N^M}`

Using the student birthday example for simplicity and relating it to hash tables and buckets, if we turn it on its head then we can say that if we have a hash table holding 23 entries, and we want to have a probability that each entry has its own bucket > 50%, then we need to have more than 365 buckets. **I bet you weren't expecting that!!** Fortunately the performance overhead of iterating over a relatively short linked-list is also small, and equally fortunately a bucket only uses 4-bytes (which is very small indeed compared to the size of a table entry, which consists of the item name and the data and the overhead of storing these and linking them into a list). Indeed mIRC's maximum bucket size is 10,007, requiring c. 40KB of memory - which in today's PCs with several GB of memory is relatively small.

**Summary:** If you are doing any lookups by item name on a frequent basis on a large table, then you should use the largest sensible bucket size to avoid mIRC iterating over long linked-lists when doing these lookups.

**HOWEVER…**

Not all hash table look-ups are able to use the hash to calculate the correct bucket - only look-ups by item name. If you want to access hash table entries by position using $hget(table,n), or if you want to use $hfind, then mIRC is going to have to iterate over a significant proportion (or all) of a hash table regardless of the number of buckets that you define. Indeed, if you are never going to look-up by item-name, you might as well save memory and use a single bucket.

**Summary:** If you are doing only lookup by position or are using $hfind, then you should use a bucket size of 1 to save memory and avoid the small overhead of iterating over empty buckets.

Finally, if you have a large hash table (perhaps several thousand records) that you want to search flexibly, then you might wish to consider whether something like mIRC SQLlite might suit your needs better.

Hash Algorithm
~~~~~~~~~~~~~~

This section describes the iteration sort order for hash tables. The algorithm used to sort tables has changed for v7.53, and will probably change in the future. Items are sorted into buckets differently in v6.35, then changed somewhere prior to v7.52. It changed again for v7.53, and there were probably different algorithms at other times in the past.

.. code:: text

   alias bucket_sort {
     hfree -sw table? | var %buckets 1 , %i 0 , %size 20
     hmake -s table1 %buckets | hmake -s table2 %buckets | hmake -s table3 %buckets
     while (%i < %size) { inc %i | hadd table1 item $+ %i }
     hadd table1 Suzy
     hadd table1 Kate
     hsave -s table1 test1.txt | hload -s table2 test1.txt
     hsave -s table2 test2.txt | hload -s table3 test2.txt
     var %j 0 | while (%j < $hget(table1,0).item) {
       inc %j
       echo -a $ord(%j) item in table1: $hget(table1,%j).item table2: $hget(table2,%j).item table3: $hget(table3,%j).item $iif($hget(table1,%j).item != $hget(table3,%j).item, *1vs3 diff*)
     }
     run notepad test1.txt | run notepad test2.txt
   }

If you run this bucket_sort alias in all 3 versions mentioned above, the items are listed in the same way in each version. The item names are listed in descending order in table1, ascending order in table2, then back to the same descending order in table3. The reason for this preservation of order is that $hget(table,N).item is listing these items in order by bucket, then within buckets it's listing them in reverse order of creation, with the older items listed last, and the newest additions listed first. Since this example used buckets=1, everything is in the same bucket, listed in reverse order of creation.

When items are /hsave'd to disk, buckets=1 saves in the same $hget(table,N).item order that's the inverse of creation order. $hget(table,1).item is the first item written to disk even though in this example it was the last item created. Note that the pair of notepad windows opened are showing the items in the 2 saved files in opposite order compared to each other, even though there were no items created or deleted between the hsave's.

But when the items are /hload'ed from disk into an empty table, they are loaded from the disk as if you /hadd'ed the first lines of the disk file first, then /hadd'ed the last lines of the disk file last. However since $hget(table,N).item lists items in the reverse order from when they're added, this causes table2 to have an order within the bucket which is the opposite of table1's, and is now listing the items in the ascending order they were created. This reversal also occurs again when table2 is saved to disk then loaded into table3, giving table3 the same $hget(table,N).item order as table1.

If you need to create a table which has $hget(table,N).item listing items in the creation order, you must:

1. Create the table using buckets=1 and create all the item names.
2. hsave table_name diskfilename
3. hfree -w table_name
4. hload -m1 table_name diskfilename

Step 3 is important, because if you /hload items into an existing table containing an item of the same name being hload'ed, it takes the existing position within the bucket instead of being added to the front as a fresh item. Without Step 3, the iteration order after Steps 1 and 4 would always be identical.

If table contains items #1-#20 in order of creation, but then items #21-#25 are added to the table, there are multiple steps required to put the table entirely into reverse creation order so they can be hsave'ed to disk in a way that lets them be hload'ed from disk into creation order:

1. hmake -m1 temptable
2. search from 1 through the last item $hget(temptable,0).item, until finding item#1.
3. Then save that location to be used later
4. From that position through end-of-file, clone the items and their data from maintable to temptable.
5. In descending N order toward N=1, clone the items preceding the above #3 location from maintable to temptable.
6. hsave temptable to disk

From this lengthy process, you can see how hashtables are ill-suited for preserving the creation order, especially when new items are added. If you need to preserve creation order in buckets=1, you might be forced to use slower methods such as holding data in a hidden @window or keeping an index to the data in the hidden @window, which is used to locate the longer data kept in the hashtable.

–

If you edit the above bucket_sort alias to change %buckets to be 101 instead of 1, you'll see the display is no longer in either ascending or descending order. That's because the order is displayed in order of their bucket placement first, before listing these items within buckets in reverse order in which they were created. Note that table2 keeps the same order as table 1, except for Kate and Suzy. These names were chosen because the v7.53 method of hashing item names assigns them to the same bucket when buckets=101, while items named Item1 through Item20 do not have more than 1 item assigned to the same bucket. Because Kate and Suzy were in the same bucket in the group of 101 buckets, they appear in reverse order of creation within table1, but their order is reversed again after loading from disk into table2, then reversed again when loaded from the 2nd disk file into table3.

The purpose of the hash algorithm is to distribute the items into the different buckets so searches for item names can be faster. If you have 1010 items in a hash table using buckets=1, it can take anywhere from 1 to 1010 tests before finding the position where an existing item is located. If the table uses 101 buckets, and if the algorithm evenly distributed the items to all buckets, the search would instead calculate the bucket which would be the destination for that item name, then check for a match only against the 10 items assigned to that bucket.

Starting with v7.53, mIRC changed the algorithm used to assign items to buckets. It now uses an algorithm replicated by the following alias.

.. code:: text

   alias fnv1a-32-mod-alt {
     var %len $len($1) , %i 0 , %hash 2166136261 , %input $upper($1)
     while (%i < %len) {
       !inc %i
       !var %hash $xor(%hash,$asc($mid(%input,%i,1)))
       !var %hash $calc(( (%hash % 256) * 16777216 + %hash * 403) % 4294967296 )
     }
     var %hash $calc((%hash * 8193) % 4294967296)
     var %hash $calc(($xor(%hash,$calc(%hash /128))    *    9) % 4294967296)
     var %hash $calc(($xor(%hash,$calc(%hash /131072)) *   33) % 4294967296)
     if (h isin $2) return $base(%hash,10,16,8) | return %hash
   } ; by maroon 2018
   ; If not for the 2^52 limit, the MUL could have been $calc((%hash * 16777619) % 4294967296)
   ; because the bits of the product above 2^32 aren't needed. $fnv1a-32-mod-alt(string,[h]) h=hash as hex
   ; is identical to original FNV1a except adding the following operations after the string is hashed, and in handling of codepoints 256+.
   ;  hash += hash << 13; (same as hash * 8193)
   ;  hash ^= hash >> 7;
   ;  hash += hash << 3; (same as hash * 9)
   ;  hash ^= hash >> 17;
   ;  hash += hash << 5; (same as hash * 33)
   alias assigned_to_bucket { return $calc(1+($fnv1a-32-mod-alt($upper($1)) % $$2)) }

.. code:: text

   //echo -a When buckets=101, item named foobar is assigned to bucket $assigned_to_bucket(foobar,101)

This fnv1a-32-mod-alt alias performs the 32-bit variant of the FNV1a hash against a text string. The FNV1a hash has been modified by mixing steps suggested by Brett Mulvey, and are performed by the 3 lines following the while loop. Note that this alias is non-standard because it adds codepoints 256-65535 as numbers larger than 8-bit values, but the FNV1a algorithm and the Mulvey mixing steps are designed where input is limited to 8 bits.

This algorithm attemps to create a hash whose output is well distributed across the 2^32 possible 32-bit values, and has significantly different values for input strings very similar to each other. If buckets=101, the hash output value is divided by 101, and the remainder is in the range 0-100. That remainder is used to assign the item to a bucket. When a script later searches for that item name, the hash is performed against the item name to identify which bucket it would have been assigned to, allowing mIRC to shrink the search to just the small fraction of items assigned to that same bucket.

.. code:: text

   alias bucket_sort2 {
     var %size 30 , %buckets 101 , %N 1 , %i 0 , %a 0
     hfree -sw table | hmake -s table %buckets
     while (%i < %size) {
       inc %i
       hadd table Item $+ %i
     }
     ; hdel -s table Item9 | hdel -s table item 23 | hadd -s table Item23 | hadd -s table Item9
     ; hdel -s table Item9 | hdel -s table item 23 | hadd -s table Item9  | hadd -s table Item23
     while ($hget(table,%N).item) {
       var %item $v1 , %prev %a , %a $calc(1+($fnv1a-32-mod-alt($upper($v1)) % %buckets))
       echo 4 -a $ord(%N) item is %item bucket: %a $iif(%prev > %a,*out of sequence*)
       inc %N
     }
   }

This /bucket_sort2 alias uses the above FNV1a-32-mod-alt alias to calculate the bucket each item was assigned. It wasn't until the 23rd item name until an item was assigned to a bucket that wasn't already empty.

For v7.53, this displays the items with a bucket number that sequentially increases. For earlier versions, the bucket number displayed is in a jumbled order because this is not the algorithm used in those versions. It's possible that future mIRC versions will use a different algorithm or use FNV1a in a different manner, so you should not count on items being assigned to the same buckets in past or future mIRC versions.

And even if item names are assigned to the same bucket, the iteration order can list them differently. Note that Item9 and Item23 are both assigned to bucket 13 of 101, and they're listed in table1 in reverse order than their creation order. However it appears that once an item has been deleted from a bucket, future items added to that bucket may not always be be listed in reverse creation order. For example, the 2 comment lines delete Item9 and Item23, but differ in the order those item names are created again. If you remove the semi-colon from 1 of the 2 comment lines, the order lists Item9 before Item23, regardless which semi-colon you remove. Notice above how the "Gary" and "Mary" example using $hfind to find the 1st match could return a different item name, depending which one appeared first in the iteration list, which can vary depending on several factors.

The FNV1a hash is performed against the upper-case string of the hash name, allowing $hget and $hfind /hdel to locate items in a case-insensitive manner, and allows /hadd to avoid creating a duplicate of an existing item name. However /hadd and the hashing algorithm have different definitions of what 'upper' means. /hadd recognizes only A-Z and a-z as being case-insensitive equivalents of each other. When /hadd is asked to create an item name as each of the codepoints 1-65535, it creates 65535-26=65509 items because only the a-z vs A-Z items are considered duplicates.

That means that it's possible to create 2 different item names from the outputs of $upper(SãoPaulo) and $lower(SãoPaulo) because the ã codepoint 227 is seen by /hadd as different than the codepoint 195 from $upper(ã). However the hashing algorithm hashes the $upper(item name) string which is identical for both item names, so it assigns both items to the same bucket.
