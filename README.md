# Overview

This creates a NanoSkimmer based on ```nanoAOD-tools```.  

## Creating skimmer

We need to create a ```package.tar.gz``` for the condor jobs.  

The selections are defined in ```extra/skimModule.py```.  

Also ```extra/keep_and_drop.txt``` contains the list of branches to keep or drop.  

Modify the files to your liking.  

Then, to create a ```package.tar.gz``` for the condor jobs

    sh create_package.sh # This creates a package.tar.gz

To test the package locally on some NanoAOD file

    sh test_package.sh package.tar.gz /hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3_ext1/merged/output.root

Copy the package.tar.gz to ```/nfs-7``` area

    cp package.tar.gz /nfs-7/userdata/phchang/NanoSkimmers/TTHID_3l_v2_package.tar.gz

## Condor

First create a ```package.tar.gz``` following the previous section instruction.

Then go to ```condor/```

    cd condor

Then, setup the ```ProjectMetis```

    cd ProjectMetis
    source setup.sh
    cd ../

And run

    python runMetis.py TTHID_3l_v2 # automatically picks up /nfs-7/userdata/phchang/NanoSkimmers/TTHID_3l_v2_package.tar.gz

Repeatedly run it until the jobs are all done and the merging is done.

Modify the file content of ```runMetis.py``` to your liking.

NOTE: ```/nfs-7/userdata/phchang``` is hardcoded! so please change if you don't have your skimmer in philip's place. (Or ask him to put it in his place.)  
Or, if needed, in ```runMetis.py```, point to the desired ```package.tar.gz``` by modifying ```tarfile``` variable, and give a new ```tag```.

## Samples

The sample list are in ```samples.py```

To find some samples there is a bash script that may be useful.
Below is an example of finding ```WZTo3LNu``` sample. (-a means "all" as in print all possible ones that matches)
Then the following text can be copied adn pasted into ```samples.py``` to build user's sample list.

    $ sh find_sample.sh -a WZTo3LNu 18
    DBSSample(dataset="/WZTo3LNu_mllmin4p0_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 2.96,nfiles: 19,nevents: 1998000,nlumis: 1998,
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 14.94,nfiles: 18,nevents: 9821283,nlumis: 9445,
    DBSSample(dataset="/WZTo3LNu_mllmin0p1_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"), # filesizeGB: 110.02,nfiles: 113,nevents: 89270000,nlumis: 89270,


