from src.lib import Spec, getAllBadSpecs, cantusSpec, firstSpeciesSpec, secondSpeciesSpec, thirdSpeciesSpec
from src.repairer import repairCF,repairS1,repairS2,repairS3
from z3.z3 import Optimize, sat
from src.lib.types2.foundry import Foundry
from src.evaluation.util import timeWithTimeout
from src.generator.generator import Generator
from src.lib.types2.pitch.constPitch import ConstPitch
import itertools
import pandas as pd
import datetime

def extractPitch(model,pitch):
    letter = model[pitch.letter].as_long()
    octave = model[pitch.octave].as_long()
    return ConstPitch(letter, octave).flattened()

def doRepair(spec : Spec, check, length, gamut, name):
    specs = getAllBadSpecs(spec=spec, maxCount=5, doShuffle=True,filterOutUnsatisfiable=False) + [spec]
    ret=[]
    for s in specs:
        numMutations = sum([1 if 'inverse' in str(x) else 0 for x in s.constraints])
        # Using this rather than generator because generator is increadibly slow in this
        # context for some reason 
        opt = Optimize()
        for c in s.constraints:
            opt.add(c.formula)
        checked, _ = timeWithTimeout(lambda : opt.check(), 10)
        if(checked == sat):
            line = [extractPitch(opt.model(), p) for p in s.line]
            res, runtime = timeWithTimeout(lambda: check(line), 10)
            if res is not None:
                ret.append((length, gamut, numMutations, runtime))
    return ret

        
def evalCF(toRun):
    name = 'cf'
    print(name)
    lineLengths = toRun.copy()
    gamutSizes = toRun.copy()
    tasks = list(itertools.product(lineLengths, gamutSizes))
    results = [] 
    print(tasks)
    res = []
    for (length, gamut) in tasks:
        print((length, gamut))
        res += doRepair(cantusSpec(length, gamut, ''), lambda x : repairCF(x, gamut+4), length, gamut,name)
    out = pd.DataFrame(columns=['length', 'gamut', 'mutations', 'time'], data=res)
    dt = str(datetime.datetime.now())
    out.to_csv('output/repairer/'+name+'/time_'+dt+'.csv')

def evalOthers(toRun, name, makeSpec, repairFunc):
    print(name)
    lineLengths = toRun.copy()
    gamutSizes = toRun.copy()
    tasks = list(itertools.product(lineLengths, gamutSizes))
    results = [] 
    print(tasks)
    res = []
    for (length, gamut) in tasks:
        try:
            print((length, gamut))
            s = cantusSpec(length, gamut, '')
            opt = Optimize()
            for c in s.constraints:
                opt.add(c.formula)
            checked, _ = timeWithTimeout(lambda : opt.check(), 10)
            if(checked == sat):
                cf = [extractPitch(opt.model(), p) for p in s.line]
                res += doRepair(makeSpec([ConstPitch(x) for x in cf], gamut+4, ''), lambda x : repairFunc(cf, x, gamut+2), length, gamut,name)
        except Exception:
            pass
        
    out = pd.DataFrame(columns=['length', 'gamut','mutations', 'time'], data=res)
    dt = str(datetime.datetime.now())
    out.to_csv('output/repairer/'+name+'/time_'+dt+'.csv')

if __name__ == "__main__":
    run = [4,8]
    #evalCF(run)
    #evalOthers(run, 's1', lambda x,y,z: firstSpeciesSpec(x,y,z), repairS1)
    #evalOthers(run, 's2', lambda x,y,z: secondSpeciesSpec(x,y,z), repairS2)
    #evalOthers(run, 's3', lambda x,y,z: thirdSpeciesSpec(x,y,z), repairS3)