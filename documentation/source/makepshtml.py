#!/usr/bin/env python
'''Process font documentation .md files for use on product sites '''
__url__ = 'https://github.com/silnrsi/fontdocs'
__copyright__ = 'Copyright (c) 2021-2026 SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Bobby de Vos'

import re
from silfont.core import execute

argspec = [
    ('infile', {'help': 'Input .html filename'}, {'type': 'infile'}),
    ('outfile',{'help': 'Output .html filename'}, {'type': 'outfile'})
]

def doit(args):
    infile = args.infile
    outfile = args.outfile

    inpara = False
    inrtlpara = False

    temptext = ""

    # Remove some attributes from some elements
    for line in infile:
        if line.startswith("<p>"):
            temptext += line.replace("<p>", "").replace("</p>", "\n")
            continue
        if line.startswith("<p "):
            inrtlpara = True
        if "</p>" in line:
            if inrtlpara:
                temptext += line
                inrtlpara = False
            else:
                temptext += line.replace("</p>", "\n")
            continue
        if line.startswith("<tr class"):
            # not needed for pandoc 3.8.2.1
            temptext = temptext + "<tr>\n"
            continue
        if line.startswith("<section") or line.startswith("<aside"):
            # see below for which versions of pandoc generate which tag
            temptext = temptext + '<div class="footnotes">\n'
            continue
        temptext = temptext + line

    # Match WordPress style HTML
    replacements = [
        ('<p>', '\n'), # only need in lists
        # ('</p>', '\n'),
        ('</h2>', '</h2>\n'),
        ('</h3>', '</h3>\n'),
        ('</h4>', '</h4>\n'),
        ('</h5>', '</h5>\n'),
        ('</h6>', '</h6>\n'),
        ('</table>', '</table>\n'),
        ('</ol>', '</ol>\n'),
        ('</ul>', '</ul>\n'),
        ('</pre>', '</pre>\n'),
        ('<hr />', '<hr />\n'),
        ('</blockquote>', '</blockquote>\n'),
        ('</aside>', '</div>\n'), # needed for pandoc version 3.1.3
        ('</section>', '</div>\n'), # needed for pandoc version at least 3.3 and later
    ]
    for replacement in replacements:
        temptext = temptext.replace(replacement[0], replacement[1])
    outfile.write(temptext)

    return


def cmd() : execute(None,doit, argspec)
if __name__ == "__main__": cmd()
