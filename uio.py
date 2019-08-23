import numpy as np 
from datetime import datetime



np.set_printoptions(suppress=True)
data = np.loadtxt('fo.csv', delimiter=',', skiprows=1)
numb = [1,7,4,7,8,5,4,9]
vspeed = []

#vtime = str(datetime.now().time())
#(h,m,s) = vtime.split(':')

for numb in numb:
	if numb > 4:
		vtime = str(datetime.now().time())
		(h,m,s) = vtime.split(':')
		(n,z) = s.split('.')
		h = int(h)
		m = int(m)
		n = int(n)
		
		vspeed.append(numb)
		newlist = [[(vspeed[0]), h, m, n]]
		data = np.append(data, newlist, axis = 0)
		vspeed = []


data1 = np.savetxt('foo.csv', data, delimiter=",")

data1 = np.loadtxt('foo.csv', delimiter=',', skiprows=1)

print(data1)