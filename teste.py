# -*- coding: utf-8 -*-

# fazendo parse do arquivo de query
import numpy as np

cfquery = 'cfc/cfquery'
queryFile = []
weight = [1, 1, 1, 1] # peso, repectivamente, referente aos avaliadores: REW, REW colleagues, REW post-doctorates e JBW

def scoreCalc(weigth, v):
    values = [int(digit) for digit in v]
    weighted_avg = np.average(values, weights=weight)
    return weighted_avg

def insertQ(i, value, vector):
    #print("aqui3")
    if(len(vector) <= i):
        #print("aqui4")
        vector.insert(i,value)
    else:
        if(type(value) is list):
            #print("aqui5")
           # print(vector[i])
            vector[i].extend(value)
        else:
           # print("aqui6")
            vector[i] += ' ' + value

def constructQueryVector(vector, line, cod):  
    if(cod == 'QN'):
        insertQ(0, line, vector)
        
    elif(cod == 'QU'):
        insertQ(1, line, vector)
        
    elif(cod == 'NR'):
        insertQ(2, line, vector)
        
    elif(cod == 'RD'):
        #line = line.strip().replace("  ", " ")
        v = line.split(' ')
        v1 = []
        ve = []
        for i, result in enumerate(v):
            if not(result):
                continue          
            v1.append(result)
            if(len(v1) == 2):
                v1[0] = int(v1[0])
                score = scoreCalc(weight, v1[1])
                v1[1] = score
                ve.append(v1)
                v1 = []
        return        
        insertQ(3, ve, vector)
    else:
        pass

def queryMatrix(file):
    matrix = []
    with open(file, 'r', encoding = 'iso-8859-1') as fp:
        vector = []
        line = fp.readline()
        cod = line[:2]
        constructQueryVector(vector, line[3:].strip(), cod)
        while line:
            line = fp.readline()
            
            if not((line[:2]).isspace()):
                cod = line[:2]
                line = line[3:]
        
            if(line.isspace()):
                matrix.append(vector)
                vector = []
            constructQueryVector(vector, line.strip(), cod)    
    
    fp.close()
    return matrix


m = queryMatrix(cfquery)

queryFile.extend(m)

print(queryFile)