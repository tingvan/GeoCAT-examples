"""
NCL_conLev_4.py
===============
This script illustrates the following concepts:
   - Explicitly setting contour levels
   - Making the labelbar be vertical
   - Adding text to a plot
   - Adding units attributes to lat/lon arrays
   - Using cnFillPalette to assign a color palette to contours

See following URLs to see the reproduced NCL plot & script:
    - Original NCL script: https://www.ncl.ucar.edu/Applications/Scripts/conLev_3.ncl
    - Original NCL plot: https://www.ncl.ucar.edu/Applications/Images/conLev_3_lg.png

Note:
    A different colormap was used in this example than in the NCL example
    because rainbow colormaps do not translate well to black and white formats,
    are not accessible for individuals affected by color blindness, and
    vary widely in how they are percieved by different people. See this
    `example <https://geocat-examples.readthedocs.io/en/latest/gallery/Colors/CB_Temperature.html#sphx-glr-gallery-colors-cb-temperature-py>`_
    for more information on choosing colormaps.
"""

###############################################################################
# Import packages:
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

import geocat.datafiles as gdf
from geocat.viz import cmaps as gvcmaps
from geocat.viz import util as gvutil

###############################################################################
# Read in data:

# Open a netCDF data file using xarray default engine and load the data into xarrays
ds = xr.open_dataset(gdf.get("netcdf_files/Tstorm.cdf"))

# Extract temperature data at the first timestep
T = ds.t.isel(timestep=0, drop=True)

###############################################################################
# Plot:

# Generate figure (set its size (width, height) in inches)
plt.figure(figsize=(8, 8))
ax = plt.axes()

# Import an NCL colormap
newcmp = 'magma'

# Contourf-plot data (for filled contours)
temp = T.plot.contourf(ax=ax, vmin=244, vmax=308, levels=np.arange(244, 312, 4),
                       cmap=newcmp, add_colorbar=False, add_labels=False)
# Contour-plot data (for line contours)
T.plot.contour(ax=ax, vmin=244, vmax=308, levels=np.arange(244, 312, 4),
               colors='black', linewidths=0.5, add_labels=False)

# Add horizontal colorbar
cbar = plt.colorbar(temp, orientation='vertical')
cbar.ax.tick_params(labelsize=11)
cbar.set_ticks(np.arange(248, 308, 4))

# Show the plot
plt.show()
