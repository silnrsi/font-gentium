
#!/usr/bin/python3
'''
Make ftml tests for Greek combinataions based on content of grk_compose.feax
Hacky script intended for rare usage. There's no cli, so edit strings below if needed.
'''

# __url__ = 'http://github.com/silnrsi/font-gentium'
__copyright__ = 'Copyright (c) 2024 SIL Global  (https://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Alan Ward'

import re
import silfont.ufo as ufo

ufo_fn = r"../source/masters/Gentium-Regular.ufo"
feax_fn = r"../source/opentype/grk_compose.feax"
ftml_fn = r"greekrecompose.ftml"

ftml_template = '''
    <test label=\"{}\">
      <string>{}</string>
    </test>
'''[1:]
# The above template should match XML like this:
# <test label="1FB9+0308">
#   <string>\u001FB9\u000308</string>
# </test>

ftml_start = '''
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="../tools/ftml.xsl" type="text/xsl"?>
<ftml version="1.0">
  <head>
    <fontscale>200</fontscale>
    <fontsrc label="GR">url(../results/Gentium-Regular.ttf)</fontsrc>
    <fontsrc label="GM">url(../results/Gentium-Medium.ttf)</fontsrc>
    <fontsrc label="GS">url(../results/Gentium-SemiBold.ttf)</fontsrc>
    <fontsrc label="GB">url(../results/Gentium-Bold.ttf)</fontsrc>
    <fontsrc label="GXB">url(../results/Gentium-ExtraBold.ttf)</fontsrc>
    <fontsrc label="GI">url(../results/Gentium-Italic.ttf)</fontsrc>
    <fontsrc label="GMI">url(../results/Gentium-MediumItalic.ttf)</fontsrc>
    <fontsrc label="GSI">url(../results/Gentium-SemiBoldItalic.ttf)</fontsrc>
    <fontsrc label="GBI">url(../results/Gentium-BoldItalic.ttf)</fontsrc>
    <fontsrc label="GXBI">url(../results/Gentium-ExtraBoldItalic.ttf)</fontsrc>
    <fontsrc label="GRv6">url(../references/v6200/GentiumPlus-Regular.ttf)</fontsrc>
    <fontsrc label="GIv6">url(../references/v6200/GentiumPlus-Italic.ttf)</fontsrc>
    <title>Greek combinations</title>
  </head>
  <testgroup label="Greek recomposition">
'''[1:]

ftml_end = '''
  </testgroup>
</ftml>
'''[1:]

# build dict to map glyph names to unicode values
name_to_unicode = {}
ufo_f = ufo.Ufont(ufo_fn)
for g_name in ufo_f.deflayer:
    ufo_g = ufo_f.deflayer[g_name]
    unicode_lst = ufo_g['unicode'] # list of USV strings
    if unicode_lst:
        usv_str = unicode_lst[0].hex # store first USV string
        # name_to_unicode.setdefault(g_name, []).append(usv_str)
        name_to_unicode[g_name] = usv_str

# extract many-to-one substitution rules from feax
# for example: sub GrCapAlpha CombRevCommaAbv by GrCapAlphaWDasia;
feax_f = open(feax_fn, "r")
feax = feax_f.readlines()
feax_f.close()

ftml_f = open(ftml_fn, "w")
ftml_f.write(ftml_start)

for l in feax:
    field = re.split(r"\W+", l) # first field of matching lines will contain white space
    glyph_lst = []
    if field[1] == "sub" and field[3] != "by": # excludes one-to-many sub rules
        for s in field[2:]: # slice off leading white space and 'sub'
            if s == "by":
                break
            else:
                glyph_lst.append(s)
    else:
        continue

    #write ftml lines to output file
    # unicode_lst = [name_to_unicode[x][0] for x in glyph_lst]
    unicode_lst = [name_to_unicode[x] for x in glyph_lst]
    test_label = "+".join(unicode_lst) # joing USVs with '+'
    test_string = "".join([f"\\u{x:0>6}" for x in unicode_lst]) # USVs with six digits and leading zeroes
    ftml_test_str = ftml_template.format(test_label, test_string) # slice of leading nl
    ftml_f.write(ftml_test_str)

ftml_f.write(ftml_end)
ftml_f.close()
