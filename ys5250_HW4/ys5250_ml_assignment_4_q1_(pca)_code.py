# -*- coding: utf-8 -*-
"""ys5250 ML Assignment 4 Q1 (PCA) Code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kjtb1C1Q8dzmBJ5ci9Sogv8pSELIL-TB
"""

import scipy.io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigh
from sklearn.model_selection import train_test_split

#importing dataset
dataset = scipy.io.loadmat('teapots.mat')

#getting the teapotImages from the datset
X = dataset['teapotImages']

#Calculating the mean
mu = np.mean(X, axis = 0)
mu = mu.reshape(1, 1900)

#Visualising the obtained mean image
print("Mean vector visualized as an image")
mu_img  = mu.reshape(50, 38)
plt.imshow(mu_img.T)
plt.show()

#calculating X - mu to further calulate covariance
X_mu = X - np.repeat(mu, 100, axis = 0)

#calculating covariance
cov = (X_mu.T@X_mu) / X_mu.shape[0]

#calculating eigenvalues and corresponding eigenvectors
eig_vals, eig_vectors = eigh(cov)

#extracting top 3 eigenvectors
eig_sort = np.argsort(-eig_vals)
e = eig_vectors[:, eig_sort[:3]]

#Visualizing the top 3 eigenvectors
print("Eigenvector 1 visualized:")
e1_img = e.T[0].reshape(50, 38)
plt.imshow(e1_img.T)
plt.show()

print("Eigenvector 2 visualized:")
e2_img = e.T[1].reshape(50, 38)
plt.imshow(e2_img.T)
plt.show()

print("Eigenvector 3 visualized:")
e3_img = e.T[2].reshape(50, 38)
plt.imshow(e3_img.T)
plt.show()

#computing the projection matrix
pro_mat = np.dot(e, e.T)

#computing reconstructed images
rec_img = np.dot(X, pro_mat)

#calculating least squared error
lse = np.square(rec_img - X).sum(axis = 1).mean()

print("Mean Squared Error: " , lse)

#printing 10 random images (original and reconstructed)
img = np.random.randint(99, size = 10)

for i in img:
  print("Original Image:", i)
  X_im = X[i].reshape(50, 38)
  plt.imshow(X_im.T)
  plt.show()
  
  print("Reconstructed Image:", i)
  X_rec = rec_img[i].reshape(50, 38)
  plt.imshow(X_rec.T)
  plt.show()
  
  print('\n')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from numpy.linalg import eigh
from scipy.io import loadmat
import pandas as pd
from sklearn.model_selection import train_test_split

data = loadmat('teapots.mat')

X = data['teapotImages']

print("Given X is:", X)
print("X.shape is:", X.shape)


#****Train-Test split
X_train, X_test = train_test_split(X, test_size = 0.1, random_state = 50)
print(X_train.shape)
print(X_test.shape)

#******Taking mean*****#
mu = np.mean(X, axis=0)
print("mu.shape is:", mu.shape)
mu = mu.reshape(1,1900)
print("mu.shape after reshape is:", mu.shape)
#print("np.repeat function is ", np.repeat(u,100,axis=0))

X_bar = X - np.repeat(mu,100,axis=0)
print("X_bar is:", X_bar)
print("X_bar.shape  is:", X_bar.shape)

Cov_mat = X_bar.T.dot(X_bar)/(X_bar.shape[0])
print("Cov_mat.shape is ", Cov_mat.shape)
print("Cov_mat is ", Cov_mat)

#Calculating eigenvalues and right eigen vectors
eig_val, eig_vec = eigh(Cov_mat)

#Sorting them in decreasing order and picking the top 3 eigenvectors
sorted_eig = np.argsort(-eig_val)
print("sorted_eig is", sorted_eig)
eig_val = eig_val[sorted_eig[:3]]
eig_vec = eig_vec[:, sorted_eig[:3]]

print("eig_val is", eig_val, "eig_vec is", eig_vec)
print("eig_vec.shape is ", eig_vec.shape)

#Now to reconstruct the images from the lower dimensional,
#we first need to project the input data onto the vector space spanned by the eignvectors
#For this, we find the projection matrix

P = eig_vec@eig_vec.T

print("P.shape is", P.shape)
print("P is", P)

#Now let's calculate loss and create an array of reconstructed images
loss = []
reconstructions = []

#Now, lets calculate reconst which will be matrix multiplication between X_test and P
reconst = X_test @ P
print("reconst shape is:", reconst.shape)
print("reconst matrix is", reconst)

#Now let's print the mean square error of the reconstructed matrix vs original matrix
error = np.square(reconst - X_test).sum(axis = 1).mean()
print("error.shape is", error.shape)
print("error is", error)


fig1, axis1 = plt.subplots(2,5)
fig1, axis2 = plt.subplots(2,5)

Orig_X = X_test[0].reshape(50,38)
axis2[0,0].imshow(Orig_X.T)

Orig_X = X_test[1].reshape(50,38)
axis2[0,1].imshow(Orig_X.T)

Orig_X = X_test[2].reshape(50,38)
axis2[0,2].imshow(Orig_X.T)

Orig_X = X_test[3].reshape(50,38)
axis2[0,3].imshow(Orig_X.T)

Orig_X = X_test[4].reshape(50,38)
axis2[0,4].imshow(Orig_X.T)

Orig_X = X_test[5].reshape(50,38)
axis2[1,0].imshow(Orig_X.T)

Orig_X = X_test[6].reshape(50,38)
axis2[1,1].imshow(Orig_X.T)

Orig_X = X_test[7].reshape(50,38)
axis2[1,2].imshow(Orig_X.T)

Orig_X = X_test[8].reshape(50,38)
axis2[1,3].imshow(Orig_X.T)

Orig_X = X_test[9].reshape(50,38)
axis2[1,4].imshow(Orig_X.T)

Rec_X = reconst[0].reshape(50,38)
axis1[0,0].imshow(Rec_X.T)

Rec_X = reconst[1].reshape(50,38)
axis1[0,1].imshow(Rec_X.T)

Rec_X = reconst[2].reshape(50,38)
axis1[0,2].imshow(Rec_X.T)

Rec_X = reconst[3].reshape(50,38)
axis1[0,3].imshow(Rec_X.T)

Rec_X = reconst[4].reshape(50,38)
axis1[0,4].imshow(Rec_X.T)

Rec_X = reconst[5].reshape(50,38)
axis1[1,0].imshow(Rec_X.T)

Rec_X = reconst[6].reshape(50,38)
axis1[1,1].imshow(Rec_X.T)

Rec_X = reconst[7].reshape(50,38)
axis1[1,2].imshow(Rec_X.T)

Rec_X = reconst[8].reshape(50,38)
axis1[1,3].imshow(Rec_X.T)

Rec_X = reconst[9].reshape(50,38)
axis1[1,4].imshow(Rec_X.T)
plt.show()