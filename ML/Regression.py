import matplotlib.pyplot as plt
from statistics import mean

import numpy as np
xs=np.random.randint(25,size=50)
ys=np.random.randint(25,size=50)
plt.scatter(xs,ys)
##xs=np.array([1,2,3,4,5],dtype=np.float64)
##ys=np.array([5,4,6,5,6],dtype=np.float64)
def best_fit_slope_and_intercept (xs,ys):
    m=(((mean(xs)*mean(ys))-mean(xs*ys))/((mean(xs)*mean(xs))-mean(xs*ys)))
    b=mean(ys)-m*mean(xs)
    return m,b
m,b=best_fit_slope_and_intercept(xs,ys)
regression_line=[(m*x)+b for x in xs]
l=[]
##print(ys)
##print(regression_line)
for n in regression_line:
    if n in xs:
        l.append(n)
print(l)
plt.plot(xs,ys,'ob',xs,regression_line)
plt.show()
