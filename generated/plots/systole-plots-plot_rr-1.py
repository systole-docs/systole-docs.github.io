from systole import import_rr
from systole.plots import plot_rr
rr = import_rr().rr.values
plot_rr(rr=rr, input_type="rr_ms", unit="bpm",)
