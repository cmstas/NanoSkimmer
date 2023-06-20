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
        ROOT.nt.Init(self._tchain)
        #ROOT.gconf.GetConfigs(ROOT.nt.year())
        pass

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def passSkim_HLT_TripleMu_5_3_3_Mass3p8_DZ(self, event):
        """>=2 mu and >=1 mu with pT>=7 GeV and >=2 mu with pT>=5 GeV and >=1 OS mu pair"""
        # print(event._entry)
        ROOT.nt.GetEntry(event._entry)
        muons = Collection(event, "Muon")
        nMu = len(muons)
        if nMu<2:
            return False

        # Looping over muons
        nMu7 = 0
        nMu5 = 0
        nMuOSPair = 0
        for i,mu1 in enumerate(muons):
            if abs(mu1.eta) < 2.4:
                if mu1.pt > 5: nMu5 += 1
                if mu1.pt > 7: nMu7 += 1
                for j in range(i+1,nMu):
                    mu2 = muons[j]
                    if abs(mu2.eta) < 2.4:
                        if mu1.pdgId == -mu2.pdgId: nMuOSPair += 1

        if nMu7>=1 and nMu5>=2 and nMuOSPair>=1:
            return True
        else:
            return False

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        return self.passSkim_HLT_TripleMu_5_3_3_Mass3p8_DZ(event)

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

skimModuleConstr = lambda: skimProducer()
