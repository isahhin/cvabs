# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:46:16 2019

@author: Hasan
"""
import tensorflow as tf
import numpy as np
from numpy import linalg as la
from keras.layers.core import Activation, Reshape
from tensorflow.python.keras import backend as K
import matplotlib.pyplot as plt
 
def projection_onto_vector(B, Q):

    m, n = Q.shape[0], Q.shape[1] 
    #m:vector size
    #n: number of vector
    Adiff=0*B    
    for ii in range(n):       
         q = Q[ :,  ii]
     
         dp = np.dot( q, B)
         #print('B', B)
         res = dp*q
         #print(res)
         Adiff = Adiff +res
         
    return Adiff

def cva_compute(data, curFrame):
    
    #print(data)
    h  = data.shape[0]
    w  = data.shape[1]
    n  = data.shape[2]
    fs = h*w
   # print('fs', fs)
    
    data = np.reshape(data, (fs,n) )
    #print('data', data)
    DiffFrms = np.zeros( (fs,n-1), dtype="float32")
    
    #DiffFrms =  0*data[:, 0:n-1]
    refIndex = 0 # selecting a reference image
    ref = data[:, refIndex ]
    
    ref_expanded = np.outer(ref, np.ones(n-1) )
    DiffFrms = data[:, 1:n] - ref_expanded 
    

    # gram schmidt orthogonalization on difference subspace (DiffFrms)
    Q, R = la.qr(DiffFrms)
    
    # Adiff: The difference vector of associated with reference vector(ref)
    # Acom: The common vector of processed class

    #difference vector assoicated with reference image  
    Adiff = projection_onto_vector(ref, Q)
    Acom = ref - Adiff

    #difference vector assoicated with test image
    curFrame = np.reshape(curFrame, (fs) )
    Adiff_ref = projection_onto_vector(curFrame, Q)
    Acom_ref = curFrame - Adiff_ref


    cva_dist = Acom_ref - Acom
    
    Acom = np.reshape(Acom, (h,w) )
    Acom_ref = np.reshape(Acom_ref, (h,w) )
    cva_dist = np.reshape(cva_dist, (h,w) )
    
    #imgplot = plt.imshow( cva_dist)
    #plt.show()
    
    return np.abs(cva_dist)