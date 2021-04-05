from systole import import_rr
from systole.plotting import plot_psd
# Import PPG recording as numpy array
rr = import_rr().rr.to_numpy()
plot_psd(rr)