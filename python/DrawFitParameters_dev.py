import sys,os
import ROOT
importSetting = 'import %s as tnpConf' % sys.argv[1].replace('/','.').split('.py')[0]
exec(importSetting)
TNP_BASE=os.getenv("TNP_BASE")
config=tnpConf.Configs[sys.argv[2]]
config.isSim=False
config.path="/".join([TNP_BASE,"results",os.path.basename(sys.argv[1]).split(".",1)[0],sys.argv[2]])

f=ROOT.TFile(config.path+"/"+config.data_fit_file)
directory=f.Get("s0m0")

hp=ROOT.TH1D("sigmaP","sigmaP",500,0,5)
hp2=config.make_eff_hist()
hp2.SetNameTitle("sigmaP","sigmaP")
for b in config.bins:
    name=b["name"]+"_resP"
    obj=directory.Get(name)
    val=obj.floatParsFinal().at(6).getVal()
    hp.Fill(val)
    if val<0.05:
        print(name)
        print(obj.floatParsFinal().at(6))
    ibin=hp2.FindBin(0.5*(b['vars'][config.vars[0]]['min']+b['vars'][config.vars[0]]['max']),0.5*(b['vars'][config.vars[1]]['min']+b['vars'][config.vars[1]]['max']))
    hp2.SetBinContent(ibin,val)
    hp2.SetBinError(ibin,0)
cp=ROOT.TCanvas()
hp.Draw()
cp2=ROOT.TCanvas()
hp2.Draw("colz")
cp2.SetLogy()
hp2.SetMinimum(0.)
hp2.SetMaximum(4)


hf=ROOT.TH1D("sigmaF","sigmaF",500,0,5)
hf2=config.make_eff_hist()
hf2.SetNameTitle("sigmaF","sigmaF")
for b in config.bins:
    name=b["name"]+"_resF"
    obj=directory.Get(name)
    val=obj.floatParsFinal().at(6).getVal()
    hf.Fill(val)
    if val<0.05:
        print(name)
        print(obj.floatParsFinal().at(6))
    ibin=hf2.FindBin(0.5*(b['vars'][config.vars[0]]['min']+b['vars'][config.vars[0]]['max']),0.5*(b['vars'][config.vars[1]]['min']+b['vars'][config.vars[1]]['max']))
    hf2.SetBinContent(ibin,val)
    hf2.SetBinError(ibin,0)
cf=ROOT.TCanvas()
hf.Draw()
cf2=ROOT.TCanvas()
hf2.Draw("colz")
cf2.SetLogy()
hf2.SetMinimum(0.)
hf2.SetMaximum(4)
raw_input()
