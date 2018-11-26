# get_r.py
import numpy as np
def get_r(K,L,alpha,Z,delta):
	K=np.array(K)
	L=np.array(L)
	r=alpha*Z*(L/K)**(1-alpha)-delta
	return r