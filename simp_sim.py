import matplotlib.pyplot as plt
import numpy as np


x1 = np.random.normal(20, 2, 100)
y1 = [4*x + np.random.normal(20,10) for x in x1]

m1, b1 = np.polyfit(x1, y1, 1)


x2 = np.random.normal(25, 2, 100)
y2 = [4*x + np.random.normal(-20, 10) for x in x2]

m2, b2 = np.polyfit(x2, y2, 1)


m3, b3 = np.polyfit(np.concatenate((x1, x2)), y1+y2, 1)

plt.subplot(1,2,1)
plt.scatter(x1, y1)
plt.scatter(x2, y2)
xr1 = np.array([14,26])
xr2 = np.array([17,30])
plt.plot(xr1, m1*xr1+b1, c='#021bf9')
plt.plot(xr2, m2*xr2+b2, c='#ff5b00')

plt.subplot(1,2,2)
plt.scatter(x1, y1, c='black')
plt.scatter(x2, y2, c='black')

xl, yl = plt.xlim(), plt.ylim()

x3 = np.array([15,30])
plt.plot(x3, m3*x3+b3, 1, c='red')

plt.xlim(xl)
plt.ylim(yl)

plt.show()
