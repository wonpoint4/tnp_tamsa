import os,sys
import ROOT

def GetNames(directory):
    names=[]
    for key in directory.GetListOfKeys():
        if "TDirectory" in key.GetClassName():
            names+=GetNames(directory.GetDirectory(key.GetName()))
        elif "TProcessID" in key.GetClassName():
            continue
        else:
            names+=[directory.GetTitle()+"/"+key.GetName()]
    return names

fout=ROOT.TFile(sys.argv[1],"recreate")
filelist=[]
for src in sys.argv[2:]:
    if os.path.isfile(src):
        filelist.append(src)
    elif os.path.isdir(src):
        filelist+=os.popen("find {} -type f -name '*.root'|sort -V".format(src)).read().split()
#print(filelist)
for fname in filelist:
    fin=ROOT.TFile(fname)
    for name in GetNames(fin):
        obj=fin.Get(name)
        basename=os.path.basename(name)
        dirname=os.path.dirname(name)
        if not fout.GetDirectory(dirname):
            fout.mkdir(dirname)
        fout.cd(dirname)
        obj.Write(basename)
