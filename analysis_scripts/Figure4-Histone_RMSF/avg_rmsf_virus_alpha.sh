#!/bin/bash




cpptraj <<_EOF
readdata virus_alpha.rmsf.H3_A_1.dat 
readdata virus_alpha.rmsf.H3_A_2.dat 
readdata virus_alpha.rmsf.H3_A_3.dat 
readdata virus_alpha.rmsf.H3_A_4.dat 
readdata virus_alpha.rmsf.H3_E_1.dat 
readdata virus_alpha.rmsf.H3_E_2.dat 
readdata virus_alpha.rmsf.H3_E_3.dat 
readdata virus_alpha.rmsf.H3_E_4.dat 
avg  virus_alpha.rmsf.H3_A_1.dat:2 virus_alpha.rmsf.H3_A_2.dat:2 virus_alpha.rmsf.H3_A_3.dat:2 virus_alpha.rmsf.H3_A_4.dat:2 virus_alpha.rmsf.H3_E_1.dat:2 virus_alpha.rmsf.H3_E_2.dat:2 virus_alpha.rmsf.H3_E_3.dat:2 virus_alpha.rmsf.H3_E_4.dat:2 oversets out virus_alpha.rmsf.H3_avg.error.dat
go
_EOF



cpptraj <<_EOF
readdata virus_alpha.rmsf.H4_B_1.dat 
readdata virus_alpha.rmsf.H4_B_2.dat 
readdata virus_alpha.rmsf.H4_B_3.dat 
readdata virus_alpha.rmsf.H4_B_4.dat 
readdata virus_alpha.rmsf.H4_F_1.dat 
readdata virus_alpha.rmsf.H4_F_2.dat 
readdata virus_alpha.rmsf.H4_F_3.dat 
readdata virus_alpha.rmsf.H4_F_4.dat 
avg  virus_alpha.rmsf.H4_B_1.dat:2 virus_alpha.rmsf.H4_B_2.dat:2 virus_alpha.rmsf.H4_B_3.dat:2 virus_alpha.rmsf.H4_B_4.dat:2 virus_alpha.rmsf.H4_F_1.dat:2 virus_alpha.rmsf.H4_F_2.dat:2 virus_alpha.rmsf.H4_F_3.dat:2 virus_alpha.rmsf.H4_F_4.dat:2 oversets out virus_alpha.rmsf.H4_avg.error.dat
go
_EOF


cpptraj <<_EOF
readdata virus_alpha.rmsf.H2A_C_1.dat
readdata virus_alpha.rmsf.H2A_C_2.dat
readdata virus_alpha.rmsf.H2A_C_3.dat
readdata virus_alpha.rmsf.H2A_C_4.dat
readdata virus_alpha.rmsf.H2A_G_1.dat
readdata virus_alpha.rmsf.H2A_G_2.dat
readdata virus_alpha.rmsf.H2A_G_3.dat
readdata virus_alpha.rmsf.H2A_G_4.dat
avg  virus_alpha.rmsf.H2A_C_1.dat:2 virus_alpha.rmsf.H2A_C_2.dat:2 virus_alpha.rmsf.H2A_C_3.dat:2 virus_alpha.rmsf.H2A_C_4.dat:2 virus_alpha.rmsf.H2A_G_1.dat:2 virus_alpha.rmsf.H2A_G_2.dat:2 virus_alpha.rmsf.H2A_G_3.dat:2 virus_alpha.rmsf.H2A_G_4.dat:2 oversets out virus_alpha.rmsf.H2A_avg.error.dat
go
_EOF


cpptraj <<_EOF
readdata virus_alpha.rmsf.H2B_D_1.dat
readdata virus_alpha.rmsf.H2B_D_2.dat
readdata virus_alpha.rmsf.H2B_D_3.dat
readdata virus_alpha.rmsf.H2B_D_4.dat
readdata virus_alpha.rmsf.H2B_H_1.dat
readdata virus_alpha.rmsf.H2B_H_2.dat
readdata virus_alpha.rmsf.H2B_H_3.dat
readdata virus_alpha.rmsf.H2B_H_4.dat
avg  virus_alpha.rmsf.H2B_D_1.dat:2 virus_alpha.rmsf.H2B_D_2.dat:2 virus_alpha.rmsf.H2B_D_3.dat:2 virus_alpha.rmsf.H2B_D_4.dat:2 virus_alpha.rmsf.H2B_H_1.dat:2 virus_alpha.rmsf.H2B_H_2.dat:2 virus_alpha.rmsf.H2B_H_3.dat:2 virus_alpha.rmsf.H2B_H_4.dat:2 oversets out virus_alpha.rmsf.H2B_avg.error.dat
go
_EOF



