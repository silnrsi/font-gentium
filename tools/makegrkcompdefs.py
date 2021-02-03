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
    "GrCapAlpha": { "R": -230, "B": -230, "I": -220, "X": -220 },
    "GrCapEpsilon": { "R": 0, "B": 0, "I": -33, "X": -33 },
    "GrCapEta": { "R": 0, "B": 0, "I": -33, "X": -33 },
    "GrCapIota": { "R": -20, "B": -20, "I": -53, "X": -53 },
    "GrCapOmega": { "R": -65, "B": -65, "I": -60, "X": -60 },
    "GrCapOmicron": { "R": -50, "B": -50, "I": -40, "X": -40 },
    "GrCapRho": { "R": 0, "B": 0, "I": -33, "X": -33 },
    "GrCapUpsilon": { "R": 100, "B": 100, "I": 60, "X": 60 },
    "GrUpsilonWHookSym": { "R": 100, "B": 100, "I": 60, "X": 60 }
}

widths = {
    "GrTonos": { "R": 461, "B": 510, "I": 480, "X": 480 },
    "GrOxia": { "R": 461, "B": 510, "I": 480, "X": 480 },
    "GrVaria": { "R": 454, "B": 505, "I": 403, "X": 464 },
    "GrDasia": { "R": 383, "B": 448, "I": 340, "X": 417 },
    "GrDasiaOxia": { "R": 660, "B": 744, "I": 580, "X": 730 },
    "GrDasiaVaria": { "R": 740, "B": 855, "I": 623, "X": 752 },
    "GrDasiaPeris": { "R": 383, "B": 488, "I": 340, "X": 445 },
    "GrPsili": { "R": 383, "B": 453, "I": 340, "X": 403 },
    "GrPsiliOxia": { "R": 660, "B": 793, "I": 580, "X": 739 },
    "GrPsiliVaria": { "R": 720, "B": 834, "I": 631, "X": 750 },
    "GrPsiliPeris": { "R": 383, "B": 488, "I": 340, "X": 445 },
    "GrDasiaPeris.Por": { "R": 383, "B": 430, "I": 340, "X": 389 },
    "GrPsiliPeris.Por": { "R": 383, "B": 430, "I": 340, "X": 394 }
}

shifts = {
    "GrCapOmicronGrTonos": { "R": 150, "B": 150, "I": 130, "X": 130 },
    "GrCapOmicronGrOxia": { "R": 150, "B": 150, "I": 130, "X": 130 },
    "GrCapOmicronGrDasiaOxia": { "R": 100, "B": 100, "I": 80, "X": 80 },
    "GrCapOmicronGrPsiliOxia": { "R": 100, "B": 100, "I": 80, "X": 80 },
    "GrCapOmegaGrTonos": { "R": 150, "B": 150, "I": 130, "X": 130 },
    "GrCapOmegaGrOxia": { "R": 150, "B": 150, "I": 130, "X": 130 },
    "GrCapOmegaGrDasiaOxia": { "R": 100, "B": 100, "I": 80, "X": 80 },
    "GrCapOmegaGrPsiliOxia": { "R": 100, "B": 100, "I": 80, "X": 80 },
    "GrCapEtaGrDasiaPeris.Por": { "R": -130, "B": -130, "I": -120, "X": -120 },
    "GrCapEtaGrPsiliPeris.Por": { "R": -130, "B": -130, "I": -120, "X": -120 },
    "GrCapIotaGrDasiaPeris.Por": { "R": -110, "B": -110, "I": -100, "X": -100 },
    "GrCapIotaGrPsiliPeris.Por": { "R": -110, "B": -110, "I": -100, "X": -100 },
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
