#!/bin/env python

from metis.Sample import DBSSample, DirectorySample

# 2022 Data
samples_2022_Data = [ DBSSample(dataset="/DoubleMuon/Run2022"+run+"-ReRecoNanoAODv11-v1/NANOAOD") for run in ["B","C"] ] + \
                    [ DBSSample(dataset="/Muon/Run2022"+run+"-ReRecoNanoAODv11-v1/NANOAOD") for run in ["C","D","E"] ] + \
                    [ DBSSample(dataset="/Muon/Run2022F-PromptNanoAODv11_v1-v2/NANOAOD") for run in ["F","G"] ]
# 2022 Total
samples_2022 = samples_2022_Data

# Total
samples = samples_2022
