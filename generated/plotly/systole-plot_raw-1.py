from systole import import_ppg
from systole.plotting import plot_raw
# Import PPG recording as pandas data frame
ppg = import_ppg()
# Only use the first 60 seconds for demonstration
ppg = ppg[ppg.time<60]
plot_raw(ppg)
