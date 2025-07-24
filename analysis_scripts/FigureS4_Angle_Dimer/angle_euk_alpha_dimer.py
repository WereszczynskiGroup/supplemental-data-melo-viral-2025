#!/bin/python3
import os
import MDAnalysis as mda
import numpy as np
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

def vector_between_resids(atomgroup, res1, res2):
    """
    Calculate the vector between two resids.
    """
    pos1 = atomgroup.select_atoms(f"resid {res1}").center_of_mass()
    pos2 = atomgroup.select_atoms(f"resid {res2}").center_of_mass()
    return pos2 - pos1


def super_helical(atomgroup, res1, res2):
    """
    Calculate the vector between two resids.
    """
    pos1 = atomgroup.select_atoms(f"{res1}").center_of_mass()
    pos2 = atomgroup.select_atoms(f"{res2}").center_of_mass()
    return pos2 - pos1


def calculate_angle(vector1, vector2):
    """
    Calculate the angle between two vectors.
    """
    cos_theta = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    return np.degrees(angle)

for i in range(1, 5):
    new_directory="../angle"+str(i)
    os.chdir(new_directory)
    u = mda.Universe("euk_alpha_align.pdb", "euk_alpha.run"+str(i)+".xtc")
    tet_H4_H3 = "resid 380 or resid 408 or resid 867 or resid 895"
    DNA_resid = "resid 74 or resid 221"
    dimer_1_start = 576
    dimer_1_end = 604
    dimer_2_start = 1063
    dimer_2_end = 1091

    with open('euk_alpha_dimer1.'+'sim'+str(i), 'w') as f:
        f.write("#Frame\t#Angle\n")
        for ts in u.trajectory[::1]:
            vector1 = super_helical(u.atoms, tet_H4_H3, DNA_resid)
            vector2 = vector_between_resids(u.atoms, dimer_1_start, dimer_1_end)
            angle = calculate_angle(vector1, vector2)
            f.write(f"{ts.frame}\t{angle}\n")

    with open('euk_alpha_dimer2.'+'sim'+str(i), 'w') as f:
        f.write("#Frame\t#Angle\n")
        for ts in u.trajectory[::1]:
            vector1 = super_helical(u.atoms, tet_H4_H3, DNA_resid)
            vector2 = vector_between_resids(u.atoms, dimer_2_start, dimer_2_end)
            angle = calculate_angle(vector1, vector2)
            f.write(f"{ts.frame}\t{angle}\n")


