from astropy.io import fits
from numpy import log10
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from pandas import DataFrame

######Assignment:  Read throught the code below and add in lines of code
######             whenever you see a #!!!! 

# get the combined data
data = fits.open("gaiaColorData.fits")
tableData = data[1].data

# print out some data meta info to see what we're working with
print("Number of stars: ",len(tableData))

cols = data[1].columns
cols.info('name')

#columns in tableData can be references by using the column name instead of the index number
#for example tableData['phot_g_mean_mag'] will pull out the Gaia release g-band average magnitude
#Use the result of the cols.info('name') function to help accessing the correct column of tableData

# create the lists of color data
starColorIndex = tableData['bmag'] - tableData['vmag']

#### Notice in the line above we calculated the color index of the star
#### with just ONE line of code, no need to loop through 2 Million rows!
#### This is a benefit of using the fits data structure that python now understands
#### when we use the Astropy library

##Create a list that corresponds with the data to determine the distances using parallax
##Don't forget to convert the parallax value to arcseconds

#!!!
distances = 1/(tableData['parallax']/1000)

#Determine the Absolute Magnitude using the apparent Visual magnitude combined and distance to the star

#!!!
starAbsMags = -(5 * log10(distances) - 5 - tableData['vmag'])#-(5 * log10(distances/10) - tableData['vmag'])
pm = np.sqrt(tableData['pmra'] ** 2 + tableData['pmdec'] ** 2)

# create and fill the pandas data frame with necessary info
# pandas's DataFrame objects allow for easier data manipulation and filtering
df = DataFrame()                 #Create empty DataFrame object called df
df['distances'] = distances
#df['bvColors'] = starColorIndex  #add the starColorIndex list as a column with the name 'bvColors'
#df['absMag'] = starAbsMags       #add the starAbsMags list as a column with the name 'absMags'
df['pm'] = pm

#Create a variable that measures the quality of the parallax data:  For example we will want to
#filter out any stars whose parallax angle is less than 10 times the parallax_error

#!!!
quality = tableData['parallax'] / tableData['parallax_error']



# isolate only the stars with color data below a certain level of error in the b and v magnitudes
# quality of 10 is suggested by Jackie.  B and V error limits suggested by BridgeUp Code

#!!Edit the line BELOW to add the quality constraint explained ABOVE
"""df = df[(tableData["e_bmag"] < .1) 
	& (tableData["e_vmag"] < .1) 
	& (tableData["e_bmag"] > 0.0) 
	& (tableData["e_vmag"] > 0.0) 
	& (quality > 10)]
"""
#print("Left after filter: ", len(df))

t = np.arange(len(df))

# # plot the graph!
df.plot.scatter('distances','pm', s=1)
#plt.axis([-.3,1.8,12,-1])  #Notice the absMag is reversed because we want increasing brightness going up

#Apply matplotlib rules to add better x and y axis names

#!!!

#Show the plot!

plt.show()

