/write
======

The **/write** command can be used to manipulate a text file in various ways. Used without switches mIRC will append the line to the end of the text file. If the file does not exist, mIRC will create it. If <words>, <wildcard>, or <regex> contains spaces, they must be enclosed by a pair of quotes.

Synopsis
--------

.. code:: text

    /write [-cidnamN l<line> s<words> w<wildcard> r</regex/>] <filename> [text]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Clears the entire file before writing to it
    * - -i
      - Inserts the text at a given line instead of replacing it
    * - -d
      - Deletes the given line
    * - -n
      - Prevent adding $crlf at the end of the text
    * - -a
      - Appends the text to an existing line
    * - -l
      - Line number for the line to write/modify/delete
    * - -s
      - Operates on a line which start with <words>
    * - -w
      - Operates on a line which match the <wildcard> expression.
    * - -r
      - same as -w - but uses a regular expression.
    * - -mN
      - handle the $crlf addition before a line:

   There is a difference in how /write behave vs /write -s or /write -w when it comes to adding a $crlf before your line, if mirc is going to add the line to end of the file and that the last line does not have a $crlf already.

   /write will always put the $crlf, whereas /write -ws won't. For compatibility and to allow you to control exactly when and if a $crlf is going to be added in this case:

   When N = 0, the current behavior is used, N = 1 means a $crlf is added only if a $crlf isn't always there, N = 2 means a $crlf is never added.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - The file name to manipulate
    * - [text]
      - The text to be written to the file
    * - <line>
      - The line number to find
    * - <words>
      - The word to scan.
    * - <wildcard>
      - :doc:`wIldcard </intermediate/matching_tools.html#wildcard>` pattern to match
    * - </regex/>
      - RegEx pattern to match

Example
-------

.. code:: text

    Alias Example {
    ;Create a file; add a few lines of text to it
    write Example.txt this is a cool line
    write Example.txt hello there!
    write Example.txt text files are cool

    /*
    Locate the line that starts with "hello"
    and insert the following text before it
    */
    write -is"Hello" Example.txt This will become line 2!

    ;Delete line 1
    write -dl1 Example.txt
    }

Compatibility
-------------

Added: mIRC v3.8 (25 Nov 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$read </identifiers/read>`
    * :doc:`$readn </identifiers/readn>`
    * :doc:`$mircini </identifiers/mircini>`
    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`/fopen </commands/fopen>`
    * :doc:`/fwrite </commands/fwrite>`
