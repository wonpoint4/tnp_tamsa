from tnpConfig import tnpConfig

############## samples ################
muondir = '/eos/cms/store/group/phys_muon/wjun/Run3_POGntuples_won/'
samples={
    'data2022preEE' : muondir+'data_2022preEE/',
    'amc2022preEE'  : muondir+'amc_2022preEE/',
    'mg2022preEE'   : muondir+'mg_2022preEE/',

    'data2022postEE' : muondir+'data_2022postEE/',
    'amc2022postEE'  : muondir+'amc_2022postEE/',
    'mg2022postEE'   : muondir+'mg_2022postEE/',

    'data2023preBPix' : muondir+'data_2023preBPix/',
    'amc2023preBPix'  : muondir+'amc_2023preBPix/',
    'mg2023preBPix'   : muondir+'mg_2023preBPix/',

    'data2023postBPix' : muondir+'data_2023postBPix/',
    'amc2023postBPix'  : muondir+'amc_2023postBPix/',
    'mg2023postBPix'   : muondir+'mg_2023postBPix/',
}

############## binning ################
binnings={
    'ID':[              ### For ID or ISO
        { 'var' : 'fabs(probe_eta)' , 'type': 'float', 'bins': [0., 0.9, 1.2, 2.1, 2.4], 'title':'|#eta|' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [15, 20, 25, 30, 40, 50, 60, 120], 'title':'p_{T} [GeV]' },
    ],
    'IsoMu24':[         ### For IsoMu24
        { 'var' : 'fabs(probe_eta)' , 'type': 'float', 'bins': [0., 0.9, 1.2, 2.1, 2.4], 'title':'|#eta|' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [26, 30, 40, 50, 60, 120, 200], 'title':'p_{T} [GeV]' },
    ],
    'Mu50':[            ### For Mu50s = (Mu50 || CascadeMu100 || HighPtTkMu100)
        { 'var' : 'fabs(probe_eta)' , 'type': 'float', 'bins': [0., 0.9, 1.2, 2.1, 2.4], 'title':'|#eta|' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [52, 56, 60, 120, 200], 'title':'p_{T} [GeV]' },
    ],
}

############## Expr ###################
## variables
tag_PFIso = '(tag_pfIso04_charged + max(0, tag_pfIso04_neutral+tag_pfIso04_photon-(0.5 * tag_pfIso04_sumPU)))/tag_pt'
probe_PFIso = tag_PFIso.replace('tag','probe')

############## fit functions ##########
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.8,0.5,3.5])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.4,0.8,2.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, aExpoP[-0.1, -1,0.1])",
    "Exponential::bkgFail(x, aExpoF[-0.35, -1,0.1])",
]
fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "RooCBShape::sigResPass(x,meanCBP[0.0,-5.0,5.0],sigmaP[0.8,0.5,3.5],aCBP[2.0, 1.2,3.5],nCBP[3, -5,5])",
    "RooCBShape::sigResFail(x,meanCBF[0.0,-5.0,5.0],sigmaF[1.4,0.8,2.0],aCBF[2.0, 1.2,3.5],nCBF[3, -5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant aCBP nCBP aCBF nCBF",
    "Exponential::bkgPass(x, aExpoP[-0.1, -1,0.1])",
    "Exponential::bkgFail(x, aExpoF[-0.35, -1,0.1])",
]
fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.8,0.5,3.5])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.4,0.8,2.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[60., 50.,80.],bCMSP[0.03, 0.01,0.05],cCMSP[0.1, -0.1,1.0],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[61.5, 50.,80.],bCMSF[0.03, 0.01,0.05],cCMSF[0.03, -0.1,1.0],peakCMSF[90.0])",
]

############## Configs ################
### ID                                                                                                                                                   
config_id=tnpConfig(
    data=samples['data2022preEE'],
    sim=samples['amc2022preEE'],
    sim_weight='(genWeight)',
    sim_maxweight=10000.,
    sim_genmatching='tag_isMatchedGen && probe_isMatchedGen',
    sim_genmass="genMass",
    tree='muon/Events',
    mass="pair_mass",
    bins=binnings['ID'],
    preselection='probe_isTracker',
    expr='tag_HLT_IsoMu24_v && tag_pt > 26 && tag_isTight && '+tag_PFIso+' < 0.15 && tag_charge*probe_charge < 0 && probe_isTracker && pair_dR > 0.3',
    test='probe_isTight',
    hist_nbins=60,
    hist_range=(70,130),
    method='fit',
    fit_parameter= fit_nominal,
    fit_range=(70,130),
    systematic=[
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altMC', 'sim.replace':[('amc','mg')]}],
        [{'title':'tagiso010','expr.replace':(tag_PFIso+' < 0.15',tag_PFIso+' < 0.10')},
         {'title':'tagiso020','expr.replace':(tag_PFIso+' < 0.15',tag_PFIso+' < 0.20')}],
        [{'title':'massbroad','fit_range':(60,130),'hist_range':(60,130)},
         {'title':'massnarrow','fit_range':(70,120)}],
        [{'title':'massbin50','hist_nbins':50},
         {'title':'massbin75','hist_nbins':75}],
    ]
)

### ISO
config_iso=config_id.clone(
    preselection='probe_isTight',
    expr='tag_HLT_IsoMu24_v && tag_pt > 26 && tag_isTight && '+tag_PFIso+' < 0.15 && tag_charge*probe_charge < 0 && probe_isTight && pair_dR > 0.3',
    test=probe_PFIso+' < 0.15',
)

### IsoMu24
config_IsoMu24=config_id.clone(
    bins=binnings['IsoMu24'],
    preselection='probe_isTight && '+probe_PFIso+' < 0.15',
    expr='tag_HLT_IsoMu24_v && tag_pt > 26 && tag_isTight && '+tag_PFIso+' < 0.15 && tag_charge*probe_charge < 0 && probe_isTight && pair_dR > 0.3',
    test='probe_HLT_IsoMu24_v',
)

### Mu50s
config_Mu50=config_IsoMu24.clone(
    bins=binnings['Mu50'],
    test='probe_HLT_Mu50_v || probe_HLT_CascadeMu100_v || probe_HLT_HighPtTkMu100_v',
)

############## Configs ################
Configs={}

## 2022 preEE - BCD
Configs["2022preEE_ID"]=config_id.clone()
Configs["2022preEE_ISO"]=config_iso.clone()
Configs["2022preEE_IsoMu24"]=config_IsoMu24.clone()
Configs["2022preEE_Mu50"]=config_Mu50.clone()

## 2022 postEE - EFG
Configs["2022postEE_ID"]=config_id.clone(
    data=samples['data2022postEE'],
    sim=samples['amc2022postEE'],
)
Configs["2022postEE_ISO"]=config_iso.clone(
    data=samples['data2022postEE'],
    sim=samples['amc2022postEE'],
)
Configs["2022postEE_IsoMu24"]=config_IsoMu24.clone(
    data=samples['data2022postEE'],
    sim=samples['amc2022postEE'],
)
Configs["2022postEE_Mu50"]=config_Mu50.clone(
    data=samples['data2022postEE'],
    sim=samples['amc2022postEE'],
)

## 2023 preBPix - BC
Configs["2023preBPix_ID"]=config_id.clone(
    data=samples['data2023preBPix'],
    sim=samples['amc2023preBPix'],
)
Configs["2023preBPix_ISO"]=config_iso.clone(
    data=samples['data2023preBPix'],
    sim=samples['amc2023preBPix'],
)
Configs["2023preBPix_IsoMu24"]=config_IsoMu24.clone(
    data=samples['data2023preBPix'],
    sim=samples['amc2023preBPix'],
)
Configs["2023preBPix_Mu50"]=config_Mu50.clone(
    data=samples['data2023preBPix'],
    sim=samples['amc2023preBPix'],
)

## 2023 postBPix - D
Configs["2023postBPix_ID"]=config_id.clone(
    data=samples['data2023postBPix'],
    sim=samples['amc2023postBPix'],
)
Configs["2023postBPix_ISO"]=config_iso.clone(
    data=samples['data2023postBPix'],
    sim=samples['amc2023postBPix'],
)
Configs["2023postBPix_IsoMu24"]=config_IsoMu24.clone(
    data=samples['data2023postBPix'],
    sim=samples['amc2023postBPix'],
)
Configs["2023postBPix_Mu50"]=config_Mu50.clone(
    data=samples['data2023postBPix'],
    sim=samples['amc2023postBPix'],
)

if __name__=="__main__":
    for key in sorted(Configs.keys()):
        print key

