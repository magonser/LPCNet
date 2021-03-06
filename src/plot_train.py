import matplotlib.pyplot as plt
import numpy as np
import sys

loss = np.loadtxt(sys.argv[1])
delta_loss = (loss[1:]-loss[:-1])/loss[1:]

plt.figure(1)
plt.plot(loss[:],'r')
plt.title('loss')
plt.show(block=False)
plt.figure(2)
plt.plot(delta_loss)
plt.title('% delta loss')
#plt.ylim([-1E-2,1E-2])
plt.show()
