from systole import import_dataset1
from systole.plotting import plot_raw
# Import PPG recording as pandas data frame
ecg = import_dataset1(modalities=['ECG'])
# Only use the first 60 seconds for demonstration
ecg = ecg[ecg.time<60]
plot_raw(ecg, type='ecg', sfreq=1000, ecg_method='pan-tompkins')
