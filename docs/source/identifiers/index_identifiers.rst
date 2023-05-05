Identifiers
===========

**mIRC identifiers** are a set of built-in value-returning routines that can be used to query mIRC for various data structures, mIRC, IRC, and OS related properties such as a file size or the 6th nick in a channel.

=$nick, $*, $&, $+ and $++ are exception and are not returning values, they are constructs interpreted in a different way.

Presently undocumented or deprecated identifiers are indicated in *italics*.  An identifier is undocumented if it doesn't reasonably appear in the current help.chm, but may appear in the `versions.txt <https://www.mirc.com/versions.txt>`_

.. tabs::

    .. tab:: A

        .. hlist::
            :columns: 4

            * :doc:`$abook() <abook>`
            * :doc:`$abs() <abs>`
            * :doc:`$acos() <acos>`
            * :doc:`$active <active>`
            * :doc:`$activecid <activecid>`
            * :doc:`$activewid <activewid>`
            * :doc:`$adate <adate>`
            * :doc:`$address <address>` :sup:`e`
            * :doc:`$address() <address>`
            * :doc:`$addtok() <addtok>`
            * :doc:`$addtokcs() <addtokcs>`
            * :doc:`$agent() <agent>`
            * :doc:`$agentname <agentname>` :sup:`e`
            * :doc:`$agentstat <agentstat>`
            * :doc:`$agentver <agentver>`
            * :doc:`$alias() <alias>`
            * :doc:`$and() <and>`
            * :doc:`$anick <anick>`
            * :doc:`$ansi2mirc() <ansi2mirc>`
            * :doc:`$aop() <aop>`
            * :doc:`$appactive <appactive>`
            * :doc:`$appstate <appstate>`
            * :doc:`$asc() <asc>`
            * :doc:`$asctime <asctime>`
            * :doc:`$asctime() <asctime>`
            * :doc:`$asin() <asin>`
            * :doc:`$atan() <atan>`
            * :doc:`$atan2() <atan2>`
            * :doc:`$auto() <auto>`
            * :doc:`$avoice() <avoice>`
            * :doc:`$away <away>`
            * :doc:`$awaymsg <awaymsg>`
            * :doc:`$awaytime <awaytime>`

    .. tab:: B

        .. hlist::
            :columns: 4

            * :doc:`$banlist() <banlist>`
            * :doc:`$banmask <banmask>` :sup:`e`
            * :doc:`$base() <base>`
            * :doc:`$beta <beta>`
            * :doc:`$bfind() <bfind>`
            * :doc:`$bindip() <bindip>`
            * :doc:`$bitoff() <bitoff>`
            * :doc:`$biton() <biton>`
            * :doc:`$bits <bits>`
            * :doc:`$bnick <bnick>` :sup:`e`
            * :doc:`$bvar() <bvar>`
            * :doc:`$bytes() <bytes>`

    .. tab:: C

        .. hlist::
            :columns: 4

            * :doc:`$calc() <calc>`
            * :doc:`$caller <caller>`
            * :doc:`$cancel <cancel>`
            * :doc:`$cb <cb>`
            * :doc:`$cb() <cb>`
            * :doc:`$cbrt() <cbrt>`
            * :doc:`$cd <cd>` :sup:`e`
            * :doc:`$ceil() <ceil>`
            * :doc:`$chan <chan>`
            * :doc:`$chan() <chan>`
            * :doc:`$chanmodes <chanmodes>`
            * :doc:`$channel() <channel>`
            * :doc:`$chantypes <chantypes>`
            * :doc:`$chat() <chat>`
            * :doc:`$chr() <chr>`
            * :doc:`$cid <cid>`
            * :doc:`$clevel <clevel>` :sup:`e`
            * :doc:`$click() <click>`
            * :doc:`$cmdbox <cmdbox>`
            * :doc:`$cmdline <cmdline>`
            * :doc:`$cnick() <cnick>`
            * :doc:`$codepage() <codepage>`
            * :doc:`$color() <color>`
            * :doc:`$colour() <colour>`
            * :doc:`$com() <com>`
            * :doc:`$comcall() <comcall>`
            * :doc:`$comchan() <comchan>`
            * :doc:`$comchar <comchar>`
            * :doc:`$comerr <comerr>`
            * :doc:`$compact <compact>`
            * :doc:`$compress() <compress>`
            * :doc:`$comval() <comval>`
            * :doc:`$cos() <cos>`
            * :doc:`$cosh() <cosh>`
            * :doc:`$count() <count>`
            * :doc:`$countcs() <countcs>`
            * :doc:`$cr <cr>`
            * :doc:`$crc() <crc>`
            * :doc:`$crc64() <crc64>`
            * :doc:`$creq <creq>`
            * :doc:`$crlf <crlf>`
            * :doc:`$ctime <ctime>`
            * :doc:`$ctime() <ctime>`
            * :doc:`$ctimer <ctimer>`
            * :doc:`$ctrlenter <ctrlenter>` :sup:`e`

    .. tab:: D

        .. hlist::
            :columns: 4

            * :doc:`$date() <date>`
            * :doc:`$day <day>`
            * :doc:`$daylight <daylight>`
            * :doc:`$dbuh <dbuh>`
            * :doc:`$dbuw <dbuw>`
            * :doc:`$dccignore <dccignore>`
            * :doc:`$dccignore() <dccignore>`
            * :doc:`$dccport <dccport>`
            * :doc:`$dde() <dde>`
            * :doc:`$ddename <ddename>`
            * :doc:`$debug <debug>`
            * :doc:`$decode() <decode>`
            * :doc:`$decompress() <decompress>`
            * :doc:`$deltok() <deltok>`
            * :doc:`$devent <devent>` :sup:`e`
            * :doc:`$dialog() <dialog>`
            * :doc:`$did <did>` :sup:`e`
            * :doc:`$did() <did>`
            * :doc:`$didreg() <didreg>`
            * :doc:`$didtok() <didtok>`
            * :doc:`$didwm() <didwm>`
            * :doc:`$dir <dir>`
            * :doc:`$disk() <disk>`
            * :doc:`$dlevel <dlevel>`
            * :doc:`$dll() <dll>`
            * :doc:`$dllcall() <dllcall>`
            * :doc:`$dname <dname>` :sup:`e`
            * :doc:`$dns() <dns>`
            * :doc:`$donotdisturb <donotdisturb>`
            * :doc:`$dqwindow <dqwindow>`
            * :doc:`$duration() <duration>`

    .. tab:: E

        .. hlist::
            :columns: 4

            * :doc:`$ebeeps <ebeeps>`
            * :doc:`$editbox() <editbox>`
            * :doc:`$email <email>`
            * :doc:`$emailaddr <emailaddr>`
            * :doc:`$encode() <encode>`
            * :doc:`$envvar() <envvar>`
            * :doc:`$error <error>`
            * :doc:`$eval() <eval>`
            * :doc:`$evalnext() <evalnext>`
            * :doc:`$event <event>` :sup:`e`
            * :doc:`$eventid <eventid>` :sup:`e`
            * :doc:`$eventparms <eventparms>` :sup:`e`
            * :doc:`$exists() <exists>`
            * :doc:`$exiting <exiting>`

    .. tab:: F

        .. hlist::
            :columns: 4

            * :doc:`$factorial() <factorial>`
            * :doc:`$false <false>`
            * :doc:`$feof <feof>`
            * :doc:`$ferr <ferr>`
            * :doc:`$fgetc() <fgetc>`
            * :doc:`$fibonacci() <fibonacci>`
            * :doc:`$file <file>`
            * :doc:`$file() <file>`
            * :doc:`$filename <filename>` :sup:`e`
            * :doc:`$filtered <filtered>`
            * :doc:`$finddir() <finddir>`
            * :doc:`$finddirn <finddirn>`
            * :doc:`$findfile() <findfile>`
            * :doc:`$findfilen <findfilen>`
            * :doc:`$findtok() <findtok>`
            * :doc:`$findtokcs() <findtokcs>`
            * :doc:`$fline() <fline>`
            * :doc:`$flinen <flinen>`
            * :doc:`$floor() <floor>`
            * :doc:`$font() <font>`
            * :doc:`$fopen() <fopen>`
            * :doc:`$fread() <fread>`
            * :doc:`$freadex() <freadex>`
            * :doc:`$fromeditbox <fromeditbox>`
            * :doc:`$fserv() <fserv>`
            * :doc:`$fserve() <fserve>`
            * :doc:`$fulladdress <fulladdress>` :sup:`e`
            * :doc:`$fulldate <fulldate>`
            * :doc:`$fullname <fullname>`
            * :doc:`$fullscreen <fullscreen>`
            * :doc:`$fupdate <fupdate>`

    .. tab:: G

        .. hlist::
            :columns: 4

            * :doc:`$gcd() <gcd>`
            * :doc:`$get() <get>`
            * :doc:`$getdir() <getdir>`
            * :doc:`$getdot() <getdot>`
            * :doc:`$gettok() <gettok>`
            * :doc:`$gmt <gmt>`
            * :doc:`$gmt() <gmt>`
            * :doc:`$group() <group>`

    .. tab:: H

        .. hlist::
            :columns: 4

            * :doc:`$halted <halted>` :sup:`e`
            * :doc:`$hash() <hash>`
            * :doc:`$height() <height>`
            * :doc:`$hfile= <hfile>`
            * :doc:`$hfile() <hfile>`
            * :doc:`$hfind() <hfind>`
            * :doc:`$hget() <hget>`
            * :doc:`$highlight <highlight>`
            * :doc:`$highlight() <highlight>`
            * :doc:`$hmac() <hmac>`
            * :doc:`$hmatch() <hmatch>`
            * :doc:`$hnick <hnick>` :sup:`e`
            * :doc:`$hnick() <hnick>`
            * :doc:`$host <host>`
            * :doc:`$hotline <hotline>` :sup:`e`
            * :doc:`$hotlinepos <hotlinepos>` :sup:`e`
            * :doc:`$hotlink() <hotlink>` :sup:`e`
            * :doc:`$hotp() <hotp>`
            * :doc:`$hregex() <hregex>`
            * :doc:`$hypot() <hypot>`

    .. tab:: I

        .. hlist::
            :columns: 4

            * :doc:`$iaddress <iaddress>` :sub:`e`
            * :doc:`$ial <ial>`
            * :doc:`$ial() <ial>`
            * :doc:`$ialchan() <ialchan>`
            * :doc:`$ibl() <ibl>`
            * :doc:`$idle <idle>`
            * :doc:`$iel() <iel>`
            * :doc:`$ifmatch <ifmatch>`
            * :doc:`$ifmatch2 <ifmatch2>`
            * :doc:`$ignore <ignore>`
            * :doc:`$ignore() <ignore>`
            * :doc:`$iif() <iif>`
            * :doc:`$iil() <iil>`
            * :doc:`$inellipse() <inellipse>`
            * :doc:`$ini() <ini>`
            * :doc:`$initopic() <initopic>`
            * :doc:`$inmidi <inmidi>`
            * :doc:`$inmode <inmode>`
            * :doc:`$inmp3 <inmp3>`
            * :doc:`$inpaste <inpaste>` :sup:`e`
            * :doc:`$inpoly() <inpoly>`
            * :doc:`$input() <input>`
            * :doc:`$inrect() <inrect>`
            * :doc:`$inroundrect() <inroundrect>`
            * :doc:`$insong <insong>`
            * :doc:`$instok() <instok>`
            * :doc:`$int() <int>`
            * :doc:`$intersect() <intersect>`
            * :doc:`$inwave <inwave>`
            * :doc:`$inwho <inwho>`
            * :doc:`$ip <ip>`
            * :doc:`$iptype() <iptype>`
            * :doc:`$iql() <iql>`
            * :doc:`$isadmin <isadmin>`
            * :doc:`$isalias() <isalias>`
            * :doc:`$isbit() <isbit>`
            * :doc:`$isdde() <isdde>`
            * :doc:`$isdir() <isdir>`
            * :doc:`$isfile() <isfile>`
            * :doc:`$isid <isid>`
            * :doc:`$islower() <islower>`
            * :doc:`$isnumber() <isnumber>`
            * :doc:`$isnum() <isnum>`
            * :doc:`$istok() <istok>`
            * :doc:`$istokcs() <istokcs>`
            * :doc:`$isupper() <isupper>`
            * :doc:`$isutf() <isutf>`

    .. tab:: K

        .. hlist::
            :columns: 4

            * :doc:`$keychar <keychar>` :sup:`e`
            * :doc:`$keylparam <keylparam>`
            * :doc:`$keyrpt <keyrpt>` :sup:`e`
            * :doc:`$keyval <keyval>` :sup:`e`
            * :doc:`$knick <knick>` :sup:`e`

    .. tab:: L

        .. hlist::
            :columns: 4

            * :doc:`$lactive <lactive>`
            * :doc:`$lactivecid <lactivecid>`
            * :doc:`$lactivewid <lactivewid>`
            * :doc:`$lcm() <lcm>`
            * :doc:`$left() <left>`
            * :doc:`$leftwin <leftwin>`
            * :doc:`$leftwincid <leftwincid>`
            * :doc:`$leftwinwid <leftwinwid>`
            * :doc:`$len() <len>`
            * :doc:`$level() <level>`
            * :doc:`$lf <lf>`
            * :doc:`$line() <line>`
            * :doc:`$lines() <lines>`
            * :doc:`$link() <link>`
            * :doc:`$lock() <lock>`
            * :doc:`$locked <locked>`
            * :doc:`$lof <lof>`
            * :doc:`$log() <log>`
            * :doc:`$log2() <log2>`
            * :doc:`$log10() <log10>`
            * :doc:`$logdir <logdir>`
            * :doc:`$logstamp <logstamp>`
            * :doc:`$logstampfmt <logstampfmt>`
            * :doc:`$longfn() <longfn>`
            * :doc:`$longip() <longip>`
            * :doc:`$lower() <lower>`
            * :doc:`$ltimer <ltimer>`

    .. tab:: M

        .. hlist::
            :columns: 4

            * :doc:`$maddress <maddress>` :sup:`e`
            * :doc:`$maddress() <maddress>`
            * :doc:`$mask() <mask>`
            * :doc:`$matchkey <matchkey>` :sup:`e`
            * :doc:`$matchtok() <matchtok>`
            * :doc:`$matchtokcs() <matchtokcs>`
            * :doc:`$max <max>`
            * :doc:`$maxlenl <maxlenl>`
            * :doc:`$maxlenm <maxlenm>`
            * :doc:`$maxlens <maxlens>`
            * :doc:`$md5() <md5>`
            * :doc:`$me <me>`
            * :doc:`$menu <menu>` :sup:`e`
            * :doc:`$menubar <menubar>`
            * :doc:`$menucontext <menucontext>` :sup:`e`
            * :doc:`$menutype <menutype>` :sup:`e`
            * :doc:`$mid() <mid>`
            * :doc:`$mididir <mididir>`
            * :doc:`$min <min>`
            * :doc:`$mircdir <mircdir>`
            * :doc:`$mircexe <mircexe>`
            * :doc:`$mircini <mircini>`
            * :doc:`$mircpid <mircpid>`
            * :doc:`$mkfn() <mkfn>`
            * :doc:`$mklogfn() <mklogfn>`
            * :doc:`$mknickfn() <mknickfn>`
            * :doc:`$mnick <mnick>`
            * :doc:`$mode() <mode>`
            * :doc:`$modefirst <modefirst>` :sup:`e`
            * :doc:`$modelast <modelast>` :sup:`e`
            * :doc:`$modespl <modespl>`
            * :doc:`$modinv() <modinv>`
            * :doc:`$mouse <mouse>`
            * :doc:`$mp3() <mp3>`
            * :doc:`$mp3dir <mp3dir>`
            * :doc:`$msfile() <msfile>`
            * :doc:`$msgstamp <msgstamp>` :sup:`e`
            * :doc:`$msgtags <msgtags>` :sup:`e`
            * :doc:`$msgtags() <msgtags>` :sup:`e`

    .. tab:: N

        .. hlist::
            :columns: 4

            * :doc:`$naddress <naddress>` :sup:`e`
            * :doc:`$network <network>`
            * :doc:`$newnick <newnick>` :sup:`e`
            * :doc:`$nhnick() <nhnick>`
            * :doc:`=$nick() <nick_identifier>`
            * :doc:`$nick <nick>` :sup:`e`
            * :doc:`$nick() <nick>`
            * :doc:`$nickmode <nickmode>`
            * :doc:`$no <no>`
            * :doc:`$nofile() <nofile>`
            * :doc:`$nonstdmsg <nonstdmsg>`
            * :doc:`$nopath <nopath>`
            * :doc:`$nopnick() <nopnick>`
            * :doc:`$noqt() <noqt>`
            * :doc:`$not() <not>`
            * :doc:`$notags() <notags>`
            * :doc:`$notify <notify>`
            * :doc:`$notify() <notify>`
            * :doc:`$null <null>`
            * :doc:`$numbits() <numbits>`
            * :doc:`$numeric <numeric>`
            * :doc:`$numtok() <numtok>`
            * :doc:`$nvnick() <nvnick>`

    .. tab:: O

        .. hlist::
            :columns: 4

            * :doc:`$ok <ok>`
            * :doc:`$online <online>`
            * :doc:`$onlineserver <onlineserver>`
            * :doc:`$onlinetotal <onlinetotal>`
            * :doc:`$onpoly() <onpoly>`
            * :doc:`$opnick <opnick>` :sup:`e`
            * :doc:`$opnick() <opnick>`
            * :doc:`$or() <or>`
            * :doc:`$ord() <ord>`
            * :doc:`$os <os>`

    .. tab:: P

        .. hlist::
            :columns: 4

            * :doc:`$parmn <parmn>`
            * :doc:`$parms <parms>`
            * :doc:`$parseem <parseem>`
            * :doc:`$parseline <parseline>` :sup:`e`
            * :doc:`$parsetype <parsetype>` :sup:`e`
            * :doc:`$parseutf <parseutf>` :sup:`e`
            * :doc:`$passivedcc <passivedcc>`
            * :doc:`$pi <pi>`
            * :doc:`$pic() <pic>`
            * :doc:`$play() <play>`
            * :doc:`$pnick <pnick>`
            * :doc:`$port <port>`
            * :doc:`$portable <portable>`
            * :doc:`$portfree() <portfree>`
            * :doc:`$pos() <pos>`
            * :doc:`$poscs() <poscs>`
            * :doc:`$powmod() <powmod>`
            * :doc:`$prefix <prefix>`
            * :doc:`$prop <prop>`
            * :doc:`$protect <protect>`
            * :doc:`$puttok() <puttok>`

    .. tab:: Q

        .. hlist::
            :columns: 4

            * :doc:`$qt() <qt>`
            * :doc:`$query() <query>`

    .. tab:: R

        .. hlist::
            :columns: 4

            * :doc:`$r <r>`
            * :doc:`$raddress <raddress>` :sup:`e`
            * :doc:`$rand() <rand>`
            * :doc:`$rands() <rands>`
            * :doc:`$rawbytes <rawbytes>` :sup:`e`
            * :doc:`$rawmsg <rawmsg>` :sup:`e`
            * :doc:`$read() <read>`
            * :doc:`$readini() <readini>`
            * :doc:`$readn <readn>`
            * :doc:`$regbr <regbr>`
            * :doc:`$regerrstr <regerrstr>`
            * :doc:`$regex() <regex>`
            * :doc:`$regml() <regml>`
            * :doc:`$regmlex() <regmlex>`
            * :doc:`$regsub() <regsub>`
            * :doc:`$regsubex() <regsubex>`
            * :doc:`$remote <remote>`
            * :doc:`$remove() <remove>`
            * :doc:`$removecs() <removecs>`
            * :doc:`$remtok() <remtok>`
            * :doc:`$remtokcs() <remtokcs>`
            * :doc:`$replace() <replace>`
            * :doc:`$replacecs() <replacecs>`
            * :doc:`$replacex() <replacex>`
            * :doc:`$replacexcs() <replacexcs>`
            * :doc:`$reptok() <reptok>`
            * :doc:`$reptokcs() <reptokcs>`
            * :doc:`$result <result>`
            * :doc:`$rgb() <rgb>`
            * :doc:`$right() <right>`
            * :doc:`$rnick() <rnick>`
            * :doc:`$round() <round>`

    .. tab:: S

        .. hlist::
            :columns: 4

            * :doc:`$samepath() <samepath>`
            * :doc:`$scid() <scid>`
            * :doc:`$scon() <scon>`
            * :doc:`$script <script>` :sup:`e`
            * :doc:`$script() <script>`
            * :doc:`$scriptdir <scriptdir>`
            * :doc:`$scriptline <scriptline>`
            * :doc:`$sdir() <sdir>`
            * :doc:`$send() <send>`
            * :doc:`$server() <server>`
            * :doc:`$serverip <serverip>`
            * :doc:`$servertarget <servertarget>`
            * :doc:`$sfile() <sfile>`
            * :doc:`$sha1() <sha1>`
            * :doc:`$sha256() <sha256>`
            * :doc:`$sha384() <sha384>`
            * :doc:`$sha512() <sha512>`
            * :doc:`$shortfn() <shortfn>`
            * :doc:`$show <show>`
            * :doc:`$signal <signal>` :sup:`e`
            * :doc:`$sin() <sin>`
            * :doc:`$sinh() <sinh>`
            * :doc:`$site <site>` :sup:`e`
            * :doc:`$sline() <sline>`
            * :doc:`$snick() <snick>`
            * :doc:`$snicks <snicks>`
            * :doc:`$snotify <snotify>`
            * :doc:`$sock() <sock>`
            * :doc:`$sockbr <sockbr>` :sup:`e`
            * :doc:`$sockerr <sockerr>` :sup:`e`
            * :doc:`$sockname <sockname>` :sup:`e`
            * :doc:`$sorttok() <sorttok>`
            * :doc:`$sorttokcs() <sorttokcs>`
            * :doc:`$sound() <sound>`
            * :doc:`$speak() <speak>`
            * :doc:`$sqrt <sqrt>`
            * :doc:`$sreq() <sreq>`
            * :doc:`$ssl <ssl>`
            * :doc:`$sslcertsha1 <sslcertsha1>`
            * :doc:`$sslcertsha256 <sslcertsha256>`
            * :doc:`$sslcertvalid <sslcertvalid>`
            * :doc:`$ssldll <ssldll>`
            * :doc:`$sslhash() <sslhash>`
            * :doc:`$ssllibdll <ssllibdll>`
            * :doc:`$sslready <sslready>`
            * :doc:`$sslversion <sslversion>`
            * :doc:`$starting <starting>`
            * :doc:`$status <status>`
            * :doc:`$str() <str>`
            * :doc:`$strip() <strip>`
            * :doc:`$stripped <stripped>`
            * :doc:`$style() <style>`
            * :doc:`$submenu() <submenu>`
            * :doc:`$switchbar <switchbar>`
            * :doc:`$sysdir() <sysdir>`

    .. tab:: T

        .. hlist::
            :columns: 4

            * :doc:`$tan() <tan>`
            * :doc:`$tanh() <tanh>`
            * :doc:`$target <target>` :sup:`e`
            * :doc:`$tempfn <tempfn>`
            * :doc:`$tempfn() <tempfn>`
            * :doc:`$ticks <ticks>`
            * :doc:`$ticksqpc <ticksqpc>`
            * :doc:`$time <time>`
            * :doc:`$timeout <timeout>`
            * :doc:`$timer() <timer>`
            * :doc:`$timestamp <timestamp>`
            * :doc:`$timestampfmt <timestampfmt>`
            * :doc:`$timezone <timezone>`
            * :doc:`$tip() <tip>`
            * :doc:`$tips <tips>`
            * :doc:`$titlebar <titlebar>`
            * :doc:`$token <token>`
            * :doc:`$toolbar() <toolbar>`
            * :doc:`$topic <topic>`
            * :doc:`$totp() <totp>`
            * :doc:`$treebar <treebar>`
            * :doc:`$true <true>`
            * :doc:`$trust() <trust>`

    .. tab:: U

        .. hlist::
            :columns: 4

            * :doc:`$ulevel <ulevel>` :sup:`e`
            * :doc:`$ulist() <ulist>`
            * :doc:`$unsafe() <unsafe>`
            * :doc:`$upper() <upper>`
            * :doc:`$uptime() <uptime>`
            * :doc:`$url() <url>`
            * :doc:`$urlget() <urlget>`
            * :doc:`$usermode <usermode>`
            * :doc:`$utfdecode() <utfdecode>`
            * :doc:`$utfencode() <utfencode>`

    .. tab:: V

        .. hlist::
            :columns: 4

            * :doc:`$v1 <v1>`
            * :doc:`$v2 <v2>`
            * :doc:`$var() <var>`
            * :doc:`$vc() <vc>`
            * :doc:`$vcmd() <vcmd>`
            * :doc:`$vcmdstat <vcmdstat>`
            * :doc:`$vcmdver <vcmdver>`
            * :doc:`$version <version>`
            * :doc:`$vnick <vnick>` :sup:`e`
            * :doc:`$vol() <vol>`

    .. tab:: W

        .. hlist::
            :columns: 4

            * :doc:`$wavedir <wavedir>`
            * :doc:`$wid <wid>`
            * :doc:`$width() <width>`
            * :doc:`$wildsite <wildsite>` :sup:`e`
            * :doc:`$wildtok() <wildtok>`
            * :doc:`$wildtokcs() <wildtokcs>`
            * :doc:`$window() <window>`
            * :doc:`$window <window>` :sup:`e`
            * :doc:`$wrap() <wrap>`

    .. tab:: X

        .. hlist::
            :columns: 4

            * :doc:`$xor() <xor>`

    .. tab:: Y

        .. hlist::
            :columns: 4

            * :doc:`$yes <yes>`

    .. tab:: Z

        .. hlist::
            :columns: 4

            * :doc:`$zip() <zip>`

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   *