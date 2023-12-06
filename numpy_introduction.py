import numpy as np
import seaborn
import matplotlib.pyplot as plt


x = np.arange(0., 5.0, 0.2)

plt.plot(x, color="red", linestyle="--", label="linear", marker="o")
plt.plot(x**2, color="blue", linestyle=":", label='quadric', marker="s")
plt.plot(x**3, color="green", linestyle=":", label='cubic', marker="^")
plt.xlabel('Goats', fontsize = 12)
plt.xlabel('Function', fontsize = 12)
plt.title('Functions to Graph', fontsize=16)
plt.legend(loc='best')
plt.show()
# plt.savefig('graph.png', dpi=100)
# plt.close()

plt.hist(x, color="red", bins=100)#, linestyle="--", label="linear", marker="o")
plt.hist(x**2, color="blue", bins=100)#, linestyle=":", label='quadric', marker="s")
plt.hist(x**3, color="green", bins=100)#, linestyle=":", label='cubic', marker="^")
plt.xlabel('Goats', fontsize = 12)
plt.xlabel('Function', fontsize = 12)
plt.title('Functions to Graph', fontsize=16)
plt.legend(loc='best')
plt.show()

plt.scatter(x=x, y=x**2)
plt.show()




