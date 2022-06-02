/hsave
======

The **/hsave** command is used to save a hash table to a file. Overwrite existing file if it already exists.

Synopsis
--------

.. code:: text

    /hsave -Bbnusa <name> <filename>
    /hsave -inusa <name> <filename> [section]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -b
      - saves binary files. $cr and $lf are preserved when saving as binary files. Ignored if -i switch used.
    * - -B
      - uses a larger index than -b to allow longer binary data to be saved. This is not compatible with files created by the -b switch.
    * - -i
      - treats the file as an ini file. You can specify an optional [section] after the filename
    * - -n
      - save files as data only. Each value is saved on a new line
    * - -u
      - forces items in the /hadd -uN unset list to be included. They are excluded by default.
    * - -s
      - display a message if successful: ``* Saved hash table <table> to <filename>``
    * - -a
      - appends to an existing file instead of overwriting it

.. note:: versions.txt change log for v5.8 shows /hsave having a -o switch to overwrite the disk file. However this was long ago deprecated without versions.txt being updated. At least as far back as v6.35, /hsave overwrites the contents of the disk file without the need to use the -o switch. If you do use -o, it is silently ignored, as mIRC often does with invalid switches.

.. note:: If table contains an item holding a binary variable longer than 65535 bytes, you should use -B instead of -b. While trying to write that item to disk, -b quits with error message "* /hsave: error saving hash table". The disk file then contains anywhere from zero to all other items which were in the hashtable, depending on the $hget(table,N).item order where the long binvar was encountered.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - the name of the hash table
    * - <filename>
      - the name of the file the table is being saved to. Must be enclosed in double quotes if contains a space
    * - [section]
      - if -i is used, you can optionally specify the section of the ini file. Default section is hashtable

Notes
-----

.. note:: If using -a switch to append to an existing file, you should also use -b, -n, or -i [section] switches if those were used to create the original file, to avoid mixing formats with undesirable results.

.. note:: If saving using -b or -B or -i or -n switches to save the hash table to disk, you should generally use those same switches again with /hload if you plan to reload the hash table from disk back into memory.

.. note::

    Disk structure of saved file

    In all cases, item names and text data is UTF-8 encoded. Both as an item name or the text data, the string tést contains the 5 bytes seen from ``$utfencode(tést)``. If a table item contains a binary variable, saving it without using -b or -B saves the portion of the variable returned by ``$bvar(&variable,1-).text``

    Disk Structure: Default with no switch:

    Each item saved as a pair of text lines, with the first line being the name of the item, and the next line being the value. (Or a blank line if the item has $null value). If saving 20 items to disk, the file has 40 lines, with the item names on the odd-numbered lines and their values being the even numbered lines which follow the line containing the name of the item.

    Disk Structure: -i switch with optional [section]

    If optional SECTION parameter not used, /hsave -i and /hload -i use the default section name hashtable enclosed in square braces. Otherwise, the optional parameter following the filename is used as the .ini's section name. /hsave -i overwrites only the active section name, without affecting other section names existing in the .ini file. If your optional parameter is wrapped inside square braces, mIRC assumes it should wrap your parameter again, so your disk file would contain a section header like [[parameter]]
    Each Item is written to that section as a single line in the format ItemName=DataValue

    Disk Structure: -n switch

    Item names not written to disk, only the data values written to disk. If saving 20 items to disk, the 20 data values are written to 20 lines, without the item names written to disk. If you /hload this file with the -n switch, the table creates item names numbered as the sequential integers beginning with 1, containing the data on disk. The Nth line of the disk file is loaded as the data for item name using the number N. If -n is used along with the -i switch, the items are written to disk in the .ini format with assigned item names, such as writing lines like n0=value n1=value etc.

    Disk Structure: -b switch

    Items saved to disk in binary format:

    * 2 bytes containing the length of the following item name in bigendian format. These bytes are 0x08 0x00 for an 8-character item name
    * The text name of the item. If the first 2 bytes were 0x08 0x00, the following 8 bytes are the name of the item.
    * 2 bytes containing the bigendian length of the following data. These bytes are 0x05 0x00 when there is a 5 byte value following these 2 bytes. The value is the number of bytes not the $len of the data. Text data value ``tést`` is UTF-8 encoded as 5 bytes and the binary format contains 0x05 0x00 even though the ``$len()`` is ``4``. For items containing no data, these bytes are 0x00 0x00 and and /hload -b expects these to be followed either by the length of the following itemname or end-of-file.
    * The bytes of the data value. There is no ``$crlf`` written to disk unless the value is a binary variable containing the ``$chr(13) $chr(10)`` bytes. Because this is binary format, there is no restriction on the contents of the item's data, so it can include 0x00's or non-UTF8 strings if created with /hadd -b, but all data created without the -b switch is UTF8 encoded.
    * Repeat the above until /hload encounters the end of file or /hsave writes the last record. There is no additional end-of-table data written to disk.

    Any binary variable can be saved into a hashtable using ``hadd -b tablename itemname &binvarname``. If the length of the &binvar was 0-65535, it can be written to disk in /hsave -b format. However any hashtable item whose contents is length 65536 or longer will not be written to disk correctly, and no later items will be written to disk either. Instead, the length-word of the itenmame and the item name are written to disk, but no other data is written.

    Disk Structure: -B switch

    Same as -b binary format except length field uses 4 bytes instead of 2:

    * 4 bytes containing the length of the following item name in bigendian format. These bytes are 0x08 0x00 0x00 0x00 for an 8-byte item name
    * The text name of the item. If the first 4 bytes were 0x08 0x00 0x00 0x00, the following 8 bytes are the name of the item.
    * 4 bytes containing the bigendian length of the following data. These bytes are 0x40 0xe2 0x01 0x00 when there is a 123456-byte value following these 2 bytes. The value is the number of bytes not the $len of the data. Data value ``tést`` is UTF-8 encoded as 5 bytes even though the ``$len()`` is ``4``. The size of this value allows the following data to be larger than the 65535 limit for -b data. For items containing no data, these bytes are 0x00 0x00 0x00 0x00 and /hload -B expects these to be followed either by the length of the following itemname or end-of-file.
    * The bytes of the data value. There is no $crlf written to disk unless the value is a binary variable containing the ``$chr(13) $chr(10)`` bytes. Because this is binary format, there is no restriction on the contents of the item's data, so it can include 0x00's or non-UTF8 strings if created with /hadd -b, but all data created without the -b switch is UTF8 encoded.
    * Repeat the above until /hload encounters the end of file or /hsave writes the last record. There is no additional end-of-table data written to disk.

.. note::

    Example of -b vs -B formats. Periods are added for readability only, numbers are byte values 0-255.

    -b format
    item name test containing the string tést
    4 0 . 116 101 115 116 . 5 0 . 116 195 169 115 116
    item name tést containing no data
    5 0 . 116 195 169 115 116 . 0 0

    -B format
    item name test containing the string tést
    4 0 0 0 . 116 101 115 116 . 5 0 0 0 . 116 195 169 115 116
    item name tést containing no data
    5 0 0 0 . 116 195 169 115 116 . 0 0 0 0


.. note::

    Itemnames are always written as UTF8 encoded because that's the way they were created. Item data is always UTF8 encoded, unless it was created with the -b switch, in case it contains the contents of the binvar used to create it. If a data item saved in -b format contains non-UTF8 encoded text, it loads into the item as the same binary data, but ``$hget(table,item)`` and ``$hget(table,item,&binvar)`` access the data differently.

    -b and -B do error checking on the data when loading, stopping when encountering a bad item 'record', such as encountering end-of-file prior to the end of the record as defined by either length byte. If 0x00 is encountered in the middle of the itemname, both the item and data are hadd'ed to the table, with the itemname truncated prior to the 0x00.

Examples
--------

.. code:: text

    //hfree -w test | hadd -m test itemname 12345 | hadd test itemB 67890 | hsave -s test file name.dat
    * hash table is written to disk to filename "file" and name.dat is ignored. A filename containing a space must be enclosed in double quotes or use $qt(hash table file name)

    //hfree -w test | hadd -m test itemname é12345 | hadd test itemB 67890 | hsave -sb test test.dat | bread test.dat 0 $file(test.dat).size &binvar | echo -a $bvar(&binvar,1-)
    Result: 8 0 105 116 101 109 110 97 109 101 7 0 195 169 49 50 51 52 53 5 0 105 116 101 109 66 5 0 54 55 56 57 48
    8 0 = Length of Item name
    105 116 101 109 110 97 109 101 = Item "itemname"
    7 0 = Length of item value
    195 169 49 50 51 52 53 = 7 byte UTF-8 encoding of é12345

    //hfree -w test | hadd -m test itemname 12345 | hadd test itemB 67890 | hsave -n test test.dat | hfree -w test2 | hload -m test2 test.dat | echo -a item 1 is $hget(test2,1).item containing $hget(test2,$hget(test2,1).item)
    Result: item 1 is 12345 containing 67890
    * Table saved using -n switch incorrectly loaded without using /hload's -n switch, causing the 1st data value to be handled as if it's an item name and the 2nd line to be the data value matching the item named by the 1st line of the file.

    //hfree -w test | hadd -m test itemA 12345 | hinc -z test itemB 67890 | hadd -u30 test itemC value3 | hsave -u test test.dat | var %i 1 , %tot $lines(test.dat) | while (%i <= %tot) { echo -a line %i is $read(test.dat,nt,%i)  | inc %i }
    * The disk file contains 6 lines (3 pairs) for the 3 items because hsave used the -u switch. If the -u switch is deleted, the 2nd and 3rd item are not written to disk because they have a non-zero property for $hget(table-name,item-name).unset

    Note: this alias will fail if any file larger than 65535 and you change /hsave to use -b instead of -B
    alias hashtable_dir {
      btrunc test.dat 0
      var -s %i 1 , %folder $nofile($mircexe) , %total $findfile(%folder,*,0,1) , %bytes 0 , %maxbytes 9999999
      echo -a limited to %maxbytes bytes, loads all files in %folder into hashtable then saves to disk
      echo -a assuming no double-spaces in filenames and no zero-byte files. spaces changed to _'s
      hfree -w test | hmake -s test 1
      while ($findfile(%folder,*,%i,1)) {
        var %item $replace($v1,$chr(32),_)
        if ($file(%item).size && (*\test.dat !iswm %item)) {
          bread $qt(%item) 0 $file(%item).size &v
          if ($calc(%bytes + $bvar(&v,0)) < %maxbytes) { inc %bytes $bvar(&v,0) | hadd -bs test %item &v }
        }
        inc %i
      }
      hsave -sB test test.dat
      echo -a test.dat filesize $file(test.dat).size contains $hget(test,0).item items
    }

Compatibility
-------------

Added: mIRC v5.8 (05 Sep 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake <hmake>`
    * :doc:`/hfree <hfree>`
    * :doc:`/hload <hload>`
    * :doc:`/hadd <hadd>`
    * :doc:`/hdel <hdel>`
    * :doc:`/hinc <hinc>`
    * :doc:`/hdec <hdec>`
    * :doc:`$hget </aliases/hget>`
    * :doc:`$hfind </aliases/hfind>`
