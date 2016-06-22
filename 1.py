import matplotlib.pyplot as plt
import numpy as np
import math



drange = np.arange(-40,40,0.1)
data = [math.sin(x) for x in drange]
data2 = [math.cos(x) for x in drange]

a = 0
b = 0

crange = np.arange(-40,40,0.1)
r = 40
cy = [(r**2-(x-a)**2)**0.5+b for x in crange]

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(drange,np.array(drange)*(0.5)+20)
plt.plot(drange,np.array(drange)*(-0.5)+20)
plt.plot(drange,data)
plt.plot(drange,data2)
plt.plot(crange,cy)
plt.show()
