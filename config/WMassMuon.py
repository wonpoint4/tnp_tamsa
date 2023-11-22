from tnpConfig import tnpConfig
### add more systematics
############## samples ################
muondir = '/data9/Users/wonjun/public/TnP_Trees/Spark_Trees/'
samples_won={
    'data2016a':muondir+'TnPTreeZ_UL2016_HIPM_SingleMuon_MiniAODv2_Run2016Bver2CDEF_v2.root',
    'mi2016a':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODAPVv2_DYJetsToMuMu_M50_powhegMiNNLO_v1.root',
    'mg2016a':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODAPVv2_DYJetsToLL_M50_MadgraphMLM_v1.root',
    'data2016b':muondir+'TnPTreeZ_UL2016_SingleMuon_MiniAODv2_Run2016FGH_v2.root',
    'mi2016b':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODv2_DYJetsToMuMu_powhegMiNNLO_v1.root',
    'mg2016b':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODv2_DYJetsToLL_M50_MadgraphMLM_v1.root',
    'data2017':muondir+'TnPTreeZ_UL2017_SingleMuon_MiniAODv2_GT36_Run2017BCDEF_v2.root',
    'mi2017':muondir+'TnPTreeZ_106XSummer20_UL17MiniAODv2_DYJetsToMuMu_M50_massWgtFix_powhegMiNNLO_v2.root',
    'mg2017':muondir+'TnPTreeZ_106XSummer20_UL17MiniAODv2_DYJetsToLL_M50_MadgraphMLM_v2.root',
    'data2018':muondir+'TnPTreeZ_UL2018_SingleMuon_MiniAODv2_GT36_Run2018ABCD_v2v3.root',
    'mi2018':muondir+'TnPTreeZ_106XSummer20_UL18MiniAODv2_DYJetsToMuMu_M50_massWgtFix_powhegMiNNLO_v2.root',
    'mg2018':muondir+'TnPTreeZ_106XSummer20_UL18MiniAODv2_DYJetsToLL_M50_MadgraphMLM_v2.root',
}
samples={
    'data2016a':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2016preVFP/DATA_SkimTree_MuonTnP/SingleMuon',
    'mi2016a':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_MuonTnP/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016a':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_MuonTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2016b':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2016postVFP/DATA_SkimTree_MuonTnP/SingleMuon',
    'mi2016b':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_MuonTnP/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016b':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_MuonTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2017':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2017/DATA_SkimTree_MuonTnP/SingleMuon',
    'mi2017':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_MuonTnP/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2017':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_MuonTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2018':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2018/DATA_SkimTree_MuonTnP/SingleMuon',
    'mi2018':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_MuonTnP/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2018':'/gv0/Users/hsseo/MuonTnP/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_MuonTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
}
############## binning ################
binnings={
    'ID':[              ### For ID
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt_cor' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'Mu8':[              ### For Mu8
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt_cor' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'Mu17':[            ### For Mu17
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt_cor' , 'type': 'float', 'bins': [15,16,17,18,19,20, 25, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'IsoMu':[            ### For IsoMu24 or IsoMu27
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt_cor' , 'type': 'float', 'bins': [20, 22,23,24,25,26,27,28,29, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'RECO':[            ### For RECO
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [20, 200], 'title':'p_{T} [GeV]' },
    ],
    'RECO_2D':[            ### For RECO
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [24,26,30,34,38,42,46,50,55,60,65], 'title':'p_{T} [GeV]' },
    ],
    'Tracking':[            ### For Tracking
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [25, 35, 45, 55, 65], 'title':'p_{T} [GeV]' },
    ],
}
############### Expr ################
## variables
IsoTkMu24 = 'hltL3fL1sMu22L1f0Tkf24QL3trkIsoFiltered0p09'
IsoMu24_2016 = 'hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09'
IsoMu24_2017 = 'hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07'
IsoMu27_2017 = 'hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07'
IsoMu24_2018 = 'hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07'

EMTFveto= '!(tag_eta*probe_eta > 0 && fabs(tag_eta) > 0.9 && fabs(probe_eta) > 0.9 && fabs(tag_phi-probe_phi) < 70/180*3.141592)'

genmatching= '(pair_gen_matched&&probe_gen_dR<0.05&&fabs(probe_gen_reldpt)<0.5)'
genmatching_loose= '(pair_gen_matched)'

fit_nominal = [
    "HistPdf::sigPass(x,histPass_genmatching,2)",
    "HistPdf::sigFail(x,histFail_genmatching,2)",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant acmsP betaP acmsF betaF gammaP gammaF",
]
fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant acmsP betaP acmsF betaF gammaP gammaF",
]
fit_altsig2 = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant meanGaussP sigmaP meanGaussF sigmaF",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant acmsP betaP acmsF betaF gammaP gammaF",
]
fit_altbkg = [
    "HistPdf::sigPass(x,histPass_genmatching,2)",
    "HistPdf::sigFail(x,histFail_genmatching,2)",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
]
fit_altbkg2 = [
    "HistPdf::sigPass(x,histPass_genmatching,2)",
    "HistPdf::sigFail(x,histFail_genmatching,2)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant alphaP alphaF",
]


########### Configs ##############
Configs={}

### ID
config_id=tnpConfig(
    data=samples['data2018'],
    sim=samples['mi2018'],
    sim_weight='weight*PUweight*prefireweight*zptweight',
    sim_maxweight=10000.,
    sim_genmatching=genmatching,
    sim_genmass="pair_gen_mass",
    tree='muon/Events',
    mass="pair_mass_cor",
    bins=binnings['ID'],
    expr='tag_IsoMu24 && tag_pt_cor>27 && tag_isTight && tag_PFIsoTight && tag_q*probe_q<0 && probe_isGlobal',
    test='probe_isMedium && probe_TkIsoLoose',
    hist_nbins=98,
    hist_range=(52,150),
    method='fit',
    fit_parameter= fit_nominal,
    fit_range=(70,112),
    count_range=(80,102),
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altbkg2','fit_parameter':fit_altbkg2}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'altsig2','fit_parameter':fit_altsig2}],
        [{'title':'alttag','expr.replace':('tag_pt_cor>','tag_pt_cor>8+')}],
        [{'title':'altmc','sim.replace':[('DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'),('DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')]}],
        [{'title':'PUweight_up','sim_weight.replace':('PUweight','PUweight_up')},{'title':'PUweight_down','sim_weight.replace':('PUweight','PUweight_down')}],
        [{'title':'prefireweight_up','sim_weight.replace':('prefireweight','prefireweight_up')},{'title':'prefireweight_down','sim_weight.replace':('prefireweight','prefireweight_down')}],
        [{'title':'zptweight','sim_weight.replace':('*zptweight','')}],
        [{'title':'z0weight','sim_weight.add':'*z0weight'}],        
        [{'title':'fitbroad','fit_range':(52,150)},
         {'title':'fitnarrow','fit_range':(80,102)}],
        [{'title':'countbroad','count_range':(70,112)},
         {'title':'countnarrow','count_range':(86,96)}],
        [{'title':'massbinmore','hist_nbins':196},
         {'title':'massbinless','hist_nbins':49}],
        [{'title':'genmatching','sim_genmatching':genmatching_loose}],
        [{'title':'fitting'}], ## only for counting
    ]
)
Configs["2016a_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2016a'],
    sim=samples['mi2016a'],
    expr=config_id.expr+" && !pair_EMTF",
    test='probe_isMedium2016a && probe_TkIsoLoose',
)    
Configs["2016b_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2016b'],
    sim=samples['mi2016b'],
)    
Configs["2017_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2017'],
    sim=samples['mi2017'],
    expr=config_id.expr.replace('tag_IsoMu24','tag_IsoMu27').replace('tag_pt_cor>27','tag_pt_cor>30'),
)    
Configs["2018_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2018'],
    sim=samples['mi2018'],
)

### tracking
config_tracking=config_id.clone(
    bins=binnings['Tracking'],
    expr='tag_IsoMu24 && tag_pt_cor>27 && tag_isTight && tag_PFIsoTight && tag_q*probe_q<0 && probe_isSA_unique',
    test='probe_isGlobal',
)    

Configs["2016a_GlobalMuon"]=config_tracking.clone(
    data=samples['data2016a'],
    sim=samples['mi2016a'],
    expr=config_tracking.expr+" && !pair_EMTF",
)    
Configs["2016b_GlobalMuon"]=config_tracking.clone(
    data=samples['data2016b'],
    sim=samples['mi2016b'],
)    
Configs["2017_GlobalMuon"]=config_tracking.clone(
    data=samples['data2017'],
    sim=samples['mi2017'],
    expr=config_tracking.expr.replace('tag_IsoMu24','tag_IsoMu27').replace('tag_pt_cor>27','tag_pt_cor>30'),
)    
Configs["2018_GlobalMuon"]=config_tracking.clone(
    data=samples['data2018'],
    sim=samples['mi2018'],
)

### trigger
config_trigger=config_id.clone(
    bins=binnings['IsoMu'],
    preselection='probe_q>0',
    expr='tag_IsoMu24 && tag_pt_cor>27 && tag_isTight && tag_PFIsoTight && tag_q*probe_q<0 && probe_isGlobal && probe_isMedium && probe_TkIsoLoose',
    test='probe_IsoMu24',
    method='count',
    systematic=[
        [{'title':'altbkg'}], ## only for fitting
        [{'title':'altbkg2'}], ## only for fitting
        [{'title':'altsig'}], ## only for fitting
        [{'title':'altsig2'}], ## only for fitting
        [{'title':'alttag','expr.replace':('tag_pt_cor>','tag_pt_cor>8+')}],
        [{'title':'altmc','sim.replace':[('DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'),('DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')]}],
        [{'title':'PUweight_up','sim_weight.replace':('PUweight','PUweight_up')},{'title':'PUweight_down','sim_weight.replace':('PUweight','PUweight_down')}],
        [{'title':'prefireweight_up','sim_weight.replace':('prefireweight','prefireweight_up')},{'title':'prefireweight_down','sim_weight.replace':('prefireweight','prefireweight_down')}],
        [{'title':'zptweight','sim_weight.replace':('*zptweight','')}],
        [{'title':'z0weight','sim_weight.add':'*z0weight'}],        
        [{'title':'fitbroad'},
         {'title':'fitnarrow'}], ## only for fitting
        [{'title':'countbroad','count_range':(70,112)},
         {'title':'countnarrow','count_range':(86,96)}],
        [{'title':'massbinmore'}, ## only for fitting
         {'title':'massbinless'}], ## only for fitting
        [{'title':'genmatching'}], ## only for fitting
        [{'title':'fitting','method':'softfit'}], 
    ]
)
Configs["2016a_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples['data2016a'],
    sim=samples['mi2016a'],
    expr=config_trigger.expr.replace('probe_isMedium','probe_isMedium2016a')+" && !pair_EMTF",
    test='probe_IsoMu24',
)    
Configs["2016b_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples['data2016b'],
    sim=samples['mi2016b'],
    test='probe_IsoMu24',
)    
Configs["2017_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples['data2017'],
    sim=samples['mi2017'],
    test='probe_IsoMu24',
)    
Configs["2017_IsoMu27_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples['data2017'],
    sim=samples['mi2017'],
    expr=config_trigger.expr.replace('tag_IsoMu24','tag_IsoMu27').replace('tag_pt_cor>27','tag_pt_cor>30'),
    test='probe_IsoMu27',
)    
Configs["2018_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples['data2018'],
    sim=samples['mi2018'],
    test='probe_IsoMu24',
)    

Configs["2016a_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2016a_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu17Leg1',
    bins=binnings['Mu17'],
)
Configs["2016b_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2016b_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu17Leg1',
    bins=binnings['Mu17'],
)
Configs["2017_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2017_IsoMu27_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu17Leg1',
    bins=binnings['Mu17'],
)
Configs["2018_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2018_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu17Leg1',
    bins=binnings['Mu17'],
)

Configs["2016a_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2016a_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu8Leg2',
    bins=binnings['Mu8'],
)
Configs["2016b_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2016b_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu8Leg2',
    bins=binnings['Mu8'],
)
Configs["2017_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2017_IsoMu27_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu8Leg2',
    bins=binnings['Mu8'],
)
Configs["2018_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2018_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test='probe_Mu8Leg2',
    bins=binnings['Mu8'],
)


### RECO
config_reco=tnpConfig(
    data=samples_won['data2018'],
    sim=samples_won['mi2018'],
    sim_weight='(genWeight/2358.)*puWeight*zptWeight_MiNNLO*L1prefiringmuonWeight',
    sim_maxweight=10000.,
    sim_genmatching='tag_isMatchedGen && probe_isMatchedGen',
    sim_genmass="genMass",
    tree='muon/Events',
    mass="pair_mass",
    bins=binnings['RECO'],
    preselection='probe_isHighPurity > 7',
    expr='probe_isHighPurity > 7 && tag_hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07 && tag_pt>27 && tag_CutBasedIdTight && tag_PFIsoTight && tag_charge*probe_charge < 0 && pair_dR > 0.3',
    test='probe_isSA',
    hist_nbins=98,
    hist_range=(52,150),
    method='fit',
    fit_parameter= fit_nominal,
    fit_range=(70,112),
    count_range=(80,102),
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altbkg2','fit_parameter':fit_altbkg2}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'altsig2','fit_parameter':fit_altsig2}],
        [{'title':'alttag','expr.replace':('tag_pt>','tag_pt>8+')}],
        [{'title':'altmc','sim.replace':[('DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'),('DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')]}],
        [{'title':'PUweight_up','sim_weight.replace':('puWeight','puWeight_up')},{'title':'PUweight_down','sim_weight.replace':('puWeight','puWeight_down')}],
        [{'title':'prefireweight','sim_weight.replace':('*L1prefiringmuonWeight','')}],
        [{'title':'zptweight','sim_weight.replace':('*zptWeight_MiNNLO','')}],
        [{'title':'z0weight','sim_weight.add':'*z0Weight'}],
        [{'title':'fitbroad','fit_range':(62,150)},
         {'title':'fitnarrow','fit_range':(80,102)}],
        [{'title':'countbroad','count_range':(70,112)},
         {'title':'countnarrow','count_range':(86,96)}],
        [{'title':'massbinmore','hist_nbins':196},
         {'title':'massbinless','hist_nbins':49}],
        [{'title':'genmatching'}], ## not implemented
        [{'title':'fitting'}], ## only for counting
    ]
)
Configs["2016a_StandaloneMuon"]=config_reco.clone(
    data=samples_won['data2016a'],
    sim=samples_won['mi2016a'],
    expr=config_reco.expr.replace(IsoMu24_2018,IsoMu24_2016)+" && "+EMTFveto,
)
Configs["2016b_StandaloneMuon"]=config_reco.clone(
    data=samples_won['data2016b'],
    sim=samples_won['mi2016b'],
    expr=config_reco.expr.replace(IsoMu24_2018,IsoMu24_2016),
)
Configs["2016b_StandaloneMuon_2D"]=Configs["2016b_StandaloneMuon"].clone(
    bins=binnings['RECO_2D'],
)
Configs["2017_StandaloneMuon"]=config_reco.clone(
    data=samples_won['data2017'],
    sim=samples_won['mi2017'],
    expr=config_reco.expr.replace(IsoMu24_2018,IsoMu27_2017).replace('tag_pt>27','tag_pt>30'),
)
Configs["2018_StandaloneMuon"]=config_reco.clone(
    data=samples_won['data2018'],
    sim=samples_won['mi2018'],
)

## cloning for minus
Configs_minus={}
for key in Configs:
    if "_Plus" in key:
        Configs_minus[key.replace("_Plus","_Minus")]=Configs[key].clone({"preselection.replace":("probe_q>0","probe_q<0")})
Configs.update(Configs_minus)

if __name__=="__main__":
    for key in sorted(Configs.keys()):
        print key
