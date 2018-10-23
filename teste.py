#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:33:48 2018

@author: natalie
"""

import pandas as pd

FILES = ['cfc/cf74', 'cfc/cf75', 'cfc/cf76', 'cfc/cf77', 'cfc/cf78', 'cfc/cf79']
matrixTotal = []

def insert(i, value, vector):
    if(len(vector) <= i):
        vector.insert(i,value)
    else:
        vector[i] += ' ' + value


def constructVector(vector, line, cod):  
    if(cod == 'PN'):
        insert(0, line[3:], vector)
        
    elif(cod == 'RN'):
        insert(1, line[3:], vector)
        
    elif(cod == 'AN'):
        insert(2, line[3:], vector)
        
    elif(cod == 'AU'):
        insert(3, line[3:], vector)

    elif(cod == 'TI'):
        insert(4, line[3:], vector)
        
    elif(cod == 'SO'):
        insert(5, line[3:], vector)
        
    elif(cod == 'MJ'):
        insert(6, line[3:], vector)
    
    elif(cod == 'MN'):
        insert(7, line[3:], vector)
        
    elif((cod == 'AB') or (cod == 'EX')):
        insert(8, line[3:], vector)
        
    elif(cod == 'RF'):
        insert(9, line[3:], vector)
        
    elif(cod == 'CT'):
        insert(10, line[3:], vector)
    else:
        pass
    

def fileToMatrix(file):
    matrix = []
    with open(file, 'r', encoding = 'iso-8859-1') as fp:
        vector = []
        line = fp.readline()
        cod = line[:2]
        constructVector(vector, line.strip().replace("  ", ""), cod)

        while line:
            line = fp.readline()
            if(line == ''):
                print(line)
            if not((line[:2]).isspace()):
                cod = line[:2]
            if((line == "\n") and (vector != [])):
                matrix.append(vector)
                vector = []
            constructVector(vector, line.strip().replace("  ", ""), cod)    
    
    fp.close()
    return matrix

    
    
    
# for file in FILES:
#     matrixTotal.extend(fileToMatrix(file))
    
    
print("aqui")    
m = fileToMatrix('cfc/cf74')    

#print(m)
    
pd.DataFrame(m)    

