import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(data)

print(c)

#frequencies
count_sum = sum(c.values())
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))
  
#Box Plot
boxplot = plt.boxplot(data)
plt.savefig("newboxplot.png")

#histogram
histogram = plt.hist(data, histtype='bar')
plt.savefig("newhistogram.png")

#QQ-Plot
plt.figure()
graph1 = stats.probplot(data, dist="norm", plot=plt)
plt.show()
plt.figure()

