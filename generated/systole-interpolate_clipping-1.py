import matplotlib.pyplot as plt
from systole import import_ppg
from systole.detection import interpolate_clipping
df = import_ppg()
clean_signal = interpolate_clipping(df.ppg.to_numpy())
plt.plot(df.time, clean_signal, color='#F15854')
plt.plot(df.time, df.ppg, color='#5DA5DA')
plt.axhline(y=255, linestyle='--', color='k')
plt.xlabel('Time (s)')
plt.ylabel('PPG level (a.u)')
