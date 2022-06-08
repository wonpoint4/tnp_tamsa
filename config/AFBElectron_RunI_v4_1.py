from tnpConfig import tnpConfig

############## samples ################
samples={
    'data2012':'/gv0/Users/hsseo/TnP_Run12/data',
    'powheg2012':'/gv0/Users/hsseo/TnP_Run12/S12pwgZee',
}
############## binning ################
bin_ID = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele35 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 31, 35, 37, 40, 45, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele32 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 28, 31, 33, 35, 38, 40, 45, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele28 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 24, 28, 30, 32, 35, 40, 45, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele27 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 23, 26, 28, 30, 32, 35, 40, 45, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele23 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 19, 23, 25, 27, 30, 35, 40, 45, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele12 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 70, 100, 500], 'title':'p_{T} [GeV]' },
]


############### Expr ################

## fits
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]

fit_nominal_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altsig_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass_random,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, 0, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, 0, 1],peakF[90.0])",
]

fit_altbkg_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]



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
    tree='e',
    mass="pair_mass",
    bins=bin_ID,
    expr='( tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )*(probe_q*tag_q<0?1.:-1.)',
    test='probe_Medium',
    hist_nbins=98,
    hist_range=(52,150),
    method="fit",
    fit_parameter=fit_nominal,
    fit_range=(60,140),
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'alttag','expr.replace':('probe_pt>30','probe_pt>35')}],
        [{'title':'altmc'}],
        [{'title':'altsub','expr.replace':('(probe_q*tag_q<0?1.:-1.)','(probe_q*tag_q<0?1.:-0.6)')}],
        [{'title':'nogenmatching','sim_genmatching':"(1)"}],
    ],
    #option="fix_ptbelow20",
)
Configs['2012_MediumID_Plus']=config.clone(test='probe_Medium')
Configs['2012_SelQ_MediumID_Plus']=config.clone(expr='( probe_Medium && tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )*(probe_q*tag_q<0?1.:-1.)',test='probe_3charge')

## trigger
config=config.clone(
    expr='( probe_Medium && tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )*(probe_q*tag_q<0?1.:-1.)',
)
Configs['2012_Ele27_MediumID_Plus']=config.clone(
    bins=bin_Ele27,
    test='probe_Ele27',
)
Configs['2012_Ele27_SelQ_MediumID_Plus']=config.clone(
    bins=bin_Ele27,
    expr='( probe_Medium&&probe_3charge && tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )*(probe_q*tag_q<0?1.:-1.)',
    test='probe_Ele27',
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
