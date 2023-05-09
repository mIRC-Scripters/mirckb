$read
=====

The $read returns a line from a disk file

Synopsis
--------

.. code:: text

    $read(filename [, ntswrp] [,matchtext] [, N] )
    Legacy syntax:
    $read [switches] [line#] filename

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - filename
      - The file from which text is returned
    * - matchtext
      - Used with switches s w r
    * - N
      - Line number to read, except when using s, w, or r switches where it's the first line of the file portion to search.

Switches
^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - n
      - Do not evaluate $identifiers contained in the returned line.
    * - t
      - Do not treat a numeric line#1 as if it's the total number of lines in the text file.
    * - s
      - Search for line beginning with <matchtext> and returns the remainder of the line beyond the spaces following <matchtext>
    * - w
      - Scan for line matching <matchtext> which can be a :ref:`matching_tools-wildcard`. If not a wildcard the line must be exact match. Returns the entire contents of the matching line
    * - r
      - Indicates that <matchtext> is a regex pattern.
    * - p
      - When evaluating text in the absence of the 'n' switch, treats the pipe symbol as a command separator allowing the remainder of the line to be executed as a /command.

Notes:
^^^^^^

* All searches are case-insensitive.
* Line can end with $cr or $lf or $crlf or end-of-file. Does not treat $chr(26) as End-of-File-Marker. Contents of a line past $chr(0) are ignored.
* If 't' switch is NOT used - if line 1 is not a number, $read functions normally. If line 1 is a number, random lines will be chosen only for the first N lines, and $readn returns 1 through N while returning the contents of actual lines 2 through N+1.
* If NO switches are used,  $read(file,0) returns the contents of line 1 if it's a number, or returns $null if contents are anything else.
* matchtext must have the presence/absence of spaces in order to match lines having/not-having those spaces, even leading/trailing/consecutive.
* Undocumented legacy syntax can be used  where parameters follow the identifier without being enclosed within quotes.

Examples
--------

.. code:: text

    //echo -a prev line read was $readn - $read(versions.txt,nt) is line $readn
    returns: a random line from versions.txt even if it is $null
    Note: You can use $read(quotes.txt,nt) as your quit message, and it will display a random line from that file when you /quit a server.
    
    If you don't use the 'n' switch, and if $read(quotes.txt) randomly chooses the line created by the following command, it will evaluate the identifiers using their current values.
    
    //write quotes.txt Banned from $ $+ network until $ $+ gmt($ $+ calc($ $+ ctime +86400*7)) GMT
    
    //echo -a $read(versions.txt,nt,3)
    returns: contents of line #3
    //echo -a $read(versions.txt,nt,2)
    returns: contents of line #2. if the line is blank (length = 0), returns $null
    
    //echo -a $read(versions.txt,nt,invalid)
    returns: If s/r/w switches not used and 3rd parameter is used without being a number >= 1, returns line #1.
    
    //echo -a $read(file.txt,t,3)
    returns: Contents of line#3. Because the 'n' switch wasn't used, evaluates any $identifiers and %variables instead of returning strings beginning with "$" or "%".
    
    //echo -a $read(file.txt,tp,3)
    returns: Same, except if the line contains the | "pipe" symbol, that is treated as a command separator, and the portion beyond the pipe is executed as if a script command.
    
    //echo -a $read(versions.txt,nts,10.fixed) line: $readn
    matches: the first line which is either a match for the matchtext, or the first line beginning with the matchtext followed by a space. If matchtext is 'yes' it will not match a line beginning with 'yesterday'. The 's' switch returns the portion of the line excluding the matchtext and the spaces following it.
    
    //echo -a $read(versions.txt,nts,10.fixed,200) line: $readn
    matches: Same, except begins scanning at line 200.
    
    //echo -a $read(versions.txt,nts,3.Changed udpate) line: $readn
    Uses matchtext containing spaces
    
    //echo -a $read(versions.txt,nts,changes:) $readn 
    returns $null because that is the full content of the matching line, so there is no remainder-of-line to return. But $readn indicates there was a match.
    
    //echo -a $read(versions.txt,ntw,changes:) $readn
    'w' differs from 's' in that it accepts wildcard, but also returns the entire line including the match.
    
    //echo -a $read(versions.txt,ntw,10.fixed) line: $readn
    returns $null and $readn returns 0 because 'w' requires matching the matchtext instead of beginning with it.
    
    //echo -a echo -a $read(versions.txt,nts,$str($chr(32),4)) $readn
    matches the 1st line which begins with 4 OR MORE spaces.
    
    //echo -a $read(versions.txt,ntw,& & &) $readn
    returns first line containing exactly 3 space-tokenized 'words'.
    
    Return all matches in file after ensuring $readn is zero:
    //var %i 1 | var %a $read(set readn to zero,nt) | while ($read(versions.txt,ntw,*- mIRC v*,$calc(1+$readn))) { echo -a $ord(%i) match: $v1 | inc %i }
    
    //write -c test.dat top line | var %i 2 | while (%i isnum 2-100) { write test.dat line %i | inc %i }
    This creates a 100-line file, where the 1st line says "top line" and lines 2-99 are that same number.
    
    //write -l1 test.dat top | echo -a $read(test.dat,n) is the contents of line $readn
    Because Line#1 is not a number, mIRC does not treat it as a line count for the file, so this returns a random line from the text file.
    
    //write -l1 test.dat  40 | echo -a $read(test.dat,n) is the contents of line $readn
    Now that line#1 is the number N, returns a random line from physical line 2 through N+1 as if they're lines 1-N, so it's possible for this to return $readn 1-40 when reading from lines 2-41. As long as line 1 is the number 40, reading a random line without using the 't' switch never returns a $readn value greater than 40
    
    //var %pattern \d{5,} | echo -a $read(versions.txt,ntr,%pattern) $readn
    'r' switch indicates matchtext is a regex pattern. Returns: first line containing at least 5 consecutive number digits. Regex defaults to case-sensitive unless the 'i' flag is used.
    
    First line containing the string 'wildcard' anywhere:
    //echo -a $read(versions.txt,ntw,*wildcard*) line: $readn
    First line containing the string 'wildcard' anywhere on/after line 2000:
    //echo -a $read(versions.txt,ntw,*wildcard*,2000) line: $readn
    
    Shows line 1 being evaluated, including a local %variable created after the disk write:
    //write -l1 test.txt $ $+ me % $+ a | var %a $asctime | echo -a $read(test.txt,n,1) vs $read(test.txt,1)
    
    quirk: if attempting to read from a non-existent line, $readn is set to 1 more than the number of lines even though it did not successfully read anything.
    //write -cl1 test.txt 5 | write -l2 test.txt test2 | write -l3 test.txt test3 | echo -a text: $read(test.txt,nt,44) readn: $readn
    the above returns 4 even though there are only 3 lines. If the 't' switch is removed, where $read treats the 2nd and 3rd lines as lines 1 and 2 due to the numeric line1, it returns the non-existent line 3.
    
    quirk: if the numeric line 1 is greater than the number of lines, and $read attempts to return a random line from the file, it sets $readn to the first non-existent line number. In this example, the numeric 10 causes $readn to be 1 or 2 a combined 20% of the time, and $readn is 3 the other 80% time when it returns $null text
    //write -cl1 test.txt 10 | write -l2 test.txt test2 | write -l3 test.txt test3 | echo -a text: $read(test.txt,n) readn: $readn
    
    quirk: where line1 is numeric. line 0 is supposed to return the number, but that doesn't happen when 'n' switch is used by itself.
    //write -c test.dat 40 | write test.dat test2 | echo -a with n: $read(test.dat,n,0) and readn= $readn without n: $read(test.dat,0) and readn= $readn
    
    This shows how $read identifies what defines a line:
    //clipboard $cr $+ 1 $+ $lf $+ 2 $+ $crlf $+ 3 $+ $cr $+ $crlf $+ 4 $+ $crlf $+ $lf $+ 5 $+ $lf $+ $cr $+ 6 $+ $cr $+ 7 | noop $regsubex(foo,$cb,,,&var) | bwrite -c test.dat 0 -1 &var | var %i $lines(test.dat) | echo -a cb(0) $cb(0) vs lines(test.dat) %i | while (%i) { noop $cb(%i,,&v2) | echo -a %i : clipboard: $bvar(&v2,1-) : $bvar(&v2,1-).text vs $ $+ read: $read(test.dat,nt,%i) | dec %i }
    
    Every $cr and every $lf  are seen as a line-ending, except for 1 $cr immediately preceding a $lf causing it to be seen as part of a $crlf. The End-of-File is also another line ending if the file does not end with a $cr or $lf

Compatibility
-------------

For modern documented syntax:

.. compatibility:: 3.6

For older undocumented syntax:

.. compatibility:: 3.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/bread </commands/bread>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$readini </identifiers/readini>`
