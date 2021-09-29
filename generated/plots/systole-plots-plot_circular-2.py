import numpy as np
import pandas as pd
from systole.plots import plot_circular

# Create angular values (two conditions)
x = np.random.normal(np.pi, 0.5, 100)
y = np.random.uniform(0, np.pi*2, 100)
data = pd.DataFrame(data={'x': x, 'y': y}).melt()

plot_circular(data=data, y='value', hue='variable')