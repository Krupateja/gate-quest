import numpy as np  
import matplotlib.pyplot as plt  
plt.figure() # Create a new figure window
X = np.linspace(0, 2.0, 100) # Create 1-D arrays for x,y dimensions


Y = 8+((X+1)**2)*(X+2)  
Z = 8/Y
plt.plot(Z)
plt.show()
