## Quick start

```
source setup.sh
# python tnp_tamsa.py CONFIG_FILE CONFIG_KEY
python tnp_tamsa.py config/AFBMuon_v15.py 2018_MediumID_LooseTrkIso
```

## Configuration
In the config file, you should define a dictionary called 'Configs' as below. See more examples in `config` directory.
```python
from tnpConfig import tnpConfig
Configs["2018_muonID"]=tnpConfig(
  data="/path/to/data.root",
  sim="/path/to/sim.root",
  ...
)
```
### tnpConfig parameters
The parameters for tnpConfig class are listed below. The parameters can be prefixed by 'data_' or 'sim_' to specify it is only for certain type of sample.
- **data**: Path to data ROOT file(s)
- **sim**: Path to simulation ROOT file(s)
- **tree**: TTree name
- **mass**: Branch name or expression for the mass variable to be used as x-axis of histograms
- **expr**: Expression for the event selection
- **test**: Expression for the pass condition
- **weight**: Expression for the event weight
- **maxweight**: maximum value of absolute weight.
- **hist_nbins**: Number of mass bins
- **hist_range**: Minimum and maximum mass as a tuple. ex) (60.0, 120.0)
- **bins**: TnP binning
- **genmatching**: Expression for the gen-matching
- **genmass**: Expression for the generator level mass.
- **method**: TnP method. 'fit' or 'count'.
- **fit_parameter** (only for fit method): List of strings for RooWorkspace factory. You should define PDFs with name of 'sigPass', 'sigFail', 'bkgPass' and 'bkgFail'.
- **fit_range** (only for fit method): Mass range for fitting
- **count_range**: Mass range for the efficiency evaluation. It could be different from **fit_range**.
- **option**: extra options separated by space; 'saveprefit', 'fix_below20'
- **systematic**: Definition of systematic variations.
