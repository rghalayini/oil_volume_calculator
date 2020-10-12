### PROBABILISTIC GAS VOLUME CALCULATIONS USING THE MONTE CARLO SIMULATION

## replace your values with the values below

# Gross-rock-volume GRV (km^3)
#Porosity (in 00.00 format as it is a percentage)
#Hydrocarbon saturation 1-Wi (in 00.00 format as it is a percentage)
#net-to-gross (in 00.00 format as it is a percentage)
#recovery factor (in 00.00 format as it is a percentage)
#Bo (formation volume factor = 1.05 + (N × 0.05), where N = number of ft3 of gas produced per bbl of oil (gas-oil ratio or GOR). For example, if a well has a GOR of 1,000, then Boi = 1.05 + (10 × 0.05) = 1.1)
#Bg (in rcf/scf, usually it's between 0.003 and 0.01)



from scipy.stats import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#insert the number of iterations (it is the number of times you wish to run the simulation. The higher the better. Remember that higher numbers need more computing time).
iterations = 1000

#in case the area and thickness need to be inserted insted of the GRV. It's better to use the GRV directly from the modelling software.
#Area = norm(200,50).rvs(iterations)
#Thickness = norm(100,25).rvs(iterations)

GRV = norm(2, 0.5).rvs(iterations)
POR = norm(.2,.03).rvs(iterations)
GS = norm(.85,.2).rvs(iterations)
NTG = norm(0.7,.2).rvs(iterations)
RF = norm(0.4,.1).rvs(iterations)
Bg= norm(0.003,.0002).rvs(iterations)

#ogiip = 3.531467e10*GRV*NTG*POR*HS*RF/BO * 0.000000000001
ogiip = 0.04*GRV*NTG*POR*GS*RF/Bg

#plot3: Plot the distribution of volumes and their frequency
plot3=sns.distplot(ogiip, kde=True, norm_hist=True, #color='skyblue', #hist_kws={"linewidth": 15,'alpha':1})
plot3.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.figure()

#plot4
plot4=sns.distplot(ogiip,hist_kws=dict(cumulative=True),kde_kws=dict(cumulative=True))

plot4.set(xlabel='OGIIP tcf', ylabel='probability')
plot4.axhline(y=0.9, label='P10', color="red")
plot4.axhline(y=0.5, label='P50', color="red")
plot4.axhline(y=0.1, label='P90', color="red")
plt.show()

#to calculate the P90, P50 and P10 values (90%, 50% and 10% probabilities to have the specified volume):
ogiip_sorted=np.sort(ogiip)
x10=int(iterations/10*9)
x50=int(iterations/2)
x90=int(iterations/10)

p10=ogiip_sorted[x10]
p50=ogiip_sorted[x50]
p90=ogiip_sorted[x90]

print("P10 value is: ", p10, "tcf")
print("P50 value is: ", p50, "tcf")
print("P90 value is: ", p90, "tcf")