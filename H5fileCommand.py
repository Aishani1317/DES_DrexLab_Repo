import h5py
import numpy as np

filename = "/Users/amehta/Desktop/DESY3_Lenser_catalogue_FSHARP_cut_no_sys_removal_w_coadd_id_12August2024.h5"
with h5py.File(filename, 'r') as f:
    print("Top-level Group", list(f.keys())) #lists items in root folder "Lenser"
    for key in f['Lenser'].keys():
       print(" ", key)
