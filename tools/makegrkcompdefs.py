#!/usr/bin/python3
'''Create composite definitions for complex Greek composites.'''
__url__ = 'http://github.com/silnrsi/font-gentium'
__copyright__ = 'Copyright (c) 2021 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

from silfont.core import execute

argspec = [
    ('input',{'help': 'Input file of CD components in csv format'}, {'type': 'incsv'}),
    ('--style', {'help': 'style'}, {}),
    ('output',{'help': 'Output file of CD in text format'}, {'type': 'outfile', 'def': '_out.txt'})
]

kerns = {
    "GrCapAlpha": { "R": -230, "B": -230, "I": -230, "X": -230 },
    "GrCapEpsilon": { "R": 0, "B": 0, "I": 0, "X": 0 },
    "GrCapEta": { "R": 0, "B": 0, "I": 0, "X": 0 },
    "GrCapIota": { "R": -20, "B": -20, "I": -20, "X": -20 },
    "GrCapOmega": { "R": -65, "B": -65, "I": -65, "X": -65 },
    "GrCapOmicron": { "R": -50, "B": -50, "I": -50, "X": -50 },
    "GrCapRho": { "R": 0, "B": 0, "I": 0, "X": 0 },
    "GrCapUpsilon": { "R": 100, "B": 100, "I": 100, "X": 100 },
    "GrUpsilonWHookSym": { "R": 100, "B": 100, "I": 100, "X": 100 }
}

widths = {
    "GrTonos": { "R": 461, "B": 510, "I": 461, "X": 461 },
    "GrOxia": { "R": 461, "B": 510, "I": 461, "X": 461 },
    "GrVaria": { "R": 454, "B": 505, "I": 454, "X": 454 },
    "GrDasia": { "R": 383, "B": 448, "I": 383, "X": 383 },
    "GrDasiaOxia": { "R": 660, "B": 744, "I": 660, "X": 660 },
    "GrDasiaVaria": { "R": 740, "B": 855, "I": 740, "X": 740 },
    "GrDasiaPeris": { "R": 383, "B": 488, "I": 383, "X": 383 },
    "GrPsili": { "R": 383, "B": 453, "I": 383, "X": 383 },
    "GrPsiliOxia": { "R": 660, "B": 793, "I": 660, "X": 660 },
    "GrPsiliVaria": { "R": 720, "B": 834, "I": 720, "X": 720 },
    "GrPsiliPeris": { "R": 383, "B": 488, "I": 383, "X": 383 },
    "GrDasiaPeris.Por": { "R": 383, "B": 430, "I": 383, "X": 383 },
    "GrPsiliPeris.Por": { "R": 383, "B": 430, "I": 383, "X": 383 }
}

shifts = {
    "GrCapOmicronGrTonos": { "R": 150, "B": 150, "I": 150, "X": 150 },
    "GrCapOmicronGrOxia": { "R": 150, "B": 150, "I": 150, "X": 150 },
    "GrCapOmicronGrDasiaOxia": { "R": 100, "B": 100, "I": 100, "X": 100 },
    "GrCapOmicronGrPsiliOxia": { "R": 100, "B": 100, "I": 100, "X": 100 },
    "GrCapOmegaGrTonos": { "R": 150, "B": 150, "I": 150, "X": 150 },
    "GrCapOmegaGrOxia": { "R": 150, "B": 150, "I": 150, "X": 150 },
    "GrCapOmegaGrDasiaOxia": { "R": 100, "B": 100, "I": 100, "X": 100 },
    "GrCapOmegaGrPsiliOxia": { "R": 100, "B": 100, "I": 100, "X": 100 },
    "GrCapEtaGrDasiaPeris.Por": { "R": -130, "B": -130, "I": -130, "X": -130 },
    "GrCapEtaGrPsiliPeris.Por": { "R": -130, "B": -130, "I": -130, "X": -130 },
    "GrCapIotaGrDasiaPeris.Por": { "R": -110, "B": -110, "I": -110, "X": -110 },
    "GrCapIotaGrPsiliPeris.Por": { "R": -110, "B": -110, "I": -110, "X": -110 },
    "GrCapUpsilonGrDasiaPeris.Por": { "R": -60, "B": -60, "I": -60, "X": -60 }
}

def doit(args) :
    ofile = args.output
    incsv = args.input
    style = args.style

    for line in incsv:
        comb = line[1] + line[2]
        offset = widths[line[2]][style] + kerns[line[1]][style]
        compdef = line[0] + " = " # end glyph name
        compdef += line[1] # 
        if comb in shifts.keys(): 
            compdef += " + " + line[2] + "@G[shift=" + str(shifts[comb][style]) + ",0]"  # diac
            offset -= shifts[comb][style]
        else:
            compdef += " + " + line[2] + "@G"  # diac
        if line[3] != "":
            compdef += " + " + line[3] + "@L"  # ypo
        if line[4] != "":
            compdef += " & " + line[4]  # pros
        compdef += " ^ " + str(offset) + ",0"  # ypo
        if line[5] != "":
            compdef += " |" + line[5]  # usv
        print(compdef)
        ofile.write(compdef +'\n')

    return

def cmd() : execute(None,doit,argspec) 
if __name__ == "__main__": cmd()    
