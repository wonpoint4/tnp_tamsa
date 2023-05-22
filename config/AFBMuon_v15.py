from tnpConfig import tnpConfig
### reproduce won's v15
############## samples ################
muondir = '/data9/Users/wonjun/public/TnP_Trees/Spark_Trees/'
samples={
    'data2016a':muondir+'TnPTreeZ_UL2016_HIPM_SingleMuon_MiniAODv2_Run2016Bver2CDEF_v2.root',
    'mi2016a':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODAPVv2_DYJetsToMuMu_M50_powhegMiNNLO_v1.root',
    'mg2016a':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODAPVv2_DYJetsToLL_M50_MadgraphMLM_v1.root',
    'data2016b':muondir+'TnPTreeZ_UL2016_SingleMuon_MiniAODv2_Run2016FGH_v2.root',
    'mi2016b':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODv2_DYJetsToMuMu_powhegMiNNLO_v1.root',
    'mg2016b':muondir+'TnPTreeZ_106XSummer20_UL16MiniAODv2_DYJetsToLL_M50_MadgraphMLM_v1.root',
    'data2017':muondir+'TnPTreeZ_UL2017_SingleMuon_MiniAODv2_Run2017BCDEF_v1.root',
    'mi2017':muondir+'TnPTreeZ_106XSummer20_UL17MiniAODv2_DYJetsToMuMu_M50_massWgtFix_powhegMiNNLO_v2.root',
    'mg2017':muondir+'TnPTreeZ_106XSummer20_UL17MiniAODv2_DYJetsToLL_M50_MadgraphMLM_v2.root',
    'data2018':muondir+'TnPTreeZ_UL2018_SingleMuon_MiniAODv2_GT36_Run2018ABCD_v1v2.root',
    'mi2018':muondir+'TnPTreeZ_106XSummer20_UL18MiniAODv2_DYJetsToMuMu_M50_massWgtFix_powhegMiNNLO_v2.root',
    'mg2018':muondir+'TnPTreeZ_106XSummer20_UL18MiniAODv2_DYJetsToLL_M50_MadgraphMLM_v2.root',
}
samples_skimmed={key:val.replace("/TnPTreeZ_","/skimmed_TnPTreeZ_") for key,val in samples.items()}
############## binning ################
binnings={
    'ID':[              ### For ID
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'Mu8':[              ### For Mu8
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'Mu17':[            ### For Mu17
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [15,16,17,18,19,20, 25, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'IsoMu':[            ### For IsoMu24 or IsoMu27
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [20, 22,23,24,25,26,27,28,29, 30, 35, 40, 45, 50, 70, 200], 'title':'p_{T} [GeV]' },
    ],
    'RECO':[            ### For RECO
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/20.,2) for i in range(-48,49)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [20, 200], 'title':'p_{T} [GeV]' },
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

Mu17_2016 = '(probe_hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17 && probe_hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4) || (probe_hltL3fL1sDoubleMu114L1f0L2f10L3Filtered17 && probe_hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4) || (probe_hltL3fL1sDoubleMu114TkFiltered17Q && probe_hltDiMuonTrk17Trk8RelTrkIsoFiltered0p4)'
Mu17_2017 = 'probe_hltL3fL1DoubleMu155fFiltered17 && probe_hltDiMuon178RelTrkIsoFiltered0p4'
Mu17_2018 = 'probe_hltL3fL1DoubleMu155fFiltered17 && probe_hltDiMuon178RelTrkIsoFiltered0p4'

Mu8_2016 = '(probe_hltL3pfL1sDoubleMu114ORDoubleMu125L1f0L2pf0L3PreFiltered8 && probe_hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4) || (probe_hltDiMuonGlbFiltered17TrkFiltered8 && probe_hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4) || (probe_hltDiTkMuonTkFiltered17TkFiltered8 && probe_hltDiMuonTrk17Trk8RelTrkIsoFiltered0p4)'
Mu8_2017 = 'probe_hltL3fL1DoubleMu155fPreFiltered8 && probe_hltDiMuon178RelTrkIsoFiltered0p4'
Mu8_2018 = 'probe_hltL3fL1DoubleMu155fPreFiltered8 && probe_hltDiMuon178RelTrkIsoFiltered0p4'


EMTFveto= '!(tag_eta*probe_eta > 0 && fabs(tag_eta) > 0.9 && fabs(probe_eta) > 0.9 && fabs(tag_phi-probe_phi) < 70/180*3.141592)'


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


########### Configs ##############
Configs={}

### ID
config_id=tnpConfig(
    data=samples['data2018'],
    sim=samples['mi2018'],
    sim_weight='(genWeight/2358.)*puWeight*zptWeight_MiNNLO*L1prefiringmuonWeight',
    sim_maxweight=10000.,
    sim_genmatching='tag_isMatchedGen && probe_isMatchedGen',
    sim_genmass="genMass",
    tree='muon/Events',
    mass="pair_mass",
    bins=binnings['ID'],
    preselection='probe_isTracker',
    expr='probe_trk_muon_dr < 0.3 && fabs(probe_trk_muon_dz) < 0.2 && fabs(probe_trk_muon_dptrel) < 0.5 && tag_hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07 && tag_pt > 26 && tag_CutBasedIdTight && tag_PFIsoTight && tag_charge*probe_charge < 0 && probe_isTracker && pair_dR > 0.3',
    test='probe_isMedium && probe_TkIsoLoose',
    hist_nbins=60,
    hist_range=(70,130),
    method='fit',
    fit_parameter= fit_nominal,
    fit_range=(70,130),
    systematic=[
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altMC',
          'sim.replace':[('DYJetsToMuMu_M50_powhegMiNNLO_v','DYJetsToLL_M50_MadgraphMLM_v'),('DYJetsToMuMu_powhegMiNNLO_v','DYJetsToLL_M50_MadgraphMLM_v'),('DYJetsToMuMu_M50_massWgtFix_powhegMiNNLO_v','DYJetsToLL_M50_MadgraphMLM_v')],
          'sim_weight.replace':[('(genWeight/2358.)','genWeight'),('MiNNLO','MG')]}],
        [{'title':'tagiso010','expr.replace':('tag_PFIsoTight','tag_PFIsoVeryTight')},
         {'title':'tagiso020','expr.replace':('tag_PFIsoTight','tag_PFIsoMedium')}],
        [{'title':'PUweight','sim_weight.replace':('*puWeight','')}],
        [{'title':'zptweight','sim_weight.replace':('*zptWeight_MiNNLO','')}],
        [{'title':'prefireweight','sim_weight.replace':('*L1prefiringmuonWeight','')}],
        [{'title':'z0weight','sim_weight.add':'*z0Weight'}],        
        [{'title':'massbroad','fit_range':(60,130),'hist_range':(60,130)},
         {'title':'massnarrow','fit_range':(70,120)}],
        [{'title':'massbin50','hist_nbins':50},
         {'title':'massbin75','hist_nbins':75}],
    ]
)
Configs["2016a_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2016a'],
    sim=samples['mi2016a'],
    expr=config_id.expr.replace(IsoMu24_2018,IsoMu24_2016)+" && "+EMTFveto,
    test='probe_isMedium2016a && probe_TkIsoLoose',
)    
Configs["2016b_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2016b'],
    sim=samples['mi2016b'],
    expr=config_id.expr.replace(IsoMu24_2018,IsoMu24_2016),
)    
Configs["2017_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2017'],
    sim=samples['mi2017'],
    expr=config_id.expr.replace(IsoMu24_2018,IsoMu27_2017).replace('tag_pt > 26','tag_pt > 29'),
)    
Configs["2018_MediumID_LooseTrkIso"]=config_id.clone(
    data=samples['data2018'],
    sim=samples['mi2018'],
)    

### RECO
config_reco=config_id.clone(
    preselection='probe_isHighPurity > 7',
    expr='probe_isHighPurity > 7 && tag_hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07 && tag_pt > 26 && tag_CutBasedIdTight && tag_PFIsoTight && tag_charge*probe_charge < 0 && pair_dR > 0.3',
    test='probe_isTracker',
    bins=binnings['RECO'],
)
Configs["2016a_TrackerMuon"]=config_reco.clone(
    data=samples['data2016a'],
    sim=samples['mi2016a'],
    expr=config_reco.expr.replace(IsoMu24_2018,IsoMu24_2016)+" && "+EMTFveto,
)
Configs["2016b_TrackerMuon"]=config_reco.clone(
    data=samples['data2016b'],
    sim=samples['mi2016b'],
    expr=config_reco.expr.replace(IsoMu24_2018,IsoMu24_2016),
)
Configs["2017_TrackerMuon"]=config_reco.clone(
    data=samples['data2017'],
    sim=samples['mi2017'],
    expr=config_reco.expr.replace(IsoMu24_2018,IsoMu27_2017).replace('tag_pt > 26','tag_pt > 29'),
)
Configs["2018_TrackerMuon"]=config_reco.clone(
    data=samples['data2018'],
    sim=samples['mi2018'],
)

### trigger
config_trigger=tnpConfig(
    data=samples_skimmed['data2018'],
    sim=samples_skimmed['mi2018'],
    sim_weight='(genWeight/2358.)*puWeight*zptWeight_MiNNLO*L1prefiringmuonWeight',
    sim_maxweight=10000.,
    sim_genmatching='tag_isMatchedGen && probe_isMatchedGen',
    sim_genmass="genMass",
    tree='muon/Events',
    mass="pair_mass",
    bins=binnings['IsoMu'],
    expr='probe_trk_muon_dr < 0.3 && fabs(probe_trk_muon_dz) < 0.2 && fabs(probe_trk_muon_dptrel) < 0.5 && tag_hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07 && tag_pt > 26 && tag_CutBasedIdTight && tag_PFIsoTight && tag_charge*probe_charge < 0 && probe_charge > 0 && probe_isMedium && probe_TkIsoLoose && pair_dR > 0.3',
    test='probe_'+IsoMu24_2018,
    hist_nbins=60,
    hist_range=(70,130),
    method='count',
    count_range=(81,101),
    systematic=[
        [{'title':'altsig'}],
        [{'title':'altbkg'}],
        [{'title':'altMC',
          'sim.replace':[('DYJetsToMuMu_M50_powhegMiNNLO_v','DYJetsToLL_M50_MadgraphMLM_v'),('DYJetsToMuMu_powhegMiNNLO_v','DYJetsToLL_M50_MadgraphMLM_v'),('DYJetsToMuMu_M50_massWgtFix_powhegMiNNLO_v','DYJetsToLL_M50_MadgraphMLM_v')],
          'sim_weight.replace':[('(genWeight/2358.)','genWeight'),('MiNNLO','MG')]}],
        [{'title':'tagiso010','expr.replace':('tag_PFIsoTight','tag_PFIsoVeryTight')},
         {'title':'tagiso020','expr.replace':('tag_PFIsoTight','tag_PFIsoMedium')}],
        [{'title':'PUweight','sim_weight.replace':('*puWeight','')}],
        [{'title':'zptweight','sim_weight.replace':('*zptWeight_MiNNLO','')}],
        [{'title':'prefireweight','sim_weight.replace':('*L1prefiringmuonWeight','')}],
        [{'title':'z0weight','sim_weight.add':'*z0Weight'}],        
        [{'title':'massbroad','count_range':(76,106)},
         {'title':'massnarrow','count_range':(86,96)}],
        [{'title':'massbin50'},
         {'title':'massbin75'}],
    ]
)
Configs["2016a_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples_skimmed['data2016a'],
    sim=samples_skimmed['mi2016a'],
    expr=config_id.expr.replace(IsoMu24_2018,IsoMu24_2016).replace('probe_isMedium','probe_isMedium2016a')+" && "+EMTFveto,
    test='probe_'+IsoMu24_2016+' || probe_'+IsoTkMu24,
    bins=binnings['IsoMu'],
)    
Configs["2016b_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples_skimmed['data2016b'],
    sim=samples_skimmed['mi2016b'],
    expr=config_trigger.expr.replace(IsoMu24_2018,IsoMu24_2016),
    test='probe_'+IsoMu24_2016+' || probe_'+IsoTkMu24,
)    
Configs["2017_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples_skimmed['data2017'],
    sim=samples_skimmed['mi2017'],
    expr=config_trigger.expr.replace(IsoMu24_2018,IsoMu24_2017),
    test='probe_'+IsoMu24_2017,
)    
Configs["2017_IsoMu27_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples_skimmed['data2017'],
    sim=samples_skimmed['mi2017'],
    expr=config_trigger.expr.replace(IsoMu24_2018,IsoMu27_2017).replace('tag_pt > 26','tag_pt > 29'),
    test='probe_'+IsoMu27_2017,
)    
Configs["2018_IsoMu24_MediumID_LooseTrkIso_Plus"]=config_trigger.clone(
    data=samples_skimmed['data2018'],
    sim=samples_skimmed['mi2018'],
    test='probe_'+IsoMu24_2018,
)    

Configs["2016a_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2016a_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu17_2016,
    bins=binnings['Mu17'],
)
Configs["2016b_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2016b_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu17_2016,
    bins=binnings['Mu17'],
)
Configs["2017_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2017_IsoMu27_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu17_2017,
    bins=binnings['Mu17'],
)
Configs["2018_Mu17Leg1_MediumID_LooseTrkIso_Plus"]=Configs["2018_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu17_2018,
    bins=binnings['Mu17'],
)

Configs["2016a_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2016a_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu8_2016,
    bins=binnings['Mu8'],
)
Configs["2016b_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2016b_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu8_2016,
    bins=binnings['Mu8'],
)
Configs["2017_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2017_IsoMu27_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu8_2017,
    bins=binnings['Mu8'],
)
Configs["2018_Mu8Leg2_MediumID_LooseTrkIso_Plus"]=Configs["2018_IsoMu24_MediumID_LooseTrkIso_Plus"].clone(
    test=Mu8_2018,
    bins=binnings['Mu8'],
)

## cloning for minus
Configs_minus={}
for key in Configs:
    if "_Plus" in key:
        Configs_minus[key.replace("_Plus","_Minus")]=Configs[key].clone({"expr.replace":("probe_charge > 0","probe_charge < 0")})
Configs.update(Configs_minus)

if __name__=="__main__":
    for key in sorted(Configs.keys()):
        print key
