import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(7.0,2.0,1000)
y = numpy.random.normal(9.0,1.0,1000)

plt.scatter(x,y)
plt.show()
