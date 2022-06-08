from tnpConfig import tnpConfig

############## samples ################
samples={
    'data2012':'/gv0/Users/hsseo/TnP_Run12/data',
    'powheg2012':'/gv0/Users/hsseo/TnP_Run12/S12pwgZuu',
}
############## binning ################
binnings={
    'Mu8':[              ### For ID or Mu8
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 120], 'title':'p_{T} [GeV]' },
    ],
    'Mu17':[            ### For Mu17
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 120], 'title':'p_{T} [GeV]' },
    ],
    'IsoMu24':[            ### For IsoMu24
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [20, 22, 24, 26, 28, 30, 35, 40, 45, 50, 60, 120], 'title':'p_{T} [GeV]' },
    ],
    'IsoMu27':[          ### For IsoMu27 (Regacy 2017)
        { 'var' : 'probe_eta' , 'type': 'float', 'bins': [round(i/10.,2) for i in range(-24,25)], 'title':'#eta' },
        { 'var' : 'probe_pt' , 'type': 'float', 'bins': [20, 22, 24, 26, 28, 30, 35, 40, 45, 50, 60, 120], 'title':'p_{T} [GeV]' },
    ],
}

########### Configs ##############
Configs={}

#### 2012
## ID
config=tnpConfig(
    data=samples['data2012'],
    sim=samples['powheg2012'],
    sim_weight='weight',
    sim_maxweight=10000.,
    sim_genmatching="gen_matching",
    sim_genmass="gen_mass",
    tree='u',
    mass="pair_mass",
    bins=binnings["Mu8"],
    expr='( tag_IsoMu24 && tag_Tight && tag_PfIso && tag_pt>25 && tag_q*probe_q<0 && probe_q>0 && pair_dR>0.3 )',
    test='probe_Medium',
    hist_nbins=72,
    hist_range=(58,130),
    method="fit",
    fit_parameter=[
        "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
        "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
        "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaGaussP[0.8,0.5,3.5])",
        "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaGaussF[0.7,0.5,3.5])",
        "FCONV::sigPass(x, sigPhysPass , sigResPass)",
        "FCONV::sigFail(x, sigPhysFail , sigResFail)",
        "Exponential::bkgPass(x, aExpoP[-0.1, -1,0.1])",
        "Exponential::bkgFail(x, aExpoF[-0.3, -1,0.1])",
    ],
    fit_range=(70,130),
    systematic=[
        [{'title':'massbroad','fit_range':(60,130)},{'title':'massnarrow','fit_range':(70,120)}],
        [{'title':'notagiso','expr.replace':('&& tag_PfIso &&', '&&')}],
        [{'title':'altmc'}],
        [{'title':'massbin50','hist_nbins':60},{'title':'massbin75','hist_nbins':90}],
    ],
)
Configs['2012_MediumID_Plus']=config.clone(test='probe_Medium')

## trigger
Configs['2012_IsoMu24_MediumID_Plus']=config.clone(
    bins=binnings["IsoMu24"],
    method="count",
    expr='( probe_Medium && tag_IsoMu24 && tag_Tight && tag_PfIso && tag_pt>25 && tag_q*probe_q<0 && probe_q>0 && pair_dR>0.3 )',
    test='probe_IsoMu24',
    count_range=(81,101),
    systematic=[
        [{'title':'massbroad','count_range':(76,106)},{'title':'massnarrow','count_range':(86,96)}],
        [{'title':'notagiso','expr.replace':('&& tag_PfIso &&', '&&')}],
        [{'title':'altmc'}],
    ],
)

#### minus
Configs_minus={}
for key in Configs:
    if "_Plus" in key:
        Configs_minus[key.replace("_Plus","_Minus")]=Configs[key].clone({"expr.replace":("probe_q>0","probe_q<0")})
Configs.update(Configs_minus)

if __name__=="__main__":
    for key in sorted(Configs.keys()):
        print key
