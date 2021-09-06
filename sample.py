import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np

#read csv data into a datafreame
df = pd.read_csv("file.csv")
#drop unneccessary information
df = df.drop(columns=['Program Title','Program Network'])
#aggregate number of viewers by hometown
df = df.groupby(['Program Genre','Viewer Hometown'],as_index=False).agg({'Number of Viewers': 'sum'})
#create our plot
df.pivot(index='Program Genre', columns='Viewer Hometown', values='Number of Viewers').plot(kind='bar')
#show our plot
plt.show()


