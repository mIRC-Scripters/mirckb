#!/usr/bin/env python3

import sys
import re
import html
import time
import os

FOLDER_IN = "../mediawiki"
FOLDER_OUT = "../test"

START = time.ctime()

# for loop in directory FOLDER_IN (*.txt)

def main():
	for filename in os.listdir(FOLDER_IN):
	    f = os.path.join(FOLDER_IN, filename)
	    # checking if it is a file
	    if os.path.isfile(f):
	        with open(f, 'r', encoding='utf-8') as y:
	        	print("Now working on: " + f)
	        	filedata = y.read()

	        	# Change the header
	        	result1 = re.sub(r'(?mi)^\{\{mirc title\|(\$\w+) identifier\}\}(.*)$', my_replace1, filedata)
	        	
	        	# if id(filedata) == id(result1): #
	        	# 	with open('status.log', 'a') as l:
	        	# 		l.write("Nothing for result1: " + f + "\n")

	        	# Change the subsections
	        	result2 = re.sub(r'(?m)^(=+) (.*?) \1$', my_replace2, result1)
	        	
	        	# Fix newlines
	        	result3 = re.sub(r'(\n\n)\n+', r'\1', result2)

	        	# Change '''word''' to word
	        	result4 = re.sub(r"'''(.*?)'''", r'\1', result3)
	        	
	        	# See also part
	        	result5 = re.sub(r'(?si)(See also\n--------\n\n)(.*)', my_replace3, result4)		# fires my_replace4!!

	        	# Code block <source lang="mIRC">
	        	result6 = re.sub(r'(?smi)^<source lang="?mIRC"?>(.*?)</source>', my_replace5, result5)

	        	result0 = re.sub(r'(?smi)^<syntaxhighlight lang="?mIRC"?>(.*?)</syntaxhighlight>', my_replace5, result6)

	        	# Code block <pre></pre>
	        	result7 = re.sub(r'(?ms)^<pre>(.*?)</pre>', my_replace5, result0) # was my_replace6

	        	result8 = re.sub(r'(?mi)^\{\{Deprecated feature\|new=\{\{mirc\|\$(\w+).*?\}\}\}\}', '.. attention:: This feature has essentially been replaced by :doc:`$' + r'\1' + ' </identifiers/' + r'\1' + '>`\n\n', result7)

	        	result10 = re.sub(r'(?s)(Parameters\n----------\n)(.*?\n\n)' , my_replace10, result8)

	        	result20 = re.sub(r'(?s)(Properties\n----------\n)(.*?\n\n)' , my_replace11, result10)

	        	result21 = re.sub(r'(?mi)^\{\{mIRC compatibility\|(.*?)\}\}', my_replace12, result20)

	        	result22 = re.sub(r'(?s)(Results\n-------\n)(.*?\n\n)' , my_replace18, result21)
	        	
	        	# Fix newlines
	        	result99 = re.sub(r'(\n\n)\n+', r'\1', result22)

	        	# Cleanup
	        	result100 = re.sub(r'\[\[Category:mIRC identifiers(?:\|.*?)?\]\]', r'', result99)
	        	result101 = re.sub(r'\{\{mIRC identifier list\}\}', r'', result100)
	        	result102 = re.sub(r'      - Description\n\n', r'      - Description\n', result101)
	        	result103 = re.sub(r'\{\{collist\n\|count = \d\n\|style = width: \d+%; display: inherit;\n\|\n', r'', result102)
	        	result104 = re.sub(r'(?m)^\}\}$', r'', result103)
	        	result105 = re.sub(r'\[\[(\w+)\]\]', r'\1', result104)
	        	result106 = re.sub(r'(?m)^(    \* :doc:.*?)\n\n', r'\1\n', result105)
	        	result107 = re.sub(r'(?m)^\* (?:\[\[)?List of identifiers.*(?:\]\])?$', '', result106)
	        	result108 = re.sub(r'(?i)\{\{mirc\|wildcard(?:\|.*?)?\}\}', ':ref:`matching_tools-wildcard`', result107)
	        	result109 = re.sub(r"(?im)^(You can use the letter 'e' or 'd' as )(.*)$", '.. note:: ' + r'\1' + '``' + r'\2' + '``', result108)
	        	result110 = re.sub(r'(?i)(\{\{mirc\|regex(?:\|\w+)?\}\})', ':ref:`matching_tools-regex`', result109)
	        	result111 = re.sub(r'(?i)<br/>|<br />', '', result110)
	        	result112 = re.sub(r'(?m)^\* List of commands.*$', '', result111)
	        	result113 = re.sub(r'(?sm)^\{\{ ?ArgsList\n(.*?)\n\n', my_replace14, result112)
	        	result114 = re.sub(r'(?i)\{\{mirc\|\$(\w+)(?:\|.*?)?\}\}', ':doc:`$' + r'\1' + ' </identifiers/' + r'\1' + '>`', result113)
	        	result115 = re.sub(r'(?i)(?<!\* )\{\{mIRC\|on events/on (unban|ban|filesent|sendfail|agent|getfail|filercvd|exit|input|parseline|dns)\|on \1(?: event)?\}\}', ':doc:`on ' + r'\1' + ' </events/on_' + r'\1' + '>`', result114)
	        	result116 = re.sub(r'(?im)^\* \{\{mIRC\|on events/on (unban|ban|filesent|sendfail|agent|getfail|filercvd|exit|input|parseline|dns)\|on \1(?: event)?\}\}', '    * :doc:`on ' + r'\1' + ' </events/on_' + r'\1' + '>`', result115)
	        	result117 = re.sub(r'(?i)(?<!\* )\{\{mirc\|on (\w+)\}\}', ':doc:`on ' + r'\1' + ' </events/on_' + r'\1' + '>`', result116)
	        	result118 = re.sub(r'(?im)^\* \{\{mirc\|on (\w+)\}\}', '    * :doc:`on ' + r'\1' + ' </events/on_' + r'\1' + '>`', result117)
	        	result119 = re.sub(r'(?i)(\{\{mirc\|msl_injection(?:\|\w+)?\}\})', ':doc:`injection </beginner/injection>`', result118)
	        	result120 = re.sub(r'(?i)(?<!\* )\[\[List of on events - mIRC(?:\|.*?)?\]\]', ':doc:`events </events/index_events>`', result119)
	        	result130 = re.sub(r'(?im)^\* \[\[List of on events - mIRC(?:\|.*?)?\]\]', '    * :doc:`events </events/index_events>`', result120)
	        	result121 = re.sub(r'(?i)\[\[Picture Windows - mIRC(?:\|.*?)?\]\]', ':ref:`picture_windows`', result130)
	        	result122 = re.sub(r'(?sm)^\{\| class="wikitable" style="margin-left: \d+px;"\n\|-\n! Property !! Description\n\|-\n(.*?)\|\}$', my_replace15, result121)
	        	result123 = re.sub(r'(?sm)^\{\| class="wikitable"\n\|-\n! Value !! Method\n\|-\n(.*?)\|\}$', my_replace15, result122)
	        	result124 = re.sub(r'(?sm)^\{\| class="wikitable"\n\|-\n! Type !! Description !! Values ?\n\|-\n(.*?)\|\}$', my_replace16, result123)

	        	result140 = re.sub(r'(?i)\{\{mIRC\|COM(?:\|.*?)?\}\}', ':doc:`com </advanced/com>`', result124)
	        	result141 = re.sub(r'(?mi)^\* \[\[/menubar command - mIRC\|/command\]\]', '    * :doc:`/menubar </commands/menubar>`', result140)
	        	result142 = re.sub(r'(?i)\{\{mirc\|/(\w+)\}\}', ':doc:`$' + r'\1' + ' </commands/' + r'\1' + '>`', result141)
	        	result143 = re.sub(r'(?i){{mirc\|binary variables(?:\|.*?)?\}\}', ':ref:`binary_variables`', result142)
	        	result144 = re.sub(r'\* \[https://dzwoneknatelefon.com/ dzwonki na telefon\]\n', '', result143)
	        	result145 = re.sub(r'(?i)(?<!\* )\{\{mIRC\|playing music(?:\|\w+)?\}\}', ':doc:`playing music </other/playing_music>`', result144)
	        	result146 = re.sub(r'(?i)\* \{\{mIRC\|playing music(?:\|\w+)?\}\}', '    * :doc:`playing music </other/playing_music>`', result145)
	        	result147 = re.sub(r'(?i)\{\{mIRC\|msl_injection#\$calc\(\)\}\}', ':ref:`injection-calc`', result146)
	        	result148 = re.sub(r'(?i)\{\{mirc\|/(\w+)\|(.*?)\}\}', ':doc:`' + r'\2' + ' </commands/' + r'\1' + '>`', result147)
	        	
	        	result149 = re.sub(r'(?i)(?<!\* )\{\{mirc\|string manipulation\}\}', ':doc:`string manipulation </beginner/string_and_token_manipulation>`', result148)
	        	result150 = re.sub(r'(?im)^\* \{\{mirc\|string manipulation\}\}', ':doc:`string manipulation </beginner/string_and_token_manipulation>`', result149)

	        	result151 = re.sub(r'(?i)(?<!\* )\{\{{{mirc\|custom windows\}\}', ':ref:`custom_windows`', result150)
	        	result152 = re.sub(r'(?im)^\* \{\{{{mirc\|custom windows\}\}', '    * :ref:`custom_windows`', result151)

	        	result153 = re.sub(r'(?i)\* \{\{mirc\|identifiers(?:\|.*?)?\}\}\n', '', result152)
	        	result154 = re.sub(r'(?i)\{\{mirc\|sendmessage(?:\|.*?)?\}\}', ':doc:`/advanced/sendmessage>`', result153)
	        	result155 = re.sub(r'(?i)\{\{mirc\|Internal \w+ list\|(.*?)\}\}', r'\1', result154)
	        	
	        	result156 = re.sub(r'(?i)\{\{mirc\|picture windows?.*?\}\}', ':ref:`picture_windows', result155)

	        	# Notes
	        	result200 = re.sub(r'(?mi)^(?:\*|\* )?Note: (.*)$', '.. note:: ' + r'\1\n', result156)

	        	result997 = re.sub(r'\[\[([^]]*?)\]\]', r'\1', result200)
	        	result998 = re.sub(r'(?m)(^)(\.\. compatibility:: .*)$', r'\n\2', result997)

	        	# Fix spaces anomaly
	        	result999 = re.sub(r'(?m)^(\.\. code:: text\n\n)\x20{4}\n', r'\1', result998)
	        	result1000 = re.sub(r'\n\x20{4}(\n\n)', r'\1', result999)

	        	# Fix newlines
	        	result1001 = re.sub(r'(\n\n)\n+', r'\1', result1000)

	        	h = os.path.join(FOLDER_OUT, filename + ".rst")

	        	with open(h, 'w', encoding='utf-8') as i:
	        		i.write(result1001)


def my_replace19(m):
	ret = '$' + m.group(1) + 'cs'
	return ret + "\n" + '=' * len(ret) + "\n\n" + '..include::`</identifiers/' + m.group(1) + '>`'

def my_replace18(m):
	ret = m.group(1) + '\n.. list-table::\n    :widths: 15 85\n    :header-rows: 1\n\n    * - Value\n      - Description\n' + m.group(2)
	ret = re.sub(r'(?m)^<span style=\"display: inline-block; width: \d+px;\">(.*?)</span>(.*)$', my_replace13, ret)
	ret = ret + '\n'
	return ret

def my_replace17(m):
	ret = "    * - " + m.group(1) + "\n" + "      - " + m.group(2) + "\n" + "      - " + m.group(3)
	return ret

def my_replace16(m):
	ret = '\n.. list-table::\n    :widths: 15 30 55\n    :header-rows: 1\n\n    * - Type\n      - Description\n      - Value\n'
	ret = ret + re.sub(r'(?m)^\|(.*?) \|\| (.*?) \|\| (.*)$', my_replace17, m.group(1))
	ret = re.sub(r'(?m)^\|-\n', '', ret)
	return ret

def my_replace15(m):
	ret = '\n.. list-table::\n    :widths: 15 85\n    :header-rows: 1\n\n    * - Value\n      - Method\n'
	ret = ret + re.sub(r'(?m)^\| (.*?) \|\| (.*?)$', my_replace13, m.group(1))
	ret = re.sub(r'(?m)^\|-\n', '', ret)
	return ret

def my_replace14(m):
	ret = '\n.. list-table::\n    :widths: 15 85\n    :header-rows: 1\n\n    * - Argument\n      - Description\n'
	ret = ret + re.sub(r'(?m)^\| (.*?) \| (.*?)$', my_replace13, m.group(1))
	ret = ret + '\n\n'
	return ret

def my_replace12(m):
	ret = ".. compatibility:: " + m.group(1) + "\n"
	return ret

def my_replace11(m):
	ret = m.group(1) + m.group(2)

	if m.group(2) == '\nNone\n\n':
		ret = m.group(1) + m.group(2)

	elif m.group(2) == 'None\n\n':
		ret = m.group(1) + '\nNone\n\n'

	else:
		ret = m.group(1) + '\n.. list-table::\n    :widths: 15 85\n    :header-rows: 1\n\n    * - Property\n      - Description\n' + re.sub(r'(?m)^(\*) (.*?) (-) (.*)$', r'    \1 \3 \2\n      \3 \4', m.group(2))
		ret = re.sub(r'(?m)^(?:: )?<span style="display: inline-block; width: \d+px;">(.*?)</span>(.*?)$', my_replace13, ret)
		ret = ret + '\n'

	return ret

def my_replace13(m):
	ret = "    * - " + m.group(1) + "\n" + "      - " + m.group(2)
	return ret

# Parameters
def my_replace10(m):
	ret = m.group(1) + m.group(2)

	if m.group(2) == '\nNone\n\n':
		ret = m.group(1) + m.group(2)

	elif m.group(2) == 'None\n\n':
		ret = m.group(1) + '\nNone\n\n'

	else:
		ret = m.group(1) + '\n.. list-table::\n    :widths: 15 85\n    :header-rows: 1\n\n    * - Parameter\n      - Description\n' + re.sub(r"(?m)^:?(\*) (.*?) (-) (?:'')?(.*?)(?:'')?$", r'    \1 \3 \2\n      \3 \4', m.group(2))
		ret = re.sub(r'(?m)^<span style="display: inline-block; width: \d+px;">(.*?)</span>(.*?)$', my_replace13, ret)
		ret = ret + '\n'

	return ret

def my_replace6(m):
	ret = "\n.. code:: text\n\n    "
	
	ret = ret + m.group(1) + "\n"

	return ret

def my_replace5(m):
	ret = "\n.. code:: text\n\n"

	ret = ret + re.sub(r"(?m)^", r"    ", m.group(1)) + "\n"

	return ret

def my_replace1(m):
	return m.group(1) + "\n" + '=' * len(m.group(1)) + "\n\n" + m.group(2) + '\n'

def my_replace2(m):
	g2 = m.group(2)

	if g2 == 'Paramters':
		g2 = 'Parameters'

	if g2 == 'See Also':
		g2 = 'See also'

	if len(m.group(1)) == 2:
		ret = '-'

	elif len(m.group(1)) == 3:
		ret = '^'

	elif len(m.group(1)) == 4:
		ret = '~'

	else:
		ret = 'my_replace2'

	return g2 + "\n" + ret * len(g2) + "\n\n"

def my_replace3(m):
	ret = m.group(1) + '.. hlist::\n' + '    :columns: 4\n\n' + re.sub(r'(?i)(\* )?\{\{mIRC\|(\$|/)(.*?)\}\}?', my_replace4, m.group(2)) 

	return ret

def my_replace4(m):
	if m.group(1):
		ret = '    * '
	
	else: 
		ret = '    * '

	if m.group(2) == '$':
		ret = ret + ':doc:`$' + m.group(3) + ' </identifiers/' + m.group(3) + '>`'

	elif m.group(2) == '/':
		ret = ret + ':doc:`/' + m.group(3) + ' </commands/' + m.group(3) + '>`'

	return ret

main()
