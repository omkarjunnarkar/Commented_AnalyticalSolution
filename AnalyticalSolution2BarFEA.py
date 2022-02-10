## ******************************************************************************************************************************
##                                  Analytical Solution for Finite Element Code for 2 Bar Problem
## Author: Omkar Junnarkar, Semester-3 MSc. Computational Material Science
## Matriculation Nr.: 66157	Email: omkar.junnarkar@student.tu-freiberg.de
## IDE : Visual Studio Code 

## os : To access a directory from system
## numpy : To perform certain matrix operations

import numpy as np
import os

## Changing directory to write files to a specific folder
os.chdir(r"E:\Documents\TU Freiberg CMS\3.Sem-Study Material\PPP\Working_Directory\Analytical_Solution_2Bar")
## Defining Variables
## a1,a2: area of left,right bar
## l1,l2: length of left,right bar
## fmax: value of maximum force applied (N)
## limit: yield stress (MPA)
## E: Young's Modulus (MPA)

a1=17
a2=10
l1=32
l2=57
fmax=6000
limit=220
E=120000

## Opening file in write mode
outF=open("AnalyticalSolution.txt","w")
outF.write("Force      Sigma1       Sigma2      Eps1        Eps2        U       RF1     RF2")
outF.write("\n")

## List of force values at 10000 steps
f=np.linspace(0,fmax,10000)

## p1,p2 : Reaction Force at left,right end
## sigma1,sigma2 : stress in left,right bar
## eps1,eos2 : total strain in left,right bar
## u : Displacement of center node

for force in f:
    ## [Refer Report for Details/Formulae]
    p2=-force/(((l2*a1)/(l1*a2)) + 1)
    p1=p2+force
    sigma1=p1/a1
    sigma2=p2/a2
    eps1=sigma1/E
    eps2=sigma2/E
    u=eps1*l1
    
    ## writing values to the file while in Elastic Limit
    if abs(sigma1)<limit:
        print(force,p1,p2,sigma1,sigma2,u)
        outF.write(str(force))
        outF.write(" ")
        outF.write(str(sigma1))
        outF.write(" ")
        outF.write(str(sigma2))
        outF.write(" ")
        outF.write(str(eps1))
        outF.write(" ")
        outF.write(str(eps2))
        outF.write(" ")
        outF.write(str(u))
        outF.write(" ")
        outF.write(str(p1))
        outF.write(" ")
        outF.write(str(p2))
        outF.write("\n")


outF.close()

## END