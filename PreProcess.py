#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:34:34 2022

@author: aishp
"""
import numpy as np
import scipy.io as scio
import pdb

def ParseMedPC(path):
    """ Reads MedPC output file and parses the events sent during the task to evaluate the animal's performance
    Input - path of the MEDPC file to be parsed."""
    f = open(path)
    li = f.readlines()
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    fi_name = li[12]
    for lines in li:
        tmp = lines.find('A:')
        if tmp>-1:
            id_a = count4
            break
        else:
            id_a = []
        count4 = count4+1
    for lines in li:
        tmp = lines.find('B:')
        if tmp>-1:
            id_b = count5
            break
        else:
            id_b = []
        count5 = count5+1
    for lines in li:
        tmp = lines.find('D:')
        if tmp>-1:
            id_d = count1
            break
        else:
            id_d = []
        count1 = count1+1
        
    for lines in li:
        tmp = lines.find('E:')
        if tmp>-1:
            id_e = count2
            break
        else:
            id_e = []
        count2 = count2+1
        
    for lines in li:
        tmp = lines.find('I:')
        if tmp>-1:
            id_i = count3
            break
        else:
            id_i = []
        count3 = count3+1
    A = li[id_a+1:id_b-1]
    B = li[id_b+1:id_d-1]
    D = li[id_d+1:id_e-1]
    E = li[id_e+1:id_i-1]
    D1 = np.empty(0);
    E1 = np.empty(0)
    A1 = np.empty(0)
    B1 = np.empty(0)
    for i_lines in D:
        tmp1 = i_lines.split(':')
        tmp1 = tmp1[1].split(' ')
        tmp2 = [k for k in tmp1 if k!='']
        tmp3 = np.array([float(j) for j in tmp2])
        D1 = np.append(D1,tmp3)
    for i_lines in E:
        tmp1 = i_lines.split(':')
        tmp1 = tmp1[1].split(' ')
        tmp2 = [k for k in tmp1 if k!='']
        tmp3 = np.array([float(j) for j in tmp2])
        E1 = np.append(E1,tmp3)
    for i_lines in A:
        tmp1 = i_lines.split(':')
        tmp1 = tmp1[1].split(' ')
        tmp2 = [k for k in tmp1 if k!='']
        tmp3 = np.array([float(j) for j in tmp2])
        A1 = np.append(A1,tmp3)
    for i_lines in B:
        tmp1 = i_lines.split(':')
        tmp1 = tmp1[1].split(' ')
        tmp2 = [k for k in tmp1 if k!='']
        tmp3 = np.array([float(j) for j in tmp2])
        B1 = np.append(B1,tmp3)
        
    return D1,E1,A1,B1,fi_name

