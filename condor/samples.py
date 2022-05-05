#!/bin/env python

from metis.Sample import DBSSample, DirectorySample

signalBaseDir = "/ceph/cms/store/user/usarica/Offshell_2L2Nu/PrivateMC/220404"

# 2018 Data
samples_2018_Data = [ DBSSample(dataset="/SingleMuon/Run2018"+run+"-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD") for run in ["A","B","C","D"] ]

# 2018 MC
samples_2018_DY = [ DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM") ]
#samples_2018_ZToMuMu = [ DBSSample(dataset="/ZToMuMu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_M_"+m1+"_"+m2+"/RunIISummer19UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v1/NANOAODSIM") for m1,m2 in zip(["50","200"],["120","400"]) ] + \
#    [ DBSSample( dataset="/ZToMuMu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_M_"+m1+"_"+m2+"/RunIISummer19UL18NanoAOD-106X_upgrade2018_realistic_v11_L1v1-v2/NANOAODSIM") for m1,m2 in zip(["120","400","800","1400","2300","3500","4500","6000"],["200","800","1400","2300","3500","4500","6000","Inf"]) ]
samples_2018_ZToMuMu = [ DBSSample(dataset="/ZToMuMu_M-"+m1+"To"+m2+"_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") for m1,m2 in zip(["50","120","200","400","800","1400","2300","3500","4500","6000"],["120","200","400","800","1400","2300","3500","4500","6000","Inf"]) ]
samples_2018_TT = [ DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") ]
samples_2018_ST = [ DBSSample(dataset="/ST_tW_"+sign+"top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") for sign in ["","anti"] ]
samples_2018_TZq = [ DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") ]
samples_2018_TTX = [ DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") ] + \
    [ DBSSample(dataset="/ttHJetTo"+fs+"bb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") for fs in ["Non",""] ]
samples_2018_Diboson = [ DBSSample(dataset="/"+VV+"_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM") for VV in ["WW","WZ","ZZ"] ]
samples_2018_MC = samples_2018_DY + samples_2018_ZToMuMu + samples_2018_TT + samples_2018_ST + samples_2018_TTX + samples_2018_TZq + samples_2018_Diboson

# 2018 Signal
samples_2018_signal_Y3 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2018_signal_DY3 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2018_signal_DYp3 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2018_signal_B3mL2 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]

# 2018 Total
samples_2018 = samples_2018_Data + samples_2018_MC + samples_2018_signal_Y3 + samples_2018_signal_DY3 + samples_2018_signal_DYp3 + samples_2018_signal_B3mL2



# 2017
# 2017 Data
samples_2017_Data = [ DBSSample(dataset="/SingleMuon/Run2017"+run+"-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD") for run in ["B","C","D","E","F","G","H"] ]

# 2017 MC
samples_2017_DY = [ DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM") ]
#samples_2017_ZToMuMu = [ DBSSample(dataset="/ZToMuMu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_M_"+m1+"_"+m2+"/RunIISummer19UL17NanoAOD-106X_mc2017_realistic_v6-v1/NANOAODSIM") for m1,m2 in zip(["50","120","200","400","800","2300","3500","4500","6000"],["120","200","400","800","1400","3500","4500","6000","Inf"]) ] + \
#    [ DBSSample(dataset="/ZToMuMu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_M_"+m1+"_"+m2+"/RunIISummer19UL17NanoAOD-106X_mc2017_realistic_v6-v2/NANOAODSIM") for m1,m2 in zip(["1400"],["2300"]) ]
samples_2017_ZToMuMu = [ DBSSample(dataset="/ZToMuMu_M-"+m1+"To"+m2+"_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM") for m1,m2 in zip(["50","120","200","400","800","1400","2300","3500","4500","6000"],["120","200","400","800","1400","2300","3500","4500","6000","Inf"]) ]
samples_2017_TT = [ DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM") ]
samples_2017_ST = [ DBSSample(dataset="/ST_tW_"+sign+"top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM") for sign in ["","anti"] ]
samples_2017_TTX = [ DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM") ] + \
    [ DBSSample(dataset="/ttHJetTo"+fs+"bb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM") for fs in ["Non",""] ]
samples_2017_TZq = [ DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM") ]
samples_2017_Diboson = [ DBSSample(dataset="/"+VV+"_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM") for VV in ["WW","WZ","ZZ"] ]
samples_2017_MC = samples_2017_DY + samples_2017_ZToMuMu + samples_2017_TT + samples_2017_ST + samples_2017_TTX + samples_2017_TZq + samples_2017_Diboson

# 2017 Signal
samples_2017_signal_Y3 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2017_signal_DY3 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2017_signal_DYp3 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2017_signal_B3mL2 = [ DirectorySample(
    location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM",
    dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]

# 2017 Total
samples_2017 = samples_2017_Data + samples_2017_MC + samples_2017_signal_Y3 + samples_2017_signal_DY3 + samples_2017_signal_DYp3 + samples_2017_signal_B3mL2



## 2016
# 2016 Data
samples_2016_Data = [ DBSSample(dataset="/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD") ] + \
    [ DBSSample(dataset="/SingleMuon/Run2016"+run+"-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD") for run in ["C","D","E","F"] ] + \
    [ DBSSample(dataset="/SingleMuon/Run2016"+run+"-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD") for run in ["F","G","H"] ]

# 2016 MC
samples_2016_DY = [ DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") ] + \
    [ DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") ]
samples_2016_ZToMuMu = [ DBSSample(dataset="/ZToMuMu_M-"+m1+"To"+m2+"_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") for m1,m2 in zip(["50","120","200","400","800","1400","2300","3500","4500","6000"],["120","200","400","800","1400","2300","3500","4500","6000","Inf"]) ] + \
    [ DBSSample(dataset="/ZToMuMu_M-"+m1+"To"+m2+"_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") for m1,m2 in zip(["50","120","200","400","800","1400","2300","3500","4500","6000"],["120","200","400","800","1400","2300","3500","4500","6000","Inf"]) ]
samples_2016_TT = [ DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") ] + \
    [ DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") ]
samples_2016_ST = [ DBSSample(dataset="/ST_tW_"+sign+"top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") for sign in ["","anti"] ] + \
    [ DBSSample(dataset="/ST_tW_"+sign+"top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") for sign in ["","anti"] ]
samples_2016_TTX = [ DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") ] + \
    [ DBSSample(dataset="/ttHJetTo"+fs+"bb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") for fs in ["Non",""] ] + \
    [ DBSSample(dataset="/ttHJetTo"+fs+"bb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") for fs in ["Non",""] ]
samples_2016_TZq = [ DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") ] + \
    [ DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") ]
samples_2016_Diboson = [ DBSSample(dataset="/"+VV+"_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM") for VV in ["WW","WZ","ZZ"] ] + \
    [ DBSSample(dataset="/"+VV+"_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM") for VV in ["WW","WZ","ZZ"] ]
samples_2016_MC = samples_2016_DY + samples_2016_ZToMuMu + samples_2016_TT + samples_2016_ST + samples_2016_TTX + samples_2016_TZq + samples_2016_Diboson

# 2016 Signal
samples_2016_signal_Y3 = [
    DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ] + \
    [ DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_Y3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2016_signal_DY3 = [
    DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ] + \
    [ DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DY3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2016_signal_DYp3 = [
    DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ] + \
    [ DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_DYp3_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]
samples_2016_signal_B3mL2 = [
    DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ] + \
    [ DirectorySample(
        location=signalBaseDir+"/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM",
        dataset ="/ZPrimeToMuMuSB_M"+m+"_bestfit_TuneCP5_13TeV_Allanach_B3mL2_5f_madgraph_pythia8_NoPSWgts/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_private/NANOAODSIM") for m in ["100","200","400","700","1000","1500","2000"] ]

# 2016 Total
samples_2016 = samples_2016_Data + samples_2016_MC + samples_2016_signal_Y3 + samples_2016_signal_DY3 + samples_2016_signal_DYp3 + samples_2016_signal_B3mL2

# Total
samples = samples_2018 + samples_2017 + samples_2016
