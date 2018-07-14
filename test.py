import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

x = np.linspace(-7, 7, 100)

# Параметры распределений
loc_h0=0
scale_h0=1

loc_h1=2
scale_h1=2

# Критерий H0 : x <= threshold; H1 x > threshold

# Вероятность ошибки I рода
pf = norm.sf(x, loc=loc_h0, scale=scale_h0)
# Вероятность ошибки II рода
pm = norm.cdf(x, loc=loc_h1, scale=scale_h1)

# Графики
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, pf, label=r'$P_F$')
ax.plot(x, pm, label=r'$P_M$')

ax.set_xlabel('Threshold')
ax.set_ylabel('P')
ax.legend()

ax.grid(True)
plt.show()
