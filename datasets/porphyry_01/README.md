This dataset contains the data used in the paper:

@article{garrido2020simulation,
  title={Simulation of synthetic exploration and geometallurgical database of porphyry copper deposits for educational purposes},
  author={Garrido, Mauricio and Sep{\'u}lveda, Exequiel and Ortiz, Julian and Townley, Brian},
  journal={Natural Resources Research},
  volume={29},
  pages={3527--3545},
  year={2020},
  publisher={Springer}
}

The files are:

1. pseudo_drillholes.gslib: samples used as conditioning samples to build simulations (GSLIB format).
1. mineralogical_distributions.csv: mineral proportions used to calculate geochemical composition (CSV format).
1. correlations.csv: correlations among variables (int the normal score space) for compositional geostatistical simulation (CSV format).
1. grindability_distributions.csv: distribution of Bwi for back transformation (CSV format).
1. block_model.csv: simulate geometallugical block model (CSV format).
1. synthetic_drillholes.gslib: synthetic drillcores sampled from the simulate geometallugical block model (GSLIB format).

# Individual file descriptions

## pseudo_drillholes.gslib

midx,midy,midz location of the sample
minz           mineralisation zone:

                1: Oxidized copper ores with evidence of leaching on the groundwater level of the deposit.
                2: Sulphides of chalcocite and digenite (sulphides layer).
                3: Primary hypogene sulphides with high chalcopyrite: pyrite ratio.
                4: Primary hypogene sulphides with low chalcopyrite: pyrite ratio.
                5: Waste and Gravel without economic content associated with copper.

## mineralogical_distributions.csv

clays         % of clays
chalcocite    % of chalcocite
bornite       % of bornite
chalcopyrite  % of chalcopyrite
tennantite    % of tennantite
molibdenite   % of molibdenite
pyrite        % of pyrite

## correlations.csv

Nscore:data   variable name
clays         % of clays
chalcocite    % of chalcocite
bornite       % of bornite
chalcopyrite  % of chalcopyrite
tennantite    % of tennantite
molibdenite   % of molibdenite
pyrite        % of pyrite

## grindability_distributions.gslib

bwi           Bond work index distribution for simulating back transform

## block_model.csv

x,y,z         location of the block centre
ton           tonnage of the block
clays         % of clays
chalcocite    % of chalcocite
bornite       % of bornite
chalcopyrite  % of chalcopyrite
tennantite    % of tennantite
molibdenite   % of molibdenite
pyrite        % of pyrite
cu            total copper grade (%)
mo            total molibdenum grade (%)
as            total arsenic grade (ppm)
rec           rougher recovery (%)
bwi           Bond work index (kwh/tc)
