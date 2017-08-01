from astropy.io import fits
from numpy import log10
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from pandas import DataFrame

data = fits.open("gaiaColorData.fits")
tableData = data[1].data

df = DataFrame()
df['ra'] = tableData['ra']
df['dec'] = tableData['dec']
distances = 1/(tableData['parallax']/1000)
df['distances'] = distances

quality = tableData['parallax'] / tableData['parallax_error']
raq = tableData['ra'] / tableData['ra_error']
decq = tableData['dec'] / tableData['dec_error']
df['raq'] = raq
df['decq'] = decq
df = df[(tableData['ra'] < 50) & (tableData['dec'] < 0) & (quality > 10)]# & (raq > 10) & (decq > 10)]

print df