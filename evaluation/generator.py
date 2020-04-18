import ast
import itertools
import datetime

import pandas as pd

from evaluation.util import timeWithTimeout
from src.generator import Generator
from src.lib import cantusSpec, Spec, firstSpeciesSpec, ConstPitch, secondSpeciesSpec, thirdSpeciesSpec

def generateCanti(powersOfTwo):
    lineLengths = powersOfTwo.copy()
    gamutSizes = powersOfTwo.copy()
    tasks = list(itertools.product(lineLengths, gamutSizes))
    results = []  # (lineLength, GamutSize, time)
    causes = [] #(lineLength, gamutSize, result)
    cfs = [] #(lineLength, gamutSize, result)
    print(tasks)
    for (length, gamut) in tasks:
        print((length, gamut))

        try:
            g = Generator(cantusSpec(length, gamut, ''))
        except Exception:
            causes.append((length, gamut, 'Invalid'))
            continue

        i = 0
        while True:
            if i == 5:
                causes.append((length, gamut, 'over5'))
                break;
            i += 1
            res, runtime = timeWithTimeout(lambda : g.createNew(), 10)

            # No more unique output for task
            if res == []:
                if i==1:
                    causes.append((length, gamut, 'No possible lines'))
                else:
                    causes.append((length, gamut, 'All outputs found'))
                break
            #timeout
            elif res is None:
                causes.append((length, gamut, 'timeout'))
                break
            else:
                out = (length, gamut,i, runtime )
                cfs.append((length, gamut, res))
                results.append(out)

    success = pd.DataFrame(columns=['length', 'gamut', 'iteration', 'times'], data=results)
    fails = pd.DataFrame(columns=['length','gamut','result'], data =causes)
    lines = pd.DataFrame(columns=['length','gamut','line'], data =cfs)
    print(success)
    print(fails)
    print(cfs)
    dt = str(datetime.datetime.now())
    success.to_csv('output/generator/cf/generateCFSuccess_Max:' + str(powersOfTwo[-1]) + "_Time:" + dt + '.csv', index=False,)
    fails.to_csv('output/generator/cf/generateCFFails_Max:' + str(powersOfTwo[-1]) + "_Time:" + dt + '.csv', index=False,)
    lines.to_csv('output/generator/cf/generateCFCFs_Max:' + str(powersOfTwo[-1]) + '.csv', index=False,)

def generateOtherLines(powersOfTwo, specMaker, name):
    lineLengths = powersOfTwo.copy()
    gamutSizes = powersOfTwo.copy()
    tasks = list(itertools.product(lineLengths, gamutSizes))
    results = []  # (lineLength, GamutSize, time)
    causes = [] #(lineLength, gamutSize, result)
    lines = []
    print(tasks)
    for (length, gamut) in tasks:
        print(length,gamut)
        try:
            cf = Generator(cantusSpec(length, gamut, '')).createNew()
            if cf == []:
                causes.append((length, gamut, 'Invalid cf'))
        except Exception:
            causes.append((length, gamut, 'Invalid cf'))
            continue

        try:
            g = Generator(specMaker([ConstPitch(x) for x in cf], gamut, ''))
        except Exception:
            causes.append((length, gamut, 'Invalid species'))
            continue

        i = 0
        while True:
            if i == 5:
                causes.append((length, gamut, 'over5'))
                break;
            i += 1
            res, runtime = timeWithTimeout(lambda : g.createNew(), 10)
            # No more unique output for task
            if res == []:
                if i==1:
                    causes.append((length, gamut, 'No possible species'))
                else:
                    causes.append((length, gamut, 'All outputs found'))
                break
            #timeout
            elif res is None:
                causes.append((length, gamut, 'timeout'))
                break
            else:
                out = (length, gamut,i, runtime )
                lines.append((length, gamut, res))
                results.append(out)

    success = pd.DataFrame(columns=['length', 'gamut', 'iteration', 'times'], data=results)
    fails = pd.DataFrame(columns=['length','gamut','result'], data =causes)
    linesDF = pd.DataFrame(columns=['length','gamut','line'], data =lines)
    print(success)
    print(fails)
    print(lines)
    dt = str(datetime.datetime.now())
    success.to_csv('output/generator/'+name+'/generate'+name+'Success_Max:' + str(powersOfTwo[-1]) + "_Time:" + dt + '.csv', index=False,)
    fails.to_csv('output/generator/'+name+'/generate'+name+'Fails_Max:' + str(powersOfTwo[-1]) + "_Time:" + dt + '.csv', index=False,)
    linesDF.to_csv('output/generator/'+name+'/generate'+name+'Lines_Max:' + str(powersOfTwo[-1]) + '.csv', index=False,)


if __name__ == '__main__':
    po2 = [4,8,12,16,20,24,28,32,36,40]
    generateCanti(po2)
    generateOtherLines(po2,lambda x,y,z : firstSpeciesSpec(x,y,z),'s1')
    generateOtherLines(po2,lambda x,y,z : secondSpeciesSpec(x,y,z),'s2')
    generateOtherLines(po2,lambda x,y,z : thirdSpeciesSpec(x,y,z),'s3')