from astropy.io import fits
from numpy import log10
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from pandas import DataFrame
import math

pmRange = 0.5
distRange = 1.

stars = fits.open("stars.fits")

data = fits.open("gaiaColorData.fits")
tableData = data[1].data

df = DataFrame()
df['ra'] = tableData['ra']
df['dec'] = tableData['dec']
distances = 1/(tableData['parallax']/1000)
df['distances'] = distances
df['pmra'] = tableData['pmra']
df['pmdec'] = tableData['pmdec']
quality = tableData['parallax'] / tableData['parallax_error']
raq = tableData['ra'] / (tableData['ra_error'] / 3600000)
decq = tableData['dec'] / (tableData['dec_error'] / 3600000)
df['parq'] = quality
df['parallax_error'] = tableData['parallax_error']
df['ra_error'] = tableData['ra_error']
df['dec_error'] = tableData['dec_error']
df['raq'] = raq
df['decq'] = decq
#df = df[(df['pmra'] > 1.1) & (df['pmra'] < 1.2) & (df['pmdec'] > 1.1) & (df['pmdec'] < 1.2)]#df[(tableData['ra'] > 95) & (tableData['ra'] < 105) & (tableData['dec'] < -10) & (tableData['dec'] > -20) & (quality > 10)]# & (raq > 0.00001) & (decq > 0.00001)]
df[(quality > 10)]# & (raq > 0.00001) & (decq > 0.00001)]

#array1 = np.array(0)
#array2 = np.array(0)

for i in range(len(df)):
	for k in range(star1 + 1, len(df)):
		star1 = df.iloc[i]
		star2 = df.iloc[k]

		theta1 = star1['dec']
		theta2 = star2['dec']
		phi1 = star1['ra']
		phi2 = star2['ra']
		r1 = star1['distances']
		r2 = star2['distances']

		theta1 = math.radians(theta1)
		theta2 = math.radians(theta2)
		phi1 = math.radians(phi1)
		phi2 = math.radians(phi2)

		if not (abs(star1['ra'] - star2['ra']) < 1) and not (abs(star1['dec'] - star2['dec']))



		if not (abs(star1['pmra'] - star2['pmra']) < pmRange) and not (abs(star1['pmdec'] - star2['pmdec']) < pmRange):
			continue


		dist = np.sqrt((r1 ** 2 + r2 ** 2) - 2 * r1 * r2 * (np.cos(theta1) * np.cos(theta2) * np.cos(phi1-phi2) + np.sin(theta1) * np.sin(theta2)))

		
		if(dist < distRange):
			continue



		avgpmra = (star1['pmra'] + star2['pmra']) / 2.
		avgpmdec = (star1['pmdec'] + star2['pmdec']) / 2.

		pmraDiff = (star1['pmra'] - star2['pmra'])
		pmdecDiff = (star1['pmdec'] - star2['pmdec'])




		
"""
for i in range(len(df)):
	for k in range(i + 1, len(df)):
		star1 = df.iloc[i]
		star2 = df.iloc[k]
		if (abs(star1['ra'] - star2['ra']) < 5.) & (abs(star1['dec'] - star2['dec']) < 5.) :
			print "\nnew stars %d and %d\n" % (i, k)
			print star1['ra'] - star2['ra']
			print star1['dec'] - star2['dec']
			print star1['distances'] - star2['distances']
for i in range(len(df)):
	for k in range(i+1, len(df)):
		if  (abs(df.iloc[i]['pmra'] - df.iloc[k]['pmra']) < 1.) & (abs(df.iloc[i]['pmdec'] - df.iloc[k]['pmdec']) < 1.) :
			star1 = df.iloc[i]
			star2 = df.iloc[k]
			print "\nnew stars %d and %d\n" % (i, k)
			print star1['ra'] - star2['ra']
			print star1['dec'] - star2['dec']
			print star1['distances'] - star2['distances']
"""
			#dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
"""col1 = fita.Column(name='stars1', format='E', array = array1)
col1 = fita.Column(name='stars2', format='E', array = array2)
t = fits.BinTableHDU.from_columns([col1, col2])
t.writeto('testfits.fits')
"""
print "done"