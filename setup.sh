#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc7_amd64_gcc900/cms/cmssw/CMSSW_11_2_5/src/
eval `scramv1 runtime -sh`
cd -

if grep -q "release 9" /etc/redhat-release; then
    export LD_LIBRARY_PATH=/lib64:$LD_LIBRARY_PATH
fi

export TNP_BASE=`pwd`
export PYTHONPATH=$TNP_BASE/python${PYTHONPATH:+:$PYTHONPATH}

if hostname | grep -q lxplus; then
    TNP_OUTPUT=`echo $HOME|sed 's@/afs/cern.ch@/eos@'`"/tnp_tamsa_output"
    if [ ! -e "$TNP_OUTPUT" ]; then
	mkdir -p $TNP_OUTPUT
    fi

    if [ -e "$TNP_BASE/results" ] && [ ! -L "$TNP_BASE/results" ]; then
	echo "Please remove results directory"
	unset TNP_BASE
	return
    fi
    
    if [ ! -e "$TNP_BASE/results" ]; then
	ln -s "$TNP_OUTPUT" "$TNP_BASE/results"
    fi
fi

