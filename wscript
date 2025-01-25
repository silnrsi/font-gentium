#!/usr/bin/python3
# this is a smith configuration file

# set the default output folders for release docs
DOCDIR = ["documentation", "web"]

STANDARDS = 'references/CI_861'

APPNAME = 'Gentium'
sourcefontfamily = APPNAME
DEBPKG = 'fonts-sil-gentium'

TESTDIR = ["tests", "../font-latin-private/tests"]

# Get VERSION and BUILDLABEL from Regular UFO; must be first function call:
getufoinfo('source/masters/' + sourcefontfamily + '-Regular' + '.ufo')

ftmlTest('tools/ftml-smith.xsl')

opts = preprocess_args({'opt': '--quick'})

# APs to ignore when generating OT and GDL classes
omitapps = '--omitaps "C _C L11 L12 L13 L21 L22 L23 L31 L32 L33 ' + \
                'C11 C12 C13 C21 C22 C23 C31 C32 C33 U11 U12 U13 U21 U22 U23 U31 U32 U33"'

cmds = []
cmds.append(cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']))
cmds.append(cmd('${TTFAUTOHINT} -n -W --reference=../source/autohinting/GentiumAutohintingRef-Regular.ttf ${DEP} ${TGT}'))

for dspace in ('Roman', 'Italic'):
    designspace('source/' + sourcefontfamily + dspace + '.designspace',
                target = process('${DS:FILENAME_BASE}.ttf', *cmds),
                instances = ['Gentium Regular'] if '--quick' in opts else None,
#                classes = 'source/${DS:FAMILYNAME_NOSPC}_classes.xml', #fails for Book fonts
                classes = 'source/classes.xml',
                opentype = fea('source/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/main.feax',
                    make_params = omitapps,
                    depends = ('source/opentype/gsub.feax', 
                        'source/opentype/gpos.feax', 
                        'source/opentype/gdef.feax'),
                    mapfile = 'source/${DS:FILENAME_BASE}.map',
                    to_ufo = 'True' # copies to instance UFOs
                    ),
                typetuner = typetuner('source/typetuner/feat_all.xml'),
                woff = woff('web/${DS:FILENAME_BASE}.woff',
                    metadata=f'../source/gentium-WOFF-metadata.xml'),
                version = VERSION,
                shortcircuit = False,
#                pdf=fret(params = '-r -oi')
                )

bookpackage = package(appname = "GentiumBook", docdir = {"documentation": "documentation", "web_book": "web"})
bookfamily = "GentiumBook"

getufoinfo('source/masters/' + sourcefontfamily + '-Regular' + '.ufo', bookpackage)

for dspace in ('Roman', 'Italic'):
    designspace('source/' + bookfamily + dspace + '.designspace',
                target = process('${DS:FILENAME_BASE}.ttf', *cmds),
                instances = [] if '--quick' in opts else None,
                classes = 'source/classes.xml',
                opentype = fea('source/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/main.feax',
                    make_params = omitapps,
                    depends = ('source/opentype/gsub.feax', 
                        'source/opentype/gpos.feax', 
                        'source/opentype/gdef.feax'),
                    mapfile = 'source/${DS:FILENAME_BASE}.map',
                    to_ufo = 'False' # copies to instance UFOs
                    ),
                typetuner = typetuner('source/typetuner/feat_all.xml'),
                woff = woff('web_book/${DS:FILENAME_BASE}.woff',
                    metadata=f'../source/gentiumbook-WOFF-metadata.xml',
                    dontship=True),
                version = VERSION,
                shortcircuit = False,
                package = bookpackage
                )

def configure(ctx):
    ctx.find_program('ttfautohint')
