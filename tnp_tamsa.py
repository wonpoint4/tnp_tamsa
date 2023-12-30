#!/usr/bin/env python

### python specific import
import os,sys,argparse
import math
import time
from zipfile import ZipFile
import ROOT as rt

TNP_BASE=os.getenv("TNP_BASE")
if TNP_BASE is None or TNP_BASE=="":
    print("[tnp_tamsa] Please source setup.sh")
    exit(1)
HOSTNAME=os.popen('hostname').read().strip()
if "lxplus" in HOSTNAME:
    HOST="lxplus"
elif "tamsa" in HOSTNAME:
    HOST="tamsa"
else:
    print("[tnp_tamsa] Unknown host {}. It may not work".format(HOSTNAME))

parser = argparse.ArgumentParser(description='tnp EGM fitter')
parser.add_argument('settings'     , help = 'setting file [mandatory]')
parser.add_argument('config'       , help = 'config name [mandatory]')
parser.add_argument('--checkBins'  , action='store_true'  , help = 'check bining definition')
parser.add_argument('--checkConfig', action='store_true'  , help = 'check configuration')
parser.add_argument('--step'       , default="hist,fit,sum", help = 'steps: hist(ogram),fit,sum(mary)')
parser.add_argument('--set','-s'   , type = int           , help = 'systematic set index (0 refers nominal)')
parser.add_argument('--member','-m', type = int           , help = 'systematic member index (s0m0 refers nominal)')
parser.add_argument('--bin', '-b'  , dest = 'bins'   , type = str, help='bin numbers separated by comma')
parser.add_argument('--data', dest='isData', action='store_true')
parser.add_argument('--sim', dest='isSim', action='store_true')
parser.add_argument('--log'        , action='store_true'     , help = 'keep logs')
parser.add_argument('--njob', '-n' , default="100,10", help = 'condor njob per job submission for each step: "HIST,FIT". Or you can use one number for all steps')
parser.add_argument('--ijob', '-i' , type = int, help = 'condor job index (for internal use)')
parser.add_argument('--nmax'       , default=300, type = int, help = 'condor nmax job (concurrency limits)')
parser.add_argument('--no-condor'  , dest = "condor", action='store_false' )
parser.add_argument('--reduction', type = int, default=1, help='reduction in hist step')
parser.add_argument('--dag'        , action='store_true', help='use condor dag')

args = parser.parse_args()

####################################################################
##### condor functions
####################################################################
def check_condor(clusterid,njob):
    os.system("sleep 2")
    lines=os.popen("condor_history {} -limit {} -scanlimit 20000 -af exitcode out err".format(clusterid,njob)).read().splitlines()
    for line in lines:
        words=line.split()
        if words[0]!="0":
            print "[tnp_tamsa] Non-zero exit code. Check the log"
            print words[2]
            print words[1]
            return False
        if os.system("grep -q 'Error in' {}".format(words[2]))==0:
            print "[tnp_tamsa] Error occurs. Check the log"
            print words[2]
            print words[1]
            return False
    return True

def submit_condor(jdspath):
    clusterid=int(os.popen('condor_submit '+jdspath+'|grep -o "cluster [0-9]*"').read().split()[1])
    return clusterid

def get_additional_condor_script(args,step=None):
    rt=[]
    if HOST=="tamsa":
        if step=="hadd":
            rt+=["concurrency_limits = n32.tnphadd"]
        else:
            rt+=["concurrency_limits = n{}.{}".format(args.nmax,os.getenv("USER"))]
    elif HOST=="lxplus":
        rt+=["max_retries = 2"]
        #rt+=['requirements = ( Machine =!= LastRemoteHost ) && ( OpSysAndVer =?= "CentOS7" || OpSysAndVer =?= "AlmaLinux9" )']
        rt+=['requirements = ( Machine =!= LastRemoteHost )']
        rt+=['+MaxRuntime = 7200']
    return "\n".join(rt)

####################################################################
##### argument handling
####################################################################
## time stamp
startTime = time.time()
print 'Starts at', time.strftime('%c', time.localtime(startTime))

## check step argument
args.step=args.step.lower().split(",")
for step in args.step:
    if step not in ["hist","fit","sum"]:
        print "[tnp_tamsa] Unknown step "+step
        exit(1)

## check bins argument
if args.bins:
    args.bins=[int(i) for i in args.bins.split(",")]

## check config argument
importSetting = 'import %s as tnpConf' % args.settings.replace('/','.').split('.py')[0]
exec(importSetting)

if not args.config in tnpConf.Configs.keys():
    print '[tnp_tamsa] config %s not found in config definitions' % args.config
    print '  --> define in settings first'
    print '  In settings I found configs: '
    for key in sorted(tnpConf.Configs.keys()):
        print key
    exit(1)

print '[tnp_tamsa] Use Configs["{}"] from {}'.format(args.config,args.settings)
config=tnpConf.Configs[args.config]
if hasattr(tnpConf,'OutputDir'):
    config.path=tnpConf.OutputDir+"/"+args.config
else:
    config.path="/".join([TNP_BASE,"results",os.path.basename(args.settings).split(".",1)[0],args.config])
os.system("mkdir -p {}".format(config.path))
config.condor_path="/".join([TNP_BASE,"condor",os.path.basename(args.settings).split(".",1)[0],args.config])
os.system("mkdir -p {}".format(config.condor_path))
with open(config.path+"/config.txt","w") as f:
    f.write(config.__str__())

args.njob=[int(i) for i in args.njob.split(",")]

if args.dag:
    os.system("rm -r {}/condor.dag*".format(config.condor_path))

####################################################################
##### check Bins
####################################################################
if args.checkBins:
    for ib in range(len(config.bins)):
        print config.bins[ib]['name']
        print '  - cut: ',config.bins[ib]['cut']
    sys.exit(0)

####################################################################
##### check Config
####################################################################
if args.checkConfig:
    if not args.set or not args.member:
        print(config)
    else:
        configs=config.make_systematics()
        print(configs[args.set][args.member])
    sys.exit(0)

####################################################################
##### Create Histograms
####################################################################
if "hist" in args.step:
    import histUtils
    hist_configs=config.make_hist_configs()
    njob=args.njob[0]
    if args.condor==False:
        histUtils.makePassFailHistograms( hist_configs[args.set], njob, args.ijob, args.reduction)
    elif args.condor==True:
        for iconf in range(len(hist_configs)):
            if args.set!=None and args.set!=iconf: continue
            hist_config=hist_configs[iconf]
            print '[Histogram] Create histograms for {}'.format(hist_config[0].sample)
            jobbatchname='{}_{}_{}'.format(os.path.basename(args.settings).split(".",1)[0],args.config,hist_config[0].hist_file.split(".",1)[0])
            condor_dir="/".join([hist_config[0].condor_path,hist_config[0].hist_file.replace(".root",".d")])
            output_dir="/".join([hist_config[0].path,hist_config[0].hist_file.replace(".root",".d")])
            os.system('mkdir -p '+condor_dir)
            os.system('mkdir -p '+output_dir)

            open(condor_dir+'/run.sh','w').write(
'''#!/bin/bash
cd $TNP_BASE
python tnp_tamsa.py {} {} --step hist --set {} --njob {} --ijob $1 --reduction {} --no-condor
exit $?
'''.format(args.settings,args.config,iconf,njob,args.reduction)
            )
            os.system("chmod +x "+condor_dir+'/run.sh')

            open(condor_dir+'/condor.jds','w').write(
'''executable = {condor_dir}/run.sh
arguments = $(Process)
output = {condor_dir}/job$(Process).out
error = {condor_dir}/job$(Process).err
log = {condor_dir}/condor.log
request_memory = 1500
jobbatchname = {name}
getenv = True
{additional}
queue {njob}
'''
                .format(
                    condor_dir=condor_dir,
                    name=jobbatchname,
                    njob=njob,
                    additional=get_additional_condor_script(args),
                )
            )

            outfiles=["{}/job{}.root".format(output_dir,i) for i in range(njob)]

            open(condor_dir+'/hadd.sh','w').write(
'''#!/bin/bash
hadd -j 4 -f {hadd_target} {hadd_source} || exit $?
python -c 'import histUtils; histUtils.postProcess("{hadd_target}")' || exit $?
/usr/bin/rm {hadd_source} || exit $?
'''
                .format(
                    hadd_target="/".join([hist_config[0].path,hist_config[0].hist_file]),
                    hadd_source=' '.join(outfiles),
                )
            )
            os.system("chmod +x "+condor_dir+'/hadd.sh')
            
            open(condor_dir+'/hadd.jds','w').write(
'''executable = {condor_dir}/hadd.sh
output = {condor_dir}/hadd.out
error = {condor_dir}/hadd.err
log = {condor_dir}/hadd.log
request_cpus = 4
request_memory = 1500
jobbatchname = {name}
getenv = True
{additional}
queue
'''
                .format(
                    hadd_target="/".join([hist_config[0].path,hist_config[0].hist_file]),
                    hadd_source=' '.join(outfiles),
                    condor_dir=condor_dir,
                    name=jobbatchname+"_hadd",
                    additional=get_additional_condor_script(args,"hadd"),
                )
            )
            
            if args.dag:
                open(config.condor_path+"/condor.dag","a").write(
'''
JOB {histjobname} {histjds}
JOB {haddjobname} {haddjds}
PARENT {histjobname} CHILD {haddjobname}
PARENT {haddjobname} CHILD hists_done
'''
                    .format(
                        histjobname=hist_config[0].hist_file.split(".",1)[0],
                        histjds=condor_dir+'/condor.jds',
                        haddjobname=hist_config[0].hist_file.split(".",1)[0]+"_hadd",
                        haddjds=condor_dir+'/hadd.jds',
                        hadd_source=' '.join(outfiles),
                    )
                )
            else:
                clusterid=submit_condor(condor_dir+'/condor.jds')
                print '  Submit', njob, 'jobs. Waiting...'
                os.system('condor_wait '+condor_dir+'/condor.log > /dev/null')
                if not check_condor(clusterid,njob):
                    exit(1)
                clusterid=submit_condor(condor_dir+'/hadd.jds')
                print '  Submit hadd job. Waiting...'
                os.system('condor_wait '+condor_dir+'/hadd.log > /dev/null')
                if not check_condor(clusterid,1):
                    exit(1)
                if not args.log:
                    os.system("rm -r "+condor_dir)

####################################################################
##### Actual Fitter
####################################################################
#import libfitUtils as fitUtils
from fitUtils import tnpFitter
if "fit" in args.step:
    configs=config.make_systematics()
    if args.condor==False:
        if not args.isSim and not args.isData:
            print "Wrong"
            exit(1)
        for ibin in args.bins:
            fitter=tnpFitter(configs[args.set][args.member].clone(isSim=args.isSim))
            fitter.run(ibin)
    elif args.condor==True:
        condorlogs={}
        for iset in range(len(configs)):
            if args.set and args.set!=iset: continue
            for imem in range(len(configs[iset])):
                if args.member and args.member!=imem: continue
                for isSim in [False,True]:
                    c=configs[iset][imem].clone(isSim=isSim)
                    jobbatchname='{}_{}_{}_{}'.format(os.path.basename(args.settings).split(".",1)[0],args.config,c.fit_file.split(".",1)[0],c.name)
                    condor_dir="/".join([c.condor_path,c.fit_file.replace(".root",".d"),c.name])
                    os.system('mkdir -p '+condor_dir)

                    open(condor_dir+'/run.sh','w').write(
'''#!/bin/bash
cd $TNP_BASE
python tnp_tamsa.py {} {} --step fit --set {} --member {} {} --bin $1 --no-condor
exit $?
'''
                        .format(args.settings,args.config,iset,imem,"--sim" if isSim else "--data")
                    )
                    os.system("chmod +x "+condor_dir+'/run.sh')
                    
                    njob=min(args.njob[-1],len(c.bins))
                    condor_arguments=[",".join([str(i) for i in range(len(c.bins)) if i%njob==j]) for j in range(njob)]
                    open(condor_dir+'/condor.jds','w').write(
'''executable = {condor_dir}/run.sh
output = {condor_dir}/job$(Process).out
error = {condor_dir}/job$(Process).err
log = {condor_dir}/condor.log
jobbatchname = {name}
getenv = True
{additional}
queue arguments from (
{arguments}
)
'''
                        .format(
                            condor_dir=condor_dir,
                            name=jobbatchname,
                            arguments="\n".join(condor_arguments),
                            additional=get_additional_condor_script(args),
                        )
                    )
                    
                    if args.dag:
                        open(config.condor_path+"/condor.dag","a").write(
'''
JOB {jobname} {jds}
PARENT hists_done CHILD {jobname}
PARENT {jobname} CHILD fits_done
'''
                            .format(jobname=c.fit_file.split(".",1)[0]+"_"+c.name,
                                    jds=condor_dir+'/condor.jds',
                                )
                        )
                    else:
                        print '[Fitting] {} {}'.format(c.fit_file.split(".",1)[0],c.name)
                        clusterid=submit_condor(condor_dir+'/condor.jds')
                        condorlogs[clusterid]=condor_dir+'/condor.log'
        if not args.dag:
            print '  Waiting...'
            for clusterid in condorlogs:
                os.system('condor_wait '+condorlogs[clusterid]+' > /dev/null')
                if not check_condor(clusterid,njob):
                    exit(1)

####################################################################
##### dumping plots
####################################################################
#    shutil.copy('etc/inputs/index.php.listPlots','%s/index.php' % plottingDir)
#            fitzip = '%s/%s/fitCanvas.zip'%(tnpConf.baseOutDir,flag)
#            with ZipFile(fitzip, 'w') as pngzip:
#                for ib in range(len(tnpBins['bins'])) if args.binNumber<0 else args.binNumber:
#                    tnpRoot.histPlotter( fitfile, tnpBins['bins'][ib], plottingDir )
#                    pngzip.write('%s/%s.png' %(plottingDir,tnpBins['bins'][ib]['name']))

                    #os.remove('%s/%s.png' %(plottingDir,tnpBins['bins'][ib]['name'])) # To save fitcanvas only in zip file. (They are too many to view on web)
#                pngzip.write('%s/index.php' % plottingDir)
#                os.remove('%s/index.php' % plottingDir)
                #os.rmdir('%s/' %plottingDir)
#            print ' ===> Plots saved in <======='
#            print fitzip
#>>>>>>> won/MuonTnP_Spark_v1

####################################################################
##### dumping egamma txt file 
####################################################################
#tnpBins = pickle.load( open( '%s/bining.pkl'%(outputDirectory),'rb') )
#outputDirectory = '%s/%s/' % (tnpConf.baseOutDir,args.flag)
#flag.histFile='%s/%s_hist.root' % ( outputDirectory , args.flag )
#flag=tnpConf.flags[args.flag]
#flag.fitFile='%s/%s_fit.root' % ( outputDirectory,args.flag )
if "sum" in args.step:
    if args.dag:
        jobbatchname='{}_{}_sum'.format(os.path.basename(args.settings).split(".",1)[0],args.config)
        open(config.condor_path+"/sum.jds","w").write(
'''executable = /usr/bin/env
arguments = {tnp_base}/tnp_tamsa.py {configfile} {configkey} --step sum
output = {path}/sum.out
error = {path}/sum.err
log = {path}/sum.log
request_memory = 4000
jobbatchname = {name}
getenv = True
{additional}
queue
'''
            .format(
                tnp_base=TNP_BASE,
                configfile=args.settings,
                configkey=args.config,
                path=config.condor_path,
                name=jobbatchname,
                additional=get_additional_condor_script(args),
            )
        )
        open(config.condor_path+"/condor.dag","a").write(
'''
JOB sum {path}/sum.jds
PARENT fits_done CHILD sum
'''
            .format(
                path=config.condor_path,
            )
        )
    else:
        from efficiencyUtils import make_combined_hist
        print '[Summary] collectFits {}'.format(config.data_fit_file)
        #exitcode=os.system("python $TNP_BASE/python/collectFits.py {0}/{1} $(find {0}/{2} -type f -name '*.root'|sort -V) > /dev/null 2>&1".format(config.path,config.data_fit_file,config.data_fit_file.replace(".root",".d")))
        exitcode=os.system("python $TNP_BASE/python/collectFits.py {0}/{1} {0}/{2}".format(config.path,config.data_fit_file,config.data_fit_file.replace(".root",".d")))
        if exitcode!=0:
            print "hadd failed (exitcode={})".format(exitcode)
            exit(1)
        print '[Summary] collectFits {}'.format(config.sim_fit_file)
        #exitcode=os.system("python $TNP_BASE/python/collectFits.py {0}/{1} $(find {0}/{2} -type f -name '*.root'|sort -V) > /dev/null 2>&1".format(config.path,config.sim_fit_file,config.sim_fit_file.replace(".root",".d")))
        exitcode=os.system("python $TNP_BASE/python/collectFits.py {0}/{1} {0}/{2}".format(config.path,config.sim_fit_file,config.sim_fit_file.replace(".root",".d")))
        if exitcode!=0:
            print "hadd failed (exitcode={})".format(exitcode)
            exit(1)

        hists=[]

        data_hists=[]
        for members in config.make_systematics(isSim=False):
            hist_set=[]
            for member in members:
                hist_set+=[member.make_eff_hist()]
            data_hists+=[hist_set]
        hists+=[make_combined_hist(data_hists)]
        hists+=[make_combined_hist(data_hists,stat=False)]
        hists+=[h for ms in data_hists for h in ms]

        sim_hists=[]
        for members in config.make_systematics(isSim=True):
            hist_set=[]
            for member in members:
                hist_set+=[member.make_eff_hist()]
            sim_hists+=[hist_set]
        hists+=[make_combined_hist(sim_hists)]
        hists+=[make_combined_hist(sim_hists,stat=False)]
        hists+=[h for ms in sim_hists for h in ms]

        sf_hists=[[h.Clone(h.GetName().replace("data_","sf_")) for h in members] for members in data_hists]
        for i in range(len(sf_hists)):
            for j in range(len(sf_hists[i])):
                sf_hists[i][j].Divide(sim_hists[i][j])
        hists+=[make_combined_hist(sf_hists)]
        hists+=[make_combined_hist(sf_hists,stat=False)]
        hists+=[h for ms in sf_hists for h in ms]

        f=rt.TFile(config.path+"/efficiency.root","recreate")
        for h in hists:
            h.Write()
        f.Close()

        print '[Summary] Save plots'
        from plotUtils import SavePlots
        SavePlots(config.path+"/efficiency.root")

        if "fix_ptbelow20" in config.option:
            print '[Summary] post-process for "fix_ptbelow20"'
            from PostProcess_fix_ptbelow20 import PostProcess_fix_ptbelow20
            PostProcess_fix_ptbelow20(config.path+"/efficiency.root")


if args.dag:
    open(config.condor_path+"/condor.dag","a").write(
'''
JOB hists_done noop.sub NOOP
JOB fits_done noop.sub NOOP
'''
    )
        
    jobbatchname='{}_{}'.format(os.path.basename(args.settings).split(".",1)[0],args.config)
    exitcode=os.system("condor_submit_dag -import_env -batch-name {name} {path}/condor.dag".format(name=jobbatchname,path=config.condor_path))
    if exitcode==0:
        print "Check dag log"
        print "tail {}/condor.dag.dagman.out".format(config.condor_path)
    else:
        print "condor_submit_dag failed"

endTime=time.time()
print 'Ends at ', time.strftime('%c',time.localtime(endTime))
print 'Time took', endTime-startTime,'seconds.'
