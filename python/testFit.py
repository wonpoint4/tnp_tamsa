import config.AFBMuon_v17 as tnpConf
from fitUtils import tnpFitter
target="2018_MediumID_LooseTrkIso"
config=tnpConf.Configs[target]
config.path="results/AFBMuon_v17/"+target
for i in [0,477]:
    configs=config.make_systematics()
    fitter=tnpFitter(configs[0][0].clone(isSim=False))
    fitter.run(i)
