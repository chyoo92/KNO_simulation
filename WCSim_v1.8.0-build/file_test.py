import os
import ROOT
import numpy as np
import h5py
from tqdm import tqdm
import argparse


ROOT.gSystem.Load("/users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/libWCSimRoot.so")
fin = ROOT.TFile("/users/hep/yewzzang/WCSim_KNO/WCSim_v1.8.0-build/mu_500_new/mu_500MeV_1.root")



eventT = fin.Get("wcsimT")
event = ROOT.WCSimRootEvent()
eventT.SetBranchAddress("wcsimrootevent", event)
eventT.GetBranch("wcsimrootevent").SetAutoDelete(1)
eventT.GetEntry(0)
nEvents = eventT.GetEntries()

## Load the geometry
geomT = fin.Get("wcsimGeoT")
geom = ROOT.WCSimRootGeom()
geomT.SetBranchAddress("wcsimrootgeom", geom)
geomT.GetEntry(0)
nODPMTs = geom.GetODWCNumPMT()
nPMTs = geom.GetWCNumPMT()

print("--------------------")
print(f" nEvents = {nEvents}")
print(f" nPMTs   = {nPMTs}")
print(f" nODPMTs = {nODPMTs}")
print("--------------------")

out_pmt_x = np.zeros(nPMTs)
out_pmt_y = np.zeros(nPMTs)
out_pmt_z = np.zeros(nPMTs)

out_pmt_px = np.zeros(nPMTs)
out_pmt_py = np.zeros(nPMTs)
out_pmt_pz = np.zeros(nPMTs)

for iPMT in range(nPMTs):
    pmt = geom.GetPMT(iPMT)
    out_pmt_x[iPMT] = pmt.GetPosition(0)
    out_pmt_y[iPMT] = pmt.GetPosition(1)
    out_pmt_z[iPMT] = pmt.GetPosition(2)
    out_pmt_px[iPMT] = pmt.GetOrientation(0)
    out_pmt_py[iPMT] = pmt.GetOrientation(1)
    out_pmt_pz[iPMT] = pmt.GetOrientation(2)

print("@@@ Start analysing data")
out_vtx_x = np.zeros(nEvents)
out_vtx_y = np.zeros(nEvents)
out_vtx_z = np.zeros(nEvents)
out_vtx_t = np.zeros(nEvents)

out_vtx_dx = np.zeros(nEvents)
out_vtx_dy = np.zeros(nEvents)
out_vtx_dz = np.zeros(nEvents)

out_vtx_px = np.zeros(nEvents)
out_vtx_py = np.zeros(nEvents)
out_vtx_pz = np.zeros(nEvents)
out_vtx_ke = np.zeros(nEvents)
out_vtx_ke2 = np.zeros(nEvents)

out_pmt_q = np.zeros((nEvents, nPMTs))
out_pmt_t = np.zeros((nEvents, nPMTs))
for iEvent in tqdm(range(nEvents)):
    eventT.GetEvent(iEvent)
    trigger = event.GetTrigger(0)

    if trigger.GetNvtxs() == 0: continue
    if trigger.GetNtrack() == 0: continue

    out_vtx_x[iEvent] = trigger.GetVtx(0)
    out_vtx_y[iEvent] = trigger.GetVtx(1)
    out_vtx_z[iEvent] = trigger.GetVtx(2)
    out_vtx_t[iEvent] = 0

    firstTrack = trigger.GetTracks()[0]

    out_vtx_dx[iEvent] = firstTrack.GetDir(0)
    out_vtx_dy[iEvent] = firstTrack.GetDir(1)
    out_vtx_dz[iEvent] = firstTrack.GetDir(2)

    out_vtx_px[iEvent] = firstTrack.GetPdir(0)
    out_vtx_py[iEvent] = firstTrack.GetPdir(1)
    out_vtx_pz[iEvent] = firstTrack.GetPdir(2)
    out_vtx_ke[iEvent] = firstTrack.GetE()
    out_vtx_ke2[iEvent] = firstTrack.GetE()-firstTrack.GetM()
    nHitsC = trigger.GetNcherenkovdigihits()
    for iHit in range(nHitsC):
        hit = trigger.GetCherenkovDigiHits().At(iHit)
        iPMT = hit.GetTubeId()-1
        out_pmt_q[iEvent, iPMT] = hit.GetQ()
        out_pmt_t[iEvent, iPMT] = hit.GetT()

pmts_num = (np.sum(out_pmt_q>0,axis=1) > 1000)
aaa = (out_vtx_z < out_pmt_z.max()-200) & (out_vtx_z > -(out_pmt_z.max()-200))
dis = (np.linalg.norm(np.zeros((2,out_vtx_x.shape[0]))-[out_vtx_x,out_vtx_y],axis=0)<(out_pmt_x.max()-200))


out_vtx_x = out_vtx_x[pmts_num & dis & aaa]
out_vtx_y = out_vtx_y[pmts_num & dis & aaa]
out_vtx_z = out_vtx_z[pmts_num & dis & aaa]
out_vtx_t = out_vtx_t[pmts_num & dis & aaa]

out_vtx_px = out_vtx_px[pmts_num & dis & aaa]
out_vtx_py = out_vtx_py[pmts_num & dis & aaa]
out_vtx_pz = out_vtx_pz[pmts_num & dis & aaa]
out_vtx_ke = out_vtx_ke[pmts_num & dis & aaa]
out_vtx_ke2 = out_vtx_ke2[pmts_num & dis & aaa]

out_pmt_t = out_pmt_t[pmts_num & dis & aaa]
out_pmt_q = out_pmt_q[pmts_num & dis & aaa]




cut_events = (out_pmt_q.shape[0]/2000)*100
print("cut % = "+ f"{cut_events:.3f}"+"%")
