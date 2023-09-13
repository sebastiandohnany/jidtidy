from calculators import Calculators

import numpy as np
import matplotlib.pyplot as plt


# Get data
data = np.load('../data/ds002898/derivatives/denoising/Schaefer2018/sub-01_run-1_atlas-Schaefer2018_200_roi-time-series.npy')

# 242 rows for timepoints and 200 columns for regions
regions = 200
timepoints = 242
assert data.shape == (timepoints, regions)

# Set up calculators
cal = Calculators()
cal.activate()

# MI
cal.mi_init('Gaussian')
r = cal.mi_calc(data[:, 10], data[:, 20])
print(r)

# MI with delay
r = cal.mi_calc(data[:, 10], data[:, 20], delay=)
print(r)

# MI with surrogates
rs, rs_pv, rs_sd = cal.mi_calc(data[:, 10], data[:, 20], surrogates=100)
print(rs)
print(rs_pv)
print(rs_sd)

# TE
cal.te_init('Gaussian')

r = cal.te_calc(data[:, 10], data[:, 20])
print(r)

# TE with surrogates
rs, rs_pv, rs_sd = cal.te_calc(data[:, 10], data[:, 20], surrogates=100)
print(rs)
print(rs_pv)
print(rs_sd)


