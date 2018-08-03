#!/usr/bin/python2
# encoding: utf-8
# this is a smith configuration file

# set the default output folders
# out="results"
# DOCDIR="documentation"
# OUTDIR="installers"
# ZIPDIR="releases"
# STANDARDS = 'standards'

# set the version control system
VCS = 'git'

# set the font name, version, licensing and description
APPNAME="GentiumPlusSIL"
# VERSION="5.701"
# BUILDLABEL = "alpha1"
# COPYRIGHT="Copyright (c) 2007-2018, SIL International (http://www.sil.org)"
# LICENSE = "OFL.txt"
# RESERVEDOFL = "Gentium and SIL"
DESC_SHORT = "Unicode font for Roman- and Cyrillic-based writing systems"

# packaging
# DESC_NAME = "GentiumPlus"
# DEBPKG = 'fonts-sil-gentium'

# set the build and test parameters
# TESTSTRING = u'\u0E07\u0331 \u0E0D\u0331 \u0E19\u0331 \u0E21\u0331'

FONTNAMEBASE="GentiumPlus"
for dspace in ('Roman', 'Italic'):
#for dspace in ['Roman']:
    designspace('source/' + FONTNAMEBASE + dspace + '.designspace',
                target = process('${DS:FILENAME_BASE}.ttf', 
                    cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${DS:FILE}'])),
                # version = VERSION,
                # copyright = COPYRIGHT;
                # license = ofl('GentiumPlus','SIL'),
                ap = 'source/' + '${DS:FILENAME_BASE}_ap.xml',
                opentype = fea('source/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/${DS:FILENAME_BASE}.fea',
                    make_params="--omitaps 'C L11 L12 L13 L21 L22 L23 L31 L32 L33 C11 C12 C13 C21 C22 C23 C31 C32 C33 U11 U12 U13 U21 U22 U23 U31 U32 U33'",
                    ),
                graphite = gdl('source/${DS:FILENAME_BASE}.gdl',
                    master = 'source/graphite/main.gdh', 
                    params = '-e gdlerr-${DS:FILENAME_BASE}.txt',
					),
				woff = woff()
				)
