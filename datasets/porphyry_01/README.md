This dataset contains the data used in the paper:

@article{Garrido2020,
author = {Garrido, Mauricio and Sep\'uveda, Exequiel and Ortiz, Juli\'an},
pages = {1--24},
title = {{A Methodology for the Simulation of Synthetic Exploration and Geometallurgical Database for Educational Purposes}},
year = {2020}
}

The files are:

1.- pseudo_drillholes.gslib: samples used as conditioning samples to build simulations (GSLIB format).
2.- mineralogical_distributions.csv: mineral proportions used to calculate geochemical composition (CSV format).
3.- correlations.csv: correlations among variables (int the normal score space) for compositional geostatistical simulation (CSV format).
4.- grindability_distributions.csv: distribution of Bwi for back transformation (CSV format).
5.- block_model.csv: simulate geometallugical block model (CSV format).
6.- synthetic_drillholes.gslib: synthetic drillcores sampled from the simulate geometallugical block model (GSLIB format).

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
