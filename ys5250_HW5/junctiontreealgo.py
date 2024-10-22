# -*- coding: utf-8 -*-
"""junctionTreeAlgo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19tuD3yPDwrnXJwciuw5Xtp-V9nXnYD9t
"""

import numpy as np

def junction_tree(clique_pot):
  
    #calculating the size of the junction tree (number of cliques)
    m = np.size(clique_pot[0])

    #initializing separator potentials
    separator_pot_init = np.ones((3, 2))
    separator_pot_updated = np.zeros((3, 2))

    #forward message passing
    for i in range(m-1):
      separator_pot_updated[i] = np.sum(clique_pot[i], axis=0)
      sep_ratio = np.divide(separator_pot_updated[i], separator_pot_init[i]).reshape(2,1)
      clique_pot[i+1] = np.multiply(sep_ratio, clique_pot[i+1])

    separator_pot_init_back = separator_pot_updated.copy()

    #backward message passing
    for i in range(m-2, -1 , -1):
      separator_pot_updated[i] = np.sum(clique_pot[i+1], axis=1)
      sep_ratio = np.divide(separator_pot_updated[i], separator_pot_init_back[i]).reshape(1, 2)
      clique_pot[i] = np.multiply(sep_ratio, clique_pot[i])

    #normalizing
    for i in range(m):
      clique_pot[i] = np.divide(clique_pot[i], np.sum(clique_pot[i]))

    print(clique_pot)