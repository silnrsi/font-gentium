README
Gentium Plus v5.000
========================

This file describes the Graphite source files included with the Gentium Plus font family. This information should be distributed along with the Gentium Plus fonts and any derivative works.

These files are from the Gentium project (https://software.sil.org/gentium/).
Copyright (c) 2003-2021 SIL International (https://www.sil.org/) with Reserved
Font Names "Gentium" and "SIL". This Font Software is licensed under the SIL
Open Font License, Version 1.1 (https://scripts.sil.org/OFL).
            
gentium.gdl              - definition of glyphs and glyph classes; auto-generated from the font
main.gdh              - bulk of Graphite rules and extra definitions to support them
features.gdh          - feature and language-feature definitions
pitches.gdh           - rules and definitions to support tone ligatures
greek_recompose.gdh   - rules to recompose decomposed Greek
takes_lowProfile.gdh  - definitions to support low-profile feature; auto-generated
fontSpecific.gdh      - font-specific definition for Gentium
stddef.gdh            - standard GDL abbreviations
kern.gdh              - kerning values and rules

In order to modify the Graphite tables in this font:
* Strip out the existing tables
  Using the Font-TTF-Scripts package ( https://scripts.sil.org/FontUtils ), you could use something like:
    ttftable -delete graphite old-font-with-Graphite-tables.ttf  new-font-without-Graphite-tables.ttf 
* Run:
    grcompiler -d -v2 -n2048 -w3521 -w510 font.gdl ttf-file-with-Graphite-tables-stripped.ttf output-ttf.ttf
          
Further detail of features is available in the file /source/opentype/featureinfo.xlsx
