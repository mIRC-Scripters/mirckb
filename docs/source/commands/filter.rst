/filter
=======

The **/filter** command is perhaps the most powerful and least understood script command in mIRC. It scans lines of text in a custom-window or file or dialog control, and any lines that match the matchtext are written out to another custom-window or file or dialog control (or indeed by using an alias to any other desired destination such as a socket). 

You can restrict the source to a range of line numbers, and you can sort the output by columns (tokens) or using an alias. It will also work correctly when the source and destination windows are the same, allowing you easily and efficiently to sort the contents of a window. The order of the switch values is important as they define the source and destination of lines; see the examples for more informations. You can filter out blank lines by using the -x switch and specifying :doc:`$crlf </identifiers/crlf>` for the matchtext. /filter also fills the :doc:`$filtered </identifiers/filtered>` identifier with the number of matches found.

.. note:: If your script takes several seconds to execute because e.g. of nested loops, then if you can find a way to use /filter instead of the script loops, you can often achieve big performance improvements.

Synopsis
--------

.. code:: text

    /filter [-asdfkwxnphNriocteubglLz] [n-n2] [c s] <in-window | in-file | in-dialog-id> <out-window | out-file | out-dialog-id | out-alias> [sort-alias] <matchtext>

Switches
--------

Source/Destination switches 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Source and destination switches are (in theory) only needed if either the source or destination is ambiguous, but it is recommended that you always explicitly define both source and destination. The first use of these indicates the source, the second indicates the destination. As long as you're using a @window as your input or output and the other part of the input/output pair is a filename that does not begin with "@" then the -fw switches are not needed. They are needed with -s and -d to indicate which are input/output. Can use the window-id as an alias for the @custom window name. @test can be replaced by $+(@,$window(@test).wid)

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -w
      - source/destination is a custom-window
    * - -f
      - source/destination is a file
    * - -d
      - source/destination is the single message window
    * - -s
      - source/destination is the status window
    * - -k
      - destination is an <alias>. The alias will be called for each filtered line, with the form $<alias>($1) where $1 is the matched line
    * - -i
      - source is a custom dialog control [dialog id]
    * - -o
      - destination is a custom dialog control [dialog id]

Other switches 
^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - specifies the range of lines n to n2 for filtering
    * - -t
      - switch sorts the output based on [c s], column C using character S as the columns separator
    * - -e
      - used with -t, specifies a descending sort
    * - -u
      - used with -t, specifies a numeric sort
    * - -a
      - sorts filtered lines by calling the optional [alias] parameter, the alias is passed two lines, $1 and $2, it must compare both and return -1, 0, or 1 to indicate relative sort order of these lines to each other
    * - -g
      - indicates the matchtext is a regular expression
    * - -x
      - excludes matching lines
    * - -n
      - prefixes lines with a line number (the Nth match)
    * - -p
      - when output destination is a custom window (but not a listbox), wraps the text output
    * - -hN
      - indents wrapped text by N spaces (same as echo -i) when the -p switch is used
    * - -b
      - strips BURK control codes when matching text
    * - -z
      - retains line colors when filtering between custom windows
    * - -c
      - switch clears the output window/file before writing to it
    * - -l
      - filters from the side-listbox in the first window
    * - -L
      - filters to the side-listbox in the second window

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [n-n2]
      - if -r is used, indicates the range of lines to be scanned*
    * - [c s]
      - if -t is used, indicates how to do the sort
    * - <in-window | in-file | in-dialog-id>
      - unless you use -d or -s switches as source (which imply a window name), you must provide an input custom-window (-w), file (-f) or dialog control (-i)
    * - <out-window | out-file | out-dialog-id | out-alias>
      - unless you use -d or -s switches as destination (which imply a window name), you must provide an output custom-window (-w), file (-f), dialog control (-o), or alias name (-k)
    * - [sort-alias]
      - if -a is used, the sorting alias called
    * - <matchtext>
      - the expression used for the search, if $null is used, it matches everything.

Examples
--------

.. code:: text

    ;filter from the file "c:\my file.txt" to the custom window @mywin
    /filter -fw "c:\my file.txt" @mywin *findthis*

    ;filter from the custom window @mywin to the file "c:\my file.txt"
    filter -wf @mywin "c:\my file.txt" *findthat*

    ;filter from the status window to the single message window
    /filter -sd *findthis*

    ;filter from the single message window to the status window
    /filter -ds *findthat*

    ;filter from the filename @this_is_a_file to the dialog 'dialog', id '1'
    /filter -fo @this_is_a_file dialog 1 *findthis*

    ;filter from a file and call an alias for each line
    /filter -fk file myalias *findthat*

    ;Fetch list of mIRC release dates from versions.txt to status window:
    /filter -fsg versions.txt \d+/\d+/\d+ - mIRC*
    ; same except looks only at lines 1-through-1000 and prefixes returned text with the line number:
    /filter -fsgrn 1-1000 versions.txt \d+/\d+/\d+ - mIRC*

    ;filter from a wordlist file to status window for words which can be spelled in an 8-digit CRC, using regex
    ; includes substitutions like 7 in place of "t", 0 in place of "0", 8 in place of "ate", etc
    alias word2hex echo -s $replace($1-,four,4,for,4,ate,8,ten,10,t,7,s,5,to,2,l,1,o,0)
    /filter -fkcg words_alpha.txt word2hex /^([A-F]|o|l|to|for|four|s|g|t|ate|ten){1,8}$/i

    ;sort by file(same file) - Input file's Column 1 delimited by Space Character $chr(32)
    /filter -ffcut 1 32 file.txt file.txt

    ; can use filter to obtain line count without creating output window/file
    //filter -fk versions.txt nosuchalias *mirc* | echo -a $filtered lines contain the string mIRC
    ; NUL is the windows device for the 'bit bucket, and creates no such file - not to be confused with the $null identifier
    //filter -ff versions.txt nul *mirc* | echo -a $filtered lines contain the string mIRC

    ; If /window -jN not used or created with -j0, size limit of @test is current value of Mirc-Options/Other/WindowBuffer
    //filter -fwc versions.txt @test * | var %missing $calc( $filtered - $line(@test,0)) | if (%missing) echo -a warning %missing of $filtered filtered lines not in @test because /window not used with large enough -jN value

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$filtered </identifiers/filtered>`
    * :doc:`$read </identifiers/read>`
    * :doc:`$fline </identifiers/fline>`
    * :doc:`/loadbuf </commands/loadbuf>`
    * :doc:`/savebuf </commands/savebuf>`
