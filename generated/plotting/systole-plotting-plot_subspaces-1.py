from systole import import_rr
from systole.plotting import plot_subspaces
# Import PPG recording as numpy array
rr = import_rr().rr.to_numpy()
plot_subspaces(rr)