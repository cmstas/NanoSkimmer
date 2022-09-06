from metis.Sample import DirectorySample, DBSSample

# Master list of all samples
# Specify a dataset name and a short name for the output root file on nfs
	
samples_signal_2018 = {
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")                               : "WWZ",
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM")                          : "WWZ_ext1",
        DBSSample(dataset="/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2")                               : "WWZ_Jets",
        DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM") : "HZJ",
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")            : "GGZHtoWW",
        DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")           : "VHToNonbb",
}

samples_signal_2017 = {
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")                                          : "WWZ",
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM")                                     : "WWZ_ext1",
        DBSSample(dataset="/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                               : "WWZ_Jets",
        DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")            : "HZJ",
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                       : "GGZHtoWW",
        DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                      : "VHToNonbb",
}

samples_signal_2016 = {
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")                                        : "WWZ",
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM")                                   : "WWZ_ext1",
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")                              : "WWZ_preVFP",
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM")                         : "WWZ_preVFP_ext1",
        DBSSample(dataset="/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")                             : "WWZ_Jets",
        DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")          : "HZJ",
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")                     : "GGZHtoWW",
        DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")            : "GGZHtoWW_PSweights",
        DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")                    : "VHToNonbb",
}

samples_ZZ_2018 = {
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")                                 : "ZZTo4L",
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")                   : "ZZTo4L_JME",
}

samples_ZZ_2017 = {
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                                            : "ZZTo4L",
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM")                              : "ZZTo4L_JME",
}

samples_ZZ_2016 = {
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")                                          : "ZZTo4L",
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")                            : "ZZTo4L_JME",
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

samples = samples_signal_2018 + samples_signal_2017 + samples_signal_2016 + samples_ZZ_2018 + samples_ZZ_2017 + samples_ZZ_2016
