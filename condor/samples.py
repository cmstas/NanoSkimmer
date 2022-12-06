from metis.Sample import DirectorySample, DBSSample

# Master list of all samples
# Specify a dataset name and a short name for the output root file on nfs
	
samples_signal_2018 = {
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")                               : "WWZ",
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM")                          : "WWZ_ext1",
        DBSSample(dataset="/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")                    : "WWZ_Jets",
        #DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM") : "HZJ",
        #DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")            : "GGZHtoWW",
	#DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")   : "GGZHtoWW_PSweights",
        #DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")           : "VHToNonbb",
}

samples_signal_2017 = {
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")                                          : "WWZ",
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM")                                     : "WWZ_ext1",
        DBSSample(dataset="/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                               : "WWZ_Jets",
        #DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")            : "HZJ",
        #DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                       : "GGZHtoWW",
	#DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")	       : "GGZHtoWW_PSweights",
        #DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                      : "VHToNonbb",
}

samples_signal_2016 = {
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")                                        : "WWZ",
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM")                                   : "WWZ_ext1",
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")                              : "WWZ_preVFP",
        #DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM")                         : "WWZ_preVFP_ext1",
        DBSSample(dataset="/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")                             : "WWZ_Jets",
        #DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")          : "HZJ",
	#DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"): "HZJ_preVFP",
        #DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")                     : "GGZHtoWW",
	#DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")	       : "GGZHtoWW_preVFP",
        #DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")            : "GGZHtoWW_PSweights",
	#DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")  : "GGZHtoWW_preVFP_PSweights",
        #DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")                    : "VHToNonbb",
	#DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "VHToNonbb_preVFP",
}

samples_ZZ_2018 = {
	DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")					       : "ZZ",
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")                                 : "ZZTo4L",
	DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")			       : "ZZTo2L2Nu",
	DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	       : "ZZTo2Q2L",
	#DBSSample(dataset="/ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")			       : "ZZTo2Q2Nu",
	DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")			       : "ZZTo4Q",
	DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")	       : "ggZZTo2e2mu",
	DBSSample(dataset="/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")	       : "ggZZTo2e2nu",
	DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")	       : "ggZZTo2e2tau",
	DBSSample(dataset="/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")            : "ggZZTo2mu2nu",
	DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")	       : "ggZZTo2mu2tau",
	DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")		       : "ggZZTo4e",
	DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")	       : "ggZZTo4mu",
	DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")	       : "ggZZTo4tau",
}

samples_ZZ_2017 = {
	DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")						       : "ZZ",
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")                                            : "ZZTo4L",
	DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")					       : "ZZTo2L2Nu",
	DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")			       : "ZZTo2Q2L",
	DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				       : "ZZTo4Q",
	DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")			       : "ggZZTo2e2mu",
	DBSSample(dataset="/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")			       : "ggZZTo2e2nu",
	DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")		       : "ggZZTo2e2tau",
	DBSSample(dataset="/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")		       : "ggZZTo2mu2nu",
	DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")		       : "ggZZTo2mu2tau",
	DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")			       : "ggZZTo4e",
	DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")			       : "ggZZTo4mu",
	DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")			       : "ggZZTo4tau",
}

samples_ZZ_2016 = {
	#DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")						       : "ZZ",
	#DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")					       : "ZZ_preVFP",
        #DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")                                          : "ZZTo4L",
	#DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")				       : "ZZTo4L_preVFP",
	#DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "ZZTo2L2Nu",
	#DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")			       : "ZZTo2L2Nu_preVFP",
	#DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")			       : "ZZTo2Q2L",
	#DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")	       : "ZZTo2Q2L_preVFP",
	#DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "ZZTo4Q",
	#DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")		       : "ZZTo4Q_preVFP",
	#DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")		       : "ggZZTo2e2mu",
	#DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "ggZZTo2e2mu_preVFP",
	#DBSSample(dataset="/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")		       : "ggZZTo2e2nu",
	#DBSSample(dataset="/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM")	       : "ggZZTo2e2nu_preVFP",
	#DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")		       : "ggZZTo2e2tau",
	#DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "ggZZTo2e2tau_preVFP",
	#DBSSample(dataset="/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")		       : "ggZZTo2mu2nu",
	#DBSSample(dataset="/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "ggZZTo2mu2nu_preVFP",
	#DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")		       : "ggZZTo2mu2tau",
	#DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "ggZZTo2mu2tau_preVFP",
	DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")			       : "ggZZTo4e",
	#DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "ggZZTo4e_preVFP",
	DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")			       : "ggZZTo4mu",
	#DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "ggZZTo4mu_preVFP",
	#DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")		       : "ggZZTo4tau",
	#DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "ggZZTo4tau_preVFP",
}

samples_ttZ_2018 = {

	DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")		       : "TTZToLL_M-1to10",
	DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")		       : "TTZToLL_M-10",
	DBSSample(dataset="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")			       : "TTZToQQ",

}

samples_ttZ_2017 = {

	DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				       : "TTZToLL_M-1to10",
	DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				       : "TTZToLL_M-10",
	DBSSample(dataset="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				               : "TTZToQQ",

}

samples_ttZ_2016 = {

	DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")			       : "TTZToLL_M-1to10",
	DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")		       : "TTZToLL_M-1to10_preVFP",
	DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")			       : "TTZToLL_M-10",
	DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")		       : "TTZToLL_M-10_preVFP",
	DBSSample(dataset="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "TTZToQQ",
	DBSSample(dataset="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")			       : "TTZToQQ_preVFP",

}

samples_ttW_2018 = {

	DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	       : "TTWlv",		
	DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	       : "TTWqq",

}

samples_ttW_2017 = {

        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")                        : "TTWlv",        
        DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")   	               : "TTWqq",

}

samples_ttW_2016 = {

        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")                      : "TTWlv",        
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")            : "TTWlv_preVFP",
	DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")   	               : "TTWqq",
        DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")             : "TTWqq_preVFP",

}

samples_tWZ_2018 = {

	DBSSample(dataset="/ST_tWll_5f_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")			       : "tWZ",

}

samples_tWZ_2017 = {

	DBSSample(dataset="/ST_tWll_5f_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				       : "tWZ",
	
}

samples_tWZ_2016 = {

	DBSSample(dataset="/ST_tWll_5f_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "tWZ",
	#Need to add preVFP sample as well (does it exist????)
}


samples_WZ_2018 = {

	DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")					       : "WZ",
	DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	       : "WZTo2Q2L",
	DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")			       : "WZTo3LNu",
	DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")		       : "WZTo1L1Nu2Q",
	DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")		       : "WZTo1L3Nu",

}

samples_WZ_2017 = {

        DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")						       : "WZ",
        DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")			       : "WZTo2Q2L",
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")				       : "WZTo3LNu",
        DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")			       : "WZTo1L1Nu2Q",
        DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				       : "WZTo1L3Nu",

}

samples_WZ_2016 = {

	DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")						       : "WZ",
        DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")					       : "WZ_preVFP",
        DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")			       : "WZTo2Q2L",	
        DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")	       : "WZTo2Q2L_preVFP",
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "WZTo3LNu",
	DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")			       : "WZTo3LNu_preVFP",
        DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")			       : "WZTo1L1Nu2Q",
        DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")		       : "WZTo1L1Nu2Q_preVFP",
        DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")			       : "WZTo1L3Nu",
        DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")		       : "WZTo1L3Nu_preVFP",

}

samples_WJets_2018 = {

	DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")			       : "WJets",
	DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")		       : "WJets-v2",

}

samples_WJets_2017 = {

        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				       : "WJets",
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")				       : "WJets-v2",

}

samples_WJets_2016 = {

        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "WJets",
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")				       : "WJets-v2",
	DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")		       : "WJets-v2_preVFP",

}

samples_DYJets_2018 = {

	DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")		       : "DYJets_M-50",
	DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	       : "DYJets_M-10to50",

}

samples_DYJets_2017 = {

        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")			       : "DYJets_M-50",
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")			       : "DYJets_M-10to50",

}

samples_DYJets_2016 = {

        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")			       : "DYJets_M-50",
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")		       : "DYJets_M-50_preVFP",
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")			       : "DYJets_M-10to50",
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")	       : "DYJets_M-10to50_preVFP",

}

samples_ttbar_2018 = {

	DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")			       : "TTTo2L2Nu",
	DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")		       : "TTToSemiLeptonic",

}

samples_ttbar_2017 = {

        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")					       : "TTTo2L2Nu",
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				       : "TTToSemiLeptonic",

}

samples_ttbar_2016 = {

        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "TTTo2L2Nu",
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")			       : "TTTo2L2Nu_preVFP",
	DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "TTToSemiLeptonic",
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")		       : "TTToSemiLeptonic_preVFP",
}

samples_WW_2018 = {

	DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")			       : "WW",

}

samples_WW_2017 = {

	DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")					       : "WW",

}

samples_WW_2016 = {

	DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				       : "WW",
	DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")			       : "WW_preVFP",
}

samples_SSWW_2018 = {

	DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")				       : "SSWW",

}

samples_SSWW_2017 = {

	DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")				               : "SSWW",

}

samples_SSWW_2016 = {

	DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")				               : "SSWW",
	DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")				       : "SSWW_preVFP",

}

samples_ttH_2018 = {

	DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")       : "ttH",

}

samples_ttH_2017 = {

	DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")		       : "ttH",

}

samples_ttH_2016 = {

	DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")		       : "ttH",
	DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")      : "ttH_preVFP",

}

samples_ST_2018 = {

	DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	       : "ST_schan_lep",	
	DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	: "ST_top_tchan",	
	DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	: "ST_antitop_tchan",	
	DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")     : "ST_top_nohad_tW",	
	DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") : "ST_antitop_nohad_tW",	

}

samples_ST_2017 = {

	DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")  		       : "ST_schan_lep",	
	DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")       : "ST_top_tchan",
	DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")   : "ST_antitop_tchan",
	DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")                : "ST_top_nohad_tW",
	DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")            : "ST_antitop_nohad_tW",	
}

samples_ST_2016 = {

	DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")  		       : "ST_schan_lep",	
	DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")        : "ST_schan_lep_preVFP",
	DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")     : "ST_top_tchan",
	DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")  : "ST_top_tchan_preVFP",
	DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") : "ST_antitop_tchan",
	DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")  : "ST_antitop_tchan_preVFP",
	DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")  	       : "ST_top_nohad_tW",
	DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")    : "ST_top_nohad_tW_preVFP",
	DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")          : "ST_antitop_nohad_tW",
	DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"): "ST_antitop_nohad_tW_preVFP",

}

samples_tZq_2018 = {

	DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")	               : "tZq",

}

samples_tZq_2017 = {

	DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")                               : "tZq",

}

samples_tZq_2016 = {

	DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")   			       : "tZq",
	DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")                   : "tZq_preVFP",

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

samples = data_2018
