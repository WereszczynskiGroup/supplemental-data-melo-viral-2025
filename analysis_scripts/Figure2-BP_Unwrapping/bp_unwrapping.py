#!/usr/bin/env python

#Viral Protein / Widom 601 DNA - Run1

######### Import packages #################


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy.linalg
import MDAnalysis as mda
from MDAnalysis.analysis import contacts
import MDAnalysis.core
from scipy.spatial import distance
from numpy import *

font ={'family': 'sans-serif',
      'color': 'black',
      'weight':'bold'}



############# Load in trajectory files and the parmtop file ############

top_file = 'virus_widom.run1.prmtop'

u1_done = mda.Universe(top_file,'virus_widom.run1.xtc')
ref_u1_done = mda.Universe(top_file,'virus_widom.run1.xtc')
u1 = mda.Universe(top_file,'virus_widom.run2.xtc')
ref_u1 = mda.Universe(top_file,'virus_widom.run2.xtc')
u3 = mda.Universe(top_file,'virus_widom.run3.xtc')
ref_u3 = mda.Universe(top_file,'virus_widom.run3.xtc')
u4 = mda.Universe(top_file,'virus_widom.run4.xtc')
ref_u4 = mda.Universe(top_file,'virus_widom.run4.xtc') 

#####

#####




#############  RMSD of Entry & Exit DNA using MDAnalysis #########


Entry_DNA='resid 0-73 or resid 222-294'
Exit_DNA='resid 74-146 or resid 147-221'


import MDAnalysis.analysis.rms

R = MDAnalysis.analysis.rms.RMSD(u1, u1,
           select="resid 295-1092",             # entire DNA 
           groupselections=[Entry_DNA,
                           Exit_DNA],
           ref_frame=0)
           
R.run()


##################################################################
######################### RMSD per residue #######################


import MDAnalysis
import MDAnalysis.analysis.rms


j=1
k=294

for i in range (0,147):
    
    BP1 = 'resid ' + str(j) + ' or resid ' + str(k)
    BP2 = 'resid ' + str(j) + ' or resid ' + str(k)
    R = MDAnalysis.analysis.rms.RMSD(u1, u1,
               select="resid 295-1092",             # entire DNA 
               groupselections=[BP1,
                                BP2],
               ref_frame=0)
    R.run()
    
    bp_df = pd.DataFrame(R.results.rmsd,columns=['Frame', 'Time (ps)','protein','BP' + str(j),'BP' + str(j)])
    
    if j == 1:
        first_bp_df = bp_df
        
    else:
        rest_bp_df = first_bp_df.merge(bp_df,how = 'left')
        first_bp_df = rest_bp_df
    
    print(j)
    j=j+1
    k=k-1


looking = first_bp_df.loc[:,~first_bp_df.columns.duplicated()].copy()

###looking is the dataframe with frame values, time, protein, BP1-BP147 rmsds to the first frame for 2000ns



#### Clean up RMSD dataframe
looking2=looking.drop("Time (ps)", axis='columns')
looking3=looking2.drop("protein", axis='columns')
looking4 = looking3
looking4["Frame"] = looking3["Frame"] + 1
looking4 =looking4.set_index(['Frame'])

#### Filter RMSD values, greater than 7A = unwrapped(1), less than 7A = wrapped(0)
rmsd_wrap = looking4.mask(looking4 <7 , 0)
rmsd_unwrap = rmsd_wrap.mask(rmsd_wrap >7 , 1)
rmsd_unwrap1 = rmsd_unwrap

###rmsd_uwrap1 is final bp dataframe alone with bp wrapped behavior for rmsd each bp


#################################################################
##################### Contacts definition #######################


def contacts_within_cutoff(u, group_a, group_b, radius=4.5):
        timeseries = []
        for ts in u.trajectory[0:20000:1]:
            gr1 = group_a.positions
            gr2 = group_b.positions
            dist = contacts.distance_array(gr1, gr2)
            n_contacts = contacts.contact_matrix(dist, radius).sum()
            timeseries.append([ts.frame, n_contacts])
        return np.array(timeseries)


###################################################################################


######### Contacts between DNA and protein for each BP using MDAnalysis ##########

j =1
k =294

for i in range(0,147):

    sel = 'resid' + " " + str(j)
    sel1 = 'resid' + " " + str(k)
    chain1 = u1.select_atoms('resid 295 to 1092') #reference against, dna
    chain2 = u1.select_atoms(sel) + u1.select_atoms(sel1)

    run1 = contacts_within_cutoff(u1, chain1, chain2, radius=4.5)

    run1_df = pd.DataFrame(run1, columns=['Frame','BP'+ str(j)])

    if j == 1:
        first_one=run1_df
    else:
        second_one = first_one.merge(run1_df,how ='left')
        first_one=second_one
        

    j = j +1
    k = k -1
    print(j)
    
contacts_df=first_one

###contacts_df is the dataframe with frame values, BP1-BP147 contact counts to the first frame for 2000ns


#### Clean up contacts dataframe
contacts_bp = contacts_df
contacts_bp["Frame"] = contacts_df["Frame"] + 1
contacts_bp =contacts_bp.set_index(['Frame'])
contacts_bp


#### Filter contact values, less than 1 = unwrapped(1), greater than 0 = wrapped(0)
contacts_1 = contacts_bp.mask(contacts_bp <1 , int(-1))
contacts_2 = contacts_1.mask(contacts_1 >0 , int(0))
contacts_3 = contacts_2.mask(contacts_2 <0 , int(1))
contacts_4 = contacts_3
#contacts_4 is final bp dataframe alone with bp wrapped behavior using contacts for each bp






####################################################################################
################## Combine and apply conditions for BP unwrapping ##################
############################				############################

combine_rmsd_con= rmsd_unwrap1 + contacts_4

#### Modify combined dataframe, values <2 are wrapped(0), values >1 are unwrapped(1)
combined_rmsd_con1 = combine_rmsd_con.mask(combine_rmsd_con <2 , int(0))
combined_rmsd_con2 = combined_rmsd_con1.mask(combined_rmsd_con1 >1 , int(1))
combined_rmsd_con3 = combined_rmsd_con2


##########
#### combined_rmsd_con3 dataframe has the unwrapping behavior for BP overtime
###########





#### Seperate data for Entry DNA & Exit DNA
##Entry DNA (BP 1-73)
entry_unwrapped=combined_rmsd_con2.iloc[:,0:73]
entry_unwrapped_1=entry_unwrapped
sum_of_bp_en_1 = entry_unwrapped.sum(axis=1)
sum_of_bp_en_1.name='Sum'
entry_unwrapped_1.insert(73,'Sum',sum_of_bp_en_1)
entry_unwrapped_1.to_csv('entry_unwrapped_1.csv')

##Exit DNA (BP 74-147)
exit_unwrapped=combined_rmsd_con2.iloc[:,74:147]
exit_unwrapped_1=exit_unwrapped
sum_of_bp_ex_1 = exit_unwrapped.sum(axis=1)
sum_of_bp_ex_1.name='Sum'
exit_unwrapped_1.insert(73,'Sum',sum_of_bp_ex_1)
exit_unwrapped_1.to_csv('exit_unwrapped_1.csv')
