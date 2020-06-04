#!/usr/bin/env python

# Imports
import xarray as xr
import numpy as np

# Read a restart file into an xarray Dataset object
ds = xr.open_dataset("GEOSChem.Restart.20160101_0000z.nc4")

# Print the contents of the DataSet
print(ds)

# Print the units of the SpeciesRst_O3 field
print(ds["SpeciesRst_O3"].units)

# Convert the SpeciesRst_O3 (O3 concentration) to
# a numpy array so that we can take the sum
O3_values = ds["SpeciesRst_O3"].values

# Take the sum of SpeciesRst_O3
sum_O3 = np.sum(O3_values)
print("Sum of SpeciesRst_O3: {}".format(sum_O3))