from systole import import_rr
from systole.plotly import plot_shortLong
from systole.detection import rr_artefacts
# Import PPG recording as numpy array
rr = import_rr().rr.to_numpy()
# Use the rr_artefacts function to short/long
# and extra/missed intervals
artefacts = rr_artefacts(rr)
plot_shortLong(artefacts=artefacts)
