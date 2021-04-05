from systole import import_rr
from systole.plotly import plot_shortLong
# Import PPG recording as numpy array
rr = import_rr().rr.to_numpy()
plot_shortLong(rr)
