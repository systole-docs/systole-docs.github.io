from systole import import_dataset1
# Import PPG recording as pandas data frame
ecg = import_dataset1(modalities=['ECG'])
# Only use the first 60 seconds for demonstration
ecg = ecg[ecg.time.between(60, 90)]
plot_raw(ecg, type='ecg', sfreq=1000, ecg_method='pan-tompkins')
