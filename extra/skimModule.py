from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

ROOT.gROOT.SetBatch(True)

class skimProducer(Module):
    def __init__(self):
        print("Loading NanoCORE shared libraries...")
        ROOT.gSystem.Load("NanoTools/NanoCORE/libNANO_CORE.so")
        header_files = ["ElectronSelections", "MuonSelections", "TauSelections", "Config"]
        for header_file in header_files:
            print("Loading NanoCORE {} header file...".format(header_file))
            ROOT.gROOT.ProcessLine(".L NanoTools/NanoCORE/{}.h".format(header_file))

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self._tchain = ROOT.TChain("Events")
        self._tchain.Add(inputFile.GetName())
        print(inputFile)
        if "UL16" in inputFile.GetName():
            ROOT.gconf.nanoAOD_ver = 8
        if "UL17" in inputFile.GetName():
            ROOT.gconf.nanoAOD_ver = 8
        if "UL18" in inputFile.GetName():
            ROOT.gconf.nanoAOD_ver = 8
        ROOT.nt.Init(self._tchain)
        ROOT.gconf.GetConfigs(ROOT.nt.year())
        print("year = {}".format(ROOT.nt.year()))
        print("WP_DeepFlav_loose = {}".format(ROOT.gconf.WP_DeepFlav_loose))
        print("WP_DeepFlav_medium = {}".format(ROOT.gconf.WP_DeepFlav_medium))
        print("WP_DeepFlav_tight = {}".format(ROOT.gconf.WP_DeepFlav_tight))
        pass

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    #def passSkim_2mu1HighPt1HighMll(self, event):
    #    """>=2 mu and >=1 mu with pT>=50 GeV skim and >=1 OS mu pair with M(ll)>100 GeV"""
    #    # print(event._entry)
    #    ROOT.nt.GetEntry(event._entry)
    #    muons = Collection(event, "Muon")
    #    nMu = len(muons)

    #    # Looping over muons
    #    nHighPtMuons = 0
    #    nHighMllOSPair = 0
    #    for i,mu1 in enumerate(muons):
    #        if mu1.pt > 50 and abs(mu1.eta) < 2.4: nHighPtMuons += 1
    #        for j in range(i+1,nMu):
    #            mu2 = muons[j]
    #            if mu1.pdgId == -mu2.pdgId:
    #                if (mu1.p4() + mu2.p4()).M() > 100: nHighMllOSPair += 1

    #    if nMu>=2 and nHighPtMuons>0 and nHighMllOSPair>0:
    #        return True
    #    else:
    #        return False

    #def passSkim_2mu1HighPt1MllonZ(self, event):
    #    """>=2 mu and >=1 mu with pT>=50 GeV skim and >=1 OS mu pair with M(ll)>60 GeV"""
        # print(event._entry)
    #    ROOT.nt.GetEntry(event._entry)
    #    muons = Collection(event, "Muon")
    #    nMu = len(muons)

        # Looping over muons
    #    nHighPtMuons = 0
    #    nMllOSPairOnZ = 0
    #    for i,mu1 in enumerate(muons):
    #        if mu1.pt > 50 and abs(mu1.eta) < 2.4: nHighPtMuons += 1
    #        for j in range(i+1,nMu):
    #            mu2 = muons[j]
    #            if mu1.pdgId == -mu2.pdgId:
    #                if (mu1.p4() + mu2.p4()).M() > 60: nMllOSPairOnZ += 1

     #   if nMu>=2 and nHighPtMuons>0 and nMllOSPairOnZ>0:
     #       return True
     #   else:
     #       return False

    def passSkim_4lep(self, event):
	""" 4 lepton skim """
	ROOT.nt.GetEntry(event._entry)
	muons = Collection(event, "Muon")
        nMu = len(muons)
        electrons = Collection(event, "Electron")
        nEle = len(electrons)

	#Loop over muons
	nCandMu = 0
        for mu in enumerate(muons):
		if mu.pt > 10 and abs(mu.eta) < 2.4 and mu.looseId = 1 and mu.pfIsoId >= 1: nCandMu += 1      

        nCandEle = 0
	for el in enumerate(electrons):
		if el.pt > 10 and abs(el.eta) < 2.5 and el.mvaFall17V2Iso_WPL = 1 and el.pfRelIso03_all > 0.4: nCandEle += 1

	if nCandMu + nCandEle >= 4:
		return True
	else:
		return False

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        #if self.passSkim_2mu1HighPt1HighMll(event):
        #if self.passSkim_2mu1HighPt1MllonZ(event):
	if self.passSkim_4lep(event):
            return True
        else:
            return False

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

skimModuleConstr = lambda: skimProducer()
