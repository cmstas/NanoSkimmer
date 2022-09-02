from metis.Sample import DirectorySample, DBSSample

# Master list of all samples
# Specify a dataset name and a short name for the output root file on nfs
	
samples_VVV4L_2018 = {
        # Data
        DBSSample(dataset="/EGamma/Run2018A-Nano25Oct2019-v1/NANOAOD")                                                                                                         : "EGamma_2018A",
        DBSSample(dataset="/EGamma/Run2018B-Nano25Oct2019-v1/NANOAOD")                                                                                                         : "EGamma_2018B",
        DBSSample(dataset="/EGamma/Run2018C-Nano25Oct2019-v1/NANOAOD")                                                                                                         : "EGamma_2018C",
        DBSSample(dataset="/EGamma/Run2018D-Nano25Oct2019-v1/NANOAOD")                                                                                                         : "EGamma_2018D",
        DBSSample(dataset="/DoubleMuon/Run2018A-Nano25Oct2019-v1/NANOAOD")                                                                                                     : "DoubleMuon_2018A",
        DBSSample(dataset="/DoubleMuon/Run2018B-Nano25Oct2019-v1/NANOAOD")                                                                                                     : "DoubleMuon_2018B",
        DBSSample(dataset="/DoubleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD")                                                                                                     : "DoubleMuon_2018C",
        DBSSample(dataset="/DoubleMuon/Run2018D-Nano25Oct2019_ver2-v1/NANOAOD")                                                                                                : "DoubleMuon_2018D",
        DBSSample(dataset="/MuonEG/Run2018A-Nano25Oct2019-v1/NANOAOD")                                                                                                         : "MuonEG_2018A",
        DBSSample(dataset="/MuonEG/Run2018B-Nano25Oct2019-v1/NANOAOD")                                                                                                         : "MuonEG_2018B",
        DBSSample(dataset="/MuonEG/Run2018C-Nano25Oct2019-v1/NANOAOD")                                                                                                         : "MuonEG_2018C",
        DBSSample(dataset="/MuonEG/Run2018D-Nano25Oct2019_ver2-v1/NANOAOD")                                                                                                    : "MuonEG_2018D",
        # "/SingleMuon/Run2018A-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018A",
        # "/SingleMuon/Run2018B-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018B",
        # "/SingleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018C",
        # "/SingleMuon/Run2018D-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018D",
        # Signals
        DBSSample(dataset="/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")           : "WWW_2l"   ,
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                     : "WWW_incl" ,
        DBSSample(dataset="/WWZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")           : "WWZ_4l"   ,
        DBSSample(dataset="/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                        : "WWZ_incl" ,
        DBSSample(dataset="/WZZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")           : "WZZ_4l"   ,
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                        : "WZZ_incl" ,
        DBSSample(dataset="/ZZZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")           : "ZZZ_4l"   ,
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                        : "ZZZ_incl" ,
        DBSSample(dataset="/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")              : "VHtoNonBB",
        DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")      : "ZHtoWW",
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM") : "GGZHtoWW",
        # Backgrounds
        # ZZ
        DBSSample(dataset="/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_ext1_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")           : "ZZcontTo2e2mu",
        DBSSample(dataset="/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_ext1_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")          : "ZZcontTo2e2tau",
        DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")              : "ZZcontTo2mu2tau",
        DBSSample(dataset="/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM")              : "ZZcontTo4e",
        DBSSample(dataset="/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM")             : "ZZcontTo4mu",
        DBSSample(dataset="/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")            : "ZZcontTo4tau",
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM")                       : "ZZ",
        # TTZ
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")           : "TTZnlo",
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_v6_102X_mc2017_realistic_v7-v1/NANOAODSIM")     : "TTZLOW",
        # WZ
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")               : "WZ",
        # TWZ
        DBSSample(dataset="/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")    : "TWZ",
        # X + gamma
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")                             : "WZG",
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")                    : "WZG",
        # DY/ttbar
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")     : "DY_low",
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")              : "DY_high",
        # "/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM" : "DYzpt150",
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")                         : "TTDL",
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext3-v1/NANOAODSIM")             : "TTSL",
        # Others
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")         : "GGHtoZZto4L",
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")                   : "TTHtoNonBB",
        # TT + X
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")   : "TTWnlo",
        # TT + XX
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/NANOAODSIM")                       : "TTWW",
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                       : "TTWZ",
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                       : "TTZZ",
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                       : "TTWH",
        DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20_ext1-v1/NANOAODSIM")                       : "TTZH",
        }

samples_VVV4L_2017 = {
        # Data
        DBSSample(dataset="/DoubleEG/Run2017B-Nano25Oct2019-v1/NANOAOD")   : "DoubleEG_2017B",
        DBSSample(dataset="/DoubleEG/Run2017C-Nano25Oct2019-v1/NANOAOD")   : "DoubleEG_2017C",
        DBSSample(dataset="/DoubleEG/Run2017D-Nano25Oct2019-v1/NANOAOD")   : "DoubleEG_2017D",
        DBSSample(dataset="/DoubleEG/Run2017E-Nano25Oct2019-v1/NANOAOD")   : "DoubleEG_2017E",
        DBSSample(dataset="/DoubleEG/Run2017F-Nano25Oct2019-v1/NANOAOD")   : "DoubleEG_2017F",
        DBSSample(dataset="/DoubleMuon/Run2017B-Nano25Oct2019-v1/NANOAOD") : "DoubleMuon_2017B",
        DBSSample(dataset="/DoubleMuon/Run2017C-Nano25Oct2019-v1/NANOAOD") : "DoubleMuon_2017C",
        DBSSample(dataset="/DoubleMuon/Run2017D-Nano25Oct2019-v1/NANOAOD") : "DoubleMuon_2017D",
        DBSSample(dataset="/DoubleMuon/Run2017E-Nano25Oct2019-v1/NANOAOD") : "DoubleMuon_2017E",
        DBSSample(dataset="/DoubleMuon/Run2017F-Nano25Oct2019-v1/NANOAOD") : "DoubleMuon_2017F",
        DBSSample(dataset="/MuonEG/Run2017B-Nano25Oct2019-v1/NANOAOD")     : "MuonEG_2017B",
        DBSSample(dataset="/MuonEG/Run2017C-Nano25Oct2019-v1/NANOAOD")     : "MuonEG_2017C",
        DBSSample(dataset="/MuonEG/Run2017D-Nano25Oct2019-v1/NANOAOD")     : "MuonEG_2017D",
        DBSSample(dataset="/MuonEG/Run2017E-Nano25Oct2019-v1/NANOAOD")     : "MuonEG_2017E",
        DBSSample(dataset="/MuonEG/Run2017F-Nano25Oct2019-v1/NANOAOD")     : "MuonEG_2017F",
        # "/SingleMuon/Run2018A-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018A",
        # "/SingleMuon/Run2018B-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018B",
        # "/SingleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018C",
        # "/SingleMuon/Run2018D-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018D",
        # Signals
        DBSSample(dataset="/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")  : "WWW_2l"   ,
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/NANOAODSIM")             : "WWW_incl" ,
        DBSSample(dataset="/WWZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")  : "WWZ_4l"   ,
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/NANOAODSIM")             : "WWZ_incl" ,
        DBSSample(dataset="/WZZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v2/NANOAODSIM")  : "WZZ_4l"   ,
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM")           : "WZZ_incl",
        DBSSample(dataset="/ZZZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")  : "ZZZ_4l"   ,
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM")           : "ZZZ_incl",
        DBSSample(dataset="/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")     : "VHtoNonBB",
        DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM") : "ZHtoWW",
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_pythia8_TuneCP5/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")      : "GGZHtoWW",
        # Backgrounds
        # ZZ
        DBSSample(dataset="/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")       : "ZZcontTo2e2mu",
        DBSSample(dataset="/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")      : "ZZcontTo2e2tau",
        DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM") : "ZZcontTo2mu2tau",
        DBSSample(dataset="/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/NANOAODSIM")      : "ZZcontTo4e",
        DBSSample(dataset="/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM")    : "ZZcontTo4mu",
        DBSSample(dataset="/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")        : "ZZcontTo4tau",
        DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM")                      : "ZZ",
        # TTZ
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM")       : "TTZnlo",
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")                 : "TTZLOW",
        # WZ
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM")   : "WZ",
        # TWZ
        DBSSample(dataset="/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM") : "TWZ",
        # X + gamma
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM")                             : "WZG",
        # DY/ttbar
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM") : "DY_low",
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv6-PU2017RECOSIMstep_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM") : "DY_high",
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM")        : "TTDL",
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM")    : "TTSL",
        # Others
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7_ext3-v1/NANOAODSIM") : "GGHtoZZto4L",
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM")  : "TTHtoNonBB",
        # TT + X
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM") : "TTWnlo",
        # TT + XX
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7_ext1-v1/NANOAODSIM")      : "TTWW",
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM")           : "TTWZ",
        DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v2/NANOAODSIM")           : "TTZH",
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM")           : "TTZZ",
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM")           : "TTWH",
        }

samples_VVV4L_2016 = {
        # Data
        DBSSample(dataset="/DoubleEG/Run2016B_ver1-Nano25Oct2019_ver1-v1/NANOAOD") : "DoubleEG_2016Bv1",
        DBSSample(dataset="/DoubleEG/Run2016B_ver2-Nano25Oct2019_ver2-v1/NANOAOD") : "DoubleEG_2016Bv2",
        DBSSample(dataset="/DoubleEG/Run2016C-Nano25Oct2019-v1/NANOAOD")           : "DoubleEG_2016C",
        DBSSample(dataset="/DoubleEG/Run2016D-Nano25Oct2019-v1/NANOAOD")           : "DoubleEG_2016D",
        DBSSample(dataset="/DoubleEG/Run2016E-Nano25Oct2019-v1/NANOAOD")           : "DoubleEG_2016E",
        DBSSample(dataset="/DoubleEG/Run2016F-Nano25Oct2019-v1/NANOAOD")           : "DoubleEG_2016F",
        DBSSample(dataset="/DoubleEG/Run2016G-Nano25Oct2019-v1/NANOAOD")           : "DoubleEG_2016G",
        DBSSample(dataset="/DoubleEG/Run2016H-Nano25Oct2019-v1/NANOAOD")           : "DoubleEG_2016H",
        DBSSample(dataset="/DoubleMuon/Run2016B_ver1-Nano25Oct2019_ver1-v1/NANOAOD") : "DoubleMuon_2016Bv1",
        DBSSample(dataset="/DoubleMuon/Run2016B_ver2-Nano25Oct2019_ver2-v1/NANOAOD") : "DoubleMuon_2016Bv2",
        DBSSample(dataset="/DoubleMuon/Run2016C-Nano25Oct2019-v1/NANOAOD")           : "DoubleMuon_2016C",
        DBSSample(dataset="/DoubleMuon/Run2016D-Nano25Oct2019-v1/NANOAOD")           : "DoubleMuon_2016D",
        DBSSample(dataset="/DoubleMuon/Run2016E-Nano25Oct2019-v1/NANOAOD")           : "DoubleMuon_2016E",
        DBSSample(dataset="/DoubleMuon/Run2016F-Nano25Oct2019-v1/NANOAOD")           : "DoubleMuon_2016F",
        DBSSample(dataset="/DoubleMuon/Run2016G-Nano25Oct2019-v1/NANOAOD")           : "DoubleMuon_2016G",
        DBSSample(dataset="/DoubleMuon/Run2016H-Nano25Oct2019-v1/NANOAOD")           : "DoubleMuon_2016H",
        DBSSample(dataset="/MuonEG/Run2016B_ver1-Nano25Oct2019_ver1-v1/NANOAOD") : "MuonEG_2016Bv1",
        DBSSample(dataset="/MuonEG/Run2016B_ver2-Nano25Oct2019_ver2-v1/NANOAOD") : "MuonEG_2016Bv2",
        DBSSample(dataset="/MuonEG/Run2016C-Nano25Oct2019-v1/NANOAOD")           : "MuonEG_2016C",
        DBSSample(dataset="/MuonEG/Run2016D-Nano25Oct2019-v1/NANOAOD")           : "MuonEG_2016D",
        DBSSample(dataset="/MuonEG/Run2016E-Nano25Oct2019-v1/NANOAOD")           : "MuonEG_2016E",
        DBSSample(dataset="/MuonEG/Run2016F-Nano25Oct2019-v1/NANOAOD")           : "MuonEG_2016F",
        DBSSample(dataset="/MuonEG/Run2016G-Nano25Oct2019-v1/NANOAOD")           : "MuonEG_2016G",
        DBSSample(dataset="/MuonEG/Run2016H-Nano25Oct2019-v1/NANOAOD")           : "MuonEG_2016H",
        # "/SingleMuon/Run2018A-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018A",
        # "/SingleMuon/Run2018B-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018B",
        # "/SingleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018C",
        # "/SingleMuon/Run2018D-Nano25Oct2019-v1/NANOAOD"                                                                                                     : "SingleMuon_2018D",
        # Signals
        DBSSample(dataset="/WWW_4F_DiLeptonFilter_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                    : "WWW_2l" ,
        DBSSample(dataset="/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                   : "WWW_incl",
        DBSSample(dataset="/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                      : "WWZ_incl",
        DBSSample(dataset="/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                      : "WZZ_incl",
        DBSSample(dataset="/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                      : "ZZZ_incl",
        DBSSample(dataset="/VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                            : "VHtoNonBB",
        DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                             : "ZHtoWW",
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                        : "GGZHtoWW",
        # "/WWZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM"                     : "WWZ_4l"   ,
        # "/WZZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v2/NANOAODSIM"                     : "WZZ_4l"   ,
        # "/ZZZJetsTo4L2Nu_4f_TuneCP5_13TeV_amcatnloFXFX_pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM"                     : "ZZZ_4l"   ,
        # Backgrounds
        # ZZ
        DBSSample(dataset="/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                              : "ZZcontTo2e2mu",
        DBSSample(dataset="/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                             : "ZZcontTo2e2tau",
        DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                            : "ZZcontTo2mu2tau",
        DBSSample(dataset="/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                 : "ZZcontTo4e",
        DBSSample(dataset="/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                : "ZZcontTo4mu",
        DBSSample(dataset="/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                               : "ZZcontTo4tau",
        DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                                  : "ZZ",
        # TTZ
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext3-v1/NANOAODSIM")                    : "TTZnlo",
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv6-Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                   : "TTZLOW",
        # WZ
        DBSSample(dataset="/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")                              : "WZ",
        # TWZ
        DBSSample(dataset="/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                         : "TWZ",
        # X + gamma
        DBSSample(dataset="/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                                      : "WZG",
        # DY/ttbar
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")             : "DY_low",
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext2-v1/NANOAODSIM")                 : "DY_high",
        DBSSample(dataset="/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")                    : "TTDL",
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")           : "TTSLtop",
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")        : "TTSLtopbar",
        # Others
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                          : "GGHtoZZto4L",
        DBSSample(dataset="/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM")                : "TTHtoNonBB",
        # TT + X
        DBSSample(dataset="/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext2-v1/NANOAODSIM")            : "TTWnlo",
        # TT + XX
        DBSSample(dataset="/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")                              : "TTWW",
        DBSSample(dataset="/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")                              : "TTWZ",
        DBSSample(dataset="/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")                              : "TTZH",
        DBSSample(dataset="/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")                              : "TTZZ",
        DBSSample(dataset="/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv6-PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM")                              : "TTWH",
        }

samples_VVV4L_2016_EFT = {
                DirectorySample(location="/hadoop/cms/store/user/rembserj/samples/WWZ_dim8_extended_20200605_four_lepton_RunIISummer16NanoAOD/NanoAODv7/", dataset="/WWZ_4l_EFT_Jonas/RunIISummer16NanoAODv7-v1/NANOAODSIM") : "EFT_WWZ_4l",
        }

samples_VVV4L_2017_EFT = {
                DirectorySample(location="/hadoop/cms/store/user/rembserj/samples/WWZ_dim8_extended_20200605_four_lepton_RunIIFall17NanoAOD/NanoAODv7/", dataset="/WWZ_4l_EFT_Jonas/RunIIFall17NanoAODv7-v1/NANOAODSIM") : "EFT_WWZ_4l",
        }

samples_VVV4L_2018_EFT = {
                DirectorySample(location="/hadoop/cms/store/user/rembserj/samples/WWZ_dim8_extended_20200605_four_lepton_RunIIAutumn18NanoAOD/NanoAODv7/", dataset="/WWZ_4l_EFT_Jonas/RunIIAutumn18NanoAODv7-v1/NANOAODSIM") : "EFT_WWZ_4l",
                DirectorySample(location="/hadoop/cms/store/user/phchang/samples/WZZ_dim8_RunIIAutumn18NanoAOD/NanoAODv7/", dataset="/WZZ_EFT_Sapta/RunIIAutumn18NanoAODv7-v1/NANOAODSIM") : "EFT_WZZ_incl",
                DirectorySample(location="/hadoop/cms/store/user/phchang/samples/ZZZ_dim8_RunIIAutumn18NanoAOD/NanoAODv7/", dataset="/ZZZ_EFT_Sapta/RunIIAutumn18NanoAODv7-v1/NANOAODSIM") : "EFT_ZZZ_incl",
        }


data_2016 = {
	DBSSample(dataset="/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")		: "data_Run2016Bv1_ee",
	DBSSample(dataset="/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")		: "data_Run2016Bv2_ee",
	DBSSample(dataset="/DoubleEG/Run2016C-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016C_ee",
	DBSSample(dataset="/DoubleEG/Run2016D-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016D_ee",
	DBSSample(dataset="/DoubleEG/Run2016E-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016E_ee",
	DBSSample(dataset="/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")		: "data_Run2016Fv1_ee",
	DBSSample(dataset="/DoubleEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016Fv2_ee",
	DBSSample(dataset="/DoubleEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016G_ee",
	DBSSample(dataset="/DoubleEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016H_ee",
	DBSSample(dataset="/MuonEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")		: "data_Run2016Bv1_em", 
	DBSSample(dataset="/MuonEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")		: "data_Run2016Bv2_em",
	DBSSample(dataset="/MuonEG/Run2016C-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016C_em",
	DBSSample(dataset="/MuonEG/Run2016D-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016D_em",
	DBSSample(dataset="/MuonEG/Run2016E-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016E_em",
	DBSSample(dataset="/MuonEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")		: "data_Run2016Fv1_em",
	DBSSample(dataset="/MuonEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016Fv2_em",
	DBSSample(dataset="/MuonEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016G_em",
	DBSSample(dataset="/MuonEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016H_em",
	DBSSample(dataset="/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")	: "data_Run2016Bv1_mm",
	DBSSample(dataset="/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")	: "data_Run2016Bv2_mm",
	DBSSample(dataset="/DoubleMuon/Run2016C-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016C_mm",
	DBSSample(dataset="/DoubleMuon/Run2016D-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016D_mm",
	DBSSample(dataset="/DoubleMuon/Run2016E-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016E_mm",
	DBSSample(dataset="/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2016Fv1_mm",
	DBSSample(dataset="/DoubleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016Fv2_mm",
	DBSSample(dataset="/DoubleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")			: "data_Run2016G_mm",
	DBSSample(dataset="/DoubleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")			: "data_Run2016H_mm",
}

data_2017 = {
        DBSSample(dataset="/DoubleEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")              : "data_Run2017B_ee",
        DBSSample(dataset="/DoubleEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")              : "data_Run2017C_ee",
        DBSSample(dataset="/DoubleEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")              : "data_Run2017D_ee",
        DBSSample(dataset="/DoubleEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")              : "data_Run2017E_ee",
        DBSSample(dataset="/DoubleEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")              : "data_Run2017F_ee",
        DBSSample(dataset="/MuonEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2017B_em",
        DBSSample(dataset="/MuonEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2017C_em",
        DBSSample(dataset="/MuonEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2017D_em",
        DBSSample(dataset="/MuonEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2017E_em",
        DBSSample(dataset="/MuonEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2017F_em",
	DBSSample(dataset="/DoubleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2017B_ee",
        DBSSample(dataset="/DoubleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2017C_ee",
        DBSSample(dataset="/DoubleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2017D_ee",
        DBSSample(dataset="/DoubleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2017E_ee",
        DBSSample(dataset="/DoubleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2017F_ee",

}

data_2018 = {

        DBSSample(dataset="/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2018A_e",
        DBSSample(dataset="/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2018B_e",
        DBSSample(dataset="/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2018C_e",
	DBSSample(dataset="/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD")		   : "data_Run2018D_e",
        DBSSample(dataset="/MuonEG/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2018A_em",
        DBSSample(dataset="/MuonEG/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2018B_em",
        DBSSample(dataset="/MuonEG/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2018C_em",
        DBSSample(dataset="/MuonEG/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")                : "data_Run2018D_em",
        DBSSample(dataset="/DoubleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2018A_mm",
        DBSSample(dataset="/DoubleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2018B_mm",
        DBSSample(dataset="/DoubleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")            : "data_Run2018C_mm",
        DBSSample(dataset="/DoubleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD")            : "data_Run2018D_mm",
}

samples = samples_VVV4L_2018
